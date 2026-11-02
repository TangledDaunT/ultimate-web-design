# Asset production and performance

Read when integrating media or expensive effects. Budgets below are initial engineering targets, not search-engine rules. Adjust to the composition and verify the rendered page.

## Plan and acquire

Inspect provided images for content, dimensions, crop, transparency, and usage constraints. Keep originals separate from derivatives. Use meaningful filenames and record whether assets are supplied, licensed, generated, or illustrations. Do not scrape competitors' media or invent usage rights.

Generate missing imagery with an available image tool and its skill. Specify subject, palette, material, lighting, camera angle, aspect ratio, negative space for HTML content, and transparency when needed. Preserve real product features and identity from references. Keep critical text in HTML. Check anatomy, text artifacts, edges, product fidelity, and mobile crops before integration.

If generation is unavailable, use suitable licensed media, provided assets, or deliberate CSS/SVG. Disclose missing required imagery. Synthetic art must not be represented as a real customer, employee, office, product photograph, or case-study outcome without a truthful basis.

## Choose a medium by need

| Need | Starting choice | Check |
| --- | --- | --- |
| Glow or simple orb | Gradient/pseudo-element or small transparent render | Contrast, clipping, paint cost; avoid giant animated blurs |
| Decorative 3D figure | Optimized transparent raster | Silhouette and edges against the actual background |
| Interactive object | Lazy-loaded 3D with a static poster | Keyboard alternative, context loss, GPU/main-thread cost |
| Logos/simple diagrams | SVG, sanitized if untrusted | ViewBox, accessible naming, complexity |
| Photography/textured illustration | Responsive WebP/AVIF, fallback as needed | Detail, color, crop, actual browser requests |

For live 3D, reduce geometry/textures, compress with compatible loaders, cap pixel ratio, render on demand where possible, pause when hidden, and dispose resources. Keep text/actions outside the canvas. Test mobile fallback and reduced motion. Do not add WebGL merely to display a static shape.

## Export raster derivatives

Use the project's existing image pipeline if it already handles conversion correctly. Otherwise the bundled helper requires Python with Pillow and the chosen codec. If absent, install it in an isolated environment rather than system Python:

```bash
python3 -m venv /tmp/uwd-images-venv
/tmp/uwd-images-venv/bin/python -m pip install Pillow
/tmp/uwd-images-venv/bin/python /absolute/path/to/ultimate-web-design/scripts/optimize_images.py \
  /absolute/path/to/source/hero.png \
  --output-dir /absolute/path/to/project/public/images \
  --widths 480 768 1280 1920 --max-kb 250
```

Resolve the skill's actual directory; the sample path is illustrative. WebP is the default. Use `--format avif` only with encoder support and appropriate browser fallback. The helper normalizes orientation/color, preserves alpha, strips nonessential export metadata, never enlarges images, and leaves originals intact. Retain provenance/licensing records with originals; do not remove watermarks.

The output `manifest.json` records width, height, bytes, quality, and budget status for this run; pass related originals together as a batch. Existing files fail unless `--force` intentionally regenerates derivatives. Inputs with colliding export names are rejected. Animation requires a dedicated workflow rather than silently exporting one frame. A missed budget returns status 2 while retaining exports for inspection; revise crop, size, or medium instead of repeatedly degrading quality. Run `--help` for options.

## Integrate by display size

Start around 150–300 KB for a large hero, 40–120 KB for content imagery, and 10–60 KB for small art. Complex imagery may justify more. Compare encodings visually. Avoid redundant variants if the framework generates them already.

Use `srcset` with accurate `sizes`, or the framework equivalent. Reserve space with intrinsic dimensions/aspect ratio. Let the likely LCP image be discovered eagerly with appropriate fetch priority; do not lazy-load it or preload everything. Lazy-load below-fold images. Important content imagery should have a discoverable `img` source and contextual alt text; decorative images need empty alt text.

Limit font families/weights; use subsetted WOFF2, suitable font-display, and fallback metrics. Defer noncritical scripts and heavy islands. Inspect unused code and third-party costs before adding infrastructure. Cache fingerprinted static assets appropriately without stale caching of changing HTML.

Measure a production build under realistic mobile constraints. Current Core Web Vitals targets are LCP ≤2.5 s, INP ≤200 ms, CLS ≤0.1 at the 75th percentile, assessed separately on mobile and desktop. Lab tests diagnose problems; they do not prove a field pass. Verify evolving thresholds against [web.dev](https://web.dev/articles/vitals) when needed.
