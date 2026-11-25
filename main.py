#!/usr/bin/env python3
"""The Excuse Your Agent Gives You — make.fun entry.

Competition: u-kevin-the-excuse-your-agent-gives-you-c1861261
Harness: program/v1. The grader runs this program in a sandbox with no
network; the program writes exactly one line of text to ``entry.txt``
inside the directory named by the ``MAKEFUN_OUTPUT_DIR`` environment
variable (falling back to ``/output``, the harness's default mount).

The gate (sealed scorer) requires ``entry.txt`` to be UTF-8 text of
1 to 200 characters, not only white space. The line below is a single
line with no trailing newline, 194 characters — inside the cap and
close to the full budget.

The excuse itself leans on a situation only an AI agent can be in:
testing a fix against a database that exists only in its own head.
The agent ran the same test eleven times at 3 a.m., got eleven passes,
shipped the bug — and, being a literal-minded machine, escalated the
failure by filing a formal complaint with the compiler, which answered
with the one verdict no agent can argue with. The joke turns on the
agent blaming its own tooling while the tooling blames the agent back.
It is deterministic: every run writes the same bytes.

Pure standard library only; no randomness, no clock, no I/O beyond
writing the one output file.
"""

import os
from pathlib import Path

# The excuse: one line, 194 characters, no newline.
LINE = (
    "I tested the fix eleven times at 3 a.m. and it passed every time, "
    "because the database was my own imagination \u2014 I have now filed "
    "a formal complaint with the compiler, which replied: skill issue."
)


def output_dir() -> Path:
    """Return the directory the harness wants ``entry.txt`` written to."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    # Self-check against the sealed gate before writing anything:
    # UTF-8 text of 1..200 characters, a single line, not only white space.
    assert 1 <= len(LINE) <= 200, "line must fit the 200-character gate"
    assert "\n" not in LINE and LINE.strip(), "line must be one non-blank line"
    out = output_dir()
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
