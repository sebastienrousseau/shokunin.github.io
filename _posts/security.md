---
name: "shokunin"
short_name: "shokunin"
title: "Security: verifying releases and reporting vulnerabilities | Shokunin"
description: "How to check an ssg release before running it (SHA-256, OpenPGP signature, build provenance), what ssg does for your site's security, and how to report a vulnerability."
keywords: "ssg security, verify ssg release, ssg gpg signature, ssg slsa provenance, report vulnerability"
author: "Sebastien Rousseau"
date: "2026-10-26"
news_publication_date: "2026-10-26"
layout: "page"
language: "en-GB"
schema: "page"
changefreq: "monthly"
eyebrow: "Security"
headline: "Check what you install, and what you publish"
lead: "Every ssg release can be checked before it runs, and every site it builds can be checked before it ships."
nav_security: "true"
---
## How do I check a download?

Each package in a release has three companions: a `.sha256` file, an
OpenPGP `.asc` signature, and a build provenance attestation recorded with
GitHub. For the macOS arm64 archive of 0.0.69:

```bash
shasum -a 256 -c ssg-v0.0.69-aarch64-apple-darwin.tar.gz.sha256

curl -fsSLO https://raw.githubusercontent.com/sebastienrousseau/static-site-generator/main/KEYS.asc
gpg --import KEYS.asc
gpg --verify ssg-v0.0.69-aarch64-apple-darwin.tar.gz.asc \
             ssg-v0.0.69-aarch64-apple-darwin.tar.gz

gh attestation verify ssg-v0.0.69-aarch64-apple-darwin.tar.gz \
  -R sebastienrousseau/static-site-generator
```

The signing key's fingerprint is
`4B7F 16C9 09C7 A8EE 9BED 338A 4F04 7EDF 5F90 F638`.

## What does ssg do for my site's security?

It moves inline scripts and styles out of the page so a strict content
security policy can be used, adds Subresource Integrity hashes to local
stylesheets and scripts, and audits both. With `[edge_headers]` it writes a
`_headers` file of security headers for hosts that read one. See the
[features](/features/#csp-and-subresource-integrity).

## Which versions get security fixes?

Only the latest release. ssg is pre-1.0, and its security policy names the
current version as the one supported.

## How do I report a vulnerability?

Email **sebastian.rousseau@gmail.com**, the address in ssg's
[security policy](https://github.com/sebastienrousseau/static-site-generator/security/policy), with a description, steps to
reproduce and the version affected. Do not open a public issue. The policy
promises an acknowledgement within 72 hours. Machine-readable contact
details are in [/.well-known/security.txt](/.well-known/security.txt).
