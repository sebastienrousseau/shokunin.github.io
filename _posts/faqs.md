---
name: "ssg"
short_name: "ssg"
title: "Frequently asked questions about ssg | Static Site Generator"
description: "Answers about Static Site Generator (ssg): the rename, installing, the minimum Rust version, the audit, themes, deploying, security and the licence."
keywords: "ssg faq, shokunin, is shokunin ssg, ssg rust version"
author: "Sebastien Rousseau"
date: "2026-10-26"
news_publication_date: "2026-10-26"
layout: "page"
language: "en-GB"
schema: "page"
changefreq: "monthly"
eyebrow: "FAQ"
headline: "Frequently asked questions"
lead: "Short answers first; each links to the page with the detail where there is one."
nav_faqs: "true"
---
## What is ssg?

Static Site Generator: an open-source static site generator written in
Rust that audits the site it builds. See the [features](/features/).

## Is Shokunin the same project as ssg?

Yes. Shokunin was renamed Static Site Generator in version 0.0.36. See
[Formerly Shokunin](/migration/).

## How do I install it?

`cargo install ssg`, or a prebuilt package from the GitHub releases. See
[getting started](/getting-started/).

## Which Rust version do I need?

Rust 1.89 or newer to build from source. The prebuilt packages need no Rust
at all.

## Does the old command line still work?

Yes, with a deprecation warning, until 1.0. See
[the flag mapping](/migration/#how-do-the-old-flags-map-to-the-new-commands).

## Where is the API reference?

At [docs.static-site-generator.com](https://docs.static-site-generator.com/).

## What does the audit check?

Fifteen gates, from WCAG and structured data to CSP, SRI, links and feeds.
See [the audit gates](/features/#fifteen-audit-gates).

## Where are the themes?

ssg resolves a theme by name with `--theme` or `theme =` in `ssg.toml`. The
published themes are on
[themes.static-site-generator.com](https://themes.static-site-generator.com/);
this site uses one of them, Prism. See [themes](/features/#themes).

## Can it deploy for me?

Yes: `ssg deploy` targets Netlify, Vercel, Cloudflare Pages, GitHub Pages
and S3. See [deploys](/features/#one-command-deploys).

## How do I know a release is genuine?

Check its SHA-256 sum, its OpenPGP signature and its provenance
attestation; the [security page](/security/#how-do-i-check-a-download)
shows the commands.

## What licence is it under?

MIT or Apache-2.0, at your option. See the [terms](/terms/).
