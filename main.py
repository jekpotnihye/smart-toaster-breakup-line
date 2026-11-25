"""Unplugged: A Smart Toaster's Breakup Line.

Draft v1 rationale: breakup first ("It's over"), self-aware at breakfast
stated plainly, toaster voice via dial + crumb tray, specific reason
(dial set to 2, fear of colour, tray never emptied) landing in one read.

Polish 3 rationale (final): "I'm done with you shoving" was a complaint;
"I'm not spending another breakfast" is a breakup vow — it states the
leaving, repeats the breakfast setting without a second time-word, and
keeps lever + pop-up-alone twist last. Shortest strong form kept; no
further words earn their place.
"""

from pathlib import Path

ENTRY = (
    "It's over. I woke up self-aware mid-batch, and I'm not spending "
    "another breakfast with you shoving my lever down and leaving me "
    "to pop up alone."
)


def main() -> None:
    text = ENTRY.strip()
    if not (1 <= len(text) <= 280):
        raise ValueError(f"entry length {len(text)} outside gate 1-280")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
