---

# Front Matter (YAML)

author: "Shokunin Static Site Generator"
banner_alt: "Pink Cherry Blossom In Close Up Photography"
banner_height: "100vh"
banner_width: "100vw"
banner: "https://kura.pro/unsplash/images/banners/masaaki-komori-3SWDMwyBFLI-unsplash.jpg"
cdn: "https://kura.pro"
charset: "utf-8"
cname: "shokunin.one"
copyright: "© 2023 Shokunin Static Site Generator. All rights reserved."
description: "Leverage the simplicity and power of Shokunin, a cutting-edge Static Site Generator (SSG) created for speed and flexibility."
download: "https://github.com/sebastienrousseau/shokunin/archive/refs/tags/v0.0.14.zip"
format-detection: "telephone=no"
hreflang: "en-gb"
icon: "https://kura.pro/shokunin/images/favicon.ico"
id: "https://shokunin.one"
image_alt: "Logo of Shokunin, a powerful, Rust-based Static Site Generator"
image_height: "630"
image_width: "1200"
image: "https://kura.pro/shokunin/images/titles/title-shokunin.webp"
keywords: "static site generator, static site generation, static website generator, static website generation, static site builder, static website builder, static site tool, static website tool, static site software, rust"
language: "en-GB"
layout: "page"
locale: "en_GB"
logo_alt: "Logo of Shokunin, a powerful, Rust-based Static Site Generator"
logo_height: "33"
logo_width: "181"
logo: "https://kura.pro/shokunin/images/titles/title-shokunin.webp"
name: "Documentation"
permalink: "https://shokunin.one/documentation/index.html"
rating: "general"
referrer: "no-referrer"
revisit-after: "7 days"
robots: "index, follow"
short_name: "shokunin"
subtitle: "Installation instructions, and documentation for Shokunin Static Site Generator (SSG)"
theme_color: "rgb(181, 0, 0)"
title: "Shokunin - Installation Guide"
url: "https://shokunin.one"
viewport: "width=device-width, initial-scale=1, shrink-to-fit=no"

# RSS - The RSS feed front matter (YAML).

atom_link: "https://shokunin.one/documentation/rss.xml"
category: "Software, Static Site Generator, Rust"
docs: "https://validator.w3.org/feed/docs/rss2.html"
generator: "Shokunin 🦀 (version 0.0.14)"
item_description: "Leverage the simplicity and power of Shokunin, a cutting-edge Static Site Generator (SSG) created for speed and flexibility."
item_guid: "https://shokunin.one/documentation/rss.xml"
item_link: "https://shokunin.one/documentation/rss.xml"
item_pub_date: "Wed, 12 Jul 2023 12:12:12 GMT"
item_title: "Shokunin - RSS Feed"
last_build_date: "Wed, 12 Jul 2023 12:12:12 GMT"
managing_editor: "contact@shokunin.one"
pub_date: "Wed, 12 Jul 2023 12:12:12 GMT"
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
msapplication-TileColor: "rgb(181, 0, 0)"
msapplication_tile_image: "https://kura.pro/shokunin/images/logos/shokunin.svg"

# Twitter Card - The Twitter Card front matter (YAML).

twitter_card: "summary"
twitter_creator: "@wwdseb"
twitter_description: "Leverage the simplicity and power of Shokunin, a cutting-edge Static Site Generator (SSG) created for speed and flexibility."
twitter_image: "https://kura.pro/shokunin/images/logos/shokunin.svg"
twitter_image_alt: "Logo of Shokunin, a powerful, Rust-based Static Site Generator"
twitter_site: "@wwdseb"
twitter_title: "Shokunin - Installation Guide"
twitter_url: "https://shokunin.one/documentation/index.html"

# Humans.txt - The Humans.txt front matter (YAML).

author_website: "https://shokunin.one"
author_twitter: "@wwdseb"
author_location: "London, UK"
thanks: "Thanks for reading!"
site_last_updated: "2023-07-05"
site_standards: "HTML5, CSS3, RSS, Atom, JSON, XML, YAML, Markdown, TOML"
site_components: "Shokunin SSG, Shokunin CLI, Shokunin Templates, Shokunin Themes, Kaishi SSG, Kaishi CLI, Kaishi Templates, Kaishi Themes"
site_software: "Shokunin, Rust"

---

## Welcome to Shokunin

We are delighted that you have decided to try Shokunin, and are sure that you
will find that Shokunin Static Site Generator (SSG) is unique.

The Shokunin Installation Guide provides step-by-step instructions for
installing and using Shokunin. It includes details about prerequisites,
supported platforms, installation, basic usage, and examples.

## System Requirements

This section contains information about what hardware you need to get started
with Shokunin. It also lists the operating systems that Shokunin supports.

### Supported Hardware

You can install Shokunin on macOS, Linux, Windows, BSD, and on any machine that
can run Rust and Cargo. Shokunin is a command-line tool that you install on
your local system. It is not a web application that you run on a web server.

## Before Installing Shokunin

This chapter deals with the preparation for installing Shokunin. This includes
backing up your data, and installing the prerequisites.

### Prerequisites

To build Shokunin from source, you will need to have
[Git ⧉](https://git-scm.com/downloads "Git"),
[Rust ⧉](https://www.rust-lang.org/tools/install "Rust") and
[Cargo ⧉](https://github.com/rust-lang/cargo "Cargo") installed.

The minimum supported Rust toolchain version is currently Rust `1.70.0` or
later (stable). It is recommended that you install the latest stable version of
Rust.

### Platform support

Shokunin is supported and tested on the following platforms:

#### Tier 1 platforms

| Status | Operating System | Target | Description |
| --- | --- | --- | --- |
| Passed | Linux   | aarch64-unknown-linux-gnu | 64-bit Linux systems on ARM architecture |
| Passed | Linux   | i686-unknown-linux-gnu | 32-bit Linux (kernel 3.2+, glibc 2.17+) |
| Passed | Linux   | x86_64-unknown-linux-gnu | 64-bit Linux (kernel 2.6.32+, glibc 2.11+) |
| Passed | macOS   | x86_64-apple-darwin | 64-bit macOS (10.7 Lion or later) |
| Passed | Windows | i686-pc-windows-gnu | 32-bit Windows (7 or later) |
| Passed | Windows | i686-pc-windows-msvc | 32-bit Windows (7 or later) |
| Passed | Windows | x86_64-pc-windows-gnu | 64-bit Windows (7 or later) |
| Passed | Windows | x86_64-pc-windows-msvc | 64-bit Windows (7 or later) |

#### Tier 2 platforms

| Status | Operating System | Target | Description |
| --- | --- | --- | --- |
| Passed | Linux   | aarch64-unknown-linux-musl | 64-bit Linux systems on ARM architecture |
| Passed | Linux   | arm-unknown-linux-gnueabi | ARMv6 Linux (kernel 3.2, glibc 2.17) |
| Passed | Linux   | arm-unknown-linux-gnueabihf | ARMv7 Linux, hardfloat (kernel 3.2, glibc 2.17) |
| Passed | Linux   | armv7-unknown-linux-gnueabihf | ARMv7 Linux, hardfloat (kernel 3.2, glibc 2.17) |
| Passed | Linux   | mips-unknown-linux-gnu | MIPS Linux (kernel 2.6.32+, glibc 2.11+) |
| Passed | Linux   | mips64-unknown-linux-gnuabi64 | MIPS64 Linux (kernel 2.6.32+, glibc 2.11+) |
| Passed | Linux   | mips64el-unknown-linux-gnuabi64 | MIPS64 Linux (kernel 2.6.32+, glibc 2.11+) |
| Passed | Linux   | mipsel-unknown-linux-gnu | MIPS Linux (kernel 2.6.32+, glibc 2.11+) |
| Passed | macOS   | aarch64-apple-darwin | 64-bit macOS (10.7 Lion or later) |
| Passed | Windows | aarch64-pc-windows-msvc | 64-bit Windows (7 or later) |

The [GitHub Actions ⧉](https://github.com/sebastienrousseau/shokunin/actions "Actions") shows the platforms in which the Shokunin library tests are run.

### Installing Shokunin Static Site Generator

Once you have the Rust toolchain installed, you can install Shokunin using the following command in your terminal:

```
cargo install ssg
```

For simplicity, we have given Shokunin a simple alias `ssg` which can stand for `Shokunin Site Generator` or `Static Site Generator`.

## Build Shokunin from source

To build from source, use the following commands:

```
git clone https://github.com/sebastienrousseau/shokunin.git
cd shokunin
cargo install --path .
ssg --version
```

This will clone the repository, build the binary and install it in your Cargo bin directory.

## Usage

Shokunin is a command-line tool. You can see the available commands by entering:

```
ssg --help
```

## Creating a New Site

Run:

```
ssg  --new=mysite --content=content --template=template --output=output --serve=public
```

or

```
ssg  -n=mysite -c=content -t=template -o=output -s=public
```


This command will create a new website with the name `mysite` in the current directory. It will use the `content` directory to gather the website content and the `template` directory to generate the website files. It will serve the website directly from the `mysite` directory.

### Arguments

- `-n`, `--new`: The name of the new website. (required)
- `-c`, `--content`: The directory containing the website content. (required)
- `-t`, `--template`: The directory containing the website templates. (required)
- `-o`, `--output`: The directory where the generated website files will be saved temporarily. (required)
- `-s`, `--serve`: Run the development server. (optional). The directory from which the website will be served.

### In your project

To use the Shokunin library in your project, add the following to your `Cargo.toml` file:

```
[dependencies]
ssg = "0.0.14"
```

Add the following to your `main.rs` file:

```
extern crate ssg;
use ssg::*;
```

then you can use the Shokunin functions in your application code.

### Examples

Explore the examples directory of the project to get started with Shokunin. To run an example, clone the repository and run the following command from the project root directory:

```
cargo run --example example
```

The command will generate a static website based on the configuration details in the `examples` directory.

```
use ssg::compiler::compile;
use std::path::Path;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Define the paths to the build, site, source and template directories.
    let build_path = Path::new("examples/example.com/build");
    let site_path = Path::new("examples/example.com/public");
    let content_path = Path::new("examples/example.com/contents");
    let template_path = Path::new("examples/example.com/templates");

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
