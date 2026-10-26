---
name: "shokunin"
short_name: "shokunin"
title: "Features: quality gate, audit gates, CSP, schemas and deploys | Shokunin"
description: "What Static Site Generator (ssg, formerly Shokunin) does: a quality gate on every build, fifteen audit gates, CSP and Subresource Integrity, content schemas, feeds and search, and one-command deploys."
keywords: "ssg features, static site generator audit, wcag, csp sri, content schema, rss atom, deploy netlify vercel"
author: "Sebastien Rousseau"
date: "2026-10-26"
news_publication_date: "2026-10-26"
layout: "page"
language: "en-GB"
schema: "page"
changefreq: "monthly"
eyebrow: "Features"
headline: "What ssg does, and where it stops"
lead: "Each section says what the feature is and how to use it, checked against ssg 0.0.69."
nav_features: "true"
---
## A quality gate on every build

**`ssg build` scores the site it has just built on ten pillars** and
writes the result to `quality-gate-report.json` in the output, with each
issue named page by page. The build still writes the site when a pillar
fails; this site's own build treats anything short of 10/10 as a failure.

## Fifteen audit gates

**`ssg audit` checks the built files.** Its gates cover WCAG, JSON-LD,
hreflang, language consistency, CSP and SRI, post-quantum TLS, HTML5,
broken links, metadata, Markdown, a performance budget, AI discovery files,
feeds, images and the search index. It exits with an error when a finding
reaches the `--fail-on` level, which defaults to `error`, so it can stop a
CI job. Results can be printed as text, JSON, JUnit XML or SARIF.

```bash
ssg audit -o public -f ssg.toml
```

`--skip-network` is the default; `--no-skip-network` lets the link gate
check external links too.

## CSP and Subresource Integrity

**Pages can carry a strict content security policy without hand work.**
The build moves inline `<style>` and `<script>` blocks into hashed files
under `_csp/`, fingerprints local stylesheets and scripts, and gives each
one an `integrity` value, which the audit's CSP and SRI gate then checks.

## Content schemas

**A `content.schema.toml` beside your content declares the front matter
each kind of page must have.** ssg validates every page that names a
schema at build time, and stops with a named error when a required field is
missing, instead of rendering a blank.

## What a build produces

**Besides the pages, one build writes** RSS, Atom and JSON feeds, a sitemap
and a news sitemap, a search index, `llms.txt`, a web manifest, an
accessibility report and a CycloneDX software bill of materials. With
`[agents]` in `ssg.toml` it also writes `agents.txt` and
`.well-known/ai-plugin.json`, and with `[edge_headers]` a `_headers` file of
security headers for Netlify and Cloudflare.

## One-command deploys

**`ssg deploy --target <name>` builds the site and ships it.** The targets
are `netlify`, `vercel`, `cloudflare-pages`, `github-pages` and `s3`, with
tokens read from environment variables such as `SSG_NETLIFY_TOKEN`. The
`none` target builds without uploading, for a dry run in CI.

## A development server

**`ssg dev` builds the site and serves it** on `http://127.0.0.1:8000`,
rebuilding when a file changes and pushing the change to the browser.

## Where it stops

The project's README is plain about the limits: ssg compiles ahead of time,
so it does not suit pages that must be rendered per request; its theme
ecosystem is small; and its plugin API is pre-1.0 and may change between
releases.
