"""Gera o site estatico em docs/ (GitHub Pages). Uso: python build.py"""
import html
import json
import os
import shutil
from datetime import date

from content import CITIES, SERVICES, SITE

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "docs")
E = html.escape


def page(path, title, desc, body, schema=None):
    canon = SITE["url"] + path
    ld = f'<script type="application/ld+json">{json.dumps(schema)}</script>' if schema else ""
    nav_services = "".join(f'<a href="/services/{s["slug"]}/">{E(s["name"])}</a>' for s in SERVICES)
    html_ = f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{canon}">
<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{canon}"><meta property="og:type" content="website">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/style.css">
{ld}
</head><body>
<header class="top"><div class="wrap bar">
  <a class="logo" href="/"><span class="mark">7</span><span>{E(SITE["brand"])}<small>Home Services</small></span></a>
  <nav><details><summary>Services</summary><div class="menu">{nav_services}</div></details>
  <a href="/areas/">Areas</a><a class="tel" href="tel:{SITE["phone_e164"]}">{E(SITE["phone"])}</a><a class="btn sm" href="/request/">Get a quote</a></nav>
</div></header>
<main>{body}</main>
<footer><div class="wrap foot">
  <div><b>{E(SITE["brand_full"])}</b><br>{E(SITE["tagline"])}.<br>{E(SITE["speaks"])}.<br>
  Call or text <a href="tel:{SITE["phone_e164"]}">{E(SITE["phone"])}</a></div>
  <div><b>Services</b><br>{"<br>".join(f'<a href="/services/{s["slug"]}/">{E(s["name"])}</a>' for s in SERVICES)}</div>
  <div><b>Areas</b><br>{"<br>".join(f'<a href="/areas/{c["slug"]}/">{E(c["name"])}</a>' for c in CITIES[:10])}<br><a href="/areas/">All areas</a></div>
</div><p class="wrap fine">&copy; {date.today().year} {E(SITE["brand_full"])} &middot; <a href="/privacy/">Privacy</a></p></footer>
<script src="/form.js" defer></script>
</body></html>"""
    d = os.path.join(OUT, path.strip("/"))
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_)
    return path


def form(service_slug="", city=""):
    opts = "".join(
        f'<option value="{s["slug"]}"{" selected" if s["slug"] == service_slug else ""}>{E(s["name"])}</option>'
        for s in SERVICES)
    return f"""<form class="lead" data-endpoint="{E(SITE["lead_endpoint"])}" novalidate>
  <h2>Get a free quote</h2>
  <p class="muted">Tell us what you need. We reply with a quote, usually the same day.
  Prefer to talk? Call or text <a href="tel:{SITE["phone_e164"]}">{E(SITE["phone"])}</a>.</p>
  <label>Service<select name="service" required><option value="">Choose a service</option>{opts}</select></label>
  <div class="row">
    <label>Town or ZIP<input name="town" required value="{E(city)}" autocomplete="postal-code"></label>
    <label>When?<select name="when"><option>As soon as possible</option><option>This week</option><option>Next week</option><option>Flexible</option><option>Recurring / ongoing</option></select></label>
  </div>
  <label>Details<textarea name="details" rows="3" placeholder="Ex.: 2-bed apartment, every other week. Or: mount 65&quot; TV on plaster wall + fix a door."></textarea></label>
  <div class="row">
    <label>Name<input name="name" required autocomplete="name"></label>
    <label>Phone<input name="phone" type="tel" autocomplete="tel"></label>
  </div>
  <label>Email<input name="email" type="email" autocomplete="email"></label>
  <label class="hp" aria-hidden="true">Company<input name="company" tabindex="-1" autocomplete="off"></label>
  <label class="check"><input type="checkbox" name="consent" required>
    <span>I agree that {E(SITE["brand_full"])} and up to 3 trusted partner pros may contact me by phone, text or email about this request.
    Message and data rates may apply. Consent is not a condition of purchase. <a href="/privacy/">Privacy</a></span></label>
  <button class="btn" type="submit">Send request</button>
  <p class="msg" role="status"></p>
</form>"""


def faq_html(items):
    return "".join(f"<details class='faq'><summary>{E(q)}</summary><p>{E(a)}</p></details>" for q, a in items)


def business_schema(extra=None):
    d = {"@context": "https://schema.org", "@type": "HomeAndConstructionBusiness",
         "name": SITE["brand_full"], "url": SITE["url"],
         "areaServed": [{"@type": "City", "name": f'{c["name"]}, MA'} for c in CITIES],
         "knowsLanguage": ["en", "pt"]}
    if SITE["phone"]:
        d["telephone"] = SITE["phone_e164"]
    if extra:
        d.update(extra)
    return d


def build():
    os.makedirs(OUT, exist_ok=True)
    for n in os.listdir(OUT):  # limpa o conteudo (a pasta pode estar aberta num servidor local)
        p = os.path.join(OUT, n)
        shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
    for f in ("style.css", "form.js", "favicon.svg"):
        shutil.copy(os.path.join(ROOT, "assets", f), os.path.join(OUT, f))
    with open(os.path.join(OUT, "CNAME"), "w") as f:
        f.write(SITE["domain"])
    urls = []

    cleaning = [s for s in SERVICES if s["group"] == "cleaning"]
    handy = [s for s in SERVICES if s["group"] == "handyman"]

    def cards(lst):
        return "".join(f'<a class="card" href="/services/{s["slug"]}/"><h3>{E(s["name"])}</h3><p>{E(s["short"])}</p><span>See details &rarr;</span></a>' for s in lst)

    area_links = "".join(f'<a href="/areas/{c["slug"]}/">{E(c["name"])}</a>' for c in CITIES)
    # ---- home
    body = f"""
<section class="hero"><div class="wrap hero-grid">
  <div><p class="eyebrow">Boston &middot; North Shore</p>
  <h1>Cleaning and handyman help, without the runaround</h1>
  <p class="lead-in">House cleaning, move-out cleaning, office cleaning, Airbnb turnovers, small repairs,
  furniture assembly and TV mounting. One request, a clear quote, and a pro at your door.</p>
  <ul class="ticks"><li>Free quote, no obligation</li><li>Weekday, evening and weekend slots</li><li>{E(SITE["speaks"])}</li></ul></div>
  {form()}
</div></section>
<section class="wrap"><h2>Cleaning</h2><div class="grid">{cards(cleaning)}</div>
<h2>Handyman</h2><div class="grid">{cards(handy)}</div></section>
<section class="band"><div class="wrap steps">
  <div><b>1. Send the request</b><p>Takes a minute. Add photos later by text if it helps.</p></div>
  <div><b>2. Get a quote</b><p>We confirm the scope and price before anything is booked.</p></div>
  <div><b>3. Job done</b><p>A pro shows up at the agreed time and does the job at the agreed price.</p></div>
</div></section>
<section class="wrap"><h2>Areas we serve</h2><div class="chips">{area_links}</div></section>"""
    urls.append(page("/", f'{SITE["brand_full"]} | Cleaning & Handyman in Boston and the North Shore',
                     "House cleaning, move-out and office cleaning, Airbnb turnovers, handyman repairs, furniture assembly "
                     "and TV mounting in Boston, Cambridge, Somerville, Lynn, Salem, Peabody and the North Shore.",
                     body, business_schema()))

    # ---- servicos
    for s in SERVICES:
        others = [o for o in SERVICES if o["group"] == s["group"] and o["slug"] != s["slug"]]
        body = f"""
<section class="hero sm"><div class="wrap hero-grid">
  <div><p class="eyebrow"><a href="/">Home</a> / {E(s["name"])}</p><h1>{E(s["h1"])}</h1>
  <p class="lead-in">{E(s["intro"])}</p>
  <h3>What's included</h3><ul class="ticks">{"".join(f"<li>{E(i)}</li>" for i in s["includes"])}</ul></div>
  {form(s["slug"])}
</div></section>
<section class="wrap"><h2>Questions</h2>{faq_html(s["faq"])}
<h2>{E(s["name"])} near you</h2><div class="chips">{"".join(f'<a href="/areas/{c["slug"]}/">{E(c["name"])}</a>' for c in CITIES)}</div>
<h2>Related services</h2><div class="grid">{cards(others)}</div></section>"""
        schema = {"@context": "https://schema.org", "@type": "Service", "serviceType": s["name"],
                  "provider": {"@type": "HomeAndConstructionBusiness", "name": SITE["brand_full"], "url": SITE["url"]},
                  "areaServed": [f'{c["name"]}, MA' for c in CITIES],
                  "description": s["short"]}
        faq_ld = {"@context": "https://schema.org", "@type": "FAQPage",
                  "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in s["faq"]]}
        urls.append(page(f'/services/{s["slug"]}/', f'{s["name"]} in Boston & North Shore | {SITE["brand"]}',
                         f'{s["short"]} Serving Boston, Cambridge, Somerville, Lynn, Salem, Peabody and the North Shore. Free quote.',
                         body, [schema, faq_ld]))

    # ---- cidades
    for c in CITIES:
        near = [o for o in CITIES if o["area"] == c["area"] and o["slug"] != c["slug"]][:6]
        body = f"""
<section class="hero sm"><div class="wrap hero-grid">
  <div><p class="eyebrow"><a href="/areas/">Areas</a> / {E(c["name"])}</p>
  <h1>Cleaning &amp; handyman services in {E(c["name"])}, MA</h1>
  <p class="lead-in">{E(c["blurb"])}</p>
  <p>Neighborhoods: {E(", ".join(c["hoods"]))}.</p></div>
  {form(city=c["name"])}
</div></section>
<section class="wrap"><h2>Cleaning in {E(c["name"])}</h2><div class="grid">{cards(cleaning)}</div>
<h2>Handyman in {E(c["name"])}</h2><div class="grid">{cards(handy)}</div>
<h2>Nearby</h2><div class="chips">{"".join(f'<a href="/areas/{o["slug"]}/">{E(o["name"])}</a>' for o in near)}</div></section>"""
        urls.append(page(f'/areas/{c["slug"]}/', f'Cleaning & Handyman in {c["name"]}, MA | {SITE["brand"]}',
                         f'House, move-out and office cleaning, Airbnb turnovers, handyman, furniture assembly and TV mounting in '
                         f'{c["name"]}, MA ({", ".join(c["hoods"][:3])}). Free quote.',
                         body, business_schema({"areaServed": {"@type": "City", "name": f'{c["name"]}, MA'}})))

    groups = {}
    for c in CITIES:
        groups.setdefault(c["area"], []).append(c)
    body = '<section class="wrap"><h1>Areas we serve</h1>' + "".join(
        f'<h2>{E(a)}</h2><div class="chips">{"".join(f"<a href=/areas/{c["slug"]}/>{E(c["name"])}</a>" for c in lst)}</div>'
        for a, lst in groups.items()) + "<p>Not listed? Send a request anyway; we cover most towns between Boston and Cape Ann.</p></section>"
    urls.append(page("/areas/", f'Areas We Serve | {SITE["brand"]}', "Towns served in Boston and the North Shore of Massachusetts.", body))

    urls.append(page("/request/", f'Get a Free Quote | {SITE["brand"]}', "Request a free quote for cleaning or handyman work.",
                     f'<section class="wrap narrow">{form()}</section>'))
    page("/thanks/", f'Request received | {SITE["brand"]}', "Thanks for your request.",
         '<section class="wrap narrow"><h1>Got it, thank you!</h1><p class="lead-in">Your request is in. '
         'We will reach out shortly with questions or a quote, usually the same day.</p><p><a class="btn" href="/">Back to home</a></p></section>')
    urls.append(page("/privacy/", f'Privacy | {SITE["brand"]}', "Privacy policy.", f"""<section class="wrap narrow"><h1>Privacy</h1>
<p>When you send a request, we collect the details you type: service, town or ZIP, description, name, phone and email.</p>
<p>We use them only to answer your request and schedule the work. If you checked the consent box, your request may be shared with
up to 3 trusted partner service providers so they can quote the job. We do not sell your information for any other purpose.</p>
<p>You can ask us to delete your information or stop contacting you at any time by replying STOP to a text or by replying to any email from us.</p>
<p>Last updated {date.today().isoformat()}.</p></section>"""))
    with open(os.path.join(OUT, "404.html"), "w", encoding="utf-8") as f:
        f.write(open(os.path.join(OUT, "thanks", "index.html"), encoding="utf-8").read()
                .replace("Got it, thank you!", "Page not found").replace("Your request is in.", "That page does not exist."))

    today = date.today().isoformat()
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for u in urls:
            f.write(f"  <url><loc>{SITE['url']}{u}</loc><lastmod>{today}</lastmod></url>\n")
        f.write("</urlset>\n")
    with open(os.path.join(OUT, "robots.txt"), "w") as f:
        f.write(f"User-agent: *\nAllow: /\nDisallow: /thanks/\nSitemap: {SITE['url']}/sitemap.xml\n")
    print(f"{len(urls)} paginas em {OUT}")


if __name__ == "__main__":
    build()
