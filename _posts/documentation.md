---
name: "ssg"
short_name: "ssg"
title: "Command reference for ssg 0.0.69 | Static Site Generator"
description: "Reference for the ssg 0.0.69 command line: the build, dev, check, plugins, audit and deploy subcommands, their shared options, the legacy flags and the main ssg.toml keys."
keywords: "ssg command reference, ssg build options, ssg audit options, ssg.toml"
author: "Sebastien Rousseau"
date: "2026-10-26"
news_publication_date: "2026-10-26"
layout: "page"
language: "en-GB"
schema: "page"
changefreq: "monthly"
eyebrow: "Reference"
headline: "Command reference"
lead: "The ssg 0.0.69 command line, as printed by ssg --help."
nav_reference: "true"
---
## Subcommands

| Command | What it does |
| :--- | :--- |
| `ssg build` | Build the site into the configured output directory |
| `ssg dev` | Build, serve on `127.0.0.1:8000`, watch for changes and push them to the browser |
| `ssg check` | Run the build-time validators without writing output |
| `ssg plugins list` | List the build plugins in the order they run |
| `ssg audit` | Run the fifteen audit gates against a built site |
| `ssg deploy` | Build the site and ship it to a target |

## Options for build, dev and check

| Option | Meaning |
| :--- | :--- |
| `-f, --config <FILE>` | Configuration file |
| `-c, --content <DIR>` | Content directory |
| `-o, --output <DIR>` | Output directory |
| `-t, --template <DIR>` | Template directory |
| `--theme <NAME>` | Theme name, which sets the template directory |
| `-j, --jobs <N>` | Number of threads |
| `-q, --quiet` / `--verbose` | Less or more output |

`ssg build` also takes `--drafts` to include draft pages and
`--incremental` to rebuild only the pages a change affects.

## ssg audit

| Option | Meaning |
| :--- | :--- |
| `-o, --output <DIR>` | The built site, `./public` by default |
| `-f, --config <FILE>` | `ssg.toml`, for its `[audit]` section |
| `--gate <NAME>` | Run one gate only |
| `--fail-on <LEVEL>` | Severity that fails the run: `info`, `warn` or `error` (default) |
| `--json`, `--junit`, `--sarif` | Machine-readable output |
| `--no-skip-network` | Also check external links |
| `--explain` | With `--gate`, print what the gate checks |

## ssg deploy

`--target` is one of `netlify`, `vercel`, `cloudflare-pages`,
`github-pages`, `s3` or `none`. Tokens come from per-target environment
variables, for example `SSG_NETLIFY_TOKEN`; `none` builds and skips the
upload.

## Legacy flags

The bare-flag command line from the Shokunin days, such as
`ssg -n mysite` or `ssg -c content -o public -t templates`, still runs in
0.0.69 with a deprecation warning, and is due to be removed in 1.0. The
[migration page](/migration/#how-do-the-old-flags-map-to-the-new-commands)
maps it to the subcommands.

## ssg.toml

The keys this site's own `ssg.toml` uses:

```toml
site_name = "Static Site Generator"
site_title = "Static Site Generator (ssg): ..."
site_description = "..."
base_url = "https://static-site-generator.com"
language = "en-GB"

content_dir = "_posts"
template_dir = "_layouts"
output_dir = "docs"

[agents]
agents_txt = true
ai_plugin = true

[edge_headers]
targets = ["netlify", "cloudflare"]
```

The repository's `ssg.schema.json` describes every key.
