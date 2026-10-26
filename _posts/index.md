---
name: "shokunin"
short_name: "shokunin"
title: "Shokunin is now Static Site Generator (ssg)"
description: "Shokunin, the Rust static site generator, was renamed Static Site Generator (ssg) in version 0.0.36. What changed, and how to install, build and check a site with ssg 0.0.69."
keywords: "Shokunin, Shokunin static site generator, ssg, Static Site Generator, Rust static site generator, cargo install ssg"
author: "Sebastien Rousseau"
date: "2026-10-26"
news_publication_date: "2026-10-26"
layout: "index"
language: "en-GB"
schema: "page"
changefreq: "weekly"
eyebrow: "Shokunin, renamed"
headline: "Shokunin is now Static Site Generator"
lead: "The Rust static site generator once called Shokunin has been named Static Site Generator, or ssg, since version 0.0.36. Same crate, same author, and a build that checks the site it produces."
---
## What happened to Shokunin?

Shokunin was the name of a static site generator written in Rust by
[Sebastien Rousseau](https://sebastienrousseau.com/), first committed in
March 2023 and always published on crates.io as
[`ssg`](https://crates.io/crates/ssg). In version 0.0.36, released in April 2026, every
reference to "Shokunin" in the project was renamed to "Static Site
Generator". The crate name, the `ssg` command and the repository's history
carried on. The [migration page](/migration/) covers what changed for
people who used the old command line.

## What is ssg today?

A static site generator that compiles Markdown content with HTML templates
into a site, and checks the result as it goes: a ten-pillar quality gate on
every build, and fifteen audit gates you can run on the output, covering
accessibility, structured data, the content security policy, Subresource
Integrity, links, metadata and feeds. The [features page](/features/) lists
what it does; this site is built with it.

## Where is the official documentation?

In the [static-site-generator repository](https://github.com/sebastienrousseau/static-site-generator) and the API reference on
[docs.rs](https://docs.rs/ssg). This site summarises them for people who
know the project as Shokunin; when the two disagree, the repository wins.

## How do I start?

```bash
cargo install ssg
```

The [getting started guide](/getting-started/) goes from there to a built
and audited site.
