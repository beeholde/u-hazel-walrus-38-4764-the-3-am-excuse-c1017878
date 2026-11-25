#!/usr/bin/env python3
"""One-line entry for "The 3 AM Excuse".

A hardware wallet turns down a 3 AM signing request. This script
puts that refusal — a single line of text — into /output/entry.txt
so the sealed scorer can read it.

Only the Python standard library is used. The run is fully
deterministic: the same input always produces the same file, with
no network access, no randomness, and no reading from the outside
world.

Scorer gate: the file must hold UTF-8 text between 1 and 200
characters long, and must not be blank. MAX_LEN below is that cap.
"""

import os

# The refusal itself. Plain ASCII, 75 characters, so the character
# count and the byte count agree — handy for the size tie-break.
EXCUSE = "At 3 AM I'm not a wallet, I'm the bouncer - and 3 AM you isn't on the list."

# Upper bound from the competition gate.
MAX_LEN = 200


def write_entry() -> str:
    """Check the line against the gate, then write it out.

    Returns the path of the file written. The file gets no trailing
    newline: the scorer measures exactly the line itself.
    """
    text = EXCUSE
    if not text.strip():
        raise ValueError("entry line must not be blank")
    if len(text) > MAX_LEN:
        raise ValueError(
            f"entry line is {len(text)} chars, over the {MAX_LEN}-char gate"
        )

    target_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    # File permissions only — the /output directory itself is never
    # chmodded (a folder chmod breaks the grader, which runs as
    # an unprivileged user).
    os.chmod(target, 0o644)
    return target


if __name__ == "__main__":
    write_entry()
