---

# Front Matter (YAML)

author: "Sebastien Rousseau"
banner_alt: "Pink Cherry Blossom In Close Up Photography"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/unsplash/images/banners/masaaki-komori-3SWDMwyBFLI-unsplash.jpg"
cdn: "https://kura.pro"
changefreq: "weekly"
charset: "utf-8"
cname: ""
copyright: "© Copyright 2024 - Shokunin Static Site Generator. All rights reserved."
date: "Mar 04, 2024"
description: "Install Shokunin on macOS, Linux, Windows, and leverage its simplicity and power to create static websites, blogs and microsites with ease."
download: "https://github.com/sebastienrousseau/shokunin/archive/refs/tags/v0.0.14.zip"
format-detection: "telephone=no"
hreflang: "en"
icon: "https://kura.pro/shokunin/images/favicon.ico"
id: "https://shokunin.one/installation/index.html"
image_alt: "Logo of Shokunin, a powerful, Rust-based Static Site Generator"
image_height: "630"
image_width: "1200"
image: "https://kura.pro/shokunin/images/logos/shokunin.webp"
keywords: "Shokunin, installation, prerequisites, SSG, static site generator, Rust, macOS, Linux, Windows, fast, easy"
language: "en-GB"
layout: "page"
locale: "en_GB"
logo_alt: "Logo of Shokunin, a powerful, Rust-based Static Site Generator"
logo_height: "33"
logo_width: "181"
logo: "https://kura.pro/shokunin/images/titles/title-shokunin.webp"
menu: "active"
measurementID: "G-8MGBE9BCZC"
name: "Installation"
permalink: "https://shokunin.one/installation/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "shokunin"
subtitle: "Installation instructions, and documentation for Shokunin Static Site Generator (SSG)"
tags: "Shokunin, SSG, installation, prerequisites, Rust, macOS, Linux, Windows, fast, easy"
theme_color: "181, 0, 0"
title: "Shokunin Installation Prerequisites: Get the Fastest SSG"
url: "https://shokunin.one"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://shokunin.one/installation/rss.xml"
category: "Software, Static Site Generator, Rust"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin SSG (version 0.0.26)"
item_description: "Install Shokunin on macOS, Linux, Windows, and leverage its simplicity and power to create static websites, blogs and microsites with ease."
item_guid: "https://shokunin.one/installation/rss.xml"
item_link: "https://shokunin.one/installation/rss.xml"
item_pub_date: "Mon, 04 Mar 2024 06:06:06 +0100"
item_title: "Shokunin Installation Prerequisites: Get the Fastest SSG"
last_build_date: "Mon, 04 Mar 2024 06:06:06 +0100"
managing_editor: "contact@shokunin.one"
pub_date: "Mon, 04 Mar 2024 06:06:06 +0100"
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
msapplication-TileColor: "181, 0, 0"
msapplication_tile_image: "https://kura.pro/shokunin/images/logos/shokunin.svg"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary"
twitter_creator: "@wwdseb"
twitter_description: "Install Shokunin on macOS, Linux, Windows, and leverage its simplicity and power to create static websites, blogs and microsites with ease."
twitter_image: "https://kura.pro/shokunin/images/logos/shokunin.svg"
twitter_image_alt: "Logo of Shokunin, a powerful, Rust-based Static Site Generator"
twitter_site: "@wwdseb"
twitter_title: "Shokunin Installation Prerequisites: Get the Fastest SSG"
twitter_url: "https://shokunin.one/installation/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://shokunin.one"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Thanks for reading!"
site_last_updated: "2024-03-04"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

![divider][divider].class=\"m-10 w-100\"

## Installation

It takes just a few minutes to get up and running with Shokunin Static Site Generator (SSG).

To install Shokunin Static Site Generator (SSG), you need to have the Rust toolchain installed on your machine. You can install the Rust toolchain by following the instructions on the [Rust website][01].

Once you have the Rust toolchain installed, you can install Shokunin Static Site Generator (SSG) using the following command:

```shell
cargo install ssg
```

For simplicity, we have given Shokunin Static Site Generator (SSG) a simple alias `ssg` which can stand for `Shokunin Site Generator` or `Static Site Generator`.

You can then run the help command to see the available options and commands:

```shell
ssg --help
```

### Requirements

The minimum supported Rust toolchain version is currently Rust
**1.72.0** or later (stable). It is recommended that you install the
latest stable version of Rust.

### Platform support

Shokunin Static Site Generator (SSG) is supported and tested on the following
platforms and architectures as part of our [CI/CD pipeline][05].

This list is based on the [Rust Platform Support][06] list.

The [GitHub Actions][05] shows the platforms in which the Shokunin Static Site Generator (SSG) library tests are run.

### Documentation

**Info:**
You can find our documentation on [docs.rs][03], [lib.rs][04] and [crates.io][02].

## Usage

### Command Line Interface (CLI)

The Shokunin Static Site Generator (SSG) library runs in a Terminal window and can be used to generate a static website.

Here’s the first command you can enter in your Terminal window to run Shokunin Static Site Generator (SSG):

```shell
ssg  --new=docs --content=content --template=template --output=output --serve=public
```

or

```shell
ssg  -n=docs -c=content -t=template -o=output -s=public
```

This command will create a new website with the name `docs` in the current directory. It will use the `content` directory to gather the website content and the `template` directory to generate the website files. It will serve the website directly from the `docs` directory.

#### Arguments

- `-n`, `--new`: The name of the new website. (required)
- `-c`, `--content`: The directory containing the website content. (required)
- `-t`, `--template`: The directory containing the website templates. (required)
- `-o`, `--output`: The directory where the generated website files will be saved temporarily. (required)
- `-s`, `--serve`: Run the development server. (optional). The directory from which the website will be served.

### In your project

To use the Shokunin Static Site Generator (SSG) library in your project, add the following to your `Cargo.toml` file:

```toml
[dependencies]
shokunin = "0.0.26"
```

Add the following to your `main.rs` file:

```rust
extern crate ssg;
use ssg::*;
```

then you can use the Shokunin Static Site Generator (SSG) functions in your application code.

### Examples

To get started with Shokunin Static Site Generator (SSG), you can use the examples provided in the `examples` directory of the project.

To run the examples, clone the repository and run the following command in your terminal from the project root directory.

```shell
cargo run --example example
```

The command will generate a static website based on the configuration details in the `examples` directory.

```shell
use ssg::compiler::compile;
use std::path::Path;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Define the paths to the build, site, content and template directories.
    let build_path = Path::new("examples/example.com/build");
    let content_path = Path::new("examples/example.com/content");
    let site_path = Path::new("examples/example.com/public");
    let template_path = Path::new("examples/example.com/template");

    compile(build_path, content_path, site_path, template_path)?;

    Ok(())
}
```

The main() function in this code compiles a website from the `content` directory, using the `template` directory to generate the website files. The compiled website is saved in the `build` directory and served directly from the `example.com` directory.

#### Args

- `build_path:` The path to the directory where the compiled website will be saved.
- `content_path:` The path to the directory containing the website content.
- `site_path:` The path to the directory where the generated website files will be served from.
- `template_path:` The path to the directory containing the website templates.

## Quick Start

You are now ready to use Shokunin and [create amazing websites][07]!

[divider]: https://kura.pro/common/images/elements/divider.svg "Divider"
[01]: https://www.rust-lang.org/learn/get-started "Rust"
[02]: https://crates.io/crates/ssg "Crate.io"
[03]: https://docs.rs/crate/ssg/ "Docs.rs"
[04]: https://lib.rs/crates/ssg "Lib.rs"
[05]: https://github.com/sebastienrousseau/shokunin/actions "Actions"
[06]: https://forge.rust-lang.org/release/platform-support.html "Rust Platform Support"
[07]: /quick-start/index.html
[divider]: https://kura.pro/common/images/elements/divider.svg "Divider"