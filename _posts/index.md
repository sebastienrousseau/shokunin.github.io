---
name: "ssg"
short_name: "ssg"
title: "Static Site Generator (ssg): a Rust static site generator that checks what it builds"
description: "Static Site Generator (ssg) is an open-source static site generator written in Rust. It builds a site from Markdown and templates, scores it on a ten-pillar quality gate and audits the output on fifteen gates."
keywords: "Static Site Generator, ssg, Rust static site generator, cargo install ssg, accessibility audit, CSP, Subresource Integrity"
author: "Sebastien Rousseau"
date: "2026-10-26"
news_publication_date: "2026-10-26"
layout: "index"
language: "en-GB"
schema: "page"
changefreq: "weekly"
eyebrow: "Open-source, written in Rust"
headline: "A static site generator that checks what it builds"
lead: "ssg turns Markdown and templates into a site, scores every build on a ten-pillar quality gate, and audits the output on fifteen gates, from WCAG to CSP, SRI, links and feeds."
---
## What is Static Site Generator?

Static Site Generator, or ssg, is a free, open-source static site generator
written in Rust by [Sebastien Rousseau](https://sebastienrousseau.com/). It
compiles Markdown content with HTML templates into a site, and checks the
result as it goes: a ten-pillar quality gate on every build, and fifteen
audit gates you can run on the output, covering accessibility, structured
data, the content security policy, Subresource Integrity, links, metadata
and feeds. It is dual-licensed under MIT or Apache-2.0, and this site is
built with it.

## How do I install it?

```bash
cargo install ssg
```

or download a signed package from the
[GitHub releases](https://github.com/sebastienrousseau/static-site-generator/releases). The
[getting started guide](/getting-started/) goes from there to a built and
audited site.

## Where is the reference?

The API reference is at
[docs.static-site-generator.com](https://docs.static-site-generator.com/),
the themes at
[themes.static-site-generator.com](https://themes.static-site-generator.com/),
and the source, the issue tracker and every release at
[GitHub](https://github.com/sebastienrousseau/static-site-generator).

## Formerly Shokunin

Until version 0.0.36 the project was called Shokunin. The crate and the
command were always `ssg`; the [Formerly Shokunin](/migration/) page maps
the old flags to the current subcommands.
