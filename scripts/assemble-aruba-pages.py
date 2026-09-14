#!/usr/bin/env python3
"""Bake Aruba pages: inline nav/hero/content/footer so first HTML is server-visible.

Run after build-aruba-site.py, world2_extend_aruba.py, generate_schedule_pages.py.
Produces extensionless apex canonicals; does not ship content/ or partials/ (see .assetsignore).
"""
from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
DOMAIN = "https://arubashoreexcursion.com"
SITE = "Aruba Shore Excursion"
EMAIL = "hello@arubashoreexcursion.com"
TODAY = date.today().isoformat()
FONTS = (
    "https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;600;700"
    "&family=DM+Sans:wght@400;500;600;700&display=swap"
)

# filename -> meta. Output stays flat slug.html (CF drop-trailing-slash → /slug).
PAGES: dict[str, dict] = {
    "index.html": {
        "slug": "",
        "page": "home",
        "hero": "partials/hero-home.html",
        "trust": "partials/trust-strip.html",
        "content": "content/home.html",
        "og_image": "images/hero-aruba.png",
        "keep_schema": True,
    },
    "best-aruba-shore-excursions.html": {
        "slug": "best-aruba-shore-excursions",
        "page": "excursions",
        "hero": "partials/hero-excursions.html",
        "trust": "partials/trust-strip.html",
        "content": "content/best-aruba-shore-excursions.html",
        "og_image": "images/best-aruba-excursions.png",
        "keep_schema": True,
    },
    "aruba-cruise-port-guide.html": {
        "slug": "aruba-cruise-port-guide",
        "page": "port",
        "hero": "partials/hero-port-guide.html",
        "trust": "partials/trust-strip.html",
        "content": "content/aruba-cruise-port-guide.html",
        "og_image": "images/aruba-cruise-port.png",
        "keep_schema": True,
    },
    "one-day-in-aruba.html": {
        "slug": "one-day-in-aruba",
        "page": "port",
        "hero": "partials/hero-one-day.html",
        "trust": "partials/trust-strip.html",
        "content": "content/one-day-in-aruba.html",
        "og_image": "images/one-day-aruba.png",
    },
    "eagle-beach-excursions.html": {
        "slug": "eagle-beach-excursions",
        "page": "beaches",
        "hero": "partials/hero-eagle-beach.html",
        "trust": "partials/trust-strip.html",
        "content": "content/eagle-beach-excursions.html",
        "og_image": "images/eagle-beach-hero.png",
    },
    "aruba-beaches-guide.html": {
        "slug": "aruba-beaches-guide",
        "page": "beaches",
        "hero": "partials/hero-beaches.html",
        "trust": "partials/trust-strip.html",
        "content": "content/aruba-beaches-guide.html",
        "og_image": "images/aruba-beaches.png",
    },
    "aruba-snorkelling-tours.html": {
        "slug": "aruba-snorkelling-tours",
        "page": "snorkelling",
        "hero": "partials/hero-snorkelling.html",
        "trust": "partials/trust-strip.html",
        "content": "content/aruba-snorkelling-tours.html",
        "og_image": "images/aruba-snorkelling.png",
    },
    "antilla-shipwreck-excursions.html": {
        "slug": "antilla-shipwreck-excursions",
        "page": "snorkelling",
        "hero": "partials/hero-antilla.html",
        "trust": "partials/trust-strip.html",
        "content": "content/antilla-shipwreck-excursions.html",
        "og_image": "images/antilla-shipwreck.png",
    },
    "aruba-island-tours.html": {
        "slug": "aruba-island-tours",
        "page": "island",
        "hero": "partials/hero-island.html",
        "trust": "partials/trust-strip.html",
        "content": "content/aruba-island-tours.html",
        "og_image": "images/aruba-island-tours.png",
    },
    "aruba-utv-atv-adventures.html": {
        "slug": "aruba-utv-atv-adventures",
        "page": "utv",
        "hero": "partials/hero-utv.html",
        "trust": "partials/trust-strip.html",
        "content": "content/aruba-utv-atv-adventures.html",
        "og_image": "images/aruba-intro.png",
    },
    "arikok-national-park-tours.html": {
        "slug": "arikok-national-park-tours",
        "page": "island",
        "hero": "partials/hero-arikok.html",
        "trust": "partials/trust-strip.html",
        "content": "content/arikok-national-park-tours.html",
        "og_image": "images/aruba-intro.png",
    },
    "california-lighthouse-tours.html": {
        "slug": "california-lighthouse-tours",
        "page": "island",
        "hero": "partials/hero-lighthouse.html",
        "trust": "partials/trust-strip.html",
        "content": "content/california-lighthouse-tours.html",
        "og_image": "images/california-lighthouse.png",
    },
    "aruba-private-tours.html": {
        "slug": "aruba-private-tours",
        "page": "private",
        "hero": "partials/hero-private.html",
        "trust": "partials/trust-strip.html",
        "content": "content/aruba-private-tours.html",
        "og_image": "images/aruba-private-tours.png",
    },
    "aruba-family-excursions.html": {
        "slug": "aruba-family-excursions",
        "page": "beaches",
        "hero": "partials/hero-family.html",
        "trust": "partials/trust-strip.html",
        "content": "content/aruba-family-excursions.html",
        "og_image": "images/aruba-family.png",
    },
    "aruba-faq.html": {
        "slug": "aruba-faq",
        "page": "port",
        "hero": "partials/hero-faq.html",
        "trust": "partials/trust-strip.html",
        "content": "content/aruba-faq.html",
        "og_image": "images/aruba-faq.png",
        "schema": "faq",
    },
    "aruba-beach-vs-island-tour.html": {
        "slug": "aruba-beach-vs-island-tour",
        "page": "excursions",
        "hero": "partials/hero-beach-vs-island.html",
        "trust": "partials/trust-strip.html",
        "content": "content/aruba-beach-vs-island-tour.html",
        "og_image": "images/eagle-beach-hero.png",
    },
    "aruba-relaxed-vs-active.html": {
        "slug": "aruba-relaxed-vs-active",
        "page": "excursions",
        "hero": "partials/hero-relaxed-vs-active.html",
        "trust": "partials/trust-strip.html",
        "content": "content/aruba-relaxed-vs-active.html",
        "og_image": "images/eagle-beach-hero.png",
    },
    "about.html": {
        "slug": "about",
        "page": "about",
        "hero": "partials/hero-about.html",
        "content": "content/about.html",
        "og_image": "images/aruba-intro.png",
        "main_class": "pt-16",
    },
    "contact.html": {
        "slug": "contact",
        "page": "contact",
        "hero": "partials/hero-contact.html",
        "content": "content/contact.html",
        "og_image": "images/aruba-intro.png",
        "main_class": "pt-16",
    },
    "methodology.html": {
        "slug": "methodology",
        "page": "methodology",
        "hero": "partials/hero-methodology.html",
        "content": "content/methodology.html",
        "og_image": "images/aruba-intro.png",
        "main_class": "pt-16",
    },
    "privacy.html": {
        "slug": "privacy",
        "page": "privacy",
        "hero": "partials/hero-privacy.html",
        "content": "content/privacy.html",
        "og_image": "images/aruba-intro.png",
        "main_class": "pt-16",
    },
    "terms.html": {
        "slug": "terms",
        "page": "terms",
        "hero": "partials/hero-terms.html",
        "content": "content/terms.html",
        "og_image": "images/aruba-intro.png",
        "main_class": "pt-16",
    },
    "404.html": {
        "slug": "404",
        "page": "404",
        "content": "content/404.html",
        "og_image": "images/hero-aruba.png",
        "main_class": "pt-16",
        "noindex": True,
        "canonical_override": f"{DOMAIN}/404.html",
    },
}

PRIORITY = {
    "": 1.0,
    "best-aruba-shore-excursions": 0.9,
    "antilla-shipwreck-excursions": 0.9,
    "eagle-beach-excursions": 0.9,
    "aruba-cruise-port-guide": 0.8,
    "aruba-family-excursions": 0.8,
    "aruba-island-tours": 0.8,
    "aruba-snorkelling-tours": 0.8,
    "one-day-in-aruba": 0.8,
    "ship-schedule/": 0.8,
}


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def canon_url(slug: str) -> str:
    if not slug or slug == "404":
        return f"{DOMAIN}/" if slug != "404" else f"{DOMAIN}/404.html"
    return f"{DOMAIN}/{slug}"


def extensionlessify_html(html: str) -> str:
    def repl(m: re.Match) -> str:
        attr, quote, url = m.group(1), m.group(2), m.group(3)
        if url.startswith(("http://", "https://", "mailto:", "tel:", "#", "data:")):
            return m.group(0)
        if url.startswith(("images/", "/images/", "css/", "/css/", "js/", "/js/")):
            if not url.startswith("/") and not url.startswith("http"):
                return f"{attr}={quote}/{url}{quote}"
            return m.group(0)
        parts = urlsplit(url)
        path = parts.path
        if path.endswith(".html"):
            if path.endswith("index.html"):
                path = path[: -len("index.html")] or "/"
            else:
                path = path[: -len(".html")]
            if path in ("", "index") or path.endswith("/index"):
                path = "/"
        if path == "index" or path == "":
            path = "/"
        if not path.startswith("/"):
            path = "/" + path
        if len(path) > 1 and path.endswith("/"):
            path = path.rstrip("/") or "/"
        rebuilt = path
        if parts.query:
            rebuilt += "?" + parts.query
        if parts.fragment:
            rebuilt += "#" + parts.fragment
        return f"{attr}={quote}{rebuilt}{quote}"

    html = re.sub(r'(href|action)=([\'"])([^\'"]+)\2', repl, html)
    # root-absolute image/css/js/src/url()
    html = re.sub(
        r"""(\b(?:src|href)=)(['"])(?!/|https?:|mailto:|tel:|#|data:)(images/|css/|js/)([^'"]+)\2""",
        lambda m: f"{m.group(1)}{m.group(2)}/{m.group(3)}{m.group(4)}{m.group(2)}",
        html,
    )
    html = re.sub(
        r"""url\((['"]?)(?!/|https?:)(images/[^)'"]+)\1\)""",
        lambda m: f"url({m.group(1)}/{m.group(2)}{m.group(1)})",
        html,
    )
    return html


def extract_existing_schema(shell_path: Path) -> str | None:
    if not shell_path.exists():
        return None
    text = shell_path.read_text(encoding="utf-8")
    m = re.search(
        r'<script type="application/ld\+json">\s*(\{.*?\})\s*</script>',
        text,
        re.S,
    )
    return m.group(1).strip() if m else None


def faq_schema_from_content(content_html: str) -> dict:
    """Build FAQPage JSON-LD from visible <details>/<summary> pairs."""
    entities = []
    for m in re.finditer(
        r"<details[^>]*>\s*<summary[^>]*>(.*?)</summary>\s*<p[^>]*>(.*?)</p>",
        content_html,
        re.S | re.I,
    ):
        q = re.sub(r"<[^>]+>", "", m.group(1))
        a = re.sub(r"<[^>]+>", "", m.group(2))
        q = re.sub(r"\s+", " ", q).strip()
        a = re.sub(r"\s+", " ", a).strip()
        if q and a:
            entities.append(
                {
                    "@type": "Question",
                    "name": q,
                    "acceptedAnswer": {"@type": "Answer", "text": a},
                }
            )
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": entities}


def rewrite_schema_urls(schema_text: str, canon: str) -> str:
    try:
        data = json.loads(schema_text)
    except json.JSONDecodeError:
        return schema_text
    if isinstance(data, dict):
        if "url" in data and isinstance(data["url"], str) and "arubashoreexcursion.com" in data["url"]:
            if data.get("@type") in ("WebPage", "Article"):
                data["url"] = canon
            elif data.get("@type") == "WebSite":
                data["url"] = f"{DOMAIN}/"
        # strip .html from any url fields
        def fix(obj):
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if k in ("url", "item") and isinstance(v, str) and v.endswith(".html"):
                        if v.endswith("/index.html"):
                            obj[k] = v[: -len("index.html")] or f"{DOMAIN}/"
                        else:
                            obj[k] = v[: -len(".html")]
                    else:
                        fix(v)
            elif isinstance(obj, list):
                for i in obj:
                    fix(i)

        fix(data)
        return json.dumps(data, ensure_ascii=False, indent=2)
    return schema_text


def build_head(meta: dict, title: str, description: str, schema_json: str | None) -> str:
    if meta.get("canonical_override"):
        url = meta["canonical_override"]
    else:
        url = canon_url(meta["slug"])
    og = f"{DOMAIN}/{meta['og_image']}"
    robots = '  <meta name="robots" content="noindex, follow" />\n' if meta.get("noindex") else ""
    preload = ""
    if meta.get("hero") or meta["slug"] == "":
        preload = f'  <link rel="preload" as="image" href="/{meta["og_image"]}" fetchpriority="high" />\n'
    schema_block = ""
    if schema_json:
        schema_block = f'  <script type="application/ld+json">\n{schema_json}\n  </script>\n'
    return f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{description}" />
{robots}  <link rel="canonical" href="{url}" />
{preload}  <meta property="og:type" content="website" />
  <meta property="og:url" content="{url}" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{description}" />
  <meta property="og:image" content="{og}" />
  <meta property="og:site_name" content="{SITE}" />
  <meta name="twitter:card" content="summary_large_image" />
{schema_block}  <script src="https://cdn.tailwindcss.com"></script>
  <script src="/js/tailwind-config.js"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="{FONTS}" rel="stylesheet" />
  <link rel="stylesheet" href="/css/site.css" />
</head>
"""


def title_desc_from_shell(filename: str, meta: dict) -> tuple[str, str]:
    shell = ROOT / filename
    if shell.exists():
        text = shell.read_text(encoding="utf-8")
        t = re.search(r"<title[^>]*>(.*?)</title>", text, re.S | re.I)
        d = re.search(r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']*)["\']', text, re.I)
        title = re.sub(r"\s+", " ", t.group(1)).strip() if t else meta["slug"] or SITE
        desc = d.group(1) if d else ""
        return title, desc
    defaults = {
        "404": ("Page not found | Aruba Shore Excursion", "The requested Aruba Shore Excursion page was not found."),
    }
    return defaults.get(meta["slug"], (SITE, ""))


def ensure_utility_heroes() -> None:
    heroes = {
        "partials/hero-about.html": ("About", "Independent Oranjestad cruise planning"),
        "partials/hero-contact.html": ("Contact", "Planning concierge for Aruba port days"),
        "partials/hero-methodology.html": ("Methodology", "How we assess Aruba excursion options"),
        "partials/hero-privacy.html": ("Privacy", "How this planning site handles information"),
        "partials/hero-terms.html": ("Terms of use", "Planning content — not a booking contract"),
    }
    for path, (h1, lead) in heroes.items():
        html = f"""<section class="site-hero site-hero--compact">
  <div class="absolute inset-0 hero-bg-custom" style="background-image: linear-gradient(135deg, rgba(146, 64, 14, 0.75) 0%, rgba(37, 99, 235, 0.6) 55%, rgba(30, 41, 59, 0.55) 100%), url('/images/aruba-intro.png');" role="img" aria-label="Aruba dry coastal landscape"></div>
  <div class="site-hero__inner max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="max-w-3xl pt-8 pb-4">
      <h1 class="site-hero__title text-4xl sm:text-5xl font-display font-bold text-white leading-tight mb-3">{h1}</h1>
      <p class="site-hero__lead text-base sm:text-lg text-white/85 font-light leading-relaxed max-w-2xl">{lead}</p>
    </div>
  </div>
  <div class="absolute bottom-0 left-0 right-0"><svg viewBox="0 0 1440 48" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none" class="site-hero__wave" aria-hidden="true"><path d="M0 24 C360 48 1080 0 1440 24 L1440 48 L0 48 Z" fill="white"/></svg></div>
</section>
"""
        (ROOT / path).write_text(html, encoding="utf-8")


def ensure_404_content() -> None:
    path = ROOT / "content" / "404.html"
    path.write_text(
        """<section class="pt-10 pb-20 bg-white">
  <div class="max-w-2xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
    <p class="section-label mx-auto mb-3">404</p>
    <h1 class="text-3xl sm:text-4xl font-display font-bold text-gray-900 mb-4">Page not found</h1>
    <p class="text-gray-600 leading-relaxed mb-8">That URL is not part of the Aruba shore excursion planning guide. Try the home page, best excursions list, or ship schedule.</p>
    <div class="flex flex-col sm:flex-row gap-3 justify-center">
      <a href="/" class="btn-ocean inline-flex items-center justify-center text-white font-semibold px-6 py-3 rounded-full text-sm no-underline">Aruba home</a>
      <a href="/best-aruba-shore-excursions" class="btn-outline inline-flex items-center justify-center font-semibold px-6 py-3 rounded-full text-sm no-underline border border-ocean-600 text-ocean-700">Best excursions</a>
      <a href="/ship-schedule" class="btn-outline inline-flex items-center justify-center font-semibold px-6 py-3 rounded-full text-sm no-underline border border-ocean-600 text-ocean-700">Ship schedule</a>
    </div>
  </div>
</section>
""",
        encoding="utf-8",
    )


def assemble_page(filename: str, meta: dict) -> str:
    nav = extensionlessify_html(read("partials/nav.html"))
    footer = extensionlessify_html(read("partials/footer.html"))
    hero = extensionlessify_html(read(meta["hero"])) if meta.get("hero") else ""
    trust = extensionlessify_html(read(meta["trust"])) if meta.get("trust") else ""
    content = extensionlessify_html(read(meta["content"]))
    title, description = title_desc_from_shell(filename, meta)
    if meta["slug"] == "404":
        title, description = (
            "Page not found | Aruba Shore Excursion",
            "The requested Aruba Shore Excursion page was not found.",
        )

    schema_json = None
    if meta.get("schema") == "faq":
        schema_json = json.dumps(faq_schema_from_content(content), ensure_ascii=False, indent=2)
    elif meta.get("keep_schema"):
        raw = extract_existing_schema(ROOT / filename)
        if raw:
            schema_json = rewrite_schema_urls(raw, canon_url(meta["slug"]))

    main_class = meta.get("main_class", "")
    main_attr = f' class="{main_class}"' if main_class else ""
    body = f"""<body class="bg-white text-gray-800 antialiased" data-page="{meta["page"]}" data-static="1">
  <div id="site-nav" data-inlined="true">{nav}</div>
  <div id="page-hero" data-inlined="true">{hero}</div>
  <div id="page-trust-strip" data-inlined="true">{trust}</div>
  <main id="page-content"{main_attr}>{content}</main>
  <div id="site-footer" data-inlined="true">{footer}</div>
  <script src="/js/site.js" defer></script>
</body>
</html>
"""
    return build_head(meta, title, description, schema_json) + body


def bake_schedule_pages() -> None:
    """Inline nav/footer into ship-schedule pages; keep schedule body + search JS."""
    nav = extensionlessify_html(read("partials/nav.html"))
    footer = extensionlessify_html(read("partials/footer.html"))
    for path in (ROOT / "ship-schedule").rglob("index.html"):
        text = path.read_text(encoding="utf-8")
        # already baked?
        if 'data-static="1"' in text and "data-inlined" in text:
            continue
        m_body = re.search(r'<main id="page-content">(.*?)</main>', text, re.S)
        if not m_body:
            continue
        body_html = m_body.group(1)
        title_m = re.search(r"<title[^>]*>(.*?)</title>", text, re.S | re.I)
        desc_m = re.search(
            r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']*)["\']', text, re.I
        )
        canon_m = re.search(r'rel=["\']canonical["\'][^>]*href=["\']([^"\']+)', text, re.I)
        title = re.sub(r"\s+", " ", title_m.group(1)).strip() if title_m else "Ship schedule"
        description = desc_m.group(1) if desc_m else ""
        canon = canon_m.group(1) if canon_m else f"{DOMAIN}/ship-schedule/"
        # force extensionless apex; no trailing slash (drop-trailing-slash compatible)
        if ".html" in canon:
            canon = canon.replace(".html", "")
        if not canon.startswith(DOMAIN):
            canon = DOMAIN + (canon if canon.startswith("/") else "/" + canon)
        if canon.endswith("/") and canon != f"{DOMAIN}/":
            canon = canon.rstrip("/")
        depth = len(path.relative_to(ROOT / "ship-schedule").parts) - 1
        # depth unused — assets always root-absolute after bake
        _ = depth
        html = f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{description}" />
  <link rel="canonical" href="{canon}" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{canon}" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{description}" />
  <meta property="og:site_name" content="{SITE}" />
  <meta name="twitter:card" content="summary_large_image" />
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="/js/tailwind-config.js"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="{FONTS}" rel="stylesheet" />
  <link rel="stylesheet" href="/css/site.css" />
</head>
<body class="bg-white text-gray-800 antialiased" data-page="schedule" data-static="1">
  <div id="site-nav" data-inlined="true">{nav}</div>
  <main id="page-content">{body_html}</main>
  <div id="site-footer" data-inlined="true">{footer}</div>
  <script src="/js/site.js" defer></script>
  <script src="/js/schedule-search.js" defer></script>
</body>
</html>
"""
        # also extensionlessify in-body schedule links that may be relative
        html = extensionlessify_html(html)
        path.write_text(html, encoding="utf-8")
        print(f"  baked {path.relative_to(ROOT)}")


def write_sitemap() -> None:
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for _, meta in PAGES.items():
        if meta.get("noindex") or meta["slug"] == "404":
            continue
        slug = meta["slug"]
        pri = PRIORITY.get(slug, 0.6)
        loc = canon_url(slug)
        freq = "weekly" if pri >= 0.9 else "monthly"
        if slug in ("about", "contact", "methodology", "privacy", "terms"):
            freq = "yearly"
            pri = 0.5 if slug in ("about", "contact", "methodology") else 0.3
        lines += [
            "  <url>",
            f"    <loc>{loc}</loc>",
            f"    <lastmod>{TODAY}</lastmod>",
            f"    <changefreq>{freq}</changefreq>",
            f"    <priority>{pri:.1f}</priority>",
            "  </url>",
        ]

    # ship-schedule from generated fragment or filesystem
    frag = ROOT / "data" / "generated" / "schedule-sitemap.json"
    schedule_paths: list[str] = []
    if frag.exists():
        try:
            for path, _pri, _freq in json.loads(frag.read_text(encoding="utf-8")):
                schedule_paths.append(path)
        except json.JSONDecodeError:
            pass
    if not schedule_paths:
        schedule_paths = ["ship-schedule/"]
        for p in sorted((ROOT / "ship-schedule").rglob("index.html")):
            rel = p.relative_to(ROOT).as_posix().replace("index.html", "")
            schedule_paths.append(rel)

    seen = set()
    for path in schedule_paths:
        path = path.strip("/")
        if not path:
            continue
        # no trailing slash in sitemap (matches live CF drop-trailing-slash)
        if path in seen:
            continue
        seen.add(path)
        pri = 0.8 if path == "ship-schedule" else 0.6
        lines += [
            "  <url>",
            f"    <loc>{DOMAIN}/{path}</loc>",
            f"    <lastmod>{TODAY}</lastmod>",
            f"    <changefreq>{'weekly' if path == 'ship-schedule' else 'monthly'}</changefreq>",
            f"    <priority>{pri:.1f}</priority>",
            "  </url>",
        ]

    lines.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("  wrote sitemap.xml")


def write_robots() -> None:
    (ROOT / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n",
        encoding="utf-8",
    )
    print("  wrote robots.txt")


def patch_image_refs_in_sources() -> None:
    """Replace RED/AMBER image filenames in remaining source fragments before bake."""
    replacements = {
        "images/arikok-national-park.png": "images/aruba-intro.png",
        "images/aruba-utv-adventures.png": "images/aruba-intro.png",
    }
    for folder in ("partials", "content"):
        for path in (ROOT / folder).rglob("*.html"):
            text = path.read_text(encoding="utf-8")
            orig = text
            for old, new in replacements.items():
                text = text.replace(old, new)
            # soften Antilla alt assertions
            text = text.replace(
                "Aerial view of the Antilla shipwreck in clear turquoise water off Aruba with snorkelers and an excursion boat nearby",
                "Aerial view of a shallow Aruba shipwreck snorkel site with swimmers and a boat nearby",
            )
            text = text.replace(
                "Natural Pool in Arikok National Park Aruba",
                "Aruba dry coastal landscape near Arikok National Park",
            )
            text = text.replace(
                "Arid desert landscape representing Aruba UTV and dry-side adventures",
                "Aruba dry coastal landscape for UTV and dry-side adventure context",
            )
            if text != orig:
                path.write_text(text, encoding="utf-8")
                print(f"  patched images in {path.relative_to(ROOT)}")


def remove_bad_images() -> None:
    for name in ("arikok-national-park.png", "aruba-utv-adventures.png"):
        p = ROOT / "images" / name
        if p.exists():
            p.unlink()
            print(f"  removed images/{name}")


def main() -> None:
    print("Assembling Aruba server-visible pages…")
    ensure_utility_heroes()
    ensure_404_content()
    patch_image_refs_in_sources()
    remove_bad_images()

    for filename, meta in PAGES.items():
        out = ROOT / filename
        html = assemble_page(filename, meta)
        out.write_text(html, encoding="utf-8")
        print(f"  wrote {filename}")

    bake_schedule_pages()
    write_sitemap()
    write_robots()

    attr = ROOT / "images" / "ATTRIBUTION.md"
    if attr.exists():
        text = attr.read_text(encoding="utf-8")
        text = re.sub(r"\|.*arikok-national-park\.png.*\n", "", text)
        text = re.sub(r"\|.*aruba-utv-adventures\.png.*\n", "", text)
        note = (
            "\n**Phase 31B:** Removed `arikok-national-park.png` (wrong geography) and "
            "`aruba-utv-adventures.png` (misleading continental desert). "
            "Arikok/UTV pages now use `aruba-intro.png`.\n"
        )
        if "Phase 31B" not in text:
            text = text.rstrip() + "\n" + note
        attr.write_text(text, encoding="utf-8")

    print("Assemble complete.")


if __name__ == "__main__":
    main()
