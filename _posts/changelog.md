---
name: "shokunin"
short_name: "shokunin"
title: "Changelog: recent ssg releases | Shokunin"
description: "What changed in recent Static Site Generator (ssg) releases, from the project's CHANGELOG: security fixes, minified inline stylesheets, SRI on highlighting stylesheets and more."
keywords: "ssg changelog, ssg 0.0.69, ssg release notes"
author: "Sebastien Rousseau"
date: "2026-10-26"
news_publication_date: "2026-10-26"
layout: "page"
language: "en-GB"
schema: "page"
changefreq: "monthly"
eyebrow: "Changelog"
headline: "Recent releases"
lead: "A summary of the ssg CHANGELOG. The full file, with every release, is in the repository."
---
## 0.0.69, 22 October 2026

- **Security:** ammonia 4.1.8, rustls-webpki 0.103.16 and webpki-roots
  1.0.10 move past RUSTSEC-2026-0373, -0381 and -0382; the fuzz workspace
  gets the same fixes, and CI now checks its advisories.
- **Inline stylesheets are minified** before they are moved into
  `_csp/`, hashed and given their SRI value.
- **A `<code>` inside `<style>`, `<script>` or a comment is left alone**
  by the repair that escapes tags in inline code spans.
- **Pages link the highlighting stylesheet the build writes,** under its
  fingerprinted name and with an `integrity` value.
- staticdatagen 0.0.26, which restores the XML declaration in
  `news-sitemap.xml` and requires Rust 1.89.

## 0.0.68, 15 October 2026

- **Security:** YAML alias amplification is refused (RUSTSEC-2026-0333),
  a page of bare email addresses no longer crashes the build, and TLS and
  HTML sanitising move past new advisories.
- **Behaviour change:** Open Graph tags use `property=`.

## 0.0.36, 13 April 2026

- **Renamed** every reference from "Shokunin" to "Static Site Generator".

The [full CHANGELOG](https://github.com/sebastienrousseau/static-site-generator/blob/main/CHANGELOG.md) covers every release.
