---
name: "ssg"
short_name: "ssg"
title: "Formerly Shokunin: the rename and the old flags | Static Site Generator"
description: "Static Site Generator was called Shokunin until version 0.0.36. What the rename changed, and how the Shokunin-era command line maps to the ssg subcommands."
keywords: "shokunin, shokunin rename, shokunin to ssg, ssg legacy flags"
author: "Sebastien Rousseau"
date: "2026-10-26"
news_publication_date: "2026-10-26"
layout: "page"
language: "en-GB"
schema: "page"
changefreq: "monthly"
eyebrow: "Formerly Shokunin"
headline: "Formerly Shokunin"
lead: "The name changed in 0.0.36. The crate and the command did not."
nav_migration: "true"
---
## What changed?

Version 0.0.36, released on 13 April 2026, renamed every reference to
"Shokunin" to "Static Site Generator". The crate has always been
[`ssg`](https://crates.io/crates/ssg) on crates.io and the command has always been `ssg`. Since
the rename the command line has grown subcommands, introduced in 0.0.43.

## How do the old flags map to the new commands?

| Shokunin-era command | ssg 0.0.69 |
| :--- | :--- |
| `ssg -n=mysite` | Still supported, with a deprecation warning |
| `ssg -c content -o public -t templates` | `ssg build -c content -o public -t templates` |
| `ssg ... -s public -w` (serve and watch) | `ssg dev` |
| `ssg --validate` | `ssg check` |

The old forms print `legacy CLI form deprecated` and are due to be removed in
1.0, so move scripts and CI jobs to the subcommands now. Expect an older
template that loads third-party scripts or inline code to need changes
before `ssg audit` passes.
