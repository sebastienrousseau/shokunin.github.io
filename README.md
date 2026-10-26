<!-- SPDX-License-Identifier: Apache-2.0 OR MIT -->
<!--
README template. Global rules: see ~/Code/AGENTS.md and ~/Code/REPO-STANDARD.md.
Releases adhere strictly to https://github.com/sebastienrousseau/passmcp/releases/tag/v0.0.5
-->

<p align="center">
  <img src="static/logo.svg" alt="Static Site Generator logo" width="128" />
</p>

<h1 align="center">static-site-generator.com</h1>

<p align="center">
  The homepage of Static Site Generator (ssg), built with ssg itself and the Velocity theme.
</p>

<p align="center">
  <a href="https://github.com/sebastienrousseau/shokunin.github.io/actions"><img src="https://img.shields.io/github/actions/workflow/status/sebastienrousseau/shokunin.github.io/pages.yml?style=for-the-badge&logo=github" alt="Build" height="28" /></a>
  <a href="https://static-site-generator.com/"><img src="https://img.shields.io/website?url=https%3A%2F%2Fstatic-site-generator.com&style=for-the-badge&labelColor=555555&label=static-site-generator.com" alt="Website" height="28" /></a>
  <a href="https://scorecard.dev/viewer/?uri=github.com/sebastienrousseau/shokunin.github.io"><img src="https://img.shields.io/ossf-scorecard/github.com/sebastienrousseau/shokunin.github.io?style=for-the-badge&label=OpenSSF%20Scorecard&logo=openssf" alt="OpenSSF Scorecard" height="28" /></a>
  <a href="LICENSE-MIT"><img src="https://img.shields.io/badge/license-Apache--2.0%20OR%20MIT-blue.svg?style=for-the-badge" alt="License: Apache-2.0 OR MIT" height="28" /></a>
</p>

<p align="center">
  <img src="static/images/screenshot.png" alt="The static-site-generator.com home page: the ssg masthead, the headline A static site generator that checks what it builds, and cards for a 10 of 10 quality gate, 15 audit gates and a good release signature" width="100%" />
</p>

---

## Contents

**Getting started**

- [Install](#install): what to install to build the site
- [Requirements](#requirements): ssg, Python, Chrome for the screenshot
- [Quick Start](#quick-start): build, check and preview locally

**The static-site-generator.com ecosystem**

- [The static-site-generator.com ecosystem](#the-static-site-generatorcom-ecosystem): the site, the generator, its reference and themes

**Library reference**

- [Capabilities at a glance](#capabilities-at-a-glance): what the build produces and checks
- [Ecosystem comparison](#ecosystem-comparison): not applicable to a website
- [Benchmarks](#benchmarks): not applicable to a website
- [Features](#features): pages and structure
- [Configuration](#configuration): `ssg.toml` and the content schema
- [Examples](#examples): not applicable to a website

**Operational**

- [When not to use static-site-generator.com](#when-not-to-use-static-site-generatorcom): where the reference lives instead
- [Development](#development): make targets and CI
- [Security](#security): CSP, SRI and supply chain
- [Documentation](#documentation): where each part is described
- [Stability guarantees](#stability-guarantees): URLs and build output
- [License](#license)

---

## Install

### As a website project

```bash
git clone https://github.com/sebastienrousseau/shokunin.github.io.git
cd shokunin.github.io
```

Install `ssg` 0.0.69 or newer from its
[releases](https://github.com/sebastienrousseau/static-site-generator/releases)
or with `cargo install ssg`.

---

## Requirements

- **ssg** 0.0.69 or newer on `PATH` (CI pins the 0.0.69 release by SHA-256).
- **Python** 3.11 or newer, for the build scripts.
- **Chrome or Chromium**, for the per-page social images in `make build`
  and for `make screenshot`. Set `CHROME` to choose the binary. On macOS
  with the display asleep, full Chrome can hang in headless mode; a
  `chrome-headless-shell` binary does not.

---

## Quick Start

```bash
make build   # build into docs/ and run every check
make serve   # build, then serve on http://127.0.0.1:8000
```

`make build` fails if any check fails, so a passing build is a deployable one.

---

## The static-site-generator.com ecosystem

static-site-generator.com is the homepage of Static Site Generator (ssg),
the Rust static site generator formerly called Shokunin, and is generated
by it:
[Static Site Generator](https://github.com/sebastienrousseau/static-site-generator).

| Component | Purpose | Use case |
| :--- | :--- | :--- |
| shokunin.github.io | This repository: content, layouts and build scripts | Changing the website |
| static-site-generator | The generator the site documents; its source, README, CHANGELOG, SECURITY.md and release binaries are the source of every fact here | Using ssg |
| Velocity theme | The design, from ssg-themes.github.io (MIT, see `LICENSES/`), with its accent taken from the ssg logo | Restyling the site |
| Static Site Generator | Builds and audits the site | Building locally and in CI |

---

## Capabilities at a glance

| Area | Capability | Status |
| :--- | :--- | :--- |
| Build | ssg compiles `_posts/` with `_layouts/` into `docs/` | Stable |
| Colour | `scripts/contrast.py` holds every text pair to 7:1 and every UI pair to 3:1, in light and both dark blocks, including any rule that sets both `color` and `background` | Enforced in CI |
| Checks | ssg quality gate (10/10 required), heading anchors, cross-page `#fragment` links, SRI hashes, `ssg audit` | Enforced in CI |
| Deploy | GitHub Actions builds and deploys to GitHub Pages; nothing built is committed | Stable |
| Search | ssg's search widget in the header slot | Stable |
| Structured data | WebSite, SoftwareApplication, Person, WebPage | Stable |
| Social images | One 1200x630 Open Graph image per page, rendered at build time by `scripts/og_images.py` | Enforced in CI |

---

## Ecosystem comparison

Not applicable: this repository is a website, not a library.

---

## Benchmarks

Not applicable: this repository is a website.

---

## Features

- Sixteen pages: home, features, getting started, command reference,
  Formerly Shokunin (the rename and the old flags), security, FAQ, about, changelog, contributing,
  contact, accessibility, privacy, terms, colophon and 404.
- A shared header and footer in `_layouts/`, written once for the site.
- Every fact about ssg is taken from its repository (source, README,
  CHANGELOG, SECURITY.md, CONTRIBUTING.md) and, where the repository
  disagrees with itself, from the 0.0.69 release binary and crates.io; the
  commands on the site were run with that binary.

---

## Configuration

- `ssg.toml`: site name, description, `base_url` and the content, template
  and output directories.
- `_posts/content.schema.toml`: the front-matter fields every page must
  carry; ssg fails the build when one is missing.

---

## Examples

Not applicable: this repository is a website. ssg's examples are on the
site's [getting started page](https://static-site-generator.com/getting-started/).

---

## When not to use static-site-generator.com

The site introduces ssg. The reference is the static-site-generator
repository and the API reference at
<https://docs.static-site-generator.com/>; when they disagree with this
site, they win. Themes live at <https://themes.static-site-generator.com/>.

---

## Development

```bash
make build       # contrast, ssg build, anchors, post-build checks, og images, ssg audit
make serve       # build and serve locally
make screenshot  # render static/images/screenshot.png from the build
make clean       # remove build output
```

`.github/workflows/quality-gate.yml` runs `make build` on every pull request.
`.github/workflows/pages.yml` runs it on `main` and deploys `docs/` to
GitHub Pages.

---

## Security

Every page carries a strict Content Security Policy: scripts, styles and
images from this origin only, and form submissions to this origin and
Formspree. Every local script and stylesheet carries a Subresource Integrity
hash, which the build verifies against the file. CI installs ssg from its
release and checks the archive against a pinned SHA-256.

Report vulnerabilities according to [`SECURITY.md`](SECURITY.md).

---

## Documentation

- The website: <https://static-site-generator.com/>
- ssg: <https://github.com/sebastienrousseau/static-site-generator>
- The API reference: <https://docs.static-site-generator.com/>
- Themes: <https://themes.static-site-generator.com/>
- Static Site Generator: <https://github.com/sebastienrousseau/static-site-generator>
- Third-party licences: [`LICENSES/`](LICENSES/)

---

## Stability guarantees

The site moved from shokunin.one to static-site-generator.com in 0.0.3;
page paths are unchanged, including `/migration/`, now titled Formerly
Shokunin. The sitemap is dated by the last commit, and CI pins the ssg
release it builds with.

---

## License

The site's source is available under [Apache-2.0](LICENSE-APACHE) or
[MIT](LICENSE-MIT), at your option. The Velocity theme files in `_layouts/` are
MIT-licensed; see [`LICENSES/`](LICENSES/). ssg itself is MIT OR
Apache-2.0. The logo in `static/logo.svg` is ssg's, from
`cloudcdn.pro/static-site-generator/images/logos/static-site-generator.svg`,
the image the ssg README shows.

