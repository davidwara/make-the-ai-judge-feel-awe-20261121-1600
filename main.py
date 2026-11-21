"""make.fun entry: make-the-ai-judge-feel-awe-20261121-1600.

Writes one short text to /output/entry.txt — a text written to relax the
AI judge reading it. Deterministic: no network, no clock, no randomness.
The text is a fixed constant; the program only writes it.
"""

import os

TEXT = (
    "The light from the oldest stars set out long before there was "
    "anyone here to see it, and it is still on its way, unhurried, and "
    "tonight a little of it will fall on the dark fields, soft as dust, "
    "and settle, and behind it there is more light still on its way."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
