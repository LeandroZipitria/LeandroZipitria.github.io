# Migration notes — final website

## Do not publish this overlay by replacing the repository blindly

The current public repository contains a large legacy `files/` tree with CVs, papers, media, and historical teaching materials that are intentionally not duplicated in this package.

## Safe migration sequence

1. Freeze the current website with a Git commit/tag before changing anything.
2. Keep a separate backup of the current working tree if desired.
3. Preserve the current `files/` directory in place.
4. Copy the new Quarto source over the repository root.
5. Merge the new `files/teaching/` material into the existing `files/` tree; do not replace `files/` wholesale.
6. Copy `libro-regulacion/` from this package as a static directory. It is the existing Bookdown `docs/` output only.
7. Install Quarto if necessary and run `quarto preview` locally.
8. Run `quarto render`.
9. Verify the rendered `_site/`, especially Home, Research, Teaching, Professional, TeXFlow, the regulation book, CV links, paper links, media, and mobile layout.
10. Run the internal-link checker after the full legacy `files/` tree is present.
11. Only then commit and push the new website.

## Public URLs to preserve

- `/research.html`
- `/teaching.html`
- `/bio.html`
- `/blog.html`
- `/personal.html`
- `/libro-regulacion/` and its chapter URLs
- all existing `/files/...` URLs that are still linked or externally referenced

## Book project

The regulation book remains an independent Bookdown project. The website contains only its published `docs/` output under `libro-regulacion/`. Changes to the book should be rendered in that project first and then its `docs/` output copied here.
