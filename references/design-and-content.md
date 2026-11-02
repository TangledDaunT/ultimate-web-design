# Design and content decisions

Read before a new site or substantial visual redesign. For refinement, apply these criteria within the existing identity.

## Find the site's visual language

Start with artifacts from the business: a manufacturing drawing, an architect's model, a restaurant's ceramics, an actual product interface, a local landscape, or a portfolio's work. Translate relevant material into composition, imagery, typography, and rhythm. Research can inform the direction without copying another site's layout, branding, or assets.

Give the first viewport the subject's most informative visual or proposition. A service may need a clear offer and place; a portfolio may open with a project; a product may benefit from a demonstration. Establish what this is, who it serves, and the next useful action without relying on an animation finishing.

Plan the first viewport as a complete composition at the actual desktop and phone sizes, rather than the top of a long page. Keep the primary graphic in view with the offer and action. If the brief calls for animation, name its subject, initial pose, movement, trigger, and fallback before implementation. It must contribute before the visitor scrolls. A nominal CSS drift that is barely perceptible, or motion hidden below the fold, does not satisfy a request for an engaging opening.

Treat saturated patterns as prompts for judgment, not bans. Purple gradients, cream-and-serif branding, neon dark themes, oversized headlines, glass cards, bento grids, orbital ornaments, and editorial rules can suit a brief. They become generic when applied regardless of subject. Explicit user direction takes precedence.

## Establish a coherent system

- Choose colors by role: canvas, surface, text, muted text, accent, border, and feedback. Check actual foreground/background pairs. A glow cannot be the sole signal that a control is interactive.
- Give typefaces a reason: material character, voice, language coverage, and readable density. Usually one or two families suffice. Limit weights. Set fluid scales, line height, and sensible text widths, generally around 45–75 characters for long body text.
- Align deliberately. Build hierarchy with scale, placement, spacing, and relationships before boxes. Cards suit independent, comparable items, not every paragraph.
- Use consistent spacing, radii, elevation, and layer tokens. Let hierarchy explain differences. Avoid late selector overrides that conceal a broken layout rule.
- Choose one dominant expressive moment and quieter supporting elements. Change composition when the information changes, rather than alternating layouts for variety.

For substantial sites, record stable decisions in the existing design-system document and implement them in CSS variables or the established theme. Keep page exceptions local. Do not create a parallel source of truth.

## Structure the visitor's decision

Choose pages and sections from intent, not a fixed hero/features/testimonials/pricing template. Place decision information near the action: relevant availability, scope, eligibility, terms, or process when known. Put genuine proof close to the claim it supports.

Navigation should use audience vocabulary and work on touch and keyboard. Repeated CTAs should mean the same thing. A booking button must reach a booking flow or clearly identify that it requests one.

Adapt content order for small screens. Preserve useful detail instead of hiding it for a screenshot. Tables, galleries, menus, and comparisons need deliberate narrow-screen behavior. Avoid horizontal overflow and fixed-height text containers. Keep sticky elements from obscuring headings, focus, or form actions.

## Write the business's copy

Draft from verified facts and visitor questions. Describe the offer, audience, what happens next, and what is included. Match the brand's voice without exaggerated sales language. Preserve exact names, units, prices, caveats, and meaning when editing supplied copy.

Read aloud and remove stock openings, repeated sentence scaffolds, unsupported superlatives, and empty phrases such as “unlock your potential” when they carry no information. Vary sentences to suit meaning rather than mechanically removing punctuation or making everything short. Avoid faux-human anecdotes and invented specificity.

Audit the small text separately: eyebrows, corner annotations, art captions, marquees, status dots, footer mottos, CTA preambles, and mobile-only messages are common hiding places for filler. Remove phrases like “independent thinking,” “open by design,” and “yo, your next chapter starts here” when invented as decoration. Do not turn a brand name into a string of vague manifestos. If removing a line loses no factual or navigational information, prefer removing it. User-supplied essential brand copy remains authoritative.

Do not use arrows as repeated service bullets, side rails, corner ornaments, or generic button suffixes. Use an icon only when it improves understanding of that control. Keep an external-link cue or directional arrow where it has a specific useful meaning; do not mechanically replace all arrows with stars or plus signs. Inspect pseudo-elements and SVG icons as well as literal text.

Make interface copy operational: “Request a consultation,” “Download the catalogue,” or “Save preferences.” Explain form errors beside the relevant field. Give loading, empty, and success states a useful next action. Do not add uppercase eyebrows, numbering, or arrows solely to fill space.

## Make motion earn its cost

Prefer direct feedback and state transitions for utility surfaces. For an expressive marketing brief, give the main visual confident motion: for example, a dimensional object assembling, an interactive product demonstration, or a deliberate sequence of project imagery. Choose the effect from the subject rather than a preset. If an entrance sequence serves the direction, choreograph it once and keep important content available immediately. Avoid making every section slide in, headings that destabilize layout, custom cursors that replace usable pointers, and scroll hijacking. Continuous ambient movement needs a pause mechanism when appropriate.

Use transform and opacity where practical, honor reduced motion, stop offscreen loops, and keep input feedback immediate. Follow the brief and device capability: an immersive brand site and a booking form need different levels of expression.
