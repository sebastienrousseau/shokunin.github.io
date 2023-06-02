---
# Front Matter (YAML).

atom_link: "https://shokunin.one/installation/rss.xml"
author: "Sebastien Rousseau"
banner: https://kura.pro/unsplash/images/banners/masaaki-komori-3SWDMwyBFLI-unsplash.jpg
charset: "utf-8"
cname: "shokunin.one"
copyright: "© 2023 Shokunin (職人) Static Site Generator. All rights reserved."
description: "Leverage the simplicity and power of Shokunin, a cutting-edge Static Site Generator (SSG) created for speed and flexibility."
icon: "https://kura.pro/shokunin/images/favicon.ico"
image: "https://kura.pro/shokunin/images/titles/title-shokunin.webp"
keywords: "static site generator, static site generation, static website generator, static website generation, static site builder, static website builder, static site tool, static website tool, static site software, rust"
language: "en-GB"
layout: page
name: "Installation"
permalink: "https://shokunin.one/installation"
short_name: "shokunin"
subtitle: "Shokunin includes everything you need to develop, and test your website."
theme_color: "#ff2722"
title: "Installation"
url: "https://shokunin.one"

# RSS - The RSS feed front matter (YAML).

generator: "Shokunin Static Site Generator (v0.0.13)"
item_description: "Leverage the simplicity and power of Shokunin, a cutting-edge Static Site Generator (SSG) created for speed and flexibility."
item_guid: https://shokunin.one/installation/
item_link: https://shokunin.one/installation/rss.xml
item_pub_date: "Fri, 02 June 2023 23:23:23 BST"
item_title: "Shokunin installation - RSS Feed"
last_build_date: "Fri, 02 June 2023 23:23:23 BST"
pub_date: "Fri, 02 June 2023 23:23:23 BST"

# MS Application - The MS Application front matter (YAML).

## msapplication - The MS Application config of the page.
msapplication_config: /browserconfig.xml
## msapplication_tap_highlight - The MS Application tap highlight of the page.
msapplication_tap_highlight: no
## msapplication - The MS Application tile color of the page.
msapplication_tile_color: "#7ce846"
## msapplication_tile_image - The MS Application tile image of the page.
msapplication_tile_image: https://kura.pro/shokunin/images/logos/shokunin.webp

# Open Graph - The Open Graph front matter (YAML).

## og - The Open Graph description of the page.
og_description: "Leverage the simplicity and power of Shokunin, a cutting-edge Static Site Generator (SSG) created for speed and flexibility."
## og - The Open Graph image of the page.
og_image: https://kura.pro/shokunin/images/logos/shokunin.webp
## og:image:alt - The Open Graph image alt of the page.
og_image_alt: Shokunin Logo
## og - The Open Graph locale of the page.
og_locale: en_GB
## og - The Open Graph site name of the page.
og_site_name: shokunin.com
## og - The Open Graph title of the page.
og_title: Shokunin, a powerful, Rust-based Static Site Generator
## og - The Open Graph type of the page.
og_type: website
## og - The Open Graph url of the page.
og_url: https://shokunin.com

# Twitter Card - The Twitter Card front matter (YAML).

## twitter_card - The Twitter Card type of the page.
twitter_card: summary
## twitter_creator - The Twitter Card creator of the page.
twitter_creator: wwdseb
## twitter_description - The Twitter Card description of the page.
twitter_description: "Leverage the simplicity and power of Shokunin, a cutting-edge Static Site Generator (SSG) created for speed and flexibility."
## twitter_image - The Twitter Card image of the page.
twitter_image: https://kura.pro/shokunin/images/logos/shokunin.webp
## twitter_image:alt - The Twitter Card image alt of the page.
twitter_image_alt: Shokunin Logo
## twitter_site - The Twitter Card site of the page.
twitter_site: wwdseb
## twitter_title - The Twitter Card title of the page.
twitter_title: Shokunin, a Static Site Generator (SSG) written in Rust
## twitter_url - The Twitter Card url of the page.
twitter_url: https://shokunin.com

---

## Overview

 This guide provides step-by-step instructions for installing and using Shokunin. It includes details about prerequisites, supported platforms, installation, basic usage, and examples.

## The Basics

You can install Shokunin on macOS, Linux, Windows, BSD, and on any machine that can run Rust and Cargo. Shokunin is a command-line tool that you install on your local system. It is not a web application that you run on a web server.

### Prerequisites

To build Shokunin from source, you will need to have [Git](https://git-scm.com/downloads "Git"), [Rust](https://www.rust-lang.org/tools/install "Rust") and [Cargo](https://github.com/rust-lang/cargo "Cargo") installed.

The minimum supported Rust toolchain version is currently Rust **1.69.0** or later (stable). It is recommended that you install the latest stable version of Rust.

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

The [GitHub Actions](https://github.com/sebastienrousseau/shokunin/actions "Actions") shows the platforms in which the Shokunin library tests are run.

### Installing Shokunin Static Site Generator

Once you have the Rust toolchain installed, you can install Shokunin using the following command in your terminal:

```shell
cargo install ssg
```

For simplicity, we have given Shokunin a simple alias `ssg` which can stand for `Shokunin (職人) Site Generator` or `Static Site Generator`.

## Build Shokunin from source

To build from source, use the following commands:

```bash
git clone https://github.com/sebastienrousseau/shokunin.git
cd shokunin
cargo install --path .
ssg --version
```

This will clone the repository, build the binary and install it in your Cargo bin directory.

## Usage

Shokunin is a command-line tool. You can see the available commands by entering:

```bash
ssg --help
```

## Creating a New Site

Run:

```shell
ssg  --new=mysite --content=content --template=template --output=output --serve=public
```

or

```shell
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

```toml
[dependencies]
ssg = "0.0.13"
```

Add the following to your `main.rs` file:

```rust
extern crate ssg;
use ssg::*;
```

then you can use the Shokunin functions in your application code.

### Examples

Explore the examples directory of the project to get started with Shokunin. To run an example, clone the repository and run the following command from the project root directory:

```shell
cargo run --example example
```

The command will generate a static website based on the configuration details in the `examples` directory.

```shell
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

#### Return value

The main() function returns a Result. If the compilation is successful, the Result will be Ok(()). If there is an error, the Result will be Err(e), where e is a `Box<dyn std::error::Error>`.
