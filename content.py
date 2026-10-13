"""Conteudo do site Expresso Sette Home Services (servicos, cidades, textos).

Regra: nada de afirmacao que nao e verdade (sem "licensed & insured", sem review inventado,
sem preco fechado). Editar aqui e rodar `python build.py`.
"""

SITE = {
    "brand": "Expresso Sette",
    "brand_full": "Expresso Sette Home Services",
    "domain": "expressosette.com",
    "url": "https://expressosette.com",
    "tagline": "Cleaning & handyman help in Boston and the North Shore",
    # endpoint do formulario (VPS, via HTTPS). Vazio = form mostra so mensagem de erro amigavel.
    "lead_endpoint": "https://api.expressosette.com/lead",
    "phone": "(617) 817-2824",
    "phone_e164": "+16178172824",
    "email": "",          # ex.: "hello@expressosette.com"
    "speaks": "We speak English and Portuguese",
}

# ------------------------------------------------------------------ servicos
SERVICES = [
    {
        "slug": "house-cleaning", "group": "cleaning",
        "name": "House Cleaning", "short": "Weekly, bi-weekly or one-time cleaning for homes and apartments.",
        "h1": "House cleaning in Boston & the North Shore",
        "intro": "Regular cleaning that keeps your home ready without eating your weekend. "
                 "Pick weekly, every other week, monthly or a single visit.",
        "includes": ["Kitchen: counters, sink, stovetop, outside of appliances", "Bathrooms: tub/shower, toilet, sink, mirrors",
                     "Dusting of reachable surfaces", "Vacuum and mop all floors", "Trash out and beds made (linens on request)"],
        "faq": [("Do I need to provide supplies?", "No. We bring standard supplies. If you prefer a specific product, just leave it out for us."),
                ("Do I have to be home?", "No. Many clients leave a key or door code. Tell us what works for you in the request."),
                ("How is the price set?", "By home size, condition and frequency. Send the request and you get a quote before anything is booked.")],
    },
    {
        "slug": "deep-cleaning", "group": "cleaning",
        "name": "Deep Cleaning", "short": "Top-to-bottom cleaning for homes that need a reset.",
        "h1": "Deep cleaning in Boston & the North Shore",
        "intro": "A detailed clean for spring cleaning, before guests arrive, or when it has been a while. "
                 "Takes longer than a regular visit and reaches the spots that get skipped.",
        "includes": ["Everything in a regular cleaning", "Baseboards, door frames and light switches", "Inside microwave; inside oven and fridge on request",
                     "Cabinet fronts and kitchen backsplash", "Bathroom grout and soap scum build-up"],
        "faq": [("How long does a deep clean take?", "Usually 1.5 to 3 times longer than a regular visit, depending on the home."),
                ("Can I switch to regular cleaning after?", "Yes. Most people start with a deep clean and then keep a regular schedule.")],
    },
    {
        "slug": "move-in-move-out-cleaning", "group": "cleaning",
        "name": "Move-In / Move-Out Cleaning", "short": "Empty-unit cleaning to get your deposit back or start fresh.",
        "h1": "Move-in & move-out cleaning in Boston & the North Shore",
        "intro": "Moving in Greater Boston is stressful enough, especially around September 1st. "
                 "We clean the empty unit so you can hand back the keys or move in to a fresh place.",
        "includes": ["Inside cabinets, drawers and closets", "Inside fridge, oven and microwave", "Bathrooms and kitchen fully detailed",
                     "Windowsills, baseboards and floors", "Good for tenants, landlords and realtors"],
        "faq": [("Can you come the same day I move out?", "Often, yes. Put your move date in the request; September fills up fast, so earlier is better."),
                ("Do you work with landlords and property managers?", "Yes, including recurring turnovers for multiple units.")],
    },
    {
        "slug": "office-cleaning", "group": "cleaning",
        "name": "Office & Commercial Cleaning", "short": "After-hours cleaning for offices, shops, studios and small businesses.",
        "h1": "Office & commercial cleaning in Boston & the North Shore",
        "intro": "Reliable cleaning for small offices, retail stores, salons, gyms and clinics' common areas, "
                 "scheduled around your business hours.",
        "includes": ["Desks, common areas and kitchenettes", "Restrooms cleaned and restocked", "Trash and recycling",
                     "Floors vacuumed and mopped", "Daily, weekly or custom schedule; post-construction cleanup on request"],
        "faq": [("Can you clean after hours?", "Yes. Evenings and weekends are common for commercial clients."),
                ("Do you do one-time post-construction cleaning?", "Yes. Describe the space and the stage of the project in the request.")],
    },
    {
        "slug": "airbnb-turnover-cleaning", "group": "cleaning",
        "name": "Airbnb & Rental Turnover", "short": "Between-guest cleaning for short-term rentals.",
        "h1": "Airbnb & short-term rental cleaning in Boston & the North Shore",
        "intro": "Turnovers done between check-out and check-in, with photos when we finish so you know the unit is ready. "
                 "Built for hosts and property managers.",
        "includes": ["Full clean between guests", "Linen change and bed making", "Restock of basics you provide",
                     "Photos after each turnover", "Report of damage or missing items"],
        "faq": [("Can you work with my booking calendar?", "Yes. We schedule from your check-out times; tell us the platform you use."),
                ("Do you handle laundry?", "Yes, on site if the unit has a washer/dryer, or by arrangement.")],
    },
    {
        "slug": "handyman", "group": "handyman",
        "name": "Handyman Services", "short": "Small repairs and odd jobs around the house.",
        "h1": "Handyman services in Boston & the North Shore",
        "intro": "The list of small things that never gets done: a door that sticks, a hole in the wall, "
                 "a loose railing, shelves to hang. Send the list and get it done in one visit.",
        "includes": ["Drywall patches and small wall repairs", "Doors, locks, hinges and cabinet hardware",
                     "Shelves, curtain rods, mirrors and pictures", "Caulking for tubs, sinks and windows", "Minor fixes before a sale or move-out"],
        "faq": [("Do you do big renovations?", "No. We focus on small jobs and repairs. For larger remodeling, we will tell you up front."),
                ("Do you do electrical or plumbing?", "Only simple tasks that do not require a licensed electrician or plumber. Anything that needs a license, we will say so.")],
    },
    {
        "slug": "furniture-assembly", "group": "handyman",
        "name": "Furniture Assembly", "short": "IKEA, Wayfair, Amazon and other flat-pack furniture assembled.",
        "h1": "Furniture assembly in Boston & the North Shore",
        "intro": "Beds, dressers, desks, shelves, cribs and outdoor furniture assembled and leveled, "
                 "with the boxes broken down when we are done.",
        "includes": ["Beds, dressers and wardrobes (PAX included)", "Desks, office chairs and bookcases",
                     "Wall-anchoring of tall furniture", "Cribs and kids' furniture", "Patio and outdoor sets"],
        "faq": [("Do I need to have the furniture delivered first?", "Yes, have the boxes on site. Send the item names or links in the request."),
                ("Do you anchor dressers to the wall?", "Yes, and we recommend it for anything tall, especially with kids at home.")],
    },
    {
        "slug": "tv-mounting", "group": "handyman",
        "name": "TV Mounting", "short": "TVs, soundbars and shelves mounted securely.",
        "h1": "TV mounting in Boston & the North Shore",
        "intro": "TVs mounted on drywall, plaster or brick, at the right height, level, with cables tidied.",
        "includes": ["Fixed, tilting or full-motion mounts", "Soundbar and floating shelf mounting",
                     "Cable cover or cable management", "Plaster and brick walls (common in older Boston homes)", "Removal of old mounts and wall patch"],
        "faq": [("Do you provide the mount?", "You can buy it or we can bring one; tell us the TV size and model in the request."),
                ("Can you hide the wires inside the wall?", "In many walls, yes. We check on site whether it can be done safely.")],
    },
]

# ------------------------------------------------------------------ cidades
# blurb proprio por cidade (conteudo real, nao so troca de nome)
CITIES = [
    {"slug": "boston", "name": "Boston", "area": "Boston",
     "hoods": ["Back Bay", "South End", "Dorchester", "Jamaica Plain", "Charlestown", "East Boston", "Brighton", "South Boston"],
     "blurb": "From South End brownstones to triple-deckers in Dorchester and condos in the Seaport, Boston homes come in every shape. "
              "Older plaster walls, tight stairways and street parking are part of the job here, and we plan for them."},
    {"slug": "cambridge", "name": "Cambridge", "area": "Boston",
     "hoods": ["Central Square", "Harvard Square", "Inman Square", "Porter Square", "Kendall Square"],
     "blurb": "Cambridge has a mix of grad-student apartments, family homes and busy offices around Kendall. "
              "Lease turnover around September 1st is our busiest time here; book move-out cleaning early."},
    {"slug": "somerville", "name": "Somerville", "area": "Boston",
     "hoods": ["Davis Square", "Union Square", "Assembly Row", "Ball Square", "Winter Hill"],
     "blurb": "Somerville's two-families and triple-deckers mean lots of apartments, lots of moves and lots of IKEA. "
              "Move-out cleaning and furniture assembly are the most common requests in the city."},
    {"slug": "medford", "name": "Medford", "area": "Boston",
     "hoods": ["West Medford", "Medford Square", "Wellington", "South Medford", "Lawrence Estates"],
     "blurb": "Medford sits between Boston and the North Shore, with single-family homes, Tufts rentals and new condos by Wellington. "
              "We are based nearby, so Medford is one of the easiest places for us to schedule."},
    {"slug": "malden", "name": "Malden", "area": "Boston",
     "hoods": ["Maplewood", "Edgeworth", "Linden", "Malden Center", "Oak Grove"],
     "blurb": "Malden's mix of older multi-family houses and new apartments near the Orange Line keeps cleaning and small-repair requests steady all year."},
    {"slug": "everett", "name": "Everett", "area": "Boston",
     "hoods": ["Everett Square", "Glendale", "Woodlawn", "Charlestown line"],
     "blurb": "Everett has grown fast, with new apartment buildings and many short-term rentals near the casino and Boston. "
              "Rental turnovers and move-out cleaning are common here."},
    {"slug": "revere", "name": "Revere", "area": "North Shore",
     "hoods": ["Revere Beach", "Beachmont", "West Revere", "Point of Pines"],
     "blurb": "Beachfront condos, older family homes and a lot of rentals: Revere needs deep cleans in spring, "
              "turnovers in summer and move-out cleanings all year."},
    {"slug": "lynn", "name": "Lynn", "area": "North Shore",
     "hoods": ["Downtown Lynn", "Wyoma", "Diamond District", "West Lynn", "Lynn Woods"],
     "blurb": "Lynn has some of the North Shore's oldest housing stock, from the Diamond District's Victorians to multi-families downtown. "
              "Small repairs and deep cleaning are the most common jobs here."},
    {"slug": "saugus", "name": "Saugus", "area": "North Shore",
     "hoods": ["Cliftondale", "Saugus Center", "East Saugus", "Lynnhurst"],
     "blurb": "Mostly single-family homes and small businesses along Route 1. Regular house cleaning and office cleaning for Route 1 businesses."},
    {"slug": "salem", "name": "Salem", "area": "North Shore",
     "hoods": ["Downtown Salem", "Derby Street", "The Point", "North Salem", "South Salem"],
     "blurb": "Historic homes, lots of rentals and a very busy October. Salem short-term rentals need fast turnovers in the fall, "
              "and older homes need careful handyman work."},
    {"slug": "peabody", "name": "Peabody", "area": "North Shore",
     "hoods": ["West Peabody", "South Peabody", "Peabody Square", "Centennial Park"],
     "blurb": "Family homes in West Peabody and many offices and stores near Route 128. Recurring house cleaning and small-office cleaning are the main requests."},
    {"slug": "beverly", "name": "Beverly", "area": "North Shore",
     "hoods": ["Beverly Farms", "Prides Crossing", "Cove", "Ryal Side", "Downtown Beverly"],
     "blurb": "From large homes in Beverly Farms to apartments downtown, Beverly clients ask for deep cleaning, regular visits and help with the honey-do list."},
    {"slug": "danvers", "name": "Danvers", "area": "North Shore",
     "hoods": ["Danvers Square", "Danversport", "Putnamville", "Hathorne"],
     "blurb": "Suburban homes and a lot of commercial space by the Liberty Tree Mall. Furniture assembly and TV mounting are frequent requests here."},
    {"slug": "swampscott", "name": "Swampscott", "area": "North Shore",
     "hoods": ["Phillips Beach", "Olmsted District", "Swampscott Center"],
     "blurb": "Ocean-side homes that see sand, salt and seasonal guests. Deep cleaning and caulking/sealing jobs are common by the water."},
    {"slug": "marblehead", "name": "Marblehead", "area": "North Shore",
     "hoods": ["Old Town", "Marblehead Neck", "Clifton"],
     "blurb": "Old Town's antique houses need a careful hand: narrow stairs, original floors and plaster walls. We take it slow and protect what matters."},
    {"slug": "melrose", "name": "Melrose", "area": "North Shore",
     "hoods": ["Melrose Highlands", "East Side", "Wyoming Hill", "Downtown Melrose"],
     "blurb": "Victorian homes and young families. Regular cleaning, furniture assembly and child-proofing tasks like anchoring dressers are the usual requests."},
    {"slug": "wakefield", "name": "Wakefield", "area": "North Shore",
     "hoods": ["Lake Quannapowitt", "Greenwood", "Montrose", "Downtown Wakefield"],
     "blurb": "Single-family homes around the lake and offices off Route 128. House cleaning and office cleaning both in steady demand."},
    {"slug": "woburn", "name": "Woburn", "area": "North Shore",
     "hoods": ["Woburn Center", "North Woburn", "Montvale", "West Side"],
     "blurb": "A mix of homes, new apartment complexes and business parks along 93 and 95. Commercial cleaning and move-out cleaning are frequent here."},
    {"slug": "gloucester", "name": "Gloucester", "area": "North Shore",
     "hoods": ["Downtown Gloucester", "East Gloucester", "Lanesville", "Annisquam", "Magnolia"],
     "blurb": "Summer homes, rentals and year-round houses on Cape Ann. Seasonal opening/closing cleans and rental turnovers in the summer months."},
]
