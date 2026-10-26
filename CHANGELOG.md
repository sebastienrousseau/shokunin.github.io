<!-- SPDX-License-Identifier: Apache-2.0 OR MIT -->

# Changelog

All notable changes to shokunin.one are documented here.

## [0.0.2] - Unreleased

### Changed

- Rebuilt the site with Static Site Generator 0.0.69 and the Prism theme,
  coloured from the ssg logo, replacing the 2024 Shokunin site.
- Rewrote every page from the static-site-generator repository at version
  0.0.69: the site now explains that Shokunin was renamed Static Site
  Generator (ssg) in 0.0.36, and documents the current `ssg build`,
  `ssg check`, `ssg dev` and `ssg audit` commands instead of the 2024
  command line, which ssg 0.0.69 marks deprecated.
- `make build` checks colour contrast (WCAG AAA), requires ssg's quality
  gate at 10/10, verifies every `#fragment` and SRI hash, renders one social
  image per page and runs `ssg audit`; the Pages workflow builds and deploys
  the result instead of uploading committed output.

### Removed

- The Google Analytics tag, the service worker, and images loaded from
  kura.pro, whose Shokunin logo no longer exists.

## [0.0.1] - 2026-10-26 (merged, not tagged)

### Changed

- Licensed the site's source under Apache-2.0 OR MIT.
- Deployed GitHub Pages with GitHub Actions instead of from a branch.
