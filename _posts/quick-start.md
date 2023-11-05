---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: ""
banner_height: ""
banner_width: ""
banner: ""
cdn: "https://kura.pro"
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© Copyright 2023 - Shokunin Static Site Generator. All rights reserved."
date: "Oct 24, 2023"
description: "Leverage the simplicity and power of Shokunin, a cutting-edge Static Site Generator (SSG) created for speed and flexibility."
format-detection: "telephone=no"
hreflang: "en"
icon: "https://kura.pro/shokunin/images/favicon.ico"
id: "https://shokunin.one/quick-start/index.html"
image_alt: "Logo of Shokunin, a powerful, Rust-based Static Site Generator"
image_height: "630"
image_width: "1200"
image: "https://kura.pro/shokunin/images/logos/shokunin.webp"
keywords: "Shokunin,static site generator,SSG,website,quick start guide,beginner,tutorial,build a website,deploy a website,local web server,GitHub Pages"
language: "en-GB"
layout: "page"
locale: "en_GB"
logo_alt: "Logo of Shokunin, a powerful, Rust-based Static Site Generator"
logo_height: "33"
logo_width: "181"
logo: "https://kura.pro/shokunin/images/titles/title-shokunin.webp"
menu: "active"
measurementID: "G-8MGBE9BCZC"
name: "Documentation"
permalink: "https://shokunin.one/quick-start/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "shokunin"
subtitle: "Installation instructions, and documentation for Shokunin Static Site Generator (SSG)"
tags: "Shokunin,SSG,website,tutorial,beginner,build,deploy,local,server,GitHub,Pages"
theme_color: "rgb(255, 39, 34)"
title: "Shokunin Quick Start Guide: Get up and running quickly"
url: "https://shokunin.one"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://shokunin.one/quick-start/rss.xml"
category: "Software, Static Site Generator, Rust"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.20)"
item_description: "Leverage the simplicity and power of Shokunin, a cutting-edge Static Site Generator (SSG) created for speed and flexibility."
item_guid: "https://shokunin.one/quick-start/rss.xml"
item_link: "https://shokunin.one/quick-start/rss.xml"
item_pub_date: "2023-10-24T20:24:20+00:00"
item_title: "Shokunin - RSS Feed"
last_build_date: "2023-10-24T20:24:20+00:00"
managing_editor: "contact@shokunin.one"
pub_date: "2023-10-24T20:24:20+00:00"
ttl: "60"
type: "website"
webmaster: "contact@shokunin.one"

# Apple - The Apple front matter (YAML).

apple_mobile_web_app_orientations: "portrait"
apple_touch_icon_sizes: "192x192"
apple-mobile-web-app-capable: "yes"
apple-mobile-web-app-status-bar-inset: "black"
apple-mobile-web-app-status-bar-style: "black-translucent"
apple-mobile-web-app-title: "Shokunin, a powerful, Rust-based Static Site Generator"
apple-touch-fullscreen: "yes"

# MS Application - The MS Application front matter (YAML).

msapplication-config: "/browserconfig.xml"
msapplication-tap-highlight: "no"
msapplication-TileColor: "rgb(255, 39, 34)"
msapplication_tile_image: "https://kura.pro/shokunin/images/logos/shokunin.svg"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary"
twitter_creator: "@wwdseb"
twitter_description: "Leverage the simplicity and power of Shokunin, a cutting-edge Static Site Generator (SSG) created for speed and flexibility."
twitter_image: "https://kura.pro/shokunin/images/logos/shokunin.svg"
twitter_image_alt: "Logo of Shokunin, a powerful, Rust-based Static Site Generator"
twitter_site: "@wwdseb"
twitter_title: "Shokunin Quick Start Guide: Get up and running quickly"
twitter_url: "https://shokunin.one/quick-start/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://shokunin.one"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Thanks for reading!"
site_last_updated: "2023-10-24"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

![Divider][00].class=\"m-10 w-100\"

## 4 easy steps to build a website with Shokunin

Let's learn how to build a website with the Shokunin Static Site Generator (SSG) in 4 easy steps:

### 1. Download the Kaishi starter template

First let's download [Kaishi][01], a simple starter template based on
[Bootstrap ⧉][04]. This guide will show you how to set up Kaishi, from creating
a website to deployment on your server.

Download the Kaishi Starter Template from our [website ⧉][02] or directly via
[Github ⧉][03].

### 2. Unzip the package

Unzip the package and rename the `kaishi` folder to your project name.

```shell
unzip kaishi.zip
mv kaishi mysite
```

#### Understanding the Kaishi folder directory

The Kaishi Starter Template is organised in a way that allows for simple content
management and website organisation. It has the following folders and files
inside:

```shell
kaishi
├── README.md
├── content
│   ├── 404.md
│   ├── contact.md
│   ├── features.md
│   ├── index.md
│   ├── offline.md
│   ├── privacy.md
│   └── terms.md
└── template
    ├── contact.html
    ├── index.html
    ├── main.js
    ├── page.html
    └── sw.js

3 directories, 13 files
```

The content and presentation are separate, so you can change the site's look and
feel without changing its content. The `content` directory stores Markdown files,
while the `template` directory holds HTML and Javascript files. This template
should be used as a starting point for your website and can be modified to suit
your needs.

#### Change to the project directory

```shell
cd mysite
```

### 3. Generate the new site

```shell
ssg  -n=docs -c=content -t=template -o=output -s=public
```

The `ssg` command will generate a new site in the `docs` directory using the
content from the `content` directory and the template from the `template`
directory. The generated site will be stored in the `docs` directory. The
`public` and the `output` directories are used during the build process and can
be safely ignored. The `ssg` command will also start a local web server on port
`8000` to serve the generated site.

You can now look at the generated site by opening the following url in your
browser:

<http://127.0.0.1:8000/>

### 4. Deploy the site (optional)

You can deploy the site to your server by copying the `docs` directory to your
server. You can also use a CI/CD pipeline to automate the deployment process.
For example, you can use [GitHub Pages ⧉][05] to host your site for free.

Congratulations! You have successfully created your first website with Shokunin.
If you would like to contribute to Shokunin, please check out our
[instructions on how to contribute][06].

[00]: https://kura.pro/common/images/elements/divider.svg "Horizontal Line"
[01]: https://kaishi.one "Website of Kaishi, a Starter Template for Shokunin"
[02]: https://kaishi.one/kaishi.zip "Package of Kaishi Starter Template"
[03]: https://github.com/sebastienrousseau/kaishi.github.io "Kaishi Starter Template on GitHub"
[04]: https://getbootstrap.com/ "Bootstrap Website"
[05]: https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site "GitHub Pages"
[06]: /contribute/index.html "Contribute to Shokunin"
