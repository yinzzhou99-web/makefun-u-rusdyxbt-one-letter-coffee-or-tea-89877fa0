"""One Letter: Coffee or Tea — entrypoint.

Writes exactly one letter, "A" (coffee), to /output/entry.txt.
Python 3.13 standard library only; no network, no third-party packages.
"""

import os
import shutil

LETTER = "A"
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Clear stale children of the output dir; never delete the dir itself
    # (the grader mounts it).
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.unlink(path)
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
