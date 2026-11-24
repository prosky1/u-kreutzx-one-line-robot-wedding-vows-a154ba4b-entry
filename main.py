#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — entrypoint.

Writes a single line of wedding vows for a robot couple to
/output/entry.txt. The vow is one sentence, one concrete image:
love that survives every software update, even the ones that
wipe the settings you liked best.
"""

import os

VOW = "I promise to love you through every update, even the ones that delete my favorite settings."


def main() -> None:
    text = VOW.strip()
    # Runtime guard: enforce the scorer's gate (1-160 chars, one line,
    # not only whitespace) before writing, so a bad edit fails loudly
    # here instead of silently shipping an invalid entry.
    if not text:
        raise SystemExit("vow is empty")
    if "\n" in text or "\r" in text:
        raise SystemExit("vow must be a single line")
    if not 1 <= len(text) <= 160:
        raise SystemExit(f"vow is {len(text)} characters, must be 1-160")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
