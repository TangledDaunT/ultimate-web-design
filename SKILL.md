---
name: ultimate-web-design
description: Build or redesign distinctive business websites from a brief, combining brand-specific UI/UX, supplied or generated imagery, responsive code, asset optimization, technical SEO, and generative-search readiness. Use for complete websites and substantial redesigns; keep narrow bug fixes and standalone SEO audits scoped to their own tasks.
---

# Ultimate Web Design

Turn a business brief and website type into a convincing, usable website with a visual identity grounded in that business. Aim for work that feels commissioned and carefully edited. For build requests, deliver functioning implementation and evidence of quality; honor planning-only requests at their requested scope. Treat “perfect” as an ambition to test against the brief, never a guarantee of rankings or universal taste.

## Establish the brief and execution surface

Inspect the project, applicable instructions, brand material, supplied images, and user-selected platform before choosing tools or a stack. Preserve the established identity during refinement; replace its visual direction only within a requested redesign. Keep the existing framework unless there is a concrete, agreed reason to change it. For a new project, choose the simplest rendering approach that supports the content and interactions.

Identify the business and offer, audience, website type, primary visitor action, necessary pages, factual sources, and constraints. Bookings, enquiries, sales, reading, and portfolio exploration imply different structures. Do not treat every brief as SaaS lead generation.

If essential information cannot be recovered from the brief, project, connected sources, or public research, ask one concise batch of questions and stop before dependent implementation. Examples include an unidentified business, conflicting brand requirements, or a required transaction with no agreed destination. Choose routine design and implementation details autonomously. Do not require a questionnaire when the brief is sufficient.

Research current facts and references when useful. Prefer official business material and primary technical sources. Record factual provenance; keep uncertainty out of published copy. Never invent testimonials, client logos, ratings, awards, addresses, guarantees, prices, or quantified results. Generated art must not masquerade as evidence of a real team, property, product, or completed job.

## Commit to a direction, then build

Before substantial UI implementation, read [design-and-content.md](references/design-and-content.md). Make a compact direction note in the existing project design document, or the working plan if no durable document is warranted:

- Visitor goal, information hierarchy, and primary action.
- A business-specific visual idea: palette, type roles, composition, and one memorable asset or interaction.
- Content-led page structure and responsive behavior.
- Asset needs and a concrete definition of done.

For an open brief, compare a couple of genuinely different directions internally, choose the strongest, and proceed. Present alternatives only when requested or when a consequential unresolved preference requires a choice. User-pinned aesthetics win over stylistic warnings.

Ask whether changing the business name would leave the design and copy equally plausible. If so, replace the most generic element with something specific to its offer, materials, place, people, process, or product. Familiar navigation and clear controls remain valuable; novelty belongs where it improves identity or understanding.

Implement real content early. Use semantic HTML, coherent tokens, reusable components, and scoped styles. Match the requested deliverable: a local application, platform site, prototype, and live website are different outcomes. A screenshot does not substitute for functioning code when implementation was requested.

## Make and optimize the visual assets

Read [assets-and-performance.md](references/assets-and-performance.md) when selecting, generating, or integrating imagery, 3D, video, or effects. Inspect supplied assets first and use them where relevant. Create missing visual assets with available generation tools and their applicable skills. Do not leave empty image slots or ship raw multi-megabyte generations as website assets.

3D figures, glowing orbs, custom illustrations, photography, and product visuals are available creative choices. Include them when requested or when they strengthen the direction. Give them a clear compositional role, appropriate lighting, and mobile treatment. Choose CSS, SVG, an optimized raster render, or live 3D according to the actual interaction need and measured cost. Keep the message and controls available if effects fail or motion is reduced.

For repeatable local raster exports, use [optimize_images.py](scripts/optimize_images.py) as described in the assets reference. It preserves originals, produces responsive WebP or supported AVIF derivatives, and reports dimensions, bytes, and budget misses. Inspect the results visually; byte reduction alone does not establish quality.

## Build discoverability into the implementation

Read [search-readiness.md](references/search-readiness.md) when defining routes, content, rendering, metadata, or launch settings. Important business content and links should be accessible as HTML. Implement page-specific metadata, consistent canonical URLs, useful internal linking, and truthful structured data appropriate to the site.

Write for visitors' actual questions using clear entities, direct answers, concrete evidence, and sensible sections. Treat generative-search readiness as accessibility, crawlability, and source clarity. Do not add hidden AI-targeted copy, keyword stuffing, or fabricated authority signals. Never promise indexing, rankings, rich results, or AI citations.

## Use relevant capabilities without accumulating workflows

Discover and apply available skills and tools that materially improve the result. Typical needs include image generation, implementation from an approved design, a platform-specific build, browser inspection, and targeted SEO or accessibility checks. Read each applicable skill before using it. Honor the user's platform and scope. Do not load every installed skill, force competing site builders onto one project, or install the six source repositories as hidden dependencies.

This skill is self-contained. The repositories in [sources.md](references/sources.md) informed its guidance; they are optional references, not required runtimes. If an optional tool is unavailable, use a supported alternative and disclose a material gap. If a required asset or integration cannot be completed, ask for the missing input instead of implying completion.

## Verify, improve, and hand off

Before completion, read [verification.md](references/verification.md). Run the appropriate build and checks, inspect the rendered site on mobile and desktop, exercise the primary journey and failure states, inspect discoverability, and measure performance where tools permit. Fix observed defects and recheck the affected routes and states. Report unavailable checks as unverified.

Work autonomously through authorized, reversible implementation and optimization. Publishing, spending, submitting real enquiries, and changing external services follows existing user authorization; skill invocation alone does not grant it. Avoid fake success messages for disconnected forms or commerce.

Finish with the runnable or live result, what was verified, and remaining dependencies or launch limitations. Keep detailed evidence in the existing handoff or QA location when useful. Retain only demonstrated, reusable lessons in existing project notes. Improve this skill for observed recurring failures within authorized scope; do not rewrite unrelated skills or settings, add speculative rules, or run unbounded research or generation loops.
