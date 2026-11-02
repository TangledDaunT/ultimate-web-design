# Search and generative-search readiness

Use for page intent, routes, HTML/metadata, and launch settings. Verify changing platform requirements from primary documentation. Never guarantee indexing, rankings, rich-result display, or AI citations.

## Useful, reachable pages

Assign each route a real visitor need and distinct content. Use stable descriptive URLs, meaningful HTML links, logical headings, and page-specific titles/descriptions. Put core offers, evidence, and navigation in initial HTML through static/server rendering or the platform equivalent when practical. Do not replace a working stack for a framework preference; inspect what users and crawlers receive.

Avoid thin doorway pages, keyword variants without distinct value, invented locations, and FAQ padding. For local businesses, consistently use verified service areas, identity, contact details, and hours. For commerce, represent products, availability, currency, prices, and policies from approved facts. Use genuine authorship and updated dates where relevant to editorial content.

## Technical implementation

- Provide document language, viewport, landmarks, descriptive titles, snippets, and favicons. Set social metadata with reachable images and consistent URLs; check platform support for the image encoding.
- Derive absolute canonical/social URLs from the actual production origin. Use self-canonicals for distinct indexable pages, rather than canonicalizing everything to the homepage. If the domain is unknown, make it configurable and identify it as a launch dependency; do not publish a guessed address.
- Return appropriate status codes. Missing pages need 404/410, redirects must resolve intentionally, and useful public pages should succeed. A client-rendered error with HTTP 200 is insufficient.
- Include canonical public pages in the sitemap when appropriate, excluding errors, redirects, private/noindex pages. Use real modification dates where available, rather than timestamps changing on each request.
- Inspect robots.txt, meta robots, HTTP X-Robots-Tag, hosting/CDN controls, and resource access. Public production pages intended for search must be crawlable and indexable. Avoid accidental preview indexing. Robots disallow alone is not reliable deindexing; crawlers must be able to discover a noindex directive. Protect private material with authentication.
- For multilingual sites, configure language routes, canonicals, and reciprocal hreflang. Avoid geography-only redirects that prevent content access.
- Add only relevant, truthful JSON-LD matching visible content, such as Organization/LocalBusiness, Product, Article, or BreadcrumbList. Follow current type-specific rules and validate syntax/eligibility. Never invent reviews or add FAQ schema expecting guaranteed rich results.

See [Google's SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide). Contextual imagery, responsive delivery, descriptive filenames, and useful alt text also support discovery; see [Google's image guidance](https://developers.google.com/search/docs/appearance/google-images).

## Help search systems understand the subject

Name entities consistently and explain who provides what, to whom, where, under what conditions, and with what evidence. Use concise answers followed by useful detail, clear headings, and tables/lists where appropriate. Keep primary facts as selectable text instead of canvas, image text, or interaction-only reveals. Link to genuine sources and relevant internal detail. Keep claims consistent across visible copy, metadata, and structured data.

Google's AI Overviews and AI Mode use the same SEO foundations and require no special AI files or schema. `llms.txt` is not a prerequisite for those features or a guaranteed citation mechanism. See [Google's AI features documentation](https://developers.google.com/search/docs/appearance/ai-features). Other engines may differ; check their official requirements when targeted. Do not conflate search access, user-requested retrieval, and model-training permissions or silently change site policies for them.

## Verify code separately from search outcomes

Inspect served HTML and headers, not only component source. Check representative routes, links, canonical consistency, JSON-LD, sitemap origin, robots behavior, and image fetches. Validate social previews on a public URL when available. Localhost checks cannot establish public crawler access or real share fetching.

With authorized access and a deployed domain, use Search Console URL Inspection, sitemap submission, rich-result checks, and field data as appropriate. Keep domain ownership/search-service setup distinct from code completion. Record observations honestly; future indexing, traffic, and conversions require post-launch evidence.
