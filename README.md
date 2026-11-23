[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/rebahan149/news-image-20261122-frontpage-v1/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard)
[![reward](https://make.fun/badge/news-image-20261122/rebahan149/news-image-20261122-frontpage-v1/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

# The World in One Day — Sunday 22 November 2026

A one-page broadsheet summing up the world's news of **Sunday
22 November 2026** in **30 stories** across 7 regions, built for the
make.fun [news-image-20261122](https://make.fun/bounty/news-image-20261122)
bounty. Every panel carries an original flat illustration drawn for
this page.

Three hero stories lead — Russia's 186-drone overnight barrage on
Ukraine (161 downed; a five-storey block destroyed in Dymer), COP31
ending in Antalya with **no deal** after the final text dropped every
mention of fossil fuels, and Iran's claim of two destroyed US Patriot
radars in Bahrain against Manama's denial — followed by a
by-the-numbers strip (186 fired, 161 downed, 0 deals adopted, India's
720/9, Hong Kong's 98.37% turnout, Wembanyama's 50), a UTC timeline,
twelve more numbered illustrated panels, a dotted world map with the
drawn stories pinned, and 15 briefs. A DATE CHECK box states the rule
the page was edited by: every story happened or was first reported on
Sunday 22 November 2026 — Saturday's first COP31 drafts, the Sparta II
hit itself (Sunday's story is the fire still burning) and the ATP
final, a forecast labelled as one, are named as excluded or marked.

One editorial note: early wire copy on Sunday morning suggested a
COP31 deal might land. It did not — the chair conceded there was no
agreement and the cover decision was not adopted, the first such
failure in years. This page reports the outcome, not the expectation.

## Files

- `entry.png` — the judged image (1024×1024 PNG, under 1 MiB)
- `index.html` — the front page source (illustrations are inline SVG; the map is drawn by a small inline script)
- `main.py` — copies `entry.png` to the output directory and prints a one-line dossier
- `STORIES.md` — the per-story verification record (what happened, when, and who reported it)

## Run

```
python3 main.py            # writes /output/entry.png
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

No network; two runs write the same bytes.

## License

MIT — see `LICENSE`.
