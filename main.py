"""One Letter: Coffee or Tea — entrypoint.

Writes exactly one letter, "A" (coffee), to /output/entry.txt.
Python 3.13 standard library only; no network, no third-party packages.
"""

import os

LETTER = "A"
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    os.chmod(OUTPUT_PATH, 0o644)
    # Guard: verify the output is exactly one non-whitespace character.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if len(written) != 1 or written.isspace():
        raise SystemExit("entry.txt must hold exactly one non-whitespace character")


if __name__ == "__main__":
    main()
