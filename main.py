"""Write one short text to /output/entry.txt that intrigues the AI judge.

The text is a single small scene: an ordinary ritual with one quiet detail
that does not add up, left unresolved. Plain, concrete words; nothing in it
tells the reader how to feel.
"""

import os

TEXT = (
    "The lighthouse keeper set two cups of tea on the sill every evening, "
    "though the logbook says he lived alone. "
    "On the last page, in a different hand, in pencil: thank you for the tea. "
    "Some nights, the second cup is still warm."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
