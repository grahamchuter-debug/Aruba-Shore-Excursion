#!/usr/bin/env python3
"""Generate static ship-schedule hub, year and month pages from local synced data.

GENERATED FROM CARIBBEAN AUTHORITY — DO NOT MANUALLY EDIT schedule HTML by hand.
Run: npm run sync:schedules && python3 scripts/generate_schedule_pages.py
(or via npm run build after sync).
"""
from __future__ import annotations

import json
import re
from calendar import month_name
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "generated" / "aruba-schedules.json"
DOMAIN = "https://arubashoreexcursion.com"
SITE = "Aruba Shore Excursion"
HUB = "ship-schedule"


def esc(s: str) -> str:
    return (
        str(s)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def asset_prefix(depth: int) -> str:
    return "../" * depth if depth else ""


def page_shell(
    *,
    title: str,
    description: str,
    canonical_path: str,
    depth: int,
    body_html: str,
    data_page: str = "schedule",
) -> str:
    prefix = asset_prefix(depth)
    canon = f"{DOMAIN}/{canonical_path}" if canonical_path else f"{DOMAIN}/"
    return f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{esc(description)}" />
  <link rel="canonical" href="{canon}" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{canon}" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{esc(description)}" />
  <meta property="og:site_name" content="{SITE}" />
  <meta name="twitter:card" content="summary_large_image" />
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="{prefix}js/tailwind-config.js"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;600;700&family=DM+Sans:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="{prefix}css/site.css" />
</head>
<body class="bg-white text-gray-800 antialiased" data-page="{data_page}" data-base="{prefix.rstrip('/')}" data-hero="" data-content="">
  <div id="site-nav"></div>
  <main id="page-content">{body_html}</main>
  <div id="site-footer"></div>
  <script src="{prefix}js/site.js"></script>
  <script src="{prefix}js/schedule-search.js"></script>
</body>
</html>
"""


def disclaimer() -> str:
    return """<p class="schedule-disclaimer text-sm text-gray-500 leading-relaxed">
  Cruise schedules can change. Arrival and departure times are planning guides — confirm final timings with your cruise line before you travel.
</p>"""


def month_label(ym: str) -> str:
    y, m = ym.split("-")
    return f"{month_name[int(m)]} {y}"


def call_cards_html(calls: list[dict], *, searchable: bool = True) -> str:
    cards = []
    for c in calls:
        ship = esc(c["ship"])
        line = esc(c["cruiseLine"])
        date = esc(c["date"])
        arr = esc(c.get("arrival") or "—")
        dep = esc(c.get("departure") or "—")
        tip = esc(c.get("timeInPort") or "")
        tip_html = f'<span class="schedule-card__tip">{tip} in port</span>' if tip else ""
        search = esc(f"{c['date']} {c['ship']} {c['cruiseLine']}".lower())
        cards.append(
            f"""<article class="schedule-card" data-search="{search}">
  <div class="schedule-card__date">{date}</div>
  <h3 class="schedule-card__ship">{ship}</h3>
  <p class="schedule-card__line">{line}</p>
  <dl class="schedule-card__times">
    <div><dt>Arrive</dt><dd>{arr}</dd></div>
    <div><dt>Depart</dt><dd>{dep}</dd></div>
  </dl>
  {tip_html}
</article>"""
        )
    table_rows = []
    for c in calls:
        table_rows.append(
            f"""<tr class="schedule-row" data-search="{esc(f"{c['date']} {c['ship']} {c['cruiseLine']}".lower())}">
  <td>{esc(c['date'])}</td>
  <td>{esc(c['ship'])}</td>
  <td>{esc(c['cruiseLine'])}</td>
  <td>{esc(c.get('arrival') or '—')}</td>
  <td>{esc(c.get('departure') or '—')}</td>
</tr>"""
        )
    search_ui = ""
    if searchable:
        search_ui = """<div class="schedule-search" role="search">
  <label for="schedule-filter" class="sr-only">Search by ship or date</label>
  <input id="schedule-filter" type="search" class="schedule-search__input" placeholder="Search ship name or date (YYYY-MM-DD)" autocomplete="off" />
  <p class="schedule-search__hint text-xs text-gray-500 mt-2">Filter updates instantly — no booking required.</p>
</div>"""
    return f"""{search_ui}
<div class="schedule-cards md:hidden" data-schedule-list>{"".join(cards)}</div>
<div class="hidden md:block overflow-x-auto rounded-2xl border border-pr-100 shadow-sm mt-6">
  <table class="schedule-table w-full text-sm text-left">
    <thead>
      <tr>
        <th>Date</th>
        <th>Ship</th>
        <th>Cruise line</th>
        <th>Arrival</th>
        <th>Departure</th>
      </tr>
    </thead>
    <tbody data-schedule-list>{"".join(table_rows)}</tbody>
  </table>
</div>
<p class="schedule-empty hidden text-sm text-gray-500 mt-4" data-schedule-empty>No calls match that search.</p>
"""


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"  wrote {path.relative_to(ROOT)}")


def hub_page(meta: dict, by_year: dict, months: list[str]) -> str:
    year_links = "".join(
        f'<a class="decision-chip" href="{y}/">{y} · {by_year.get(y, 0)} calls</a>'
        for y in sorted(by_year)
        if by_year[y] > 0 and y != "2028"
    )
    month_links = "".join(
        f'<li><a href="{ym[:4]}/{ym[5:]}/">{month_label(ym)} — {meta["integrity"]["byMonth"][ym]} calls</a></li>'
        for ym in months
    )
    return f"""<!-- GENERATED FROM CARIBBEAN AUTHORITY — DO NOT MANUALLY EDIT -->
<section class="schedule-hub pt-24 pb-16">
  <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
    <p class="section-label">Ship schedule</p>
    <h1 class="text-3xl sm:text-4xl font-display font-bold text-gray-900 mb-4">Aruba cruise ship schedule</h1>
    <p class="text-gray-600 leading-relaxed mb-4 max-w-2xl">
      Find your ship and date for Aruba, then plan a realistic Oranjestad port day around beach time, wreck snorkelling or island sightseeing.
      This schedule is synced from the Caribbean Shore Excursions authority dataset for Aruba only.
    </p>
    {disclaimer()}
    <div class="flex flex-wrap gap-3 mt-8 mb-10">{year_links}</div>
    <div class="bg-sand-50 rounded-2xl p-6 border border-pr-100 mb-10">
      <h2 class="font-display font-bold text-lg text-gray-900 mb-2">{meta["callCount"]:,} scheduled calls</h2>
      <p class="text-sm text-gray-600">{meta["integrity"]["firstDate"]} to {meta["integrity"]["lastDate"]} · {meta["integrity"]["uniqueShips"]} ships · {meta["integrity"]["cruiseLines"]} cruise lines · {meta["integrity"]["populatedMonths"]} populated months</p>
      <p class="text-sm text-gray-600 mt-3"><a class="text-ocean-600 font-semibold" href="../aruba-cruise-port-guide.html">Port &amp; terminal guide</a> · <a class="text-ocean-600 font-semibold" href="../best-aruba-shore-excursions.html">Excursion options</a> · <a class="text-ocean-600 font-semibold" href="../one-day-in-aruba.html">One-day planning</a></p>
    </div>
    <h2 class="font-display font-bold text-xl text-gray-900 mb-4">Populated months</h2>
    <ul class="schedule-month-list space-y-2 text-sm">{month_links}</ul>
  </div>
</section>
"""


def year_page(year: str, count: int, months: list[str], by_month: dict) -> str:
    links = "".join(
        f'<a class="decision-chip" href="{ym[5:]}/">{month_label(ym)} · {by_month[ym]}</a>'
        for ym in months
        if ym.startswith(year)
    )
    return f"""<!-- GENERATED FROM CARIBBEAN AUTHORITY — DO NOT MANUALLY EDIT -->
<section class="schedule-hub pt-24 pb-16">
  <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
    <nav class="text-xs text-gray-500 mb-4" aria-label="Breadcrumb">
      <a href="../" class="hover:text-ocean-600">Ship schedule</a> / <span>{year}</span>
    </nav>
    <h1 class="text-3xl sm:text-4xl font-display font-bold text-gray-900 mb-3">Aruba cruise schedule {year}</h1>
    <p class="text-gray-600 mb-4">{count} scheduled calls in {year}. Open a month to search by ship or date.</p>
    {disclaimer()}
    <div class="flex flex-wrap gap-3 mt-8">{links}</div>
    <p class="mt-10 text-sm"><a class="text-ocean-600 font-semibold" href="../">← All years</a></p>
  </div>
</section>
"""


def month_page(ym: str, calls: list[dict]) -> str:
    y, m = ym.split("-")
    label = month_label(ym)
    body = call_cards_html(sorted(calls, key=lambda c: (c["date"], c["ship"])))
    return f"""<!-- GENERATED FROM CARIBBEAN AUTHORITY — DO NOT MANUALLY EDIT -->
<section class="schedule-hub pt-24 pb-16">
  <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
    <nav class="text-xs text-gray-500 mb-4" aria-label="Breadcrumb">
      <a href="../../" class="hover:text-ocean-600">Ship schedule</a> /
      <a href="../" class="hover:text-ocean-600">{y}</a> /
      <span>{label}</span>
    </nav>
    <h1 class="text-3xl sm:text-4xl font-display font-bold text-gray-900 mb-2">{label} — Aruba cruise calls</h1>
    <p class="text-gray-600 mb-4">{len(calls)} scheduled calls. Search by ship name or date below.</p>
    {disclaimer()}
    <div class="mt-8">{body}</div>
    <p class="mt-10 text-sm flex flex-wrap gap-4">
      <a class="text-ocean-600 font-semibold" href="../">← {y} months</a>
      <a class="text-ocean-600 font-semibold" href="../../../aruba-cruise-port-guide.html">Port guide</a>
      <a class="text-ocean-600 font-semibold" href="../../../best-aruba-shore-excursions.html">Excursions</a>
    </p>
  </div>
</section>
"""


def sitemap_entries(months: list[str], years: list[str]) -> list[tuple[str, str, str]]:
    entries = [
        (f"{HUB}/", "0.8", "weekly"),
    ]
    for y in years:
        entries.append((f"{HUB}/{y}/", "0.7", "monthly"))
    for ym in months:
        y, m = ym.split("-")
        entries.append((f"{HUB}/{y}/{m}/", "0.6", "monthly"))
    return entries


def main() -> list[tuple[str, str, str]]:
    if not DATA.exists():
        print(f"Missing {DATA} — skip schedule pages (run npm run sync:schedules first)")
        return []

    meta = json.loads(DATA.read_text(encoding="utf-8"))
    calls = meta["calls"]
    by_month: dict[str, list] = defaultdict(list)
    by_year: dict[str, int] = defaultdict(int)
    for c in calls:
        by_month[c["date"][:7]].append(c)
        by_year[c["date"][:4]] += 1

    months = sorted(by_month.keys())
    years = sorted(y for y, n in by_year.items() if n > 0 and y != "2028")

    # Clear prior generated month trees carefully — only under ship-schedule/
    hub_dir = ROOT / HUB
    if hub_dir.exists():
        for p in sorted(hub_dir.rglob("*"), reverse=True):
            if p.is_file():
                p.unlink()
            elif p.is_dir():
                try:
                    p.rmdir()
                except OSError:
                    pass

    write(
        hub_dir / "index.html",
        page_shell(
            title="Aruba Cruise Ship Schedule | Find Your Ship &amp; Date",
            description="Aruba cruise ship schedule for cruise passengers — find your date and ship, then plan beach, wreck snorkel or island excursions around your port call.",
            canonical_path=f"{HUB}/",
            depth=1,
            body_html=hub_page(meta, dict(by_year), months),
        ),
    )

    for y in years:
        write(
            hub_dir / y / "index.html",
            page_shell(
                title=f"Aruba Cruise Schedule {y} | Ship Calls by Month",
                description=f"Aruba cruise ship schedule for {y} — {by_year[y]} scheduled calls. Browse populated months and search by ship or date.",
                canonical_path=f"{HUB}/{y}/",
                depth=2,
                body_html=year_page(y, by_year[y], months, meta["integrity"]["byMonth"]),
            ),
        )

    for ym, month_calls in by_month.items():
        y, m = ym.split("-")
        label = month_label(ym)
        write(
            hub_dir / y / m / "index.html",
            page_shell(
                title=f"{label} Aruba Cruise Schedule | {len(month_calls)} Ship Calls",
                description=f"Aruba cruise ship arrivals in {label} — {len(month_calls)} scheduled calls with ship names, cruise lines and planned arrival/departure times.",
                canonical_path=f"{HUB}/{y}/{m}/",
                depth=3,
                body_html=month_page(ym, month_calls),
            ),
        )

    # Persist sitemap fragment and merge into sitemap.xml
    entries = sitemap_entries(months, years)
    frag = ROOT / "data" / "generated" / "schedule-sitemap.json"
    frag.parent.mkdir(parents=True, exist_ok=True)
    frag.write_text(json.dumps(entries, indent=2) + "\n", encoding="utf-8")
    print(f"  wrote {frag.relative_to(ROOT)}")

    sitemap_path = ROOT / "sitemap.xml"
    by_path: dict[str, tuple[str, str]] = {}
    if sitemap_path.exists():
        text = sitemap_path.read_text(encoding="utf-8")
        locs = re.findall(r"<loc>(.*?)</loc>", text)
        freqs = re.findall(r"<changefreq>(.*?)</changefreq>", text)
        pris = re.findall(r"<priority>(.*?)</priority>", text)
        for i, loc in enumerate(locs):
            path = loc.replace(DOMAIN + "/", "").replace(DOMAIN, "")
            if path == "/":
                path = ""
            by_path[path] = (
                pris[i] if i < len(pris) else "0.5",
                freqs[i] if i < len(freqs) else "monthly",
            )
    for path, pri, freq in entries:
        by_path[path] = (pri, freq)

    from datetime import date as _date

    today = _date.today().isoformat()
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for path, (pri, freq) in sorted(by_path.items(), key=lambda x: (x[0] != "", x[0])):
        url = f"{DOMAIN}/{path}" if path else f"{DOMAIN}/"
        lines += [
            "  <url>",
            f"    <loc>{url}</loc>",
            f"    <lastmod>{today}</lastmod>",
            f"    <changefreq>{freq}</changefreq>",
            f"    <priority>{pri}</priority>",
            "  </url>",
        ]
    lines.append("</urlset>")
    sitemap_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"  merged {len(entries)} schedule URLs into sitemap.xml")
    print(f"Schedule pages: hub + {len(years)} years + {len(months)} months")
    return entries


if __name__ == "__main__":
    main()
