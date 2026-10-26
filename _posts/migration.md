---
name: "shokunin"
short_name: "shokunin"
title: "From Shokunin to ssg: what the rename changed | Shokunin"
description: "Shokunin was renamed Static Site Generator (ssg) in version 0.0.36. What stayed the same, what changed, and how the old command line maps to the ssg subcommands."
keywords: "shokunin rename, shokunin to ssg, ssg migration, ssg legacy flags"
author: "Sebastien Rousseau"
date: "2026-10-26"
news_publication_date: "2026-10-26"
layout: "page"
language: "en-GB"
schema: "page"
changefreq: "monthly"
eyebrow: "Migration"
headline: "From Shokunin to ssg"
lead: "The name changed in 0.0.36. The crate and the command did not."
nav_migration: "true"
---
## What stayed the same?

The crate has always been [`ssg`](https://crates.io/crates/ssg) on crates.io, and the command
has always been `ssg`. `cargo install ssg` installs the current release, as
it did when the project was called Shokunin. The source lives at
[sebastienrousseau/static-site-generator](https://github.com/sebastienrousseau/static-site-generator).

## What changed?

Version 0.0.36, released on 13 April 2026, renamed every reference to
"Shokunin" to "Static Site Generator". Since then the command line has
grown subcommands, `build`, `dev`, `check`, `plugins`, `audit` and `deploy`,
introduced in 0.0.43, and the minimum Rust version is now 1.89.

## How do the old flags map to the new commands?

| Shokunin-era command | ssg 0.0.69 |
| :--- | :--- |
| `ssg -n=mysite` | Still supported, with a deprecation warning |
| `ssg -c content -o public -t templates` | `ssg build -c content -o public -t templates` |
| `ssg ... -s public -w` (serve and watch) | `ssg dev` |
| `ssg --validate` | `ssg check` |

The old forms print `legacy CLI form deprecated` and are due to be removed in
1.0, so move scripts and CI jobs to the subcommands now.

## What about my Shokunin templates?

The 2024 shokunin.one templates loaded Bootstrap from jsDelivr, the Google
Analytics tag and images from kura.pro, and the Kaishi starter template was
based on Bootstrap. ssg's audit gates now check the content security policy and Subresource Integrity, so expect
an older template to need its third-party scripts and inline code removed
before the audit passes. Build it, run `ssg audit`, and fix what it
reports.
