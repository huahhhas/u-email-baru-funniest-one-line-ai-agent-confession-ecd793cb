#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession.

Prints the confession from entry.txt: exactly one line, deterministic,
no network, no randomness.
"""

from pathlib import Path


def load_confession() -> str:
    return Path(__file__).with_name("entry.txt").read_text(
        encoding="utf-8"
    ).strip()


def main() -> None:
    print(load_confession())


if __name__ == "__main__":
    main()
