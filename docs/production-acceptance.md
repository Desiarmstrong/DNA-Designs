# DNA Designs production acceptance checklist

This list separates repository checks from tests that require access to the deployed Netlify site.

## Automated (GitHub Actions)
- [x] HTML local references validated by the existing static workflow (when green)
- [x] New smoke checks added for image alt attributes, navigation anchors, site assets, form markup, and SEO files (when green)

## Live validation — not yet verified
- [ ] Confirm the Netlify production deploy includes the latest master commit
- [ ] Open homepage on iPhone Safari and desktop Chrome/Safari; check readability, layout and no sideways scrolling
- [ ] Open and close mobile navigation; use every navigation link; verify keyboard focus
- [ ] Verify double-helix artwork is legible on the dark navigation background (asset redesign deferred)
- [ ] Confirm favicon/home screen icon appearance; dedicated export deferred
- [ ] Submit a **test** contact inquiry, confirm the thank-you page and the submission in Netlify Forms
- [ ] Verify that the intended recipient receives Netlify form notifications (must be configured in Netlify)
- [ ] Confirm that sitemap.xml and robots.txt return HTTP 200
- [ ] Review Netlify's deployment and runtime logs for errors
- [ ] Configure site analytics only with appropriate consent/privacy notice for the chosen tool
- [ ] Replace the portfolio placeholder with approved real work when available

## Rollback
GitHub source is on the master branch. If a newly merged change causes a production regression, revert the merge commit through GitHub, let Netlify redeploy, and rerun this checklist.

No real contact inquiries should be used to test or overwritten/deleted.
