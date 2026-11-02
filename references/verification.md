# Verification and improvement

Read before handing off a website. Scale checks to the changed surface and intended deliverable. Compilation does not prove a functioning booking flow or accessible site.

## Inspect the visitor's artifact

Run relevant repository lint, type, build, and existing tests. Measure production output for performance. Add tests for meaningful behavior when warranted, especially integrations; avoid asserting chosen wording or CSS classes merely to mirror implementation.

Open actual routes with an available browser/preview. Inspect a narrow phone width (about 360–390 CSS pixels), a middle width, and wide desktop (about 1280–1440); add cases where behavior changes materially. Review screenshots for composition and DOM state for behavior. If unavailable, complete other checks and explicitly identify visual verification as incomplete.

Review the opening at scroll position zero separately from scrolled sections and anchored URLs such as `#work`. Inspect the initial visual and a later animation state; verify that requested motion actually starts without interaction and that the primary graphic is visible on a phone. Check pause and reduced-motion states. A build pass, a high Lighthouse score, or planning-only evaluation cannot establish visual quality or an engaging first impression.

Run a visible-copy and ornament pass: inspect all small labels and art captions, repeated slogans, pseudo-element bullets, corner glyphs, and button suffixes. Delete filler and redundant arrows at the source; do not merely hide them on one breakpoint. Preserve meaningful control labels, real statuses, and factual information. Record the specific visual or copy correction made when a user reports one.

Review every interactive panel for visitor value. Remove standalone shape demos and arbitrary controls that do not explain the offer, reveal real work, support comparison or enable an intended action. When removing a rejected scene, also remove its controls, unused rendering code and styles, repair anchors, and reconnect any continuous scroll motif; verify the surrounding transitions rather than leaving an empty gap.

| Area | Evidence |
| --- | --- |
| Brief/identity | Required pages/content; type, palette, imagery, and interaction match the direction |
| Composition | Clear first viewport, sound text wrapping, no clipping/overflow, useful crops, sustained quality through footer |
| Primary journey | Navigation/CTAs, menus, forms, booking/cart steps, and confirmation states work as scoped |
| Recovery | Required/invalid input, loading, empty, network/error, and success states behave truthfully where applicable |
| Accessibility | Keyboard, visible/unobscured focus, labels/names, semantics, contrast, reduced motion, dialog focus/Escape |
| Health | Relevant console errors, asset failures, broken routes, hydration issues, and dependencies |
| Search | Served HTML, unique metadata, canonical origin, robots, sitemap, JSON-LD, and links |
| Performance | Production route/device settings, media bytes, heavy scripts/effects, lab metrics, field data if available |

## Accessibility beneath visual polish

Prefer native controls; use established accessible primitives for complex widgets in the current stack. Supply names for icon-only controls, associate labels/errors with inputs, and announce asynchronous status without excess. Support keyboard alternatives to hover, restore dialog focus on close, and keep sticky navigation from covering focus.

Measure text contrast (generally 4.5:1 normal and 3:1 large text) and relevant nontext controls (generally 3:1). Aim for generous touch targets, often about 44 CSS pixels, without confusing this ergonomic preference with every formal WCAG exception. Respect zoom, text enlargement, safe areas, and motion preferences. Automated scans complement manual checks; neither alone certifies compliance.

## Test boundaries truthfully

Do not send enquiries, book appointments, charge cards, email customers, or alter production data merely to test without authorization. Use an existing sandbox, test endpoint, or local mock and state its limits. If a form lacks a backend, provide a truthful demo/unavailable state or approved destination; never display “sent” after only a timeout.

## Improve observed weaknesses

Review against the brief and rendered evidence. Prioritize broken journeys/misleading claims, accessibility barriers, layout/content failures, performance, then visual refinement. Fix actionable defects within scope; recheck affected flows, widths, and shared components. Repeat broad checks only for new changes or unresolved concerns.

For subjective polish, return to the business's visual idea rather than adding ornament. Remove weak competing elements. Stop when the requested result exists and relevant checks pass, or a concrete missing input prevents useful progress. Avoid arbitrary numeric perfection and invented “human design” scores.

## Handoff

Provide the actual local path/preview/live URL and run instructions when needed. Summarize observed checks and outstanding dependencies; include representative captures when useful. Substantial sites can retain route, viewport, tool/command, result, and limitation in the existing QA record. Do not require paperwork for a small adjustment.

If the requested result is live, a local build remains incomplete. Deploy when already authorized; otherwise prepare a concrete reviewable result and identify publication as the remaining step. A local Lighthouse score is a lab result, not proof of field Core Web Vitals or ranking.
