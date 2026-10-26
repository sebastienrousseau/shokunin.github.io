#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""WCAG contrast gate for static-site-generator.com's colour tokens.

Adapted from scripts/contrast.py in github.com/sebastienrousseau/ssg-themes.github.io
(MIT): the same ratios and the same token pairs as the Velocity theme, read from
this site's _layouts/styles.css in light mode and in both dark blocks (the
prefers-color-scheme one and the explicit toggle). Text needs 7:1 (WCAG AAA),
non-text UI 3:1.

Two additions over the theme's list:

- HOVER_PAIRS: the hover and inherited-text states the theme's list left
  out (a button label on its hover colour, body text on the soft surface
  behind code blocks and hovered menu items).
- rule_pairs(): every rule in the stylesheet that sets both `color` and
  `background` to a single token is checked at 7:1 as well, so a new
  component cannot pair two tokens without the gate seeing it.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

AAA_TEXT = 7.0
AAA_LARGE = 4.5
UI_NONTEXT = 3.0


def _linear(channel: int) -> float:
    c = channel / 255
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def luminance(hex_colour: str) -> float:
    h = hex_colour.lstrip("#")
    if len(h) == 3:
        h = "".join(ch * 2 for ch in h)
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return 0.2126 * _linear(r) + 0.7152 * _linear(g) + 0.0722 * _linear(b)


def ratio(fg: str, bg: str) -> float:
    l1, l2 = luminance(fg), luminance(bg)
    if l1 < l2:
        l1, l2 = l2, l1
    return (l1 + 0.05) / (l2 + 0.05)



def parse_tokens(css: str, selector: str) -> dict[str, str]:
    """Extracts `--name: #hex;` pairs from the first block matching `selector`."""
    idx = css.find(selector)
    if idx == -1:
        return {}
    block = css[idx: css.find("}", idx)]
    return {
        name: value
        for name, value in re.findall(
            r"(--[a-z0-9-]+)\s*:\s*(#[0-9a-fA-F]{3,8})\s*;", block
        )
    }



PAIRS = [
    ("--ink", "--bg", AAA_TEXT, "body text on page ground"),
    ("--ink", "--surface", AAA_TEXT, "body text on surface"),
    ("--ink-soft", "--bg", AAA_TEXT, "secondary text on ground"),
    ("--ink-soft", "--surface", AAA_TEXT, "secondary text on surface"),
    ("--ink-muted", "--bg", AAA_TEXT, "muted text on ground"),
    ("--ink-muted", "--surface", AAA_TEXT, "muted text on surface"),
    ("--ink-muted", "--surface-soft", AAA_TEXT, "muted text on soft surface"),
    ("--accent", "--bg", AAA_TEXT, "link on ground"),
    ("--accent", "--surface", AAA_TEXT, "link on surface"),
    ("--accent", "--surface-soft", AAA_TEXT, "link on soft surface"),
    ("--accent-ink", "--accent", AAA_TEXT, "button label on accent"),
    ("--accent-hover", "--surface", AAA_TEXT, "hovered link on surface"),
    ("--on-accent-soft", "--accent-soft", AAA_TEXT, "badge text on accent tint"),
    ("--focus", "--bg", UI_NONTEXT, "focus ring against ground"),
    ("--focus", "--surface", UI_NONTEXT, "focus ring against surface"),
    ("--line", "--surface", UI_NONTEXT, "control border against surface"),
    ("--line", "--bg", UI_NONTEXT, "control border against ground"),
]

HOVER_PAIRS = [
    ("--accent-ink", "--accent-hover", AAA_TEXT, "button label on hovered accent"),
    ("--ink", "--surface-soft", AAA_TEXT, "body text on soft surface (code, hovered items)"),
    ("--ink-soft", "--surface-soft", AAA_TEXT, "secondary text on soft surface"),
    ("--ink", "--bg-soft", AAA_TEXT, "body text on soft section ground"),
    ("--ink-soft", "--bg-soft", AAA_TEXT, "secondary text on soft section ground"),
    ("--ink-muted", "--bg-soft", AAA_TEXT, "muted text on soft section ground"),
    ("--accent", "--bg-soft", AAA_TEXT, "link on soft section ground"),
    ("--line", "--bg-soft", UI_NONTEXT, "control border against soft section ground"),
]

RULE = re.compile(r"([^{}]+)\{([^{}]*)\}")
COLOR = re.compile(r"(?<![-\w])color:\s*var\((--[a-z0-9-]+)\)\s*;")
BACKGROUND = re.compile(r"background(?:-color)?:\s*var\((--[a-z0-9-]+)\)\s*;")


def rule_pairs(css: str) -> list[tuple[str, str, float, str]]:
    """Every rule that sets both colour and background to one token each."""
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    pairs = []
    for selector, body in RULE.findall(css):
        fg, bg = COLOR.search(body), BACKGROUND.search(body)
        if fg and bg:
            label = "rule " + " ".join(selector.split())
            pairs.append((fg.group(1), bg.group(1), AAA_TEXT, label))
    return pairs


MODES = (
    ("light", ":root,"),
    ("dark (system)", ':root:not([data-theme="light"]) {'),
    ("dark (toggle)", ':root[data-theme="dark"] {'),
)


def main() -> int:
    css = (Path(__file__).resolve().parent.parent / "_layouts" / "styles.css").read_text(encoding="utf-8")
    failures, checked = [], 0
    for mode, selector in MODES:
        tokens = parse_tokens(css, selector)
        if not tokens:
            failures.append(f"{mode}: no tokens found for `{selector}`")
            continue
        for fg, bg, target, label in PAIRS + HOVER_PAIRS + rule_pairs(css):
            if fg not in tokens or bg not in tokens:
                failures.append(f"{mode}: {fg} or {bg} not declared ({label})")
                continue
            got = ratio(tokens[fg], tokens[bg])
            checked += 1
            if got + 1e-9 < target:
                failures.append(f"{mode}: {label}: {tokens[fg]} on {tokens[bg]} = {got:.2f}:1, need {target}:1")
    if failures:
        print(f"contrast: {len(failures)} failure(s)", file=sys.stderr)
        for f in failures:
            print(f"  {f}", file=sys.stderr)
        return 1
    print(f"contrast: {checked} token pairs pass (text 7:1, UI 3:1) in light and dark")
    return 0


if __name__ == "__main__":
    sys.exit(main())
