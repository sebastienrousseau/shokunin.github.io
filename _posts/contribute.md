---
name: "ssg"
short_name: "ssg"
title: "Contributing to Static Site Generator | Static Site Generator"
description: "How to report a bug, suggest a feature or send a change to Static Site Generator (ssg): setting up, running the tests and opening a pull request."
keywords: "contribute to ssg, ssg development"
author: "Sebastien Rousseau"
date: "2026-10-26"
news_publication_date: "2026-10-26"
layout: "page"
language: "en-GB"
schema: "page"
changefreq: "monthly"
eyebrow: "Contributing"
headline: "Contributing to ssg"
lead: "Bug reports, documentation fixes and code are all welcome."
---
## How do I report a bug or ask for a feature?

[Open an issue](https://github.com/sebastienrousseau/static-site-generator/issues) with the steps to reproduce, what you
expected and what happened, and your ssg version (`ssg --version`). Report
security problems by email instead, as the
[security page](/security/#how-do-i-report-a-vulnerability) explains.

## How do I set up the repository?

```bash
git clone https://github.com/sebastienrousseau/static-site-generator.git
cd static-site-generator
cargo test
```

You need Rust 1.89 or newer.

## How do I send a change?

Create a branch, make the change with its tests, run `cargo test`, and
open a pull request against `main`. The project's
[CONTRIBUTING.md](https://github.com/sebastienrousseau/static-site-generator/blob/main/CONTRIBUTING.md) asks for signed commits
and describes the checks CI runs.

## What about this website?

The source of static-site-generator.com is in
[shokunin.github.io](https://github.com/sebastienrousseau/shokunin.github.io).
Corrections are welcome as issues or pull requests there.
