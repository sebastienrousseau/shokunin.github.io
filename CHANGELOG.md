<!-- SPDX-License-Identifier: Apache-2.0 OR MIT -->

# Changelog

All notable changes to this website, static-site-generator.com (formerly
shokunin.one), are documented here.

## [0.0.4] - Unreleased

### Changed

- Re-themed the site with the Velocity theme from ssg-themes.github.io,
  replacing Prism. The accent colour tokens keep the terracotta taken from
  the ssg logo; every other colour is Velocity's. Content, URLs, structured
  data and the build checks are unchanged; the contrast gate now checks
  Velocity's tokens.

## [0.0.3] - 2026-10-26 (merged, not tagged)

### Changed

- The site is now the Static Site Generator homepage at
  https://static-site-generator.com/ instead of a legacy-name site at
  shokunin.one: base URL, canonical and Open Graph URLs, robots.txt,
  security.txt and the README follow.
- The home page, FAQ and about page present ssg itself; the rename is a
  short "Formerly Shokunin" page at the same `/migration/` URL, keeping the
  old-flag mapping table.
- A themes section links themes.static-site-generator.com, and the API
  reference links docs.static-site-generator.com.

## [0.0.2] - 2026-10-26 (merged, not tagged)

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
