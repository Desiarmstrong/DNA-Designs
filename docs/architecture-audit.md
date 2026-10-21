# DNA Designs architecture baseline

Source inspected: root `index.html` on `master` (2026-10-20).

## Verified
- Static HTML entrypoint at repository root.
- Local `style.css` referenced.
- Bootstrap 3.4.1, jQuery 3.4.1, Font Awesome 4.7 loaded from CDNs.
- Universal Analytics UA-169240650-1 snippet is present; Universal Analytics is retired.
- Two HTML form elements present (functionality not verified).
- Navigation uses fragment anchors; many links use `href="#"`.
- No root `package.json`, `netlify.toml`, or `.github/workflows/ci.yml` at inspected paths.

## Not yet verified
- Netlify site-to-repository linkage and publish settings.
- Complete directory inventory and asset references.
- Form submission behavior, mobile rendering, accessibility, and security headers.
- Whether any automated tests already exist elsewhere.

## Recommended sequence
1. Verify Netlify production repository and deployment settings.
2. Inventory CSS, JavaScript, images, and form handling.
3. Fix broken/placeholder links and content, with accessible navigation.
4. Replace retired analytics with consent-aware GA4 only if analytics is desired.
5. Introduce proportionate static-site validation and preview checks.
6. Upgrade legacy frontend dependencies with visual regression checks.

No live-site changes or test-pass claims are implied by this audit.
