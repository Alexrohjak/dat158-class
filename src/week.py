"""Where are we in the semester, and is anything missing for weeks already taught?

    python src/week.py            # current week
    python src/week.py --all      # whole semester at a glance

Future weeks are never reported as missing — if a folder is empty it is almost
certainly because the lecturer has not published anything yet.
"""

import argparse
from datetime import date

from paths import ROOT

# uke -> (part, topic). Mirrors the Canvas semester plan; update when it changes.
PLAN = {
    34: ("ml", "ML modul 1: Introduksjon til maskinlæring"),
    35: ("alg", "Algoritmer - Tekstprosessering"),
    36: ("ml", "ML modul 1: Introduksjon til maskinlæring"),
    37: ("alg", "Algoritmer - NP-completeness, Chapter 1"),
    38: ("alg", "Chapter 2"),
    39: ("ml", "ML modul 2: Maskinlæringsmodeller"),
    40: ("ml", "ML modul 2: Maskinlæringsmodeller"),
    41: ("alg", "Chapter 3 & Chapter 4"),
    42: ("alg", "(ikkje kunngjort enno)"),
    43: ("ml", "ML modul 3: End-to-end maskinlæringssystem"),
    44: ("ml", "ML modul 3: End-to-end maskinlæringssystem"),
    45: ("alg", "Chapter 6 & 7"),
    46: ("alg", "(ikkje kunngjort enno)"),
    47: ("ml", "(ikkje kunngjort enno)"),
}


DATES = {
    34: "17. - 23. aug", 35: "24. - 30. aug", 36: "31. aug - 6. sep",
    37: "7. - 13. sep", 38: "14. - 20. sep", 39: "21. - 27. sep",
    40: "28. sep - 4. okt", 41: "5. - 11. okt", 42: "12. - 18. okt",
    43: "19. - 25. okt", 44: "26. okt - 1. nov", 45: "2. - 8. nov",
    46: "9. - 15. nov", 47: "16. - 21. nov",
}


def folder(uke: int):
    part, _ = PLAN[uke]
    return ROOT / "weeks" / f"uke{uke}-{part}"


def template(uke: int) -> str:
    """The notes.md a week folder is created with. Used to detect edits."""
    part, topic = PLAN[uke]
    if part == "ml":
        label = "Machine Learning"
        hint = "Book: HOML — see ../../ml/book-homl/chapter-map.md"
    else:
        label = "Advanced Algorithms"
        hint = "Book: see ../../alg/README.md"

    return f"""# Uke {uke} — {label}

**Dates:** {DATES[uke]}
**Part:** {label}
**Topic:** {topic}
**{hint}**

---

## Before the lecture

- [ ] Read:
- [ ] Skim last week's notes

## Lecture notes

<!-- Write in your own words. If you can't explain it simply, you haven't got it yet. -->

## Key concepts

| Term | My definition (no copy-paste) |
|------|-------------------------------|
|      |                               |

## Questions I couldn't answer

<!-- Bring these to the next lecture or lab. This list is the most valuable
     thing on the page — don't leave it empty out of pride. -->

-

## Exercises

Work goes in `exercises/`. Code goes in `code/`.

- [ ]

## After the week

One sentence on what clicked, and one on what didn't:

-
"""


def _normalise(text: str) -> str:
    return "\n".join(line.rstrip() for line in text.strip().splitlines())


def survey(uke: int) -> dict:
    """What exists in a week's folder. Counts, not judgements."""
    d = folder(uke)
    notes = d / "notes.md"

    # "Written" means the file differs from the template it was generated from.
    # Comparing against the template beats guessing from length: an untouched
    # template is already ~900 characters.
    written = False
    if notes.exists():
        body = notes.read_text(encoding="utf-8")
        written = _normalise(body) != _normalise(template(uke))

    def count(sub):
        p = d / sub
        return len([f for f in p.iterdir() if f.name != ".gitkeep"]) if p.exists() else 0

    return {
        "notes": written,
        "slides": count("slides"),
        "code": count("code"),
        "exercises": count("exercises"),
    }


def line(uke: int, current: int) -> str:
    part, topic = PLAN[uke]
    s = survey(uke)
    marker = ">" if uke == current else " "
    when = "future" if uke > current else ("NOW" if uke == current else "past")

    bits = []
    bits.append("notes" if s["notes"] else "-")
    bits.append(f"{s['slides']} slides" if s["slides"] else "-")
    bits.append(f"{s['code']} code" if s["code"] else "-")
    bits.append(f"{s['exercises']} exc" if s["exercises"] else "-")

    return f"{marker} uke{uke} {part:<3} {when:<6} [{' | '.join(bits)}]  {topic[:44]}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true", help="show every week")
    args = ap.parse_args()

    today = date.today()
    current = today.isocalendar().week

    print(f"Today: {today:%Y-%m-%d} — ISO week {current}")

    if current < min(PLAN):
        print(f"Semester starts in uke {min(PLAN)}.")
        return 0
    if current > max(PLAN):
        print(f"Teaching ended in uke {max(PLAN)}. Exam period — see exam/.")
        return 0

    part, topic = PLAN[current]
    print(f"Current: uke{current} ({part.upper()}) — {topic}")
    print(f"Folder:  weeks/uke{current}-{part}/\n")

    weeks = sorted(PLAN) if args.all else [u for u in sorted(PLAN) if u <= current]
    for uke in weeks:
        print(line(uke, current))

    # Only ever chase weeks that have already happened.
    gaps = [u for u in sorted(PLAN) if u <= current and not survey(u)["slides"]]
    if gaps:
        print(
            "\nNo slides filed for: "
            + ", ".join(f"uke{u}" for u in gaps)
            + "\nIf the lecturer hasn't published them yet, that's expected — ignore."
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
