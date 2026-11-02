# Ultimate Web Design

A Codex skill that turns one business brief into an image-led, dimensional website. It handles art direction, original image generation, polished SVG/3D artifacts, useful interactive panels, responsive code, asset optimization and search readiness.

## Install

Clone this repository into your Codex skills directory:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
git clone https://github.com/TangledDaunT/ultimate-web-design.git "${CODEX_HOME:-$HOME/.codex}/skills/ultimate-web-design"
```

If the skill is already installed, preserve any local changes before replacing or updating that directory.

## Use

Give `$ultimate-web-design` a natural-language business brief. The skill handles the visual direction, imagery and artifacts; you do not need to request images or 3D work separately. Include any real business facts, brand constraints and primary action you already know. It asks only when essential information is missing.

For example:

```text
$ultimate-web-design Build a website for my bicycle repair workshop in Pune.
We repair bicycles by appointment, and the main action is requesting a booking.
```

The default for open marketing/portfolio briefs is a visually rich composition with original artwork, dimensional layers and a coherent scroll journey. Interactions must help visitors inspect work, understand services, compare meaningful options or take action. Arbitrary shape playgrounds, filler slogans and decorative arrow rails are excluded. Explicit brand or restrained-design requirements take precedence. Image generation and browser verification depend on tools available in your environment. The six source repositories are not installation dependencies.

Read [SKILL.md](SKILL.md) for the workflow, [design and content](references/design-and-content.md) for visual guidance, and [verification](references/verification.md) for delivery checks.

## Preview

[Explore the Open Limits website](https://open-limits-studio-premium.admin794311.chatgpt.site/) to see the image-led visual quality, floating project previews and continuous scroll thread. It is a visual-quality reference, not a template that forces its palette or layout onto every business.

## Image optimizer

The optional Python helper creates responsive WebP or AVIF exports without changing source images. It preserves transparency, normalizes orientation and color, avoids upscaling, and records dimensions, byte sizes, quality, and budget misses in a per-run manifest.

Install Pillow in an isolated environment, then run from the repository root:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install Pillow
.venv/bin/python scripts/optimize_images.py /path/to/hero.png \
  --output-dir /path/to/site/public/images \
  --widths 480 768 1280 1920 --max-kb 250
```

WebP is the default; AVIF requires a compatible encoder in Pillow. Pass related originals together to generate one manifest. Existing exports are protected unless `--force` is selected. Exit codes are `0` for success, `1` for an export failure, and `2` for invalid CLI arguments or completed exports that missed a requested byte budget; inspect the message and manifest to distinguish them.

See [assets and performance](references/assets-and-performance.md) and [search readiness](references/search-readiness.md) for integration details. Performance and search guidance improves implementation quality; it does not guarantee indexing, rankings, rich results, or AI citations.

## Sources

Informed by Impeccable, revüe Proof Workflow, Unslop, UI Skills, UI UX Pro Max, Brainwave, and supplied frontend-design guidance. The implementation and condensed instructions in this repository do not bundle upstream code, assets, datasets, or launchers. See [source credits and inspected versions](references/sources.md).
