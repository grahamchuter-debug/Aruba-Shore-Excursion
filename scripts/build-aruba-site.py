#!/usr/bin/env python3
from __future__ import annotations
"""Generate Aruba Shore Excursion static site files."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
DOMAIN = "https://arubashoreexcursion.com"
SITE = "Aruba Shore Excursion"
DATE = "2026-06-04"
FONTS = "https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;600;700&family=DM+Sans:wght@400;500;600;700&display=swap"
HERO_GRADIENT = (
    "linear-gradient(135deg, rgba(146, 64, 14, 0.7) 0%, "
    "rgba(37, 99, 235, 0.65) 50%, rgba(30, 41, 59, 0.5) 100%)"
)
ACCENT = "text-teal-400"

HOME_HERO = "images/hero-aruba.png"
HOME_HERO_ALT = "Sailboat at sunset off Eagle Beach Aruba"
BEST_IMG = "images/best-aruba-excursions.png"
BEST_ALT = "Best Aruba shore excursions including beaches island tours and snorkelling"
PORT_IMG = "images/aruba-cruise-port.png"
PORT_ALT = "Cruise ship visiting Oranjestad Aruba cruise port"
ONE_DAY_IMG = "images/one-day-aruba.png"
ONE_DAY_ALT = "Oranjestad palm-lined street for cruise passengers spending one day in Aruba"
EAGLE_IMG = "images/eagle-beach-hero.png"
EAGLE_ALT = "Eagle Beach Aruba one of the Caribbean's most famous beaches"
SNORKEL_IMG = "images/aruba-snorkelling.png"
SNORKEL_ALT = "Snorkelling tour with clear water and tropical fish"
ANTILLA_IMG = "images/antilla-shipwreck.png"
ANTILLA_ALT = (
    "Aerial view of a shallow Aruba shipwreck snorkel site "
    "with swimmers and a boat nearby"
)
ISLAND_IMG = "images/aruba-island-tours.png"
ISLAND_ALT = "Island sightseeing tour visiting Aruba landmarks and viewpoints"
UTV_IMG = "images/aruba-intro.png"
UTV_ALT = "Aruba dry coastal landscape for UTV and dry-side adventure context"
ARIKOK_IMG = "images/aruba-intro.png"
ARIKOK_ALT = "Aruba dry coastal landscape near Arikok National Park"
LIGHTHOUSE_IMG = "images/california-lighthouse.png"
LIGHTHOUSE_ALT = "California Lighthouse in Aruba on an island sightseeing tour"
PRIVATE_IMG = "images/aruba-private-tours.png"
PRIVATE_ALT = "Colourful Oranjestad streetscape for private Aruba shore excursions"
FAMILY_IMG = "images/aruba-family.png"
FAMILY_ALT = "Eagle Beach Aruba for family friendly shore excursions"
BEACHES_IMG = "images/aruba-beaches.png"
BEACHES_ALT = "Palm Beach loungers and turquoise water in Aruba"
FAQ_IMG = "images/aruba-faq.png"
FAQ_ALT = "Cruise passengers exploring Oranjestad Aruba"
INTRO_IMG = "images/aruba-intro.png"
INTRO_ALT = "Aruba cactus and dry landscape inland from the beaches"


def page_shell(
    *,
    title: str,
    description: str,
    keywords: str,
    canonical_path: str,
    data_page: str,
    hero: str,
    content: str,
    preload: str = HOME_HERO,
    schema: dict | None = None,
    trust: bool = True,
) -> str:
    canon = f"{DOMAIN}/" if not canonical_path else f"{DOMAIN}/{canonical_path}"
    schema_block = ""
    if schema:
        schema_block = (
            f'  <script type="application/ld+json">\n'
            f"{json.dumps(schema, indent=2)}\n"
            f"  </script>\n"
        )
    trust_attr = '\n  data-trust-strip="partials/trust-strip.html"' if trust else ""
    content_file = content if content.startswith("content/") else f"content/{content}"
    return f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <title>{title}</title>
  <meta name="description" content="{description}" />
  <meta name="keywords" content="{keywords}" />
  <link rel="canonical" href="{canon}" />
  <link rel="preload" as="image" href="{preload}" fetchpriority="high" />

  <meta property="og:type" content="website" />
  <meta property="og:url" content="{canon}" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{description}" />
  <meta property="og:image" content="{DOMAIN}/{preload}" />
  <meta property="og:site_name" content="{SITE}" />
  <meta name="twitter:card" content="summary_large_image" />

{schema_block}
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="js/tailwind-config.js"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="{FONTS}" rel="stylesheet" />
  <link rel="stylesheet" href="css/site.css" />
</head>
<body
  class="bg-white text-gray-800 antialiased"
  data-page="{data_page}"
  data-base=""
  data-hero="{hero}"
  data-content="{content_file}"{trust_attr}
>

  <div id="site-nav"></div>
  <div id="page-hero"></div>
  <div id="page-trust-strip"></div>
  <main id="page-content"></main>
  <div id="site-footer"></div>

  <script src="js/site.js"></script>
</body>
</html>
"""


def write(path: str, content: str) -> None:
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    print(f"  wrote {path}")


def cruise_snapshot(
    *,
    time_in_port: str,
    best_for: str,
    activity_level: str,
    family: str,
    return_ship: str,
    popular: str,
) -> str:
    return f"""<aside class="cruise-snapshot mb-10 px-4 sm:px-0" aria-label="Cruise passenger snapshot">
  <h3 class="font-display font-bold text-lg text-gray-900 mb-4">Cruise Passenger Snapshot</h3>
  <dl class="cruise-snapshot__grid">
    <div class="cruise-snapshot__item"><dt>Typical Time In Port</dt><dd>{time_in_port}</dd></div>
    <div class="cruise-snapshot__item"><dt>Best For</dt><dd>{best_for}</dd></div>
    <div class="cruise-snapshot__item"><dt>Activity Level</dt><dd>{activity_level}</dd></div>
    <div class="cruise-snapshot__item"><dt>Family Friendly</dt><dd>{family}</dd></div>
    <div class="cruise-snapshot__item"><dt>Return To Ship Friendly</dt><dd>{return_ship}</dd></div>
    <div class="cruise-snapshot__item"><dt>Popular Excursion Types</dt><dd>{popular}</dd></div>
  </dl>
</aside>"""


def _hero_wave() -> str:
    return '<div class="absolute bottom-0 left-0 right-0"><svg viewBox="0 0 1440 48" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none" class="site-hero__wave" aria-hidden="true"><path d="M0 24 C360 48 1080 0 1440 24 L1440 48 L0 48 Z" fill="white"/></svg></div>'


def _hero_inner(
    eyebrow: str,
    title: str,
    lead: str,
    image: str,
    aria: str,
    breadcrumb: str = "",
    cta: tuple[str, str] | None = None,
    tags: list[str] | None = None,
) -> str:
    bc = ""
    if breadcrumb:
        bc = f"""<nav class="site-hero__breadcrumb flex items-center gap-2 mb-4 text-xs text-white/60" aria-label="Breadcrumb">
        <a href="index.html" class="hover:text-white transition-colors">Home</a>
        <svg class="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
        <span class="text-white/80">{breadcrumb}</span>
      </nav>"""
    cta_html = ""
    if cta:
        cta_html = f'<a href="{cta[0]}" class="btn-ocean inline-flex items-center justify-center gap-2 text-white font-semibold px-7 py-3 rounded-full text-sm shadow-xl">{cta[1]}</a>'
    tags_html = ""
    if tags:
        tags_html = '<div class="site-hero__tags flex flex-wrap gap-2 mt-5 pt-4 border-t border-white/20">' + "".join(
            f'<span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">{t}</span>'
            for t in tags
        ) + "</div>"
    return f"""<section class="site-hero">
  <div class="absolute inset-0 hero-bg-custom" style="background-image: {HERO_GRADIENT}, url('{image}');" role="img" aria-label="{aria}"></div>
  <div class="site-hero__inner max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="max-w-3xl">
      {bc}
      <div class="site-hero__eyebrow inline-flex items-center gap-2 bg-white/15 backdrop-blur-sm border border-white/30 rounded-full px-4 py-1.5 mb-3">
        <span class="w-2 h-2 rounded-full bg-teal-400 animate-pulse"></span>
        <span class="text-white/90 text-xs font-semibold tracking-widest uppercase">{eyebrow}</span>
      </div>
      <h1 class="site-hero__title text-4xl sm:text-5xl lg:text-[3.25rem] font-display font-bold text-white leading-tight mb-3">{title}</h1>
      <p class="site-hero__lead text-base sm:text-lg text-white/85 font-light leading-relaxed mb-5 max-w-2xl">{lead}</p>
      <div class="site-hero__actions flex flex-col sm:flex-row gap-3">{cta_html}</div>
      {tags_html}
    </div>
  </div>
  {_hero_wave()}
</section>"""


def _internal_links() -> str:
    return """<nav class="mt-10 pt-8 border-t border-gray-100" aria-label="Related Aruba guides">
  <p class="text-sm font-semibold text-gray-900 mb-3">Plan your port day</p>
  <div class="flex flex-wrap gap-3 text-sm">
    <a href="aruba-cruise-port-guide.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Port Guide</a>
    <span class="text-gray-300">·</span>
    <a href="best-aruba-shore-excursions.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Best Excursions</a>
    <span class="text-gray-300">·</span>
    <a href="eagle-beach-excursions.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Eagle Beach</a>
    <span class="text-gray-300">·</span>
    <a href="aruba-snorkelling-tours.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Snorkelling</a>
    <span class="text-gray-300">·</span>
    <a href="antilla-shipwreck-excursions.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Antilla Shipwreck</a>
    <span class="text-gray-300">·</span>
    <a href="aruba-island-tours.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Island Tours</a>
    <span class="text-gray-300">·</span>
    <a href="aruba-utv-atv-adventures.html" class="text-ocean-600 hover:text-ocean-800 font-medium">UTV Adventures</a>
    <span class="text-gray-300">·</span>
    <a href="aruba-private-tours.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Private Tours</a>
    <span class="text-gray-300">·</span>
    <a href="aruba-faq.html" class="text-ocean-600 hover:text-ocean-800 font-medium">FAQ</a>
  </div>
</nav>"""


def _comparison_section() -> str:
    rows = [
        ("Eagle Beach", "4–6 hrs", "Iconic white sand &amp; swim", "Low — beach time", "eagle-beach-excursions.html"),
        ("Snorkelling", "3–4 hrs", "Reef &amp; clear water", "Moderate — swim", "aruba-snorkelling-tours.html"),
        ("Antilla Shipwreck", "3–4 hrs", "Wreck snorkel highlight", "Moderate — boat &amp; swim", "antilla-shipwreck-excursions.html"),
        ("Island Tour", "4–5 hrs", "Lighthouse, aloe &amp; sights", "Low to moderate", "aruba-island-tours.html"),
        ("UTV Adventure", "3–4 hrs", "Rugged coast &amp; desert trails", "Moderate to high", "aruba-utv-atv-adventures.html"),
        ("Private Tour", "4–6 hrs", "Custom pacing for groups", "Varies", "aruba-private-tours.html"),
        ("Family Beach Day", "4–6 hrs", "Kids &amp; relaxed parents", "Low", "aruba-family-excursions.html"),
    ]
    body = ""
    for name, dur, best, activity, link in rows:
        body += f"""<tr class="border-b border-aruba-50 hover:bg-sand-50/80">
      <td class="py-4 pr-4 font-semibold text-gray-900"><a href="{link}" class="text-ocean-600 hover:text-ocean-800">{name}</a></td>
      <td class="py-4 px-3 text-gray-600">{dur}</td>
      <td class="py-4 px-3 text-gray-600">{best}</td>
      <td class="py-4 px-3 text-gray-600">{activity}</td>
      <td class="py-4 pl-3"><a href="{link}" class="text-teal-600 font-medium text-xs whitespace-nowrap">Guide →</a></td>
    </tr>"""
    return f"""<section class="py-16 bg-sand-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-3xl sm:text-4xl font-display font-bold text-gray-900 text-center mb-4">Which Aruba Excursion Is Right for Me?</h2>
  <p class="text-center text-gray-600 text-sm max-w-2xl mx-auto mb-10">Match your Oranjestad port day to beaches, wreck snorkelling, island drives or UTV trails — all timed for typical cruise schedules.</p>
  <div class="overflow-x-auto rounded-3xl border border-aruba-100 shadow-sm">
    <table class="w-full text-sm text-left min-w-[720px]">
      <thead class="bg-ocean-800 text-white">
        <tr>
          <th class="py-4 px-4 font-semibold rounded-tl-3xl">Excursion</th>
          <th class="py-4 px-3 font-semibold">Duration</th>
          <th class="py-4 px-3 font-semibold">Best For</th>
          <th class="py-4 px-3 font-semibold">Activity Level</th>
          <th class="py-4 px-4 font-semibold rounded-tr-3xl">Details</th>
        </tr>
      </thead>
      <tbody class="bg-white">{body}</tbody>
    </table>
  </div>
</div></section>"""


def _card_grid(cards: list[tuple]) -> str:
    items = []
    for img, alt, title, desc, link, label in cards:
        items.append(f"""<div class="card-hover bg-white rounded-3xl overflow-hidden shadow-md border border-aruba-50 flex flex-col">
      <div class="card-media h-44 relative overflow-hidden">
        <img src="{img}" alt="{alt}" width="600" height="352" loading="lazy" decoding="async" />
      </div>
      <div class="p-6 flex flex-col flex-1">
        <h3 class="text-lg font-display font-semibold text-gray-900 mb-2">{title}</h3>
        <p class="text-sm text-gray-500 leading-relaxed flex-1">{desc}</p>
        <a href="{link}" class="mt-5 btn-ocean inline-flex items-center justify-center text-white text-xs font-semibold px-5 py-2.5 rounded-full">{label}</a>
      </div>
    </div>""")
    return '<div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">' + "".join(items) + "</div>"


def _snapshot_default(**overrides: str) -> str:
    defaults = dict(
        time_in_port="8–10 hours (typical)",
        best_for="Beaches, wreck snorkel, island tours",
        activity_level="Varies — see comparison",
        family="Excellent with age-appropriate picks",
        return_ship="Build your own buffer; confirm operator return plan",
        popular="Eagle Beach, Antilla snorkel, UTV, island drive",
    )
    defaults.update(overrides)
    return cruise_snapshot(**defaults)


def _content_excursion_page(
    intro: str,
    bullets: list[str],
    snapshot_kwargs: dict,
    img: str,
    alt: str,
) -> str:
    bl = "".join(
        f'<li class="flex gap-2 text-sm text-gray-600"><span class="text-ocean-500">✓</span>{b}</li>'
        for b in bullets
    )
    snap = _snapshot_default(**snapshot_kwargs)
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-start">
      <div>
        <p class="text-gray-600 leading-relaxed mb-6">{intro}</p>
        <ul class="space-y-3 mb-6">{bl}</ul>
      </div>
      <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
        <img src="{img}" alt="{alt}" width="600" height="450" loading="lazy" decoding="async" />
      </div>
    </div></div></section>
    <section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
    <section class="pb-16 bg-white"><div class="max-w-3xl mx-auto px-4">{_internal_links()}</div></section>"""


def _hero_home() -> str:
    return f"""  <section class="site-hero">
    <div class="absolute inset-0 hero-bg" style="background-image: {HERO_GRADIENT}, url('{HOME_HERO}');" role="img" aria-label="{HOME_HERO_ALT}"></div>
    <div class="site-hero__inner max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="max-w-3xl">
        <div class="site-hero__eyebrow inline-flex items-center gap-2 bg-white/15 backdrop-blur-sm border border-white/30 rounded-full px-4 py-1.5 mb-3">
          <span class="w-2 h-2 rounded-full bg-teal-400 animate-pulse"></span>
          <span class="text-white/90 text-xs font-semibold tracking-widest uppercase">One Happy Island · Oranjestad</span>
        </div>
        <h1 class="site-hero__title text-4xl sm:text-5xl lg:text-[3.25rem] font-display font-bold text-white leading-tight mb-3">
          Aruba Shore<br/><span class="{ACCENT}">Excursions</span><br/>from the Cruise Port
        </h1>
        <p class="site-hero__lead text-base sm:text-lg text-white/85 font-light leading-relaxed mb-5 max-w-2xl">
          Eagle Beach, Antilla shipwreck snorkelling, island sightseeing and UTV adventures — the experiences cruise passengers book most in Aruba.
        </p>
        <div class="site-hero__actions flex flex-col sm:flex-row gap-3">
          <a href="best-aruba-shore-excursions.html" class="btn-primary inline-flex items-center justify-center gap-2 text-white font-semibold px-7 py-3 rounded-full text-sm shadow-xl">Compare Excursions</a>
          <a href="eagle-beach-excursions.html" class="btn-outline inline-flex items-center justify-center gap-2 text-white font-semibold px-7 py-3 rounded-full text-sm">Eagle Beach</a>
        </div>
        <div class="site-hero__tags flex flex-wrap gap-2 mt-5 pt-4 border-t border-white/20">
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Eagle Beach</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Turquoise Water</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Antilla Wreck</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">UTV Adventures</span>
        </div>
      </div>
    </div>
    {_hero_wave()}
  </section>"""


def _content_home() -> str:
    cards = _card_grid([
        (EAGLE_IMG, EAGLE_ALT, "Eagle Beach", "Famous fofoti trees, wide white sand and calm turquoise swim — Aruba's signature beach day.", "eagle-beach-excursions.html", "Eagle Beach"),
        (ANTILLA_IMG, ANTILLA_ALT, "Antilla Shipwreck", "Snorkel the WWII freighter wreck in clear Caribbean water off Aruba's west coast.", "antilla-shipwreck-excursions.html", "Wreck Snorkel"),
        (ISLAND_IMG, ISLAND_ALT, "Island Tours", "California Lighthouse, aloe factory, Casibari rocks and north-coast viewpoints.", "aruba-island-tours.html", "Island Tour"),
        (UTV_IMG, UTV_ALT, "UTV &amp; ATV", "Desert trails and rugged coastline — high-energy contrast to a beach morning.", "aruba-utv-atv-adventures.html", "UTV Tours"),
    ])
    snap = _snapshot_default()
    return f"""<section class="pt-8 pb-8 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-center">
      <div>
        <div class="inline-flex items-center gap-2 text-ocean-600 text-xs font-semibold tracking-widest uppercase mb-3"><div class="w-8 h-px bg-ocean-400"></div>Oranjestad Cruise Port</div>
        <h2 class="text-3xl sm:text-4xl font-display font-bold text-gray-900 mb-5">Why Cruise Guests<br/><span class="text-ocean-600">Choose Aruba</span></h2>
        <p class="text-gray-600 leading-relaxed mb-5">Aruba pairs desert interior with world-class beaches — Eagle Beach, Palm Beach, wreck snorkelling and Arikok National Park fit a typical <strong>8–10 hour</strong> Oranjestad call.</p>
        <a href="best-aruba-shore-excursions.html" class="btn-ocean inline-flex items-center gap-2 text-white font-semibold px-7 py-3.5 rounded-full text-sm shadow-lg">Browse All Excursions</a>
      </div>
      <div class="info-image rounded-3xl aspect-[4/3] shadow-2xl overflow-hidden">
        <img src="{INTRO_IMG}" alt="{INTRO_ALT}" width="800" height="600" loading="lazy" decoding="async" />
      </div>
    </div></div></section>
    <section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
    <section class="py-16 bg-sand-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-12"><h2 class="text-3xl font-display font-bold text-gray-900">Top Aruba Experiences</h2></div>
      {cards}
    </div></section>
    {_comparison_section()}
    <section class="py-16 cta-gradient"><div class="max-w-3xl mx-auto px-4 text-center">
      <h2 class="text-3xl font-display font-bold text-white mb-4">Plan Your Aruba Port Day</h2>
      <div class="flex flex-col sm:flex-row gap-4 justify-center">
        <a href="aruba-cruise-port-guide.html" class="btn-primary inline-flex items-center justify-center text-white font-semibold px-8 py-4 rounded-full">Port Guide</a>
        <a href="aruba-faq.html" class="btn-outline inline-flex items-center justify-center text-white font-semibold px-8 py-4 rounded-full">FAQ</a>
      </div>
    </div></section>"""


def _content_best() -> str:
    cards = _card_grid([
        (EAGLE_IMG, EAGLE_ALT, "Eagle Beach", "Transport, chairs and timed returns for cruise schedules.", "eagle-beach-excursions.html", "Beach Day"),
        (ANTILLA_IMG, ANTILLA_ALT, "Antilla Wreck", "Boat snorkel over the famous freighter wreck.", "antilla-shipwreck-excursions.html", "Wreck Tour"),
        (SNORKEL_IMG, SNORKEL_ALT, "Snorkelling", "Reef sites, turtles and clear water with gear included.", "aruba-snorkelling-tours.html", "Snorkel"),
        (PRIVATE_IMG, PRIVATE_ALT, "Private Tours", "Custom island routes for your group.", "aruba-private-tours.html", "Private"),
    ])
    snap = _snapshot_default(best_for="Comparing all excursion types", popular="See comparison table below")
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4 text-center">
      <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Best Aruba Shore Excursions</h2>
      <p class="text-gray-600 leading-relaxed text-sm">Operators meet at <strong>Oranjestad cruise terminals</strong> and plan returns with buffer before all aboard.</p>
    </div></section>
    <section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
    {_comparison_section()}
    <section class="py-16 bg-white"><div class="max-w-7xl mx-auto px-4">
      <h2 class="text-2xl font-display font-bold text-center mb-8">Excursion Guides</h2>
      {cards}
      <div class="mt-12 max-w-3xl mx-auto">{_internal_links()}</div>
    </div></section>"""


def _content_port() -> str:
    snap = _snapshot_default(
        activity_level="Low at terminal; moderate on tours",
        popular="Walk-on port, taxis, tour pickups",
    )
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4 text-center">
      <p class="text-gray-600 leading-relaxed text-sm">Ships dock at <strong>Oranjestad</strong> — downtown shops, beaches and tour pickups are minutes away on a typical <strong>8–10 hour</strong> call.</p>
    </div></section>
    <section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
    <section class="py-12 bg-sand-50"><div class="max-w-7xl mx-auto px-4">
      <h2 class="text-2xl font-display font-bold text-center mb-8">Where Ships Arrive</h2>
      <div class="info-image rounded-3xl aspect-[21/9] shadow-xl overflow-hidden mb-8 max-w-5xl mx-auto">
        <img src="{PORT_IMG}" alt="{PORT_ALT}" width="1200" height="514" loading="lazy" decoding="async" />
      </div>
      <div class="grid lg:grid-cols-2 gap-6 text-sm">
        <div class="bg-white rounded-3xl p-6 border border-aruba-100"><h3 class="font-display font-bold text-lg mb-2">Oranjestad Terminals</h3><p class="text-gray-600">Modern piers place you steps from colourful Dutch-Caribbean streets, taxis and shore-excursion desks.</p></div>
        <div class="bg-white rounded-3xl p-6 border border-aruba-100"><h3 class="font-display font-bold text-lg mb-2">Getting To Beaches</h3><p class="text-gray-600">Eagle Beach and Palm Beach are 10–20 minutes by taxi or included on organised beach transfers.</p></div>
      </div>
    </div></section>
    <section class="py-12 bg-white"><div class="max-w-7xl mx-auto px-4">
      <div class="grid sm:grid-cols-3 gap-6 text-sm">
        <div class="bg-sand-50 rounded-2xl p-6"><strong class="text-gray-900">Currency</strong><p class="mt-2 text-gray-600">Aruban florin (AWG); <strong>US dollars</strong> widely accepted at excursions and taxis.</p></div>
        <div class="bg-ocean-50 rounded-2xl p-6"><strong class="text-gray-900">Language</strong><p class="mt-2 text-gray-600">Dutch and Papiamento official; English common in tourism and at the port.</p></div>
        <div class="bg-sand-50 rounded-2xl p-6"><strong class="text-gray-900">Getting Around</strong><p class="mt-2 text-gray-600">Taxis at the pier; island tours and UTV operators include hotel/port pickup.</p></div>
      </div>
      <p class="text-center mt-8"><a href="one-day-in-aruba.html" class="text-ocean-600 font-semibold text-sm">One-day itinerary →</a></p>
      <div class="mt-10 max-w-3xl mx-auto">{_internal_links()}</div>
    </div></section>"""


def _content_one_day() -> str:
    snap = _snapshot_default(best_for="Beach morning + wreck snorkel or island tour")
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4 text-center">
      <p class="text-gray-600 text-sm">Sample timeline for an <strong>8–10 hour</strong> Oranjestad call. Adjust for your ship's actual times.</p>
    </div></section>
    <section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
    <section class="py-12 bg-sand-50"><div class="max-w-3xl mx-auto px-4">
      <h2 class="text-2xl font-display font-bold text-center mb-8">Classic Aruba Port Day</h2>
      <ol class="space-y-4 text-sm">
        <li class="flex gap-4 bg-white rounded-2xl p-5 border border-aruba-100"><span class="font-bold text-ocean-600 shrink-0">08:00</span><div><strong>Depart pier</strong><p class="text-gray-600 mt-1">Meet beach transfer or snorkel boat — morning slots beat afternoon heat.</p></div></li>
        <li class="flex gap-4 bg-white rounded-2xl p-5 border border-aruba-100"><span class="font-bold text-ocean-600 shrink-0">09:30</span><div><strong>Eagle Beach or Antilla snorkel</strong><p class="text-gray-600 mt-1">Choose calm beach time or wreck snorkel — both are cruise favourites.</p></div></li>
        <li class="flex gap-4 bg-white rounded-2xl p-5 border border-aruba-100"><span class="font-bold text-ocean-600 shrink-0">13:00</span><div><strong>Island tour or UTV</strong><p class="text-gray-600 mt-1">California Lighthouse, aloe factory or afternoon desert trail if energy allows.</p></div></li>
        <li class="flex gap-4 bg-white rounded-2xl p-5 border border-aruba-100"><span class="font-bold text-ocean-600 shrink-0">15:30</span><div><strong>Oranjestad stroll</strong><p class="text-gray-600 mt-1">Shopping and cafés near the pier before return buffer.</p></div></li>
        <li class="flex gap-4 bg-white rounded-2xl p-5 border border-aruba-100"><span class="font-bold text-ocean-600 shrink-0">17:00</span><div><strong>Back at ship</strong><p class="text-gray-600 mt-1">Allow margin before published all-aboard.</p></div></li>
      </ol>
      <div class="mt-10">{_internal_links()}</div>
    </div></section>"""


def _content_eagle() -> str:
    return _content_excursion_page(
        "Eagle Beach is Aruba's most photographed stretch — wide white sand, leaning fofoti trees and calm turquoise water west of Oranjestad. Cruise excursions include transport, often chair rental and a fixed return to the pier.",
        [
            "Morning visits avoid peak sun and crowds on busy ship days.",
            "Public access is free; organised tours add transport and timing.",
            "Pair with afternoon island tour only on long port calls.",
            "Reef-safe sunscreen and shade recommended.",
        ],
        dict(
            best_for="Beach lovers and photographers",
            activity_level="Low — swimming and walking",
            popular="Beach transfers, Eagle Beach chair packages",
        ),
        EAGLE_IMG,
        EAGLE_ALT,
    )


def _content_snorkelling() -> str:
    return _content_excursion_page(
        "Aruba's leeward coast offers clear snorkelling over coral patches, turtles and tropical fish. Tours supply masks, fins and guides; many combine reef stops with the Antilla shipwreck on the same sail.",
        [
            "Half-day trips fit most 8–10 hour port schedules.",
            "Beginners welcome — flotation aids often available.",
            "Use reef-safe sunscreen or a rash guard.",
            "See our Antilla guide for dedicated wreck snorkel boats.",
        ],
        dict(
            best_for="Reef swimmers and wildlife watchers",
            activity_level="Moderate — boat and snorkelling",
            popular="Reef snorkel, Antilla combo sails",
        ),
        SNORKEL_IMG,
        SNORKEL_ALT,
    )


def _content_antilla() -> str:
    return _content_excursion_page(
        "The SS Antilla is a WWII German freighter wreck resting in shallow water off Aruba's west coast — one of the Caribbean's best snorkel wrecks. Organised boats reach the site quickly from Oranjestad-area marinas.",
        [
            "Snorkel only — no penetration; follow crew safety briefing.",
            "Calm mornings improve visibility over the hull.",
            "Often paired with a second reef snorkel stop.",
            "Moderate swimming confidence helps in open water.",
        ],
        dict(
            best_for="Wreck snorkel enthusiasts",
            activity_level="Moderate — boat entry and swim",
            popular="Antilla wreck snorkel boats",
        ),
        ANTILLA_IMG,
        ANTILLA_ALT,
    )


def _content_island() -> str:
    return _content_excursion_page(
        "Island sightseeing tours cover Aruba's contrasts — California Lighthouse on the north tip, Casibari Rock Formations, aloe factory visits and coastal viewpoints. Air-conditioned vans suit guests who want land culture between beach and snorkel days.",
        [
            "4–5 hour loops fit standard port calls.",
            "Natural Bridge area offers dramatic photo stops.",
            "Less physically demanding than UTV trails.",
            "Private options let you prioritise lighthouse vs aloe.",
        ],
        dict(
            best_for="Sightseers and first-time visitors",
            activity_level="Low to moderate — van and short walks",
            popular="North coast drives, lighthouse tours",
        ),
        ISLAND_IMG,
        ISLAND_ALT,
    )


def _content_utv() -> str:
    return _content_excursion_page(
        "UTV and ATV adventures explore Aruba's arid interior and rugged north coast — dusty trails, coastline overlooks and hidden coves. Operators provide helmets, briefing and cruise-timed returns from Oranjestad pickups.",
        [
            "Drivers typically need a valid licence — check operator rules.",
            "Wear closed-toe shoes, sunglasses and dust-friendly clothing.",
            "Not ideal for guests with serious back or mobility limits.",
            "Book morning slots to leave afternoon beach time.",
        ],
        dict(
            best_for="Adventure seekers and active groups",
            activity_level="Moderate to high — off-road driving",
            popular="UTV coastline tours, desert trail rides",
        ),
        UTV_IMG,
        UTV_ALT,
    )


def _content_arikok() -> str:
    return _content_excursion_page(
        "Arikok National Park protects Aruba's desert hills, cacti and hidden pools — including the famous Natural Pool (Conchi) on the north coast. Guided tours handle park access and rough terrain vehicles where required.",
        [
            "Natural Pool access depends on sea conditions and route.",
            "Wear sturdy shoes — rocky paths and sun exposure.",
            "Allow half to full day if combining with other sights.",
            "Pair with island tour for guests who prefer less dust than UTV.",
        ],
        dict(
            best_for="Nature lovers and photographers",
            activity_level="Moderate — hiking and uneven ground",
            popular="Arikok guided hikes, Natural Pool tours",
        ),
        ARIKOK_IMG,
        ARIKOK_ALT,
    )


def _content_lighthouse() -> str:
    return _content_excursion_page(
        "California Lighthouse stands on Aruba's windy north tip with panoramic views over desert scrub and deep blue Atlantic swells. Most visits are part of island sightseeing tours with short photo stops and nearby dining options.",
        [
            "Sunset tours available on late-departure ship days.",
            "Windy at the point — light layer helps.",
            "Often combined with aloe factory and north-coast lookouts.",
            "Minimal walking from parking areas.",
        ],
        dict(
            best_for="Scenic photographers and lighthouse fans",
            activity_level="Low — short walks at viewpoints",
            popular="North coast island tours",
        ),
        LIGHTHOUSE_IMG,
        LIGHTHOUSE_ALT,
    )


def _content_private() -> str:
    return _content_excursion_page(
        "Private SUVs, vans and charter boats let your group set the pace — Eagle Beach first, Antilla snorkel, aloe factory and lighthouse stops in one custom loop. Drivers serving cruise guests understand all-aboard deadlines.",
        [
            "Split cost across families to rival per-person coach pricing.",
            "Share priorities when booking — routes are flexible.",
            "Ideal for mixed mobility within one group.",
            "Confirm return time in writing before payment.",
        ],
        dict(
            best_for="Groups wanting custom pacing",
            activity_level="Low to moderate — varies by itinerary",
            popular="Private island tours, custom snorkel charters",
        ),
        PRIVATE_IMG,
        PRIVATE_ALT,
    )


def _content_family() -> str:
    return _content_excursion_page(
        "Family excursions in Aruba favour calm Eagle Beach time, gentle snorkel sails, short island drives and shallow wreck viewing with strong supervision. Two well-paced stops beat three rushed attractions with children.",
        [
            "Eagle Beach suits school-age kids with shade breaks.",
            "UTV tours publish age and height rules — verify when booking.",
            "Private vans simplify nap timing and snack stops.",
            "Reef snorkel operators often offer junior gear.",
        ],
        dict(
            best_for="Kids, parents and multi-generational groups",
            family="Excellent with age-appropriate tour choice",
            popular="Beach transfers, family island tours",
        ),
        FAMILY_IMG,
        FAMILY_ALT,
    )


def _content_beaches() -> str:
    snap = _snapshot_default(
        best_for="Choosing Eagle vs Palm vs Baby Beach",
        popular="Eagle Beach, Palm Beach, Mangel Halto",
    )
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-start">
      <div>
        <p class="text-gray-600 leading-relaxed mb-6">Aruba's leeward beaches offer calm turquoise water — <strong>Eagle Beach</strong> for iconic sand and trees, <strong>Palm Beach</strong> for resorts and water sports, and quieter coves for snorkel-from-shore fans on longer port days.</p>
        <ul class="space-y-3 mb-6">
          <li class="flex gap-2 text-sm text-gray-600"><span class="text-ocean-500">✓</span><strong>Eagle Beach</strong> — wide sand, fofoti trees, cruise-friendly transfers.</li>
          <li class="flex gap-2 text-sm text-gray-600"><span class="text-ocean-500">✓</span><strong>Palm Beach</strong> — resorts, bars and jet-ski rentals.</li>
          <li class="flex gap-2 text-sm text-gray-600"><span class="text-ocean-500">✓</span><strong>Baby Beach</strong> — shallow lagoon on the south end (longer drive).</li>
        </ul>
        <a href="eagle-beach-excursions.html" class="text-ocean-600 font-semibold text-sm">Eagle Beach excursions →</a>
      </div>
      <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
        <img src="{BEACHES_IMG}" alt="{BEACHES_ALT}" width="600" height="450" loading="lazy" decoding="async" />
      </div>
    </div></div></section>
    <section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
    <section class="pb-16 bg-white"><div class="max-w-3xl mx-auto px-4">{_internal_links()}</div></section>"""


def _content_faq() -> str:
    snap = _snapshot_default(best_for="Quick planning answers", popular="See FAQ topics below")
    return f"""<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
    <section class="py-8 bg-white"><div class="max-w-3xl mx-auto px-4 space-y-4">
      <details class="faq-item rounded-2xl border border-aruba-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">How long do cruise ships stay in Aruba?</summary>
        <p class="mt-4 text-sm text-gray-500">Most Oranjestad calls are 8 to 10 hours. A beach morning plus Antilla snorkel or island tour fits comfortably with return buffer.</p></details>
      <details class="faq-item rounded-2xl border border-aruba-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Is the Antilla shipwreck suitable for beginners?</summary>
        <p class="mt-4 text-sm text-gray-500">Organised snorkel boats typically keep viewing at the surface with crew guidance and no hull penetration. Comfort in open water still varies — ask the operator about conditions, gear and experience level before you book.</p></details>
      <details class="faq-item rounded-2xl border border-aruba-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Do I need Aruban florin cash?</summary>
        <p class="mt-4 text-sm text-gray-500">US dollars are widely accepted. Small vendors may prefer cash; ATMs are in Oranjestad near the port.</p></details>
      <details class="faq-item rounded-2xl border border-aruba-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Eagle Beach or Palm Beach for a port day?</summary>
        <p class="mt-4 text-sm text-gray-500">Eagle Beach is quieter and iconic; Palm Beach has more facilities and water sports. Cruise transfers often default to Eagle Beach.</p></details>
      <details class="faq-item rounded-2xl border border-aruba-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Ship excursion or book independently?</summary>
        <p class="mt-4 text-sm text-gray-500">Ship-sold tours often include a wait-if-late policy from the cruise line. Independent operators typically plan a return window — confirm policies, build your own buffer, and do not cut it fine.</p></details>
      {_internal_links()}
    </div></section>"""


def _faq_schema() -> dict:
    qa = [
        ("How long do cruise ships stay in Aruba?", "Most Oranjestad calls are 8 to 10 hours."),
        ("Is the Antilla shipwreck suitable for beginners?", "Organised snorkel boats typically keep viewing at the surface with crew guidance and no hull penetration. Comfort in open water still varies — ask the operator about conditions, gear and experience level before you book."),
        ("Do I need Aruban florin cash?", "US dollars are widely accepted; ATMs are in Oranjestad."),
        ("Eagle Beach or Palm Beach for a port day?", "Eagle Beach is quieter; Palm Beach has more facilities."),
        ("Ship excursion or book independently?", "Ship-sold tours often include wait-if-late; confirm independent operator policies and build your own buffer."),
    ]
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in qa
        ],
    }


def main() -> None:
    print("Building Aruba Shore Excursion site…")

    write(
        "partials/nav.html",
        f"""<nav class="fixed top-0 left-0 right-0 z-50 bg-white/90 border-b border-aruba-100 shadow-sm">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex items-center justify-between h-12">
      <a href="index.html" class="flex items-center gap-2">
        <div class="w-7 h-7 rounded-full btn-ocean flex items-center justify-center">
          <svg class="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
            <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 14H9V8h2v8zm4 0h-2V8h2v8z"/>
          </svg>
        </div>
        <span class="font-display font-semibold text-ocean-800 text-base leading-tight">Aruba<br/><span class="text-[10px] font-body font-normal text-teal-600 tracking-widest uppercase">Shore Excursion</span></span>
      </a>
      <div class="hidden lg:flex items-center gap-5 text-sm font-medium">
        <a href="index.html" data-nav="home" class="text-gray-600 hover:text-ocean-600 transition-colors">Home</a>
        <a href="best-aruba-shore-excursions.html" data-nav="excursions" class="text-gray-600 hover:text-ocean-600 transition-colors">Excursions</a>
        <a href="eagle-beach-excursions.html" data-nav="beaches" class="text-gray-600 hover:text-ocean-600 transition-colors">Eagle Beach</a>
        <a href="aruba-snorkelling-tours.html" data-nav="snorkelling" class="text-gray-600 hover:text-ocean-600 transition-colors">Snorkelling</a>
        <a href="aruba-island-tours.html" data-nav="island" class="text-gray-600 hover:text-ocean-600 transition-colors">Island Tours</a>
        <a href="aruba-utv-atv-adventures.html" data-nav="utv" class="text-gray-600 hover:text-ocean-600 transition-colors">UTV</a>
        <a href="aruba-cruise-port-guide.html" data-nav="port" class="text-gray-600 hover:text-ocean-600 transition-colors">Port Guide</a>
      </div>
      <a href="best-aruba-shore-excursions.html" class="hidden md:inline-flex items-center gap-2 btn-ocean text-white text-sm font-semibold px-4 py-2 rounded-full shadow-md">
        Compare Tours
      </a>
      <button type="button" class="lg:hidden p-2 rounded-lg text-gray-600 hover:bg-sand-50" id="menu-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-menu">
        <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/></svg>
      </button>
    </div>
    <div id="mobile-menu" class="hidden lg:hidden pb-4 border-t border-aruba-100">
      <div class="flex flex-col gap-3 pt-3 text-sm font-medium">
        <a href="index.html" data-nav="home" class="text-gray-600 hover:text-ocean-600">Home</a>
        <a href="best-aruba-shore-excursions.html" data-nav="excursions" class="text-gray-600 hover:text-ocean-600">Excursions</a>
        <a href="eagle-beach-excursions.html" data-nav="beaches" class="text-gray-600 hover:text-ocean-600">Eagle Beach</a>
        <a href="aruba-snorkelling-tours.html" data-nav="snorkelling" class="text-gray-600 hover:text-ocean-600">Snorkelling</a>
        <a href="aruba-island-tours.html" data-nav="island" class="text-gray-600 hover:text-ocean-600">Island Tours</a>
        <a href="ship-schedule/" data-nav="schedule" class="text-gray-600 hover:text-ocean-600">Ship Schedule</a>
        <a href="aruba-cruise-port-guide.html" data-nav="port" class="text-gray-600 hover:text-ocean-600">Port Guide</a>
        <a href="contact.html" data-nav="contact" class="text-gray-600 hover:text-ocean-600">Contact</a>
      </div>
    </div>
  </div>
</nav>
""",
    )

    write(
        "partials/footer.html",
        f"""  <footer class="bg-gray-900 text-gray-400 py-14">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-10 mb-12">
        <div class="sm:col-span-2 lg:col-span-1">
          <a href="index.html" class="font-display font-semibold text-white text-lg">{SITE}</a>
          <p class="mt-3 text-sm leading-relaxed">Planning guide for cruise visitors to Aruba from Oranjestad port. Not affiliated with any cruise line.</p>
        </div>
        <div>
          <h3 class="text-white text-sm font-semibold uppercase tracking-wider mb-4">Excursions</h3>
          <ul class="space-y-2 text-sm">
            <li><a href="best-aruba-shore-excursions.html" class="hover:text-white transition-colors">All Excursions</a></li>
            <li><a href="eagle-beach-excursions.html" class="hover:text-white transition-colors">Eagle Beach</a></li>
            <li><a href="aruba-snorkelling-tours.html" class="hover:text-white transition-colors">Snorkelling</a></li>
            <li><a href="antilla-shipwreck-excursions.html" class="hover:text-white transition-colors">Antilla Shipwreck</a></li>
            <li><a href="aruba-island-tours.html" class="hover:text-white transition-colors">Island Tours</a></li>
            <li><a href="aruba-utv-atv-adventures.html" class="hover:text-white transition-colors">UTV &amp; ATV</a></li>
            <li><a href="arikok-national-park-tours.html" class="hover:text-white transition-colors">Arikok National Park</a></li>
            <li><a href="aruba-private-tours.html" class="hover:text-white transition-colors">Private Tours</a></li>
          </ul>
        </div>
        <div>
          <h3 class="text-white text-sm font-semibold uppercase tracking-wider mb-4">Resources</h3>
          <ul class="space-y-2 text-sm">
            <li><a href="aruba-cruise-port-guide.html" class="hover:text-white transition-colors">Port Guide</a></li>
            <li><a href="one-day-in-aruba.html" class="hover:text-white transition-colors">One Day in Aruba</a></li>
            <li><a href="aruba-beaches-guide.html" class="hover:text-white transition-colors">Beaches Guide</a></li>
            <li><a href="california-lighthouse-tours.html" class="hover:text-white transition-colors">California Lighthouse</a></li>
            <li><a href="aruba-family-excursions.html" class="hover:text-white transition-colors">Family Excursions</a></li>
            <li><a href="aruba-faq.html" class="hover:text-white transition-colors">FAQ</a></li>
          </ul>
        </div>
      </div>
      <div class="border-t border-gray-800 pt-8 text-xs text-center sm:text-left">
        <p>&copy; 2026 {SITE}. Verify times and prices with operators before booking.</p>
      </div>
    </div>
  </footer>
""",
    )

    write(
        "partials/trust-strip.html",
        f"""<section class="trust-strip" aria-label="Aruba shore excursion highlights">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <ul class="trust-strip__list">
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Eagle Beach</li>
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Antilla Shipwreck</li>
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Island Sightseeing</li>
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Cruise-Friendly Returns</li>
    </ul>
  </div>
</section>
""",
    )

    heroes = {
        "hero-home.html": _hero_home(),
        "hero-excursions.html": _hero_inner(
            "Oranjestad · One Happy Island",
            f"Best Aruba<br/><span class=\"{ACCENT}\">Shore Excursions</span>",
            "Compare Eagle Beach, Antilla wreck snorkel, island tours, Arikok, UTV trails and private options for your ship schedule.",
            BEST_IMG,
            BEST_ALT,
            breadcrumb="Best Excursions",
        ),
        "hero-port-guide.html": _hero_inner(
            "Cruise Passenger Guide",
            f"Aruba<br/><span class=\"{ACCENT}\">Cruise Port Guide</span>",
            "Oranjestad terminals, taxis, currency and how to plan shore time ashore.",
            PORT_IMG,
            PORT_ALT,
            breadcrumb="Port Guide",
            cta=("best-aruba-shore-excursions.html", "View Shore Excursions →"),
            tags=["🚢 Oranjestad", "🏖️ Eagle Beach", "🤿 Antilla Wreck", "🛻 UTV Tours"],
        ),
        "hero-one-day.html": _hero_inner(
            "Port Day Timeline",
            f"One Day in<br/><span class=\"{ACCENT}\">Aruba</span>",
            "Hour-by-hour plan from gangway to departure — beach, wreck snorkel or island tour with return buffer.",
            ONE_DAY_IMG,
            ONE_DAY_ALT,
            breadcrumb="One Day in Aruba",
        ),
        "hero-eagle-beach.html": _hero_inner(
            "West Coast · Aruba",
            f"Eagle Beach<br/><span class=\"{ACCENT}\">Excursions</span>",
            "White sand, fofoti trees and calm turquoise water — Aruba's most famous beach for cruise guests.",
            EAGLE_IMG,
            EAGLE_ALT,
            breadcrumb="Eagle Beach",
        ),
        "hero-snorkelling.html": _hero_inner(
            "Leeward Coast · Aruba",
            f"Aruba<br/><span class=\"{ACCENT}\">Snorkelling</span> Tours",
            "Clear Caribbean water, coral patches and reef fish — boat trips with gear from Oranjestad.",
            SNORKEL_IMG,
            SNORKEL_ALT,
            breadcrumb="Snorkelling Tours",
        ),
        "hero-antilla.html": _hero_inner(
            "SS Antilla Wreck",
            f"Antilla Shipwreck<br/><span class=\"{ACCENT}\">Excursions</span>",
            "Snorkel over a WWII freighter wreck in shallow turquoise water — Aruba's top underwater highlight.",
            ANTILLA_IMG,
            ANTILLA_ALT,
            breadcrumb="Antilla Shipwreck",
        ),
        "hero-island.html": _hero_inner(
            "Sightseeing · Aruba",
            f"Aruba<br/><span class=\"{ACCENT}\">Island Tours</span>",
            "California Lighthouse, aloe factory, rock formations and north-coast viewpoints by air-conditioned van.",
            ISLAND_IMG,
            ISLAND_ALT,
            breadcrumb="Island Tours",
        ),
        "hero-utv.html": _hero_inner(
            "Off-Road Adventure",
            f"Aruba UTV &amp;<br/><span class=\"{ACCENT}\">ATV Adventures</span>",
            "Explore rugged coastline and desert trails — high-energy shore excursions from the cruise port.",
            UTV_IMG,
            UTV_ALT,
            breadcrumb="UTV & ATV",
        ),
        "hero-arikok.html": _hero_inner(
            "National Park · Aruba",
            f"Arikok National Park<br/><span class=\"{ACCENT}\">Tours</span>",
            "Desert hills, cacti and the Natural Pool — guided access to Aruba's protected wild side.",
            ARIKOK_IMG,
            ARIKOK_ALT,
            breadcrumb="Arikok National Park",
        ),
        "hero-lighthouse.html": _hero_inner(
            "North Tip · Aruba",
            f"California Lighthouse<br/><span class=\"{ACCENT}\">Tours</span>",
            "Panoramic views from Aruba's iconic lighthouse on island sightseeing excursions.",
            LIGHTHOUSE_IMG,
            LIGHTHOUSE_ALT,
            breadcrumb="California Lighthouse",
        ),
        "hero-private.html": _hero_inner(
            "Custom Shore Trips",
            f"Aruba<br/><span class=\"{ACCENT}\">Private Tours</span>",
            "Private vans and charters at your group's pace — beaches, wreck snorkel and custom island routes.",
            PRIVATE_IMG,
            PRIVATE_ALT,
            breadcrumb="Private Tours",
        ),
        "hero-family.html": _hero_inner(
            "All Ages Welcome",
            f"Aruba<br/><span class=\"{ACCENT}\">Family</span> Excursions",
            "Calm beaches, gentle snorkel and relaxed island drives for every generation.",
            FAMILY_IMG,
            FAMILY_ALT,
            breadcrumb="Family Excursions",
        ),
        "hero-beaches.html": _hero_inner(
            "Beach Guide · Aruba",
            f"Aruba<br/><span class=\"{ACCENT}\">Beaches Guide</span>",
            "Eagle Beach, Palm Beach and quiet coves — choose the right sand for your port day.",
            BEACHES_IMG,
            BEACHES_ALT,
            breadcrumb="Beaches Guide",
        ),
        "hero-faq.html": _hero_inner(
            "Cruise Planning Answers",
            f"Aruba<br/><span class=\"{ACCENT}\">Excursions FAQ</span>",
            "Port timing, Antilla wreck, beaches, currency and booking independent vs ship tours.",
            FAQ_IMG,
            FAQ_ALT,
            breadcrumb="FAQ",
        ),
    }
    for name, html in heroes.items():
        write(f"partials/{name}", html)

    contents = {
        "home.html": _content_home(),
        "best-aruba-shore-excursions.html": _content_best(),
        "aruba-cruise-port-guide.html": _content_port(),
        "one-day-in-aruba.html": _content_one_day(),
        "eagle-beach-excursions.html": _content_eagle(),
        "aruba-snorkelling-tours.html": _content_snorkelling(),
        "antilla-shipwreck-excursions.html": _content_antilla(),
        "aruba-island-tours.html": _content_island(),
        "aruba-utv-atv-adventures.html": _content_utv(),
        "arikok-national-park-tours.html": _content_arikok(),
        "california-lighthouse-tours.html": _content_lighthouse(),
        "aruba-private-tours.html": _content_private(),
        "aruba-family-excursions.html": _content_family(),
        "aruba-beaches-guide.html": _content_beaches(),
        "aruba-faq.html": _content_faq(),
    }
    for name, html in contents.items():
        write(f"content/{name}", html)

    pages = [
        dict(
            file="index.html",
            title=f"{SITE} | Eagle Beach, Antilla Snorkel &amp; Island Tours from Oranjestad",
            description="Plan Aruba shore excursions for cruise passengers — Eagle Beach, Antilla shipwreck snorkelling, island sightseeing, UTV adventures and private tours from Oranjestad cruise port.",
            keywords="Aruba shore excursions, Aruba cruise excursions, Eagle Beach cruise tour, Oranjestad cruise port tours, Antilla shipwreck snorkel",
            path="",
            data_page="home",
            hero="partials/hero-home.html",
            content="home.html",
            schema={"@context": "https://schema.org", "@type": "WebSite", "name": SITE, "url": f"{DOMAIN}/", "description": "Planning guide for Aruba cruise shore excursions from Oranjestad"},
        ),
        dict(
            file="best-aruba-shore-excursions.html",
            title="Best Aruba Shore Excursions | Compare Oranjestad Cruise Tours",
            description="Compare the best Aruba shore excursions — Eagle Beach, Antilla wreck snorkel, island tours, Arikok, UTV adventures and private options with cruise timing.",
            keywords="best Aruba shore excursions, Aruba cruise port tours, compare Aruba excursions, Oranjestad shore trips",
            path="best-aruba-shore-excursions.html",
            data_page="excursions",
            hero="partials/hero-excursions.html",
            content="best-aruba-shore-excursions.html",
            preload=BEST_IMG,
            schema={"@context": "https://schema.org", "@type": "WebPage", "name": "Best Aruba Shore Excursions", "url": f"{DOMAIN}/best-aruba-shore-excursions.html"},
        ),
        dict(
            file="aruba-cruise-port-guide.html",
            title="Aruba Cruise Port Guide | Oranjestad for Cruise Passengers",
            description="Aruba cruise port guide — Oranjestad terminals, taxis, AWG and USD, and top shore excursions timed for your ship's schedule.",
            keywords="Aruba cruise port guide, Oranjestad cruise port, Aruba port day, cruise passenger guide Aruba",
            path="aruba-cruise-port-guide.html",
            data_page="port",
            hero="partials/hero-port-guide.html",
            content="aruba-cruise-port-guide.html",
            preload=PORT_IMG,
            schema={"@context": "https://schema.org", "@type": "Article", "headline": "Aruba Cruise Port Guide", "url": f"{DOMAIN}/aruba-cruise-port-guide.html"},
        ),
        dict(
            file="one-day-in-aruba.html",
            title="One Day in Aruba from a Cruise Ship | Port Itinerary",
            description="How to spend one day in Aruba on a cruise stop — Eagle Beach, Antilla snorkel and island tour sample timeline with return-to-ship buffer.",
            keywords="one day in Aruba cruise, Aruba port day itinerary, Oranjestad cruise stop planning",
            path="one-day-in-aruba.html",
            data_page="port",
            hero="partials/hero-one-day.html",
            content="one-day-in-aruba.html",
            preload=ONE_DAY_IMG,
        ),
        dict(
            file="eagle-beach-excursions.html",
            title="Eagle Beach Excursions | Aruba Cruise Beach Days",
            description="Eagle Beach excursions from Oranjestad — white sand, fofoti trees, calm turquoise water and cruise-friendly returns.",
            keywords="Eagle Beach excursion Aruba, Eagle Beach cruise port, Aruba beach day cruise",
            path="eagle-beach-excursions.html",
            data_page="beaches",
            hero="partials/hero-eagle-beach.html",
            content="eagle-beach-excursions.html",
            preload=EAGLE_IMG,
        ),
        dict(
            file="aruba-snorkelling-tours.html",
            title="Aruba Snorkelling Tours | Reef Cruise Excursions from Oranjestad",
            description="Aruba snorkelling tours on the leeward coast — reef sites, turtles and clear water with cruise-friendly returns; Antilla combos available.",
            keywords="Aruba snorkelling tours, reef snorkel cruise Aruba, Oranjestad snorkel excursion",
            path="aruba-snorkelling-tours.html",
            data_page="snorkelling",
            hero="partials/hero-snorkelling.html",
            content="aruba-snorkelling-tours.html",
            preload=SNORKEL_IMG,
        ),
        dict(
            file="antilla-shipwreck-excursions.html",
            title="Antilla Shipwreck Excursions | Aruba Wreck Snorkel Cruises",
            description="Antilla shipwreck snorkelling excursions from Oranjestad — WWII freighter wreck in shallow turquoise water for cruise passengers.",
            keywords="Antilla shipwreck Aruba, Antilla snorkel cruise, SS Antilla excursion Aruba",
            path="antilla-shipwreck-excursions.html",
            data_page="snorkelling",
            hero="partials/hero-antilla.html",
            content="antilla-shipwreck-excursions.html",
            preload=ANTILLA_IMG,
        ),
        dict(
            file="aruba-island-tours.html",
            title="Aruba Island Tours | Sightseeing from Oranjestad Cruise Port",
            description="Aruba island tours for cruise passengers — California Lighthouse, aloe factory, rock formations and north-coast viewpoints.",
            keywords="Aruba island tour cruise, sightseeing Aruba shore excursion, Oranjestad island drive",
            path="aruba-island-tours.html",
            data_page="island",
            hero="partials/hero-island.html",
            content="aruba-island-tours.html",
            preload=ISLAND_IMG,
        ),
        dict(
            file="aruba-utv-atv-adventures.html",
            title="Aruba UTV &amp; ATV Adventures | Off-Road Cruise Excursions",
            description="Aruba UTV and ATV adventures from the cruise port — rugged coastline and desert trails with cruise-friendly timing.",
            keywords="Aruba UTV tour cruise, ATV excursion Aruba, off road shore excursion Oranjestad",
            path="aruba-utv-atv-adventures.html",
            data_page="utv",
            hero="partials/hero-utv.html",
            content="aruba-utv-atv-adventures.html",
            preload=UTV_IMG,
        ),
        dict(
            file="arikok-national-park-tours.html",
            title="Arikok National Park Tours | Natural Pool Aruba Cruise Excursions",
            description="Arikok National Park tours from Oranjestad — desert landscape, guided hikes and Natural Pool visits for cruise passengers.",
            keywords="Arikok National Park tour Aruba, Natural Pool Aruba cruise, Aruba national park excursion",
            path="arikok-national-park-tours.html",
            data_page="island",
            hero="partials/hero-arikok.html",
            content="arikok-national-park-tours.html",
            preload=ARIKOK_IMG,
        ),
        dict(
            file="california-lighthouse-tours.html",
            title="California Lighthouse Tours | North Coast Aruba Island Excursions",
            description="California Lighthouse tours on Aruba island sightseeing trips — north-tip views and photo stops for cruise guests.",
            keywords="California Lighthouse Aruba tour, north coast Aruba excursion, lighthouse cruise Aruba",
            path="california-lighthouse-tours.html",
            data_page="island",
            hero="partials/hero-lighthouse.html",
            content="california-lighthouse-tours.html",
            preload=LIGHTHOUSE_IMG,
        ),
        dict(
            file="aruba-private-tours.html",
            title="Aruba Private Tours | Custom Cruise Shore Excursions",
            description="Private Aruba tours for cruise passengers — custom vans and charters with flexible beach, wreck snorkel and island itineraries.",
            keywords="Aruba private tours cruise, private shore excursion Aruba, custom Oranjestad tour",
            path="aruba-private-tours.html",
            data_page="private",
            hero="partials/hero-private.html",
            content="aruba-private-tours.html",
            preload=PRIVATE_IMG,
        ),
        dict(
            file="aruba-family-excursions.html",
            title="Aruba Family Excursions | Kid-Friendly Oranjestad Cruise Tours",
            description="Family-friendly Aruba excursions — Eagle Beach, gentle snorkel and relaxed island tours for cruise guests with children.",
            keywords="Aruba family excursions, kid friendly Aruba cruise tours, family shore excursion Aruba",
            path="aruba-family-excursions.html",
            data_page="beaches",
            hero="partials/hero-family.html",
            content="aruba-family-excursions.html",
            preload=FAMILY_IMG,
        ),
        dict(
            file="aruba-beaches-guide.html",
            title="Aruba Beaches Guide | Eagle &amp; Palm Beach for Cruise Passengers",
            description="Aruba beaches guide for cruise visitors — Eagle Beach, Palm Beach and where to swim on an Oranjestad port day.",
            keywords="Aruba beaches guide cruise, Eagle Beach Palm Beach, best beach Aruba port day",
            path="aruba-beaches-guide.html",
            data_page="beaches",
            hero="partials/hero-beaches.html",
            content="aruba-beaches-guide.html",
            preload=BEACHES_IMG,
        ),
        dict(
            file="aruba-faq.html",
            title="Aruba Shore Excursions FAQ | Oranjestad Cruise Planning",
            description="FAQ for Aruba shore excursions — port hours, Antilla wreck, Eagle Beach, currency and independent vs ship booking.",
            keywords="Aruba shore excursions FAQ, Aruba cruise port questions, Antilla shipwreck FAQ cruise",
            path="aruba-faq.html",
            data_page="port",
            hero="partials/hero-faq.html",
            content="aruba-faq.html",
            preload=FAQ_IMG,
            schema=_faq_schema(),
        ),
    ]

    for p in pages:
        write(
            p["file"],
            page_shell(
                title=p["title"],
                description=p["description"],
                keywords=p["keywords"],
                canonical_path=p["path"],
                data_page=p["data_page"],
                hero=p["hero"],
                content=p["content"],
                preload=p.get("preload", HOME_HERO),
                schema=p.get("schema"),
            ),
        )

    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n")

    urls = [
        ("", "1.0", "weekly"),
        ("best-aruba-shore-excursions.html", "0.9", "monthly"),
        ("aruba-cruise-port-guide.html", "0.8", "monthly"),
        ("one-day-in-aruba.html", "0.8", "monthly"),
        ("eagle-beach-excursions.html", "0.9", "monthly"),
        ("aruba-snorkelling-tours.html", "0.8", "monthly"),
        ("antilla-shipwreck-excursions.html", "0.9", "monthly"),
        ("aruba-island-tours.html", "0.8", "monthly"),
        ("aruba-utv-atv-adventures.html", "0.8", "monthly"),
        ("arikok-national-park-tours.html", "0.7", "monthly"),
        ("california-lighthouse-tours.html", "0.7", "monthly"),
        ("aruba-private-tours.html", "0.8", "monthly"),
        ("aruba-family-excursions.html", "0.8", "monthly"),
        ("aruba-beaches-guide.html", "0.8", "monthly"),
        ("aruba-faq.html", "0.7", "monthly"),
        ("aruba-beach-vs-island-tour.html", "0.8", "monthly"),
        ("aruba-relaxed-vs-active.html", "0.8", "monthly"),
        ("about.html", "0.5", "yearly"),
        ("contact.html", "0.5", "yearly"),
        ("privacy.html", "0.3", "yearly"),
        ("terms.html", "0.3", "yearly"),
        ("methodology.html", "0.5", "yearly"),
    ]
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, priority, freq in urls:
        url = f"{DOMAIN}/{loc}" if loc else f"{DOMAIN}/"
        lines += [
            "  <url>",
            f"    <loc>{url}</loc>",
            f"    <lastmod>{DATE}</lastmod>",
            f"    <changefreq>{freq}</changefreq>",
            f"    <priority>{priority}</priority>",
            "  </url>",
        ]
    lines.append("</urlset>")
    write("sitemap.xml", "\n".join(lines) + "\n")

    write(
        "package.json",
        """{
  "name": "aruba-shore-excursion",
  "private": true,
  "scripts": {
    "sync:schedules": "node scripts/sync-schedules.mjs",
    "qa:schedules": "node scripts/qa-schedules.mjs",
    "build": "python3 scripts/build-aruba-site.py && python3 scripts/world2_extend_aruba.py && python3 scripts/generate_schedule_pages.py && python3 scripts/assemble-aruba-pages.py",
    "build:all": "npm run sync:schedules && npm run qa:schedules && npm run build",
    "images": "python3 scripts/fetch-aruba-images.py",
    "deploy": "npm run build && wrangler deploy",
    "preview": "python3 -m http.server 8902"
  },
  "devDependencies": {
    "wrangler": "^4.94.0"
  }
}
""",
    )

    # Phase 31B: Workers Assets + worker redirects/404. Routes required for custom domains.
    write(
        "wrangler.jsonc",
        """{
  "$schema": "node_modules/wrangler/config-schema.json",
  "name": "aruba-shore-excursion",
  "main": "worker.js",
  "compatibility_date": "2026-06-04",
  "workers_dev": true,
  "observability": { "enabled": true },
  "assets": {
    "directory": ".",
    "binding": "ASSETS",
    "html_handling": "drop-trailing-slash",
    "not_found_handling": "404-page",
    "run_worker_first": true
  },
  "routes": [
    {
      "pattern": "arubashoreexcursion.com/*",
      "zone_name": "arubashoreexcursion.com"
    },
    {
      "pattern": "www.arubashoreexcursion.com/*",
      "zone_name": "arubashoreexcursion.com"
    }
  ]
}
""",
    )

    write(
        "deploy.sh",
        f"""#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"

if [[ ! -f node_modules/.bin/wrangler ]]; then
  npm install
fi

echo "Building Aruba Shore Excursion…"
npm run build

echo "Deploying Aruba Shore Excursion to Cloudflare..."
npx wrangler deploy

echo "Done. Check {DOMAIN}/ shortly."
""",
    )

    (ROOT / "deploy.sh").chmod(0o755)

    images_dir = ROOT / "images"
    images_dir.mkdir(exist_ok=True)
    placeholders = [
        HOME_HERO, BEST_IMG, PORT_IMG, ONE_DAY_IMG, EAGLE_IMG, SNORKEL_IMG,
        ANTILLA_IMG, ISLAND_IMG, UTV_IMG, ARIKOK_IMG, LIGHTHOUSE_IMG,
        PRIVATE_IMG, FAMILY_IMG, BEACHES_IMG, FAQ_IMG, INTRO_IMG,
    ]
    for img in placeholders:
        p = ROOT / img
        if p.exists() and p.stat().st_size > 5000:
            continue
        if not p.exists() or p.stat().st_size <= 5000:
            p.write_bytes(
                b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01"
                b"\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89"
                b"\x00\x00\x00\nIDATx\x9cc\x00\x01\x00\x00\x05\x00\x01\r\n"
                b"\xdb\x00\x00\x00\x00IEND\xaeB`\x82"
            )

    print("Done.")


if __name__ == "__main__":
    main()
