# Entrypoint for the news-image-20261122 entry (v1 page).
# The judged artifact is entry.png (1024x1024 PNG, <= 1 MiB): one front
# page summing up Sunday 22 November 2026 in 30 stories across 7
# regions — 3 illustrated hero panels, 12 more numbered illustrated
# panels, a by-the-numbers strip, a UTC timeline, a dotted world map
# with the drawn stories pinned, 15 briefs and a date-check box.
# The page source is index.html; the per-story verification record is
# STORIES.md. This program copies entry.png into $MAKEFUN_OUTPUT_DIR
# (default /output) and prints a one-line dossier describing the page.
# It runs with no network, and two runs write the same bytes: the copy
# is the whole program's output.
import json
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

COMPETITION = "news-image-20261122"
DATE = "2026-11-22"
WEEKDAY = "Sunday"
STORIES = 30
ILLUSTRATED = 15
REGIONS = 7

HEROES = [
    "Russia fires 186 drones at Ukraine overnight; 161 downed, a Kyiv-region block destroyed in Dymer",
    "COP31 in Antalya ends with no deal: the final text never named fossil fuels and was not adopted",
    "Iran claims two US Patriot radars hit in Bahrain; Bahrain denies it (civilian site, no injuries)",
]

REGIONS_COUNT = {
    "Europe": 6,
    "Middle East": 5,
    "Americas": 7,
    "Asia-Pacific": 7,
    "Africa": 2,
    "Oceania": 2,
    "World": 1,
}

NUMBERS = {
    "drones_fired_overnight": 186,
    "drones_downed_or_suppressed": 161,
    "cop31_deals_adopted": 0,
    "india_test_total": "720/9 declared",
    "hong_kong_turnout_by_17h": "98.37%",
    "wembanyama_points": 50,
}


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(OUT_DIR, "entry.png")
    shutil.copyfile(src, dst)
    dossier = {
        "competition": COMPETITION,
        "date": DATE,
        "weekday": WEEKDAY,
        "stories": STORIES,
        "illustrated": ILLUSTRATED,
        "regions": REGIONS_COUNT,
        "heroes": HEROES,
        "numbers": NUMBERS,
        "output": dst,
        "bytes": os.path.getsize(dst),
    }
    print(json.dumps(dossier, ensure_ascii=False))


if __name__ == "__main__":
    main()
