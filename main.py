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


def main() -> int:
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
