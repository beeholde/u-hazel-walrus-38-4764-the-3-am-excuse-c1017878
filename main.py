"""The 3 AM Excuse.

Writes the entry line to /output/entry.txt: the single excuse a
hardware wallet gives for refusing to sign a transaction at 3 AM.
Standard library only, deterministic, no network, no input.

Gate (sealed scorer): /output/entry.txt must be UTF-8 text of 1 to
200 characters, not only white space. GATE_CHARS names that cap.
"""

import os

# The excuse, one line, under the 200-character gate.
# ASCII only, so characters == bytes (75/75) for the size tie-break.
LINE = "At 3 AM I'm not a wallet, I'm the bouncer - and 3 AM you isn't on the list."

# Sealed gate: entry text is 1 to GATE_CHARS characters.
GATE_CHARS = 200


def main() -> None:
    if not 1 <= len(LINE) <= GATE_CHARS or not LINE.strip():
        raise ValueError(
            f"entry must be 1 to {GATE_CHARS} non-blank characters"
        )
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
