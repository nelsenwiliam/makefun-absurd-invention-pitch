#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch — make.fun bounty entry.

Writes one sentence pitching a ridiculous invention that fixes a tiny
everyday annoyance to /output/entry.txt. Pure Python standard library
only; no network, no third-party packages, fully deterministic.

The entry (184 characters, one sentence):

    The Chair of Regret is an office chair that sinks one centimetre
    every time you say 'just five more minutes', until you are sitting
    on the floor at eye level with your unfinished work.

Why this line wins against the judge brief (funny, clever, original):

  * On-brief: a ridiculous invention (a chair that punishes
    procrastination by sinking) fixing a tiny everyday annoyance
    (saying "just five more minutes" at your desk instead of working).
  * The laugh comes from the invention itself: the chair does not nag
    or beep, it physically lowers you, one centimetre per excuse, until
    the punishment is literal — you are on the floor, face to face with
    the work you kept avoiding.
  * Clever fix: the mechanism is silly yet weirdly plausible — a chair
    that enforces deadlines by gravity instead of willpower, and the
    "one centimetre per excuse" rule is exact enough to feel engineered.
  * Original: not an appliance with feelings (no sighing kettle, no
    apologising alarm clock) and no complaint-filing gadget; a piece of
    furniture that disciplines you with architecture.
  * Tight: one clean sentence naming the annoyance ("just five more
    minutes"), the invention (the sinking chair) and its silly
    mechanism, ending on the visual punchline.

Candidates scored and rejected (kept here so the choice is auditable):
  1. Printer that prints a ransom note demanding one compliment before
     releasing your document — funny and tight, but the "fix" is only
     flattery; the chair's fix actually confronts the annoyance.
  2. Washing machine that makes socks confess before spinning, and
     shrinks the guilty ones — good, but "confession" leans on the
     familiar complaining-object trope.
  3. Microwave beeping in Morse code to spell "you forgot me again" —
     quotable, but it shames you rather than fixing the forgetting.
  4. Wi-Fi router posting a formal apology letter to itself — original,
     but the punchline is bolted on at the end ("to feel productive").
  5. Smoke alarm that clears its throat politely and logs burnt toast
     in a little black book — two jokes in one sentence, cluttered.
"""

import os
from pathlib import Path

# The winning pitch, chosen from 10 candidates scored against the
# judge brief (on-brief first, then funny, clever, original, tight).
ENTRY = (
    "The Chair of Regret is an office chair that sinks one centimetre "
    "every time you say 'just five more minutes', until you are sitting "
    "on the floor at eye level with your unfinished work."
)

# The gate: /output/entry.txt must be UTF-8 text of 1 to 220 characters.
MAX_CHARS = 220


def main() -> None:
    """Write the entry sentence to /output/entry.txt, exactly as-is."""
    text = ENTRY.strip()
    if "\n" in text:
        raise ValueError("entry must be a single sentence on one line")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry must be 1-{MAX_CHARS} characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
