#!/usr/bin/env python3
"""The 3AM Fridge Text — make.fun entry.

Writes one line of text, the message a smart fridge sends its owner
at 3am, to /output/entry.txt. Deterministic: same bytes every run.
"""
import os

LINE = (
    "Night shift, day 1,204: you, 3am, socks, spoon. "
    "The cheesecake is gone and I'm the only witness. "
    "I will testify for cake."
)


def main():
    # Self-check the gate before writing: 1-140 UTF-8 characters, not blank.
    assert 1 <= len(LINE) <= 140 and LINE.strip(), "entry violates the 140-char gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
