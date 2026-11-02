# Ultimate Web Design

A Codex skill for building distinctive business websites from a brief, with deliberate UI/UX, responsive implementation, supplied or generated imagery, fast assets, and search-ready content.

## Install

Clone this repository into your Codex skills directory:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
git clone https://github.com/TangledDaunT/ultimate-web-design.git "${CODEX_HOME:-$HOME/.codex}/skills/ultimate-web-design"
```

If the skill is already installed, preserve any local changes before replacing or updating that directory.

## Use

Invoke `$ultimate-web-design` with your business, target audience, website type, primary visitor action, and any brand material or images you have.

For example:

```text
$ultimate-web-design Build a website for my bicycle repair workshop in Pune.
The primary action is requesting an appointment. Use a practical, warm visual
identity. Ask for essential missing business information before implementation.
```

The skill supports business-specific visual directions, natural copy, 3D figures and glowing orbs where appropriate, image generation through available tools, accessibility, responsive layouts, performance, technical SEO, and generative-search readiness. Image generation and browser verification depend on tools available in your environment. The six source repositories are not installation dependencies.

Read [SKILL.md](SKILL.md) for the workflow, [design and content](references/design-and-content.md) for visual guidance, and [verification](references/verification.md) for delivery checks.

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
