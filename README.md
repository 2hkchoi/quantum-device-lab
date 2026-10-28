# Quantum Device Lab

Static website for Quantum Device Lab, Jeonbuk National University.

## Preview

From this directory: `python3 -m http.server 8766 --bind 127.0.0.1`
Open http://127.0.0.1:8766/index.html.

## Validate

Run `python3 scripts/check_site.py` and `node --check site.js`.
Check Home and Research on desktop and mobile, including the Menu toggle and research theme links.

## Deployment

Keep the existing GitHub Pages repository and publishing configuration. No framework build or package installation is required. Publish the HTML, CSS, site.js, assets, .nojekyll and sitemap.xml together. Relative asset links support the /quantum-device-lab/ project path. Verify the Pages deployment after publishing.

## Editing

- index.html: home introduction and research overview.
- research.html: four research themes in a text-only layout.
- people.html: profiles and education.
- publications.html: existing bibliography, with no paper links or filters.
- enhancements.css: shared accessibility, mobile navigation and Home/Research refinements.
- site.js: progressive-enhancement mobile menu; navigation remains available without JavaScript.
- Research uses a text-only layout with no figures or background imagery. Home retains its conceptual hero illustration.

October 2026 checks: 7 pages at widths 390, 768 and 1280; no horizontal overflow; mobile menu opens and closes with Escape; local links/assets/anchors pass; bibliography entries unchanged.

Contact details use `hkchoi AT jbnu.ac.kr`. Do not add raw email addresses, mailto links or email clipboard actions. Supporting pages include student inquiry guidance, equipment purposes and section navigation.
