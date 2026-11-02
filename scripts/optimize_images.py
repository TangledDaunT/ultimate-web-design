#!/usr/bin/env python3
"""Export responsive raster derivatives without modifying original images.

Requires Pillow with the selected encoder. Exit 0: exported within budget;
1: invalid input/export failure; 2: exported, but a requested byte budget was missed.
"""

import argparse
import io
import json
import math
import os
from pathlib import Path
import sys
import tempfile


def arguments():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs", nargs="+", type=Path, help="Static raster originals")
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--widths", nargs="+", type=int, default=[480, 768, 1280, 1920])
    parser.add_argument("--format", choices=["webp", "avif"], default="webp")
    parser.add_argument("--quality", type=int, default=80)
    parser.add_argument("--min-quality", type=int, default=60)
    parser.add_argument("--max-kb", type=float, help="Per-derivative target, in KiB")
    parser.add_argument("--force", action="store_true", help="Replace existing derivatives/manifest")
    args = parser.parse_args()
    if not all(width > 0 for width in args.widths):
        parser.error("Widths must be positive integers")
    if not 1 <= args.min_quality <= args.quality <= 100:
        parser.error("Require 1 <= min-quality <= quality <= 100")
    if args.max_kb is not None and (not math.isfinite(args.max_kb) or args.max_kb <= 0):
        parser.error("max-kb must be a finite positive number")
    return args


def normalize_image(source, Image, ImageOps, ImageCms):
    """Apply orientation and transform tagged images into sRGB, preserving alpha."""
    with Image.open(source) as original:
        if getattr(original, "n_frames", 1) != 1:
            raise ValueError(f"Animated or multipage input needs a separate workflow: {source}")
        original.load()
        image = ImageOps.exif_transpose(original)
        alpha = image.convert("RGBA").getchannel("A") if (
            "A" in image.getbands() or "transparency" in image.info
        ) else None
        profile = image.info.get("icc_profile")
        if profile:
            # Preserve CMYK/LAB channels until the profile conversion when present.
            base = image if image.mode in ("RGB", "CMYK", "LAB", "L") else image.convert("RGB")
            try:
                rgb = ImageCms.profileToProfile(
                    base,
                    ImageCms.ImageCmsProfile(io.BytesIO(profile)),
                    ImageCms.createProfile("sRGB"),
                    outputMode="RGB",
                )
            except Exception as exc:
                raise ValueError(f"Cannot convert the embedded color profile: {source}: {exc}") from exc
        else:
            rgb = image.convert("RGB")
        if alpha is not None:
            rgb.putalpha(alpha)
        # Fresh pixel-only image prevents carrying EXIF/XMP into web derivatives.
        clean = Image.new(rgb.mode, rgb.size)
        clean.paste(rgb)
        return clean


def encode(image, fmt, quality):
    buffer = io.BytesIO()
    options = {"quality": quality}
    if fmt == "WEBP":
        options.update(method=6, exact=True)
    else:
        options.update(speed=6)
    image.save(buffer, format=fmt, **options)
    return buffer.getvalue()


def export(args):
    try:
        from PIL import Image, ImageCms, ImageOps
    except ImportError as exc:
        raise ValueError("Pillow is required. Install it in an isolated Python environment.") from exc
    Image.init()
    fmt = args.format.upper()
    if fmt not in Image.SAVE:
        raise ValueError(f"This Pillow installation does not support {fmt} encoding")

    output = args.output_dir.resolve()
    sources = [path.resolve(strict=True) for path in args.inputs]
    if len(set(sources)) != len(sources):
        raise ValueError("Input paths must be distinct")
    if not all(path.is_file() for path in sources):
        raise ValueError("Every input must be a regular image file")
    manifest_path = output / "manifest.json"
    destinations = {manifest_path}
    plans = []
    # Inspect every input and destination before writing anything.
    for source in sources:
        image = normalize_image(source, Image, ImageOps, ImageCms)
        widths = sorted({min(width, image.width) for width in args.widths})
        variants = []
        for width in widths:
            height = max(1, round(image.height * width / image.width))
            destination = output / f"{source.stem}-{width}.{args.format}"
            if destination in destinations:
                raise ValueError(f"Colliding output names: {destination}")
            destinations.add(destination)
            variants.append((width, height, destination))
        plans.append((source, image, variants))
    for destination in destinations:
        if destination.resolve() in sources:
            raise ValueError(f"An export would overwrite an original: {destination}")
        if destination.is_dir():
            raise ValueError(f"An output path is a directory: {destination}")
        if (destination.exists() or destination.is_symlink()) and not args.force:
            raise ValueError(f"Output exists; choose a new directory or intentional --force: {destination}")

    budget = args.max_kb * 1024 if args.max_kb is not None else None
    qualities = list(range(args.quality, args.min_quality - 1, -5))
    if qualities[-1] != args.min_quality:
        qualities.append(args.min_quality)
    manifest = {"format": args.format, "max_kb": args.max_kb, "images": []}
    payloads = []
    missed = 0
    for source, image, variants in plans:
        record = {
            "source": str(source), "source_bytes": source.stat().st_size,
            "oriented_width": image.width, "oriented_height": image.height,
            "variants": [],
        }
        for width, height, destination in variants:
            resized = image.resize((width, height), Image.Resampling.LANCZOS)
            best = None
            for quality in qualities:
                data = encode(resized, fmt, quality)
                if best is None or len(data) < len(best[0]):
                    best = (data, quality)
                if budget is None or len(data) <= budget:
                    best = (data, quality)
                    break
            data, quality = best
            within_budget = None if budget is None else len(data) <= budget
            missed += within_budget is False
            payloads.append((destination, data))
            record["variants"].append({
                "file": destination.name, "width": width, "height": height,
                "bytes": len(data), "quality": quality, "within_budget": within_budget,
            })
        manifest["images"].append(record)
    manifest["budget_misses"] = missed
    payloads.append((manifest_path, (json.dumps(manifest, indent=2) + "\n").encode()))
    output.mkdir(parents=True, exist_ok=True)
    # Encode first, then stage files in the destination filesystem for atomic replacement.
    with tempfile.TemporaryDirectory(prefix=".uwd-export-", dir=output) as temporary:
        staged = []
        for index, (destination, data) in enumerate(payloads):
            stage = Path(temporary) / str(index)
            stage.write_bytes(data)
            staged.append((stage, destination))
        for stage, destination in staged:
            if args.force:
                os.replace(stage, destination)
            else:
                # An intervening writer must not be silently overwritten.
                os.link(stage, destination)
    print(json.dumps({
        "manifest": str(manifest_path), "variants": len(payloads) - 1,
        "bytes": sum(len(data) for _, data in payloads[:-1]), "budget_misses": missed,
    }))
    return 2 if missed else 0


def main():
    args = arguments()
    try:
        return export(args)
    except (OSError, ValueError) as exc:
        print(f"Export failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
