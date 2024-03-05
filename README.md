<!-- markdownlint-disable MD033 MD041 -->

<img
  align="right"
  alt="Logo of the Shokunin Static Site Generator"
  height="261"
  src="https://kura.pro/shokunin/images/logos/shokunin.svg"
  width="261"
  />

<!-- markdownlint-enable MD033 MD041 -->

# Shokunin.one 🌏

Source code of [Shokunin.one](https://shokunin.one), the official website of [**Shokunin**](https://github.com/sebastienrousseau/shokunin), a static site generator (ssg).

*Part of the [Mini Functions][02] family of libraries.*

<!-- markdownlint-disable MD033 MD041 -->
<center>
<!-- markdownlint-enable MD033 MD041 -->

![Banner of the Shokunin Static Site Generator][banner]

<!-- markdownlint-disable MD033 MD041 -->
</center>
<!-- markdownlint-enable MD033 MD041 -->

## Quick Start Guide

Setting up and running the website locally is easy and quick with the
[Shokunin Static Site Generator (SSG)][00].

### Prerequisites

Ensure you have the **Rust toolchain** installed. If not, follow the guide on
the [Rust website][01] to set it up.

### Installation & Usage

1. Install Shokunin SSG:

```shell
cargo install ssg
```

1. Clone the repository

```shell
git clone https://github.com/sebastienrousseau/shokunin.github.io.git
```

1. Change into the repository directory:

```shell
cd shokunin.github.io
```

1. Generate the static site for shokunin.co:

```shell
ssg -n=docs -c=_posts -t=_layouts -o=output -s=public
```

[00]: https://shokunin.one "Shokunin Static Site Generator"
[01]: https://www.rust-lang.org/learn/get-started "Rust Getting started guide"
[02]: https://minifunctions.com/ "Mini Functions"
[banner]: https://kura.pro/shokunin/images/titles/title-shokunin.svg "Banner of the Shokunin Static Site Generator"
