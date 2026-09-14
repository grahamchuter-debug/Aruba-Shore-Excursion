#!/usr/bin/env python3
"""World 2.0 content extensions for Aruba Shore Excursion.

Runs after build-aruba-site.py. Rewrites homepage decision architecture,
decision pages, legal pages, nav/footer, softens unsupported claims, and
merges schedule sitemap fragments. Does not modify Cozumel.
"""
from __future__ import annotations

import importlib.util
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOMAIN = "https://arubashoreexcursion.com"
SITE = "Aruba Shore Excursion"
DATE = "2026-09-04"

_spec = importlib.util.spec_from_file_location(
    "build_aruba", ROOT / "scripts" / "build-aruba-site.py"
)
_build = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_build)

page_shell = _build.page_shell
cruise_snapshot = _build.cruise_snapshot
_hero_inner = _build._hero_inner
write = _build.write
HOME_HERO = _build.HOME_HERO
EAGLE_IMG = _build.EAGLE_IMG
EAGLE_ALT = _build.EAGLE_ALT
ANTILLA_IMG = _build.ANTILLA_IMG
ANTILLA_ALT = _build.ANTILLA_ALT
ISLAND_IMG = _build.ISLAND_IMG
ISLAND_ALT = _build.ISLAND_ALT
UTV_IMG = _build.UTV_IMG
UTV_ALT = _build.UTV_ALT
ARIKOK_IMG = _build.ARIKOK_IMG
ARIKOK_ALT = _build.ARIKOK_ALT
LIGHTHOUSE_IMG = _build.LIGHTHOUSE_IMG
LIGHTHOUSE_ALT = _build.LIGHTHOUSE_ALT
PORT_IMG = _build.PORT_IMG
PORT_ALT = _build.PORT_ALT
INTRO_IMG = _build.INTRO_IMG
INTRO_ALT = _build.INTRO_ALT
ACCENT = _build.ACCENT
HERO_GRADIENT = _build.HERO_GRADIENT
_hero_wave = _build._hero_wave
ONE_DAY_IMG = _build.ONE_DAY_IMG
ONE_DAY_ALT = _build.ONE_DAY_ALT
HOME_HERO_ALT = _build.HOME_HERO_ALT


def soft_claims_in_text(html: str) -> str:
    replacements = [
        (
            r"Operators usually allow 60[–-]90 min buffer",
            "Build your own buffer; confirm operator return plan",
        ),
        (
            r"Ship tours guarantee the vessel waits if the operator is late\. Reputable Aruba operators plan returns with buffer — confirm policies and read reviews\.",
            "Ship-sold tours often include a wait-if-late policy from the cruise line. Independent operators typically plan a return window — confirm policies, build your own buffer, and do not cut it fine.",
        ),
        (
            r"Ship tours guarantee wait-if-late; reputable locals plan buffer returns\.",
            "Ship-sold tours often include wait-if-late; confirm independent operator policies and build your own buffer.",
        ),
        (
            r"with return buffer",
            "with a sensible return window",
        ),
        (
            r"Allow margin before published all-aboard\.",
            "Build your own buffer before published all-aboard — confirm times with your ship and operator.",
        ),
        (
            r"plan returns with buffer before all aboard",
            "plan returns with enough time before all aboard — confirm with the operator",
        ),
        (
            r"and a fixed return to the pier",
            "and a timed return window to the pier — confirm details with the operator",
        ),
        (
            r"understand all-aboard deadlines",
            "usually plan around all-aboard — still confirm return timing in writing",
        ),
    ]
    out = html
    for pat, repl in replacements:
        out = re.sub(pat, repl, out)
    return out


def soft_all_content() -> None:
    content_dir = ROOT / "content"
    for path in content_dir.glob("*.html"):
        original = path.read_text(encoding="utf-8")
        updated = soft_claims_in_text(original)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            print(f"  softened claims in content/{path.name}")


def internal_links() -> str:
    return """<nav class="mt-10 pt-8 border-t border-gray-100" aria-label="Related Aruba guides">
  <p class="text-sm font-semibold text-gray-900 mb-3">Plan your Oranjestad port day</p>
  <div class="flex flex-wrap gap-3 text-sm">
    <a href="aruba-cruise-port-guide.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Port Guide</a>
    <span class="text-gray-300">·</span>
    <a href="best-aruba-shore-excursions.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Best Excursions</a>
    <span class="text-gray-300">·</span>
    <a href="aruba-beach-vs-island-tour.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Beach vs Island</a>
    <span class="text-gray-300">·</span>
    <a href="aruba-relaxed-vs-active.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Relaxed vs Active</a>
    <span class="text-gray-300">·</span>
    <a href="ship-schedule/" class="text-ocean-600 hover:text-ocean-800 font-medium">Ship Schedule</a>
    <span class="text-gray-300">·</span>
    <a href="aruba-faq.html" class="text-ocean-600 hover:text-ocean-800 font-medium">FAQ</a>
  </div>
</nav>"""


def concierge_panel() -> str:
    return """<section class="py-14 bg-white" id="concierge" aria-labelledby="concierge-heading">
  <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="concierge-panel">
      <h2 id="concierge-heading" class="font-display font-bold text-2xl sm:text-3xl mb-3">Need help shaping your Aruba day?</h2>
      <p class="text-white/90 text-sm sm:text-base leading-relaxed mb-4">
        Tell us your ship, call date, and whether you lean beach, Antilla snorkel, island sightseeing, Arikok, or a UTV trail.
        We are an independent planning resource — not the cruise line and not a ticket marketplace.
      </p>
      <p class="text-white/80 text-sm leading-relaxed mb-5">
        Email <a href="mailto:hello@arubashoreexcursion.com">hello@arubashoreexcursion.com</a> with your ship, date and preferences.
        We do not promise instant replies or 24/7 staffing.
      </p>
      <div class="flex flex-col sm:flex-row gap-3">
        <a href="mailto:hello@arubashoreexcursion.com" class="btn-primary inline-flex items-center justify-center text-white font-semibold px-6 py-3 rounded-full text-sm no-underline">Email the Aruba concierge</a>
        <a href="best-aruba-shore-excursions.html" class="btn-outline inline-flex items-center justify-center text-white font-semibold px-6 py-3 rounded-full text-sm no-underline">Compare excursion types</a>
      </div>
    </div>
  </div>
</section>"""


def snapshot(**overrides: str) -> str:
    defaults = dict(
        time_in_port="8–10 hours (typical)",
        best_for="Beaches, wreck snorkel, island tours, dry-side trails",
        activity_level="Varies — beach calm to UTV / Arikok",
        family="Excellent with age-appropriate picks",
        return_ship="Build your own buffer; confirm operator return plan",
        popular="Eagle Beach, Antilla, California Lighthouse, Arikok, UTV",
    )
    defaults.update(overrides)
    return cruise_snapshot(**defaults)


def write_nav() -> None:
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
        <a href="ship-schedule/" data-nav="schedule" class="text-gray-600 hover:text-ocean-600 transition-colors">Ship Schedule</a>
        <a href="aruba-cruise-port-guide.html" data-nav="port" class="text-gray-600 hover:text-ocean-600 transition-colors">Port Guide</a>
      </div>
      <a href="contact.html" class="hidden md:inline-flex items-center gap-2 btn-ocean text-white text-sm font-semibold px-4 py-2 rounded-full shadow-md">
        Contact concierge
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


def write_footer() -> None:
    write(
        "partials/footer.html",
        f"""  <footer class="bg-gray-900 text-gray-400 py-14">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-10 mb-12">
        <div class="sm:col-span-2 lg:col-span-1">
          <a href="index.html" class="font-display font-semibold text-white text-lg">{SITE}</a>
          <p class="mt-3 text-sm leading-relaxed">Independent planning guide for cruise visitors docking at Oranjestad. Not affiliated with any cruise line.</p>
        </div>
        <div>
          <h3 class="text-white text-sm font-semibold uppercase tracking-wider mb-4">Excursions</h3>
          <ul class="space-y-2 text-sm">
            <li><a href="best-aruba-shore-excursions.html" class="hover:text-white transition-colors">All Excursions</a></li>
            <li><a href="eagle-beach-excursions.html" class="hover:text-white transition-colors">Eagle Beach</a></li>
            <li><a href="antilla-shipwreck-excursions.html" class="hover:text-white transition-colors">Antilla Shipwreck</a></li>
            <li><a href="aruba-island-tours.html" class="hover:text-white transition-colors">Island Tours</a></li>
            <li><a href="aruba-utv-atv-adventures.html" class="hover:text-white transition-colors">UTV &amp; ATV</a></li>
            <li><a href="arikok-national-park-tours.html" class="hover:text-white transition-colors">Arikok National Park</a></li>
            <li><a href="aruba-beach-vs-island-tour.html" class="hover:text-white transition-colors">Beach vs Island</a></li>
            <li><a href="aruba-relaxed-vs-active.html" class="hover:text-white transition-colors">Relaxed vs Active</a></li>
          </ul>
        </div>
        <div>
          <h3 class="text-white text-sm font-semibold uppercase tracking-wider mb-4">Resources</h3>
          <ul class="space-y-2 text-sm">
            <li><a href="aruba-cruise-port-guide.html" class="hover:text-white transition-colors">Port Guide</a></li>
            <li><a href="ship-schedule/" class="hover:text-white transition-colors">Ship Schedule</a></li>
            <li><a href="one-day-in-aruba.html" class="hover:text-white transition-colors">One Day in Aruba</a></li>
            <li><a href="aruba-beaches-guide.html" class="hover:text-white transition-colors">Beaches Guide</a></li>
            <li><a href="california-lighthouse-tours.html" class="hover:text-white transition-colors">California Lighthouse</a></li>
            <li><a href="aruba-faq.html" class="hover:text-white transition-colors">FAQ</a></li>
            <li><a href="methodology.html" class="hover:text-white transition-colors">Methodology</a></li>
          </ul>
        </div>
        <div>
          <h3 class="text-white text-sm font-semibold uppercase tracking-wider mb-4">Legal</h3>
          <ul class="space-y-2 text-sm">
            <li><a href="about.html" class="hover:text-white transition-colors">About</a></li>
            <li><a href="contact.html" class="hover:text-white transition-colors">Contact</a></li>
            <li><a href="privacy.html" class="hover:text-white transition-colors">Privacy</a></li>
            <li><a href="terms.html" class="hover:text-white transition-colors">Terms</a></li>
          </ul>
        </div>
      </div>
      <div class="border-t border-gray-800 pt-8 text-xs text-center sm:text-left">
        <p>&copy; 2026 {SITE}. Confirm times with your cruise line and operators. No fabricated prices or ratings on this site.</p>
      </div>
    </div>
  </footer>
""",
    )


def hero_home() -> str:
    return f"""  <section class="site-hero">
    <div class="absolute inset-0 hero-bg" style="background-image: {HERO_GRADIENT}, url('{HOME_HERO}');" role="img" aria-label="{HOME_HERO_ALT}"></div>
    <div class="site-hero__inner max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="max-w-3xl">
        <div class="site-hero__eyebrow inline-flex items-center gap-2 bg-white/15 backdrop-blur-sm border border-white/30 rounded-full px-4 py-1.5 mb-3">
          <span class="w-2 h-2 rounded-full bg-teal-400 animate-pulse"></span>
          <span class="text-white/90 text-xs font-semibold tracking-widest uppercase">Oranjestad pier · Dry side meets turquoise</span>
        </div>
        <h1 class="site-hero__title text-4xl sm:text-5xl lg:text-[3.25rem] font-display font-bold text-white leading-tight mb-3">
          Aruba Shore<br/><span class="{ACCENT}">Excursion</span>
        </h1>
        <p class="site-hero__lead text-base sm:text-lg text-white/85 font-light leading-relaxed mb-5 max-w-2xl">
          Step off at Oranjestad and choose your Aruba: calm Eagle Beach sand, Antilla wreck snorkelling, California Lighthouse viewpoints, or the cactus hills of Arikok.
        </p>
        <div class="site-hero__actions flex flex-col sm:flex-row gap-3">
          <a href="aruba-beach-vs-island-tour.html" class="btn-primary inline-flex items-center justify-center gap-2 text-white font-semibold px-7 py-3 rounded-full text-sm shadow-xl">Beach or island day?</a>
          <a href="ship-schedule/" class="btn-outline inline-flex items-center justify-center gap-2 text-white font-semibold px-7 py-3 rounded-full text-sm">Find your ship</a>
        </div>
        <div class="site-hero__tags flex flex-wrap gap-2 mt-5 pt-4 border-t border-white/20">
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Eagle Beach</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Antilla Wreck</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Arikok</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">California Lighthouse</span>
        </div>
      </div>
    </div>
    {_hero_wave()}
  </section>"""


def content_home() -> str:
    snap = snapshot()
    return f"""<section class="pt-8 pb-6 bg-white"><div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
  <p class="section-label mx-auto">Oranjestad cruise call</p>
  <h2 class="text-2xl sm:text-3xl font-display font-bold text-gray-900 mb-3">Aruba is two moods in one island</h2>
  <p class="text-gray-600 text-sm sm:text-base leading-relaxed">Ships dock at Oranjestad — no tender for a typical call. From the pier you can chase wide white sand, wreck snorkelling on the leeward coast, or the dry cactus landscape that makes Aruba feel unlike a rainforested Caribbean stop.</p>
</div></section>
<section class="pb-10 bg-white"><div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
  <div class="decision-grid">
    <div class="decision-card"><h3 class="font-display font-bold text-gray-900">Beach day</h3><p>Eagle Beach for fofoti trees and calm water, or Palm Beach when you want resorts and facilities.</p><a href="eagle-beach-excursions.html" class="text-ocean-600 font-semibold text-sm">Eagle Beach →</a></div>
    <div class="decision-card"><h3 class="font-display font-bold text-gray-900">Island / dry side</h3><p>California Lighthouse, aloe stops, Casibari rocks and north-coast viewpoints without committing to UTV dust.</p><a href="aruba-island-tours.html" class="text-ocean-600 font-semibold text-sm">Island tours →</a></div>
    <div class="decision-card"><h3 class="font-display font-bold text-gray-900">Wreck snorkel</h3><p>Antilla freighter wreck in shallow turquoise water — Aruba’s signature underwater stop.</p><a href="antilla-shipwreck-excursions.html" class="text-ocean-600 font-semibold text-sm">Antilla →</a></div>
    <div class="decision-card"><h3 class="font-display font-bold text-gray-900">Active / Arikok</h3><p>UTV trails or Arikok National Park when you want cactus hills and Natural Pool energy.</p><a href="aruba-relaxed-vs-active.html" class="text-ocean-600 font-semibold text-sm">Relaxed vs active →</a></div>
    <div class="decision-card"><h3 class="font-display font-bold text-gray-900">Beach vs island</h3><p>Honest trade-offs between sand time and sightseeing on a typical 8–10 hour call.</p><a href="aruba-beach-vs-island-tour.html" class="text-ocean-600 font-semibold text-sm">Compare →</a></div>
    <div class="decision-card"><h3 class="font-display font-bold text-gray-900">Find your ship</h3><p>Search Oranjestad call dates, then leave a sensible return window before all aboard.</p><a href="ship-schedule/" class="text-ocean-600 font-semibold text-sm">Ship schedule →</a></div>
  </div>
</div></section>
<section class="py-12 bg-sand-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-center">
  <div>
    <p class="section-label">Pier orientation</p>
    <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Oranjestad is a walk-on port</h2>
    <p class="text-gray-600 leading-relaxed mb-4">Cruise ships berth at Oranjestad’s piers. Tendering is not part of a normal Aruba call — you step ashore into Dutch-Caribbean streets, taxis and tour meeting points. That pier access is why beach transfers and island loops fit so many schedules.</p>
    <a href="aruba-cruise-port-guide.html" class="btn-ocean inline-flex items-center gap-2 text-white font-semibold px-7 py-3.5 rounded-full text-sm shadow-lg">Port guide</a>
  </div>
  <div class="info-image rounded-3xl aspect-[4/3] shadow-2xl overflow-hidden">
    <img src="{PORT_IMG}" alt="{PORT_ALT}" width="800" height="600" loading="lazy" decoding="async" />
  </div>
</div></div></section>
<section class="py-12 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-center">
  <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg order-2 lg:order-1">
    <img src="{INTRO_IMG}" alt="{INTRO_ALT}" width="800" height="600" loading="lazy" decoding="async" />
  </div>
  <div class="order-1 lg:order-2">
    <p class="section-label">Dry landscape identity</p>
    <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Cactus hills beside turquoise beaches</h2>
    <p class="text-gray-600 leading-relaxed mb-4">Aruba’s arid interior is part of the appeal — Arikok’s rocky trails and north-coast lookouts sit a short drive from Eagle Beach’s calm sand. Choose soft or dusty; do not assume every “island tour” means the same intensity.</p>
    <a href="arikok-national-park-tours.html" class="text-ocean-600 font-semibold text-sm">Arikok →</a>
    <span class="text-gray-300 mx-2">·</span>
    <a href="aruba-utv-atv-adventures.html" class="text-ocean-600 font-semibold text-sm">UTV adventures →</a>
  </div>
</div></div></section>
<section class="pb-4 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="py-12 bg-sand-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <div class="text-center mb-10">
    <p class="section-label mx-auto">Signature stops</p>
    <h2 class="text-3xl font-display font-bold text-gray-900 mb-3">Four Aruba experiences cruise guests compare most</h2>
  </div>
  <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
    <div class="bg-white rounded-3xl overflow-hidden shadow-md border border-aruba-50 flex flex-col">
      <div class="card-media h-44"><img src="{EAGLE_IMG}" alt="{EAGLE_ALT}" width="600" height="352" loading="lazy" decoding="async" /></div>
      <div class="p-6 flex flex-col flex-1"><h3 class="text-lg font-display font-semibold text-gray-900 mb-2">Eagle Beach</h3><p class="text-sm text-gray-500 flex-1">Wide sand, fofoti trees and a calmer swim day.</p><a href="eagle-beach-excursions.html" class="mt-5 text-ocean-600 font-semibold text-sm">Eagle Beach →</a></div>
    </div>
    <div class="bg-white rounded-3xl overflow-hidden shadow-md border border-aruba-50 flex flex-col">
      <div class="card-media h-44"><img src="{ANTILLA_IMG}" alt="{ANTILLA_ALT}" width="600" height="352" loading="lazy" decoding="async" /></div>
      <div class="p-6 flex flex-col flex-1"><h3 class="text-lg font-display font-semibold text-gray-900 mb-2">Antilla wreck</h3><p class="text-sm text-gray-500 flex-1">WWII freighter snorkel in clear leeward water.</p><a href="antilla-shipwreck-excursions.html" class="mt-5 text-ocean-600 font-semibold text-sm">Antilla →</a></div>
    </div>
    <div class="bg-white rounded-3xl overflow-hidden shadow-md border border-aruba-50 flex flex-col">
      <div class="card-media h-44"><img src="{LIGHTHOUSE_IMG}" alt="{LIGHTHOUSE_ALT}" width="600" height="352" loading="lazy" decoding="async" /></div>
      <div class="p-6 flex flex-col flex-1"><h3 class="text-lg font-display font-semibold text-gray-900 mb-2">California Lighthouse</h3><p class="text-sm text-gray-500 flex-1">North-tip views on most sightseeing loops.</p><a href="california-lighthouse-tours.html" class="mt-5 text-ocean-600 font-semibold text-sm">Lighthouse →</a></div>
    </div>
    <div class="bg-white rounded-3xl overflow-hidden shadow-md border border-aruba-50 flex flex-col">
      <div class="card-media h-44"><img src="{ARIKOK_IMG}" alt="{ARIKOK_ALT}" width="600" height="352" loading="lazy" decoding="async" /></div>
      <div class="p-6 flex flex-col flex-1"><h3 class="text-lg font-display font-semibold text-gray-900 mb-2">Arikok</h3><p class="text-sm text-gray-500 flex-1">Protected dry hills and Natural Pool access with a guide.</p><a href="arikok-national-park-tours.html" class="mt-5 text-ocean-600 font-semibold text-sm">Arikok →</a></div>
    </div>
  </div>
  <p class="text-center mt-8"><a href="best-aruba-shore-excursions.html" class="text-ocean-600 font-semibold text-sm">Full comparison →</a></p>
</div></section>
<section class="py-12 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-center">
  <div>
    <p class="section-label">Ship planning</p>
    <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Match the day to your Oranjestad call</h2>
    <p class="text-gray-600 leading-relaxed mb-4">Browse arrivals by month, note your all-aboard window, then choose beach calm or dry-side intensity. Schedules can change — treat published times as planning aids and build your own buffer.</p>
    <a href="ship-schedule/" class="btn-ocean inline-flex items-center gap-2 text-white font-semibold px-7 py-3.5 rounded-full text-sm">Find your ship schedule</a>
  </div>
  <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="{ONE_DAY_IMG}" alt="{ONE_DAY_ALT}" width="800" height="600" loading="lazy" decoding="async" />
  </div>
</div></div></section>
<section class="py-16 cta-gradient"><div class="max-w-3xl mx-auto px-4 text-center">
  <h2 class="text-3xl font-display font-bold text-white mb-4">Still deciding?</h2>
  <p class="text-white/85 text-sm mb-6">Compare beach versus island sightseeing, or email the Aruba concierge with your ship and date.</p>
  <div class="flex flex-col sm:flex-row gap-4 justify-center">
    <a href="aruba-beach-vs-island-tour.html" class="btn-primary inline-flex items-center justify-center text-white font-semibold px-8 py-4 rounded-full">Beach vs island</a>
    <a href="contact.html" class="btn-outline inline-flex items-center justify-center text-white font-semibold px-8 py-4 rounded-full">Contact concierge</a>
  </div>
</div></section>
{concierge_panel()}"""


def content_port() -> str:
    snap = snapshot(
        activity_level="Low at pier; moderate on tours",
        popular="Pier walk-off, taxis, organised pickups",
        best_for="Orienting at Oranjestad before beach or island plans",
    )
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4 text-center">
  <p class="text-gray-600 leading-relaxed text-sm">Aruba is a <strong>pier port</strong>. Ships berth at <strong>Oranjestad</strong> — downtown shops, taxis and excursion meeting points are close ashore on a typical <strong>8–10 hour</strong> call. Tendering is not required for a standard Aruba cruise stop.</p>
</div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="py-12 bg-sand-50"><div class="max-w-7xl mx-auto px-4">
  <h2 class="text-2xl font-display font-bold text-center mb-8">Where ships arrive</h2>
  <div class="info-image rounded-3xl aspect-[21/9] shadow-xl overflow-hidden mb-8 max-w-5xl mx-auto">
    <img src="{PORT_IMG}" alt="{PORT_ALT}" width="1200" height="514" loading="lazy" decoding="async" />
  </div>
  <div class="grid lg:grid-cols-2 gap-6 text-sm">
    <div class="bg-white rounded-3xl p-6 border border-aruba-100"><h3 class="font-display font-bold text-lg mb-2">Oranjestad piers</h3><p class="text-gray-600">Modern berths place you steps from colourful Dutch-Caribbean streets. Confirm your meeting point with the operator — pier plazas and taxi ranks are busy on multi-ship days.</p></div>
    <div class="bg-white rounded-3xl p-6 border border-aruba-100"><h3 class="font-display font-bold text-lg mb-2">Getting to beaches</h3><p class="text-gray-600">Eagle Beach and Palm Beach are typically 10–20 minutes by taxi or organised transfer. Build your own return window rather than assuming a fixed buffer.</p></div>
  </div>
</div></section>
<section class="py-12 bg-white"><div class="max-w-7xl mx-auto px-4">
  <div class="grid sm:grid-cols-3 gap-6 text-sm">
    <div class="bg-sand-50 rounded-2xl p-6"><strong class="text-gray-900">Currency</strong><p class="mt-2 text-gray-600">Aruban florin (AWG); <strong>US dollars</strong> widely accepted at excursions and taxis.</p></div>
    <div class="bg-ocean-50 rounded-2xl p-6"><strong class="text-gray-900">Language</strong><p class="mt-2 text-gray-600">Dutch and Papiamento official; English common in tourism and at the port.</p></div>
    <div class="bg-sand-50 rounded-2xl p-6"><strong class="text-gray-900">Landscape note</strong><p class="mt-2 text-gray-600">Expect arid hills and cactus inland — Aruba’s dry identity sits beside its famous beaches.</p></div>
  </div>
  <p class="text-center mt-8"><a href="one-day-in-aruba.html" class="text-ocean-600 font-semibold text-sm">One-day itinerary →</a>
  <span class="text-gray-300 mx-2">·</span>
  <a href="ship-schedule/" class="text-ocean-600 font-semibold text-sm">Ship schedule →</a></p>
  <div class="mt-10 max-w-3xl mx-auto">{internal_links()}</div>
</div></section>
{concierge_panel()}"""


def content_beach_vs_island() -> str:
    snap = snapshot(
        best_for="Choosing beach sand vs island / Arikok sightseeing",
        activity_level="Beach low; island low–moderate; Arikok higher",
        popular="Eagle Beach vs lighthouse / north coast / Arikok",
    )
    return f"""<section class="pt-8 pb-6 bg-white"><div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
  <p class="text-gray-600 leading-relaxed mb-4">On a typical Oranjestad call, Aruba often comes down to a <strong>beach day</strong> or an <strong>island / dry-side day</strong>. Both are excellent. They spend your hours differently.</p>
  <p class="text-gray-600 leading-relaxed">Beach days maximise sand and swimming. Island sightseeing and Arikok trade lounger time for lighthouse views, cactus hills and north-coast drama.</p>
</div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="py-12 bg-sand-50"><div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-2xl font-display font-bold text-gray-900 text-center mb-8">Beach day vs island / Arikok day</h2>
  <div class="grid md:grid-cols-2 gap-6 text-sm">
    <div class="bg-white rounded-3xl p-6 border border-aruba-100">
      <div class="card-media rounded-2xl overflow-hidden aspect-[16/10] mb-4">
        <img src="{EAGLE_IMG}" alt="{EAGLE_ALT}" width="600" height="375" loading="lazy" decoding="async" />
      </div>
      <h3 class="font-display font-bold text-lg mb-3">Beach day</h3>
      <ul class="space-y-2 text-gray-600">
        <li>Eagle Beach for iconic fofoti trees and calmer water</li>
        <li>Palm Beach when you want resorts and water sports nearby</li>
        <li>Shorter logistics from Oranjestad on organised transfers</li>
        <li>Best when swimming and shade matter more than sightseeing stops</li>
      </ul>
      <p class="mt-4"><a href="eagle-beach-excursions.html" class="text-ocean-600 font-semibold">Eagle Beach →</a> · <a href="aruba-beaches-guide.html" class="text-ocean-600 font-semibold">Beaches guide →</a></p>
    </div>
    <div class="bg-white rounded-3xl p-6 border border-aruba-100">
      <div class="card-media rounded-2xl overflow-hidden aspect-[16/10] mb-4">
        <img src="{ISLAND_IMG}" alt="{ISLAND_ALT}" width="600" height="375" loading="lazy" decoding="async" />
      </div>
      <h3 class="font-display font-bold text-lg mb-3">Island / north coast / Arikok</h3>
      <ul class="space-y-2 text-gray-600">
        <li>California Lighthouse, aloe visits and rock formations on van tours</li>
        <li>Arikok for protected dry hills and Natural Pool access (conditions vary)</li>
        <li>More moving parts and sun exposure than a lounger day</li>
        <li>Better when you want Aruba’s arid character, not only its beaches</li>
      </ul>
      <p class="mt-4"><a href="aruba-island-tours.html" class="text-ocean-600 font-semibold">Island tours →</a> · <a href="arikok-national-park-tours.html" class="text-ocean-600 font-semibold">Arikok →</a></p>
    </div>
  </div>
</div></section>
<section class="py-12 bg-white"><div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
  <div class="grid lg:grid-cols-2 gap-10 items-center mb-12">
    <div>
      <h2 class="text-2xl font-display font-bold text-gray-900 mb-3">Mixing both on a long call</h2>
      <p class="text-gray-600 leading-relaxed mb-3">On a longer Oranjestad day, some guests beach in the morning and add a short lighthouse stop later — or the reverse. Two well-paced blocks beat three rushed attractions.</p>
      <p class="text-gray-600 leading-relaxed">Check your ship’s all-aboard time and build your own buffer. Do not rely on a published “60–90 minutes” promise.</p>
      <p class="mt-4"><a href="one-day-in-aruba.html" class="text-ocean-600 font-semibold">One-day paths →</a> · <a href="ship-schedule/" class="text-ocean-600 font-semibold">Ship schedule →</a></p>
    </div>
    <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
      <img src="{LIGHTHOUSE_IMG}" alt="{LIGHTHOUSE_ALT}" width="600" height="450" loading="lazy" decoding="async" />
    </div>
  </div>
  <div class="mt-4 max-w-3xl mx-auto">{internal_links()}</div>
</div></section>
{concierge_panel()}"""


def content_relaxed_vs_active() -> str:
    snap = snapshot(
        best_for="Choosing Eagle Beach calm vs UTV / Arikok intensity",
        activity_level="Relaxed low; UTV/Arikok moderate to high",
        popular="Eagle Beach vs UTV trails / Natural Pool",
    )
    return f"""<section class="pt-8 pb-6 bg-white"><div class="max-w-3xl mx-auto px-4">
  <p class="text-gray-600 leading-relaxed mb-4">If your Aruba priority is energy level, compare a <strong>relaxed Eagle Beach day</strong> with an <strong>active UTV or Arikok day</strong>. Heat, dust and uneven ground change who enjoys which option.</p>
</div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="py-12 bg-sand-50"><div class="max-w-5xl mx-auto px-4">
  <div class="grid md:grid-cols-2 gap-6 text-sm">
    <div class="bg-white rounded-3xl p-6 border border-aruba-100">
      <div class="card-media rounded-2xl overflow-hidden aspect-[16/10] mb-4">
        <img src="{EAGLE_IMG}" alt="{EAGLE_ALT}" width="600" height="375" loading="lazy" decoding="async" />
      </div>
      <h3 class="font-display font-bold text-lg mb-2">Relaxed — Eagle Beach</h3>
      <p class="text-gray-600 mb-3">Better when you want swimming, shade breaks and minimal bouncing. Family groups and first-time visitors often start here. Confirm transfer return times with the operator.</p>
      <a href="eagle-beach-excursions.html" class="text-ocean-600 font-semibold">Eagle Beach →</a>
      <span class="text-gray-300 mx-2">·</span>
      <a href="aruba-family-excursions.html" class="text-ocean-600 font-semibold">Family options →</a>
    </div>
    <div class="bg-white rounded-3xl p-6 border border-aruba-100">
      <div class="card-media rounded-2xl overflow-hidden aspect-[16/10] mb-4">
        <img src="{UTV_IMG}" alt="{UTV_ALT}" width="600" height="375" loading="lazy" decoding="async" />
      </div>
      <h3 class="font-display font-bold text-lg mb-2">Active — UTV / Arikok</h3>
      <p class="text-gray-600 mb-3">Better when you want dusty trails, north-coast overlooks or Natural Pool access. Expect sun, uneven ground and operator age/height rules on UTV rides. Not ideal for serious back or mobility limits.</p>
      <a href="aruba-utv-atv-adventures.html" class="text-ocean-600 font-semibold">UTV adventures →</a>
      <span class="text-gray-300 mx-2">·</span>
      <a href="arikok-national-park-tours.html" class="text-ocean-600 font-semibold">Arikok →</a>
    </div>
  </div>
  <p class="text-center mt-8 text-sm text-gray-600">Want scenery without UTV intensity? An air-conditioned <a href="aruba-island-tours.html" class="text-ocean-600 font-semibold">island sightseeing tour</a> sits between these poles.</p>
  <div class="mt-10 max-w-3xl mx-auto">{internal_links()}</div>
</div></section>
{concierge_panel()}"""


def content_about() -> str:
    return f"""<section class="pt-10 pb-16 bg-white"><div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">About Aruba Shore Excursion</h2>
  <p class="text-gray-600 leading-relaxed mb-4">Aruba is not a lush-rainforest Caribbean stereotype. Cruise guests step off at Oranjestad into a dry, cactus-edged landscape with some of the region’s calmest swimming beaches a short transfer away. This site exists to make those trade-offs clear before you spend the call.</p>
  <p class="text-gray-600 leading-relaxed mb-4">We write for passengers weighing Eagle Beach sand against Antilla wreck time, California Lighthouse viewpoints, Arikok trails or a UTV loop — timed around a typical pier day. We are not a cruise line, ticket marketplace or port authority.</p>
  <p class="text-gray-600 leading-relaxed mb-4">Ship schedules here are synced from the Caribbean Shore Excursions authority import for Aruba only. Arrival and departure times can still change; confirm with your cruise line.</p>
  <p class="text-gray-600 leading-relaxed mb-8">Network context: <a href="https://caribbeanshoreexcursion.com/" class="text-ocean-600 font-medium">Caribbean Shore Excursions</a>. Destination detail for Aruba lives on this site.</p>
  {internal_links()}
</div></section>
{concierge_panel()}"""


def content_contact() -> str:
    return f"""<section class="pt-10 pb-8 bg-white"><div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Contact</h2>
  <p class="text-gray-600 leading-relaxed mb-4">If you want help narrowing an Aruba port day, include your ship name, call date, and whether you prefer Eagle Beach, Antilla snorkelling, island sightseeing, Arikok or a UTV trail.</p>
  <p class="text-gray-600 leading-relaxed mb-6">Email <a class="text-ocean-600 font-semibold" href="mailto:hello@arubashoreexcursion.com">hello@arubashoreexcursion.com</a>. Replies are handled when we can — this is a planning concierge, not a booking desk.</p>
  <ul class="space-y-2 text-sm text-gray-600 mb-8">
    <li><a class="text-ocean-600 font-semibold" href="ship-schedule/">Find your ship schedule</a></li>
    <li><a class="text-ocean-600 font-semibold" href="best-aruba-shore-excursions.html">Compare excursion types</a></li>
    <li><a class="text-ocean-600 font-semibold" href="aruba-cruise-port-guide.html">Read the port guide</a></li>
    <li><a class="text-ocean-600 font-semibold" href="aruba-beach-vs-island-tour.html">Beach vs island decision</a></li>
  </ul>
  {internal_links()}
</div></section>
{concierge_panel()}"""


def content_privacy() -> str:
    return """<section class="pt-10 pb-16 bg-white"><div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Privacy</h2>
  <p class="text-gray-600 leading-relaxed mb-4">This is a static planning website. In this phase we do not operate a booking engine, payment system, or passenger account database.</p>
  <p class="text-gray-600 leading-relaxed mb-4">Messages sent to hello@arubashoreexcursion.com are used only to respond about Aruba port-day planning. We will not sell contact details.</p>
  <p class="text-gray-600 leading-relaxed mb-4">Standard web server and CDN logs may record technical request data (such as IP address, user agent and requested URL) as part of delivering the site securely. We do not add analytics trackers in this build.</p>
  <p class="text-gray-600 leading-relaxed">If our contact or tooling practices change, this page will be updated before those features go live.</p>
</div></section>"""


def content_terms() -> str:
    return """<section class="pt-10 pb-16 bg-white"><div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Terms of use</h2>
  <p class="text-gray-600 leading-relaxed mb-4">Content on Aruba Shore Excursion is provided for general information and planning. It is not a contract of carriage, not travel insurance, and not a guarantee of excursion availability, wildlife sightings, weather or on-time return to your ship.</p>
  <p class="text-gray-600 leading-relaxed mb-4">Cruise schedules, pier operations and excursion details can change. Confirm final arrangements with your cruise line and any operator you choose.</p>
  <p class="text-gray-600 leading-relaxed mb-4">We are independent of cruise lines and of Aruba’s port operators. Mentions of beaches, parks or landmarks are for orientation and do not imply partnership unless we say so explicitly.</p>
  <p class="text-gray-600 leading-relaxed">You are responsible for leaving enough time to reboard, for following local rules, and for checking any medical or activity requirements before water or adventure activities.</p>
</div></section>"""


def content_methodology() -> str:
    return f"""<section class="pt-10 pb-16 bg-white"><div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">How we assess Aruba excursions</h2>
  <p class="text-gray-600 leading-relaxed mb-4">We judge options the way a cruise passenger has to: against the length of the Oranjestad call, pier logistics, heat and transfer time, and how much return buffer you need before all aboard.</p>
  <div class="space-y-4 text-sm text-gray-600 mb-8">
    <div class="bg-sand-50 rounded-2xl p-5 border border-aruba-100"><h3 class="font-display font-bold text-gray-900 mb-2">Cruise timing first</h3><p>A brilliant full-day UTV-and-Arikok mash-up is the wrong answer on a short call. We favour options that leave a realistic return window.</p></div>
    <div class="bg-ocean-50 rounded-2xl p-5 border border-ocean-100"><h3 class="font-display font-bold text-gray-900 mb-2">Decision clarity</h3><p>Beach versus island sightseeing, relaxed Eagle Beach versus UTV/Arikok intensity — passengers need honest trade-offs, not marketplace noise.</p></div>
    <div class="bg-sand-50 rounded-2xl p-5 border border-aruba-100"><h3 class="font-display font-bold text-gray-900 mb-2">No invented proof</h3><p>We do not invent star ratings, review counts, “places left” or fabricated prices. Trust comes from clear planning language and transparent limits.</p></div>
    <div class="bg-ocean-50 rounded-2xl p-5 border border-ocean-100"><h3 class="font-display font-bold text-gray-900 mb-2">Schedule integrity</h3><p>Call lists are generated from the Caribbean authority import for Aruba, then checked for count and record-level match before pages are built.</p></div>
  </div>
  {internal_links()}
</div></section>
{concierge_panel()}"""


NEW_PAGES = [
    dict(
        file="aruba-beach-vs-island-tour.html",
        title="Aruba Beach Day vs Island Tour | Oranjestad Cruise Decision",
        description="Compare an Aruba beach day with island sightseeing or Arikok on a cruise call from Oranjestad — honest trade-offs for sand versus dry-side views.",
        keywords="Aruba beach vs island tour, Eagle Beach vs Arikok, Oranjestad cruise decision",
        path="aruba-beach-vs-island-tour.html",
        data_page="excursions",
        hero="partials/hero-beach-vs-island.html",
        content="aruba-beach-vs-island-tour.html",
        preload=EAGLE_IMG,
    ),
    dict(
        file="aruba-relaxed-vs-active.html",
        title="Aruba Relaxed vs Active Excursions | Eagle Beach or UTV",
        description="Choose a relaxed Eagle Beach day or an active UTV / Arikok Aruba excursion — intensity trade-offs for cruise passengers from Oranjestad.",
        keywords="Aruba relaxed vs active, Eagle Beach vs UTV, Arikok cruise excursion",
        path="aruba-relaxed-vs-active.html",
        data_page="excursions",
        hero="partials/hero-relaxed-vs-active.html",
        content="aruba-relaxed-vs-active.html",
        preload=UTV_IMG,
    ),
    dict(
        file="about.html",
        title="About Aruba Shore Excursion | Independent Port Planning",
        description="About Aruba Shore Excursion — independent planning guidance for cruise passengers calling at Oranjestad.",
        keywords="about Aruba Shore Excursion, Aruba cruise planning",
        path="about.html",
        data_page="about",
        hero="partials/hero-about.html",
        content="about.html",
        preload=INTRO_IMG,
    ),
    dict(
        file="contact.html",
        title="Contact Aruba Shore Excursion | Concierge",
        description="Contact the Aruba shore excursion concierge at hello@arubashoreexcursion.com for Oranjestad port-day planning help.",
        keywords="contact Aruba Shore Excursion, Aruba cruise concierge",
        path="contact.html",
        data_page="contact",
        hero="partials/hero-contact.html",
        content="contact.html",
        preload=INTRO_IMG,
    ),
    dict(
        file="privacy.html",
        title="Privacy | Aruba Shore Excursion",
        description="Privacy policy for Aruba Shore Excursion — static planning site practices.",
        keywords="privacy Aruba Shore Excursion",
        path="privacy.html",
        data_page="privacy",
        hero="partials/hero-privacy.html",
        content="privacy.html",
        preload=INTRO_IMG,
    ),
    dict(
        file="terms.html",
        title="Terms of Use | Aruba Shore Excursion",
        description="Terms of use for Aruba Shore Excursion planning content.",
        keywords="terms Aruba Shore Excursion",
        path="terms.html",
        data_page="terms",
        hero="partials/hero-terms.html",
        content="terms.html",
        preload=INTRO_IMG,
    ),
    dict(
        file="methodology.html",
        title="How We Assess Aruba Excursions | Methodology",
        description="How Aruba Shore Excursion assesses cruise excursion options — timing, honest claims and schedule integrity.",
        keywords="Aruba excursion methodology, how we choose Aruba tours",
        path="methodology.html",
        data_page="methodology",
        hero="partials/hero-methodology.html",
        content="methodology.html",
        preload=INTRO_IMG,
    ),
]


def merge_sitemap(extra: list[tuple[str, str, str]]) -> None:
    sitemap_path = ROOT / "sitemap.xml"
    existing: list[tuple[str, str, str]] = []
    if sitemap_path.exists():
        text = sitemap_path.read_text(encoding="utf-8")
        locs = re.findall(r"<loc>(.*?)</loc>", text)
        freqs = re.findall(r"<changefreq>(.*?)</changefreq>", text)
        pris = re.findall(r"<priority>(.*?)</priority>", text)
        for i, loc in enumerate(locs):
            path = loc.replace(DOMAIN + "/", "").replace(DOMAIN, "")
            if path == "/":
                path = ""
            freq = freqs[i] if i < len(freqs) else "monthly"
            pri = pris[i] if i < len(pris) else "0.5"
            existing.append((path, pri, freq))

    by_path = {p: (pri, freq) for p, pri, freq in existing}
    for path, pri, freq in extra:
        by_path[path] = (pri, freq)

    frag = ROOT / "data" / "generated" / "schedule-sitemap.json"
    if frag.exists():
        try:
            for path, pri, freq in json.loads(frag.read_text(encoding="utf-8")):
                by_path[path] = (pri, freq)
        except json.JSONDecodeError:
            pass

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for path, (pri, freq) in sorted(by_path.items(), key=lambda x: (x[0] != "", x[0])):
        url = f"{DOMAIN}/{path}" if path else f"{DOMAIN}/"
        lines += [
            "  <url>",
            f"    <loc>{url}</loc>",
            f"    <lastmod>{DATE}</lastmod>",
            f"    <changefreq>{freq}</changefreq>",
            f"    <priority>{pri}</priority>",
            "  </url>",
        ]
    lines.append("</urlset>")
    write("sitemap.xml", "\n".join(lines) + "\n")


def write_package_json() -> None:
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


def ensure_decision_css() -> None:
    css_path = ROOT / "css" / "site.css"
    css = css_path.read_text(encoding="utf-8")
    if ".decision-grid" not in css:
        css += """
.section-label {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  color: #0d9488;
  font-size: 0.7rem;
  font-weight: 600;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  margin-bottom: 0.75rem;
}
.decision-grid {
  display: grid;
  gap: 1rem;
}
@media (min-width: 640px) {
  .decision-grid { grid-template-columns: repeat(2, 1fr); }
}
@media (min-width: 1024px) {
  .decision-grid { grid-template-columns: repeat(3, 1fr); }
}
.decision-card {
  background: #fff;
  border: 1px solid #ffedd5;
  border-radius: 1.25rem;
  padding: 1.25rem 1.35rem;
}
.decision-card h3 {
  font-size: 1.05rem;
  margin-bottom: 0.4rem;
}
.decision-card p {
  font-size: 0.875rem;
  color: #4b5563;
  line-height: 1.55;
  margin-bottom: 0.75rem;
}
"""
        css_path.write_text(css, encoding="utf-8")
        print("  updated css/site.css with decision styles")


def main() -> None:
    print("World 2.0 extending Aruba Shore Excursion…")
    ensure_decision_css()
    write_nav()
    write_footer()
    write("partials/hero-home.html", hero_home())
    write(
        "partials/hero-beach-vs-island.html",
        _hero_inner(
            "Oranjestad decision",
            f"Beach Day vs<br/><span class=\"{ACCENT}\">Island Tour</span>",
            "Eagle Beach sand versus California Lighthouse, north coast and Arikok — choose how to spend an Aruba cruise call.",
            EAGLE_IMG,
            EAGLE_ALT,
            breadcrumb="Beach vs Island",
        ),
    )
    write(
        "partials/hero-relaxed-vs-active.html",
        _hero_inner(
            "Intensity choice",
            f"Relaxed vs<br/><span class=\"{ACCENT}\">Active</span>",
            "Eagle Beach calm versus UTV dust and Arikok trails — match Aruba to your energy on ship day.",
            UTV_IMG,
            UTV_ALT,
            breadcrumb="Relaxed vs Active",
        ),
    )

    write("content/home.html", content_home())
    write("content/aruba-cruise-port-guide.html", content_port())
    write("content/aruba-beach-vs-island-tour.html", content_beach_vs_island())
    write("content/aruba-relaxed-vs-active.html", content_relaxed_vs_active())
    write("content/about.html", content_about())
    write("content/contact.html", content_contact())
    write("content/privacy.html", content_privacy())
    write("content/terms.html", content_terms())
    write("content/methodology.html", content_methodology())

    soft_all_content()

    for p in NEW_PAGES:
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
            ),
        )

    # Refresh index shell meta slightly for World 2.0 voice (URL preserved)
    write(
        "index.html",
        page_shell(
            title=f"{SITE} | Oranjestad Pier — Beach, Antilla &amp; Dry-Side Days",
            description="Independent Aruba shore excursion planning from Oranjestad — Eagle Beach, Antilla wreck snorkelling, California Lighthouse, Arikok and UTV choices for cruise passengers.",
            keywords="Aruba shore excursions, Oranjestad cruise port, Eagle Beach, Antilla shipwreck, Arikok National Park",
            canonical_path="",
            data_page="home",
            hero="partials/hero-home.html",
            content="home.html",
            schema={
                "@context": "https://schema.org",
                "@type": "WebSite",
                "name": SITE,
                "url": f"{DOMAIN}/",
                "description": "Planning guide for Aruba cruise shore excursions from Oranjestad",
            },
        ),
    )

    extra = [
        ("aruba-beach-vs-island-tour.html", "0.8", "monthly"),
        ("aruba-relaxed-vs-active.html", "0.8", "monthly"),
        ("about.html", "0.5", "yearly"),
        ("contact.html", "0.5", "yearly"),
        ("privacy.html", "0.3", "yearly"),
        ("terms.html", "0.3", "yearly"),
        ("methodology.html", "0.5", "yearly"),
    ]
    merge_sitemap(extra)
    write_package_json()
    print("World 2.0 extend done.")


if __name__ == "__main__":
    main()
