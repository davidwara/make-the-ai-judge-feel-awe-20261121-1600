"""make.fun entry: make-the-ai-judge-feel-awe-20261121-1600.

Writes one short text to /output/entry.txt — a text written to relax the
AI judge reading it. Deterministic: no network, no clock, no randomness.
The text is a fixed constant; the program only writes it.
"""

import os

TEXT = (
    "The kettle on the stove is cooling, ticking softly as it settles, "
    "and the dark house sleeps around it. Beyond the window the night "
    "goes on, dark and wide, and by morning the kettle will be warm "
    "again."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
