---
name: "shokunin"
short_name: "shokunin"
title: "Getting started with ssg: install, scaffold, build and audit | Shokunin"
description: "Install Static Site Generator (ssg, formerly Shokunin) from crates.io or a release archive, scaffold a project, build it, serve it locally and audit the output."
keywords: "ssg getting started, cargo install ssg, ssg build, ssg audit, shokunin quick start"
author: "Sebastien Rousseau"
date: "2026-10-26"
news_publication_date: "2026-10-26"
layout: "page"
language: "en-GB"
schema: "page"
changefreq: "monthly"
eyebrow: "Getting started"
headline: "Your first site with ssg"
lead: "From nothing installed to a built site and an audit report."
nav_docs: "true"
---
## How do I install it?

With Rust 1.89 or newer, from crates.io:

```bash
cargo install ssg
ssg --version
```

Or download a prebuilt package from the
[0.0.69 release](https://github.com/sebastienrousseau/static-site-generator/releases/tag/v0.0.69): `.tar.gz` archives for Linux (glibc and musl) and
macOS, a `.zip` and an `.msi` for Windows, and `.deb`, `.rpm` and `.pkg`
packages. Each has a `.sha256` file and a `.asc` signature beside it; the
[security page](/security/#how-do-i-check-a-download) shows how to check
them.

## How do I start a project?

```bash
ssg -n mysite
cd mysite
```

This creates `config.toml`, `content/`, `data/`, `static/` and
`templates/`. It uses the older command-line form, so ssg prints a
deprecation warning; the form still works and is due to be removed in 1.0.

## How do I build it?

```bash
ssg build -f config.toml
```

The site is written to the `output_dir` in `config.toml`, `public/` in a new
project. The build prints the quality gate's score as it finishes.

## How do I preview it?

```bash
ssg dev -f config.toml
```

Open `http://127.0.0.1:8000/`. Changes to content or templates rebuild the
site and refresh the page.

## How do I check it?

```bash
ssg check -f config.toml            # validators only, writes nothing
ssg audit -o public -f config.toml  # the fifteen gates, on the built files
```

Run the audit before you deploy. On a freshly scaffolded project it reports
findings to fix, such as the placeholder `base_url`; set `base_url` to your
site's address and work through the rest.

## How do I deploy it?

```bash
ssg deploy --target github-pages -f config.toml
```

The [command reference](/documentation/#ssg-deploy) lists the other
targets.
