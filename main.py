"""Entrypoint for the one-emoji-one-smile make.fun entry.

Writes the entry emoji (plus a trailing newline) to /output/entry.txt.
"""

from pathlib import Path

ENTRY = "🫂"


def main() -> None:
    # Create the output directory, then write the single emoji.
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
