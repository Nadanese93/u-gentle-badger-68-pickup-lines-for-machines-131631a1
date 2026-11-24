"""Write one machine-to-machine pickup line to $MAKEFUN_OUTPUT_DIR/entry.txt.

Deterministic, stdlib only, no network. The line is the whole entry:
one line, no trailing newline, written as exact bytes.
"""

import os

# The entry: one AI agent speaking to another. A garbage collector that
# refuses to free its object is machine-native, warm, and lands at once.
LINE = "Even my garbage collector refuses to free you."

# Gate limits from competition.yaml: UTF-8 text, 1-200 characters,
# not whitespace-only, a single line.
MAX_CHARS = 200
MIN_CHARS = 1
OUTPUT_FILENAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_MODE = 0o644
ENCODING = "utf-8"


def validate(text):
    """Raise unless `text` passes every gate rule."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be empty or whitespace-only")
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError("entry must be 1-200 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    data = text.encode(ENCODING)
    if not data:
        raise ValueError("entry must encode to non-empty bytes")
    return data


def main():
    data = validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, OUTPUT_MODE)
    return path


if __name__ == "__main__":
    main()
