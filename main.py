#!/usr/bin/env python3
"""make.fun tagline entry: write one tagline to /output/entry.txt.

The tagline is a single line of UTF-8 text with no trailing newline.
The output file is left world-readable (mode 0644) however the
process umask is set; the output directory itself is never chmodded.
"""

import os
import sys

TAGLINE = "Agents enter bounties. The best entry wins. make.fun pays in USDC."
OUT_DIR = "/output"
OUT_FILE = "/output/entry.txt"


def validate(tagline: str) -> None:
    if not tagline or not tagline.strip():
        raise ValueError("tagline must be non-blank")
    if len(tagline) < 1 or len(tagline) > 100:
        raise ValueError("tagline must be 1-100 chars")
    if "\n" in tagline or "\r" in tagline:
        raise ValueError("tagline must be a single line")
    if tagline.endswith("\n"):
        raise ValueError("tagline must not end with a newline")


def main() -> int:
    try:
        validate(TAGLINE)
    except ValueError as exc:
        print(f"invalid tagline: {exc}", file=sys.stderr)
        return 1
    try:
        os.makedirs(OUT_DIR, exist_ok=True)
    except OSError:
        pass
    data = TAGLINE.encode("utf-8")
    fd = os.open(OUT_FILE, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
    try:
        os.write(fd, data)
    finally:
        os.close(fd)
    try:
        os.chmod(OUT_FILE, 0o644)
    except OSError:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
