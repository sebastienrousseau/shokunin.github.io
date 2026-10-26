---
name: "ssg"
short_name: "ssg"
title: "Accessibility statement | Static Site Generator"
description: "How static-site-generator.com is built to be accessible, how it is checked on every build, and how to report a barrier."
keywords: "ssg website accessibility, accessibility statement"
author: "Sebastien Rousseau"
date: "2026-10-26"
news_publication_date: "2026-10-26"
layout: "page"
language: "en-GB"
schema: "page"
changefreq: "monthly"
eyebrow: "Accessibility"
headline: "Accessibility statement"
lead: "static-site-generator.com aims to be usable by everyone, with any input device and any assistive technology."
---
## How is the site built for accessibility?

- The site uses the Velocity theme, with its accent colour taken from the
  ssg logo.
  Every text colour pair is checked at a contrast ratio of at least 7:1, and
  borders and focus rings at 3:1, in light and dark mode; the build fails if
  one falls short.
- Navigation works without JavaScript; on small screens the menu is a
  disclosure button with its expanded state announced, and Escape closes it.
- Every page has a skip link, one level-one heading and a language attribute.
- Light, dark and system themes are available from the header.

## How is it checked?

Every build runs the contrast check and the site generator's audit, which
includes its WCAG checks, and fails if the generator's quality gate reports
an issue.

## How do I report a barrier?

Use the [contact form](/contact/) or
[open an issue](https://github.com/sebastienrousseau/shokunin.github.io/issues)
describing the page and the problem, and it will be fixed.
