"""English content for SistemSehat. Pages here are written to the site root.

Writing rules for this file are in WRITING-GUIDE.md. In short: plain words, one idea per sentence,
an example for every rule, and the same rule numbers and glossary ids as content_id.py.
"""
from engine import (begin, clause, reviewed, keypoints, related, pager, guide_card, tool_card, table,
                    checklist_groups, glossary_list, library_group, S)

REVIEWED = "11 October 2026"

# file, number, short label, the question it answers, card summary, icon
GUIDES = [
    ("specification.html", "1", "Specification", "What should we ask for?",
     "A specification decides what arrives at the facility. Seven rules for writing one that several manufacturers can meet and clinicians can use.", "doc"),
    ("pricing.html", "2", "Pricing", "What should it cost?",
     "A price means little until you know what it includes. Six rules for building a reference price you can explain and defend.", "tag"),
    ("process.html", "3", "Process", "How do we buy it without a failed tender?",
     "How you divide the lots, score the bids and set the deadlines decides the result before any bid is opened. Seven rules for running the tender.", "route"),
    ("regulation.html", "A", "Regulation", "What must a device comply with?",
     "Marketing authorisation, risk class, quality certificates, standards, local content and calibration. Eight rules for checking the documents.", "shield"),
    ("technology.html", "B", "Technology", "How do we judge the technology?",
     "How it works, what evidence supports it, its history in use and whether it suits your facility. Seven rules for judging a device you did not design.", "monitor"),
]

MAIN_NAV = [
    ("guides.html", "Guides"),
    ("dossiers.html", "Dossiers"),
    ("checklist.html", "Checklist"),
    ("glossary.html", "Glossary"),
    ("library.html", "Sources"),
    ("about.html", "About"),
]

PAGE_LABELS = {
    "guides.html": "Guides",
    "dossiers.html": "Dossiers",
    "checklist.html": "Checklist",
    "glossary.html": "Glossary",
    "library.html": "Sources",
    "about.html": "About",
    "search.html": "Search",
}

UI = {
    "skip": "Skip to main content",
    "nav_label": "Main",
    "crumbs_label": "Breadcrumb",
    "home": "Home",
    "guides_label": "Guides",
    "tabs_label": "Guides in this series",
    "f_guides_label": "All guides",
    "og_alt": "SistemSehat: Ask for the right device. Pay a fair price. Run a tender that works.",
    "search_label": "Search this site",
    "search_placeholder": "Search rules and terms",
    "search": "Search",
    "menu": "Menu",
    "lang_label": "Language",
    "footer_about": "An independent, non-commercial initiative. Not linked to or endorsed by any government body, lender or manufacturer.",
    "f_tools": "Tools",
    "f_about": "About",
    "f_about_label": "About this site",
    "f_about_site": "About SistemSehat",
    "f_independent": "How it stays independent",
    "f_dossiers": "Device dossiers",
    "legal": "The guidance here is general. It does not replace the procurement rules that apply to your organisation.",
    "test": "Ask yourself",
    "example": "Example",
    "check_count": "{n} of {total} ticked",
    "check_note": "Ticks are kept in this browser only.",
    "check_clear": "Clear all ticks",
    "last_reviewed": "Last reviewed {date}",
    "n_rules": "{n} rules",
    "reading_time": "About {n} min to read",
    "checklist_for_guide": "Checklist for this guide",
    "key_points": "The {n} rules in this guide",
    "related": "Related",
    "rel_checklist": "The {n} questions from this guide, to tick or print",
    "rel_glossary": "Terms and abbreviations used here, explained",
    "rel_library": "The public documents behind the guides",
    "rel_dossiers": "All three questions answered for one device",
    "prev_guide": "Previous guide",
    "next_guide": "Next guide",
    "finished": "Finished the guides?",
    "open_checklist": "Open the checklist",
    "pager_label": "More guides",
    "guide_more": "{label} guide",
    "library_headers": ["Source", "Published by", "Use it for"],
    "k_guide": "Guide",
    "k_rule": "Rule in {label}",
    "k_page": "Page",
}

begin("en", UI, GUIDES, MAIN_NAV, PAGE_LABELS, REVIEWED)

IN_PREP = '<span class="status">In preparation</span>'

STATUS_TABLE = table(
    ["Area", "Dossiers", "Status"],
    [
        ["Newborn care", "One device", IN_PREP],
        ["Primary care laboratory", "Two analyzers", IN_PREP],
    ],
)


# ------------------------------------------------------------------ Home

home = f"""    <section class="hero">
      <div class="wrap hero-grid">
        <div>
          <h1>
            <span>Ask for the right device.</span>
            <span>Pay a fair price.</span>
            <span>Run a tender that works.</span>
          </h1>
          <p class="hero-lead">SistemSehat is free, independent guidance on buying medical equipment for Indonesia's public health facilities. It covers what to ask for, what it should cost, and how to run the tender. The name means &ldquo;healthy system&rdquo; in Indonesian.</p>
          <form class="search search-large" action="search.html" method="get" role="search" aria-label="Search the guides">
            <label for="hero-search">Search the guides</label>
            <div class="search-row">
              <input id="hero-search" type="search" name="q" placeholder="For example: calibration">
              <button type="submit">Search</button>
            </div>
          </form>
          <p class="hero-actions">
            <a class="button" href="guides.html">Browse the guides</a>
            <a class="button button-quiet" href="checklist.html">Open the checklist</a>
          </p>
        </div>

        <aside class="plate" aria-label="SistemSehat at a glance">
          <p class="plate-name">SistemSehat</p>
          <dl>
            <div><dt>Purpose</dt><dd>Guidance on specifying, pricing and buying medical equipment</dd></div>
            <div><dt>For</dt><dd>Procurement officials, clinicians and technical staff in district health offices and public hospitals in Indonesia</dd></div>
            <div><dt>Sources</dt><dd>Public documents only, each one cited</dd></div>
            <div><dt>Funding</dt><dd>None from manufacturers or distributors</dd></div>
            <div><dt>Status</dt><dd>Guides published. Device dossiers in preparation.</dd></div>
          </dl>
        </aside>
      </div>
    </section>

    <section class="band">
      <div class="wrap">
        <div class="section-head">
          <h2>How to use this site</h2>
        </div>
        <ol class="howto">
          <li>
            <h3>Find your task</h3>
            <p>Choose what you need to do from the list below, or open the guide that matches it.</p>
          </li>
          <li>
            <h3>Read the rules</h3>
            <p>Each rule says what to do, gives an example, and ends with a question to ask yourself.</p>
          </li>
          <li>
            <h3>Use the checklist</h3>
            <p>Take all 35 questions to your planning meeting or document review, on screen or on paper.</p>
          </li>
        </ol>

        <div class="section-head section-head-sub">
          <h2>What do you need to do?</h2>
        </div>
        <ul class="tasks">
          <li><a href="specification.html">Write a specification</a></li>
          <li><a href="pricing.html">Set a budget or cost estimate I can explain</a></li>
          <li><a href="regulation.html">Check the documents in a bid</a></li>
          <li><a href="process.html#rule-3-7">Run a tender again after it failed</a></li>
          <li><a href="technology.html#rule-b-7">Judge a new technology a supplier is offering</a></li>
          <li><a href="checklist.html">Get a checklist for a meeting</a></li>
        </ul>
      </div>
    </section>

    <section class="band band-tint">
      <div class="wrap">
        <div class="section-head">
          <h2>Three questions every purchase must answer</h2>
          <a class="all-link" href="guides.html">All guides</a>
        </div>
        <p class="band-lead">Answer them in this order. A weak answer to one question cannot be fixed by the next one.</p>
        <ul class="cards cards-3">
{guide_card(GUIDES[0])}
{guide_card(GUIDES[1])}
{guide_card(GUIDES[2])}
        </ul>

        <div class="section-head section-head-sub">
          <h2>Two guides that support all three</h2>
        </div>
        <p class="band-lead">Like the annexes of a bidding document, they give the background that all three answers depend on.</p>
        <ul class="cards cards-2">
{guide_card(GUIDES[3])}
{guide_card(GUIDES[4])}
        </ul>
      </div>
    </section>

    <section class="band">
      <div class="wrap">
        <div class="section-head">
          <h2>Tools</h2>
        </div>
        <ul class="cards cards-3">
{tool_card("checklist.html", "Checklist", "All 35 questions from the guides. Tick them on screen or print them on two pages.", "check")}
{tool_card("glossary.html", "Glossary", "Indonesian terms, procurement words and abbreviations, explained in plain English.", "book")}
{tool_card("library.html", "Sources", "The public documents behind the guides: specifications, prices, process and evidence.", "shelf")}
        </ul>
      </div>
    </section>

    <section class="band band-tint">
      <div class="wrap two-col">
        <div>
          <div class="section-head">
            <h2>Device dossiers</h2>
            <a class="all-link" href="dossiers.html">About dossiers</a>
          </div>
          <p>A dossier is a short report on one device. It answers all three questions for that device: a model specification, a reference price range, and lessons for running the purchase. The first three are being written.</p>
{STATUS_TABLE}
        </div>
        <div>
          <div class="section-head">
            <h2>Latest updates</h2>
          </div>
          <ul class="updates">
            <li><span class="update-meta">October 2026<span class="update-type">Guides</span></span><a href="guides.html">Every rule now has an example</a></li>
            <li><span class="update-meta">October 2026<span class="update-type">Site</span></span><a href="id/index.html" hreflang="id">SistemSehat is now also in Bahasa Indonesia</a></li>
            <li><span class="update-meta">October 2026<span class="update-type">Guides</span></span><a href="guides.html">Five guides published, with 35 rules</a></li>
            <li><span class="update-meta">October 2026<span class="update-type">Dossiers</span></span><a href="dossiers.html">First three device dossiers in preparation</a></li>
          </ul>
        </div>
      </div>
    </section>

    <section class="band">
      <div class="wrap">
        <div class="section-head">
          <h2>How this site stays independent</h2>
          <a class="all-link" href="about.html#how">How it works</a>
        </div>
        <ul class="rules">
          <li>
            <h3>Public sources only</h3>
            <p>Every figure and requirement comes from a document anyone can download, and each one is cited.</p>
          </li>
          <li>
            <h3>No money from sellers</h3>
            <p>No funding, gifts or sponsored content from manufacturers or distributors.</p>
          </li>
          <li>
            <h3>No current tenders</h3>
            <p>Nothing is published about a tender that is still being evaluated.</p>
          </li>
          <li>
            <h3>Public corrections</h3>
            <p>When something here is wrong or outdated, it is corrected and the change is noted on the page.</p>
          </li>
        </ul>
      </div>
    </section>"""

# ------------------------------------------------------------------ Specification

spec_clauses = "\n".join([
    clause("1.1", "Start from the clinical need",
           ["Before you list any features, write down what the device must do, for which patients, and in which type of facility. A device for a district hospital ward and one for a village health post may have the same name but need very different specifications."],
           "Can a clinician who will use the device explain, in one sentence, why each requirement is needed?",
           "For an infant warmer: &ldquo;Keeps a newborn warm during resuscitation and the first hours after birth, in the delivery room of a PONED puskesmas.&rdquo;"),
    clause("1.2", "Describe what it must do, not which product to buy",
           ["State the range, accuracy, capacity or output you need. Do not name a brand or model. Do not copy a design detail that only one manufacturer uses. A requirement copied from one brochure usually fits only one product."],
           "Can more than one manufacturer meet this requirement as written?",
           "Write &ldquo;heater output controlled automatically by a skin temperature sensor, with a manual mode&rdquo;, not the model name of the warmer you used before."),
    clause("1.3", "Separate &ldquo;must have&rdquo; from &ldquo;nice to have&rdquo;",
           ["A &ldquo;must have&rdquo; is something without which the device is unsafe or useless, because a bid that lacks it is rejected. Everything else is &ldquo;nice to have&rdquo;. If the evaluation method allows it, give extra points for &ldquo;nice to have&rdquo; items instead of rejecting bids without them."],
           "If a bid did not meet this line, would you really want to reject it?",
           "For an infant warmer, an alarm when the temperature goes out of range is a must have. A built-in baby scale is nice to have."),
    clause("1.4", "Name the right standards",
           ["Medical electrical equipment must meet the general safety standard IEC 60601-1. Many types of device also have a particular standard of their own. For example, IEC 60601-2-21 covers infant radiant warmers. Name the standards that apply, and ask for proof such as a test report, not just a statement that the device complies."],
           "Does each standard you name actually apply to this type of device?",
           "Weak: &ldquo;Meets international standards.&rdquo; Strong: &ldquo;Meets IEC 60601-1 and IEC 60601-2-21. Attach the test report.&rdquo;"),
    clause("1.5", "Choose for the place where it will be used",
           ["The device must keep working where it is used. Think about the electricity supply and the climate: heat, humidity and dust. Think also about the journey to remote facilities, the skills of the staff who will use it, and who will maintain it."],
           "Would this device still work in the facility on the delivery list with the fewest resources?",
           "A laboratory analyzer for a puskesmas with frequent power cuts may need a UPS, and reagents that can be stored without a refrigerator."),
    clause("1.6", "List everything that must come with the device",
           ["A device is not ready to use without its accessories, its first supply of consumables and a manual its users can read. Include these, and also training, the warranty period, spare parts, and how fast the supplier must respond to a breakdown."],
           "On delivery day, will everything needed to treat the first patient be there?",
           "For a laboratory analyzer: the first reagents, control and calibration materials, printer paper, and training for the laboratory staff."),
    clause("1.7", "Make every requirement checkable",
           ["For each requirement, say what evidence the bidder must submit, and how you will check it when the device is delivered. If you cannot check a requirement, you cannot enforce it."],
           "For each line: which document proves it, and which check confirms it at delivery?",
           "Requirement: temperature control within the range you set. Evidence in the bid: the test report. Check at delivery: measure with a calibrated thermometer during the acceptance test."),
])

spec_rewrite = table(
    ["Often written", "The problem", "Better"],
    [
        ["&ldquo;Brand X or equivalent&rdquo;", "Names a product, and does not say what &ldquo;equivalent&rdquo; means.", "State what the device must achieve, with the range and accuracy needed."],
        ["&ldquo;High-quality display&rdquo;", "Cannot be checked, so it cannot be enforced.", "&ldquo;Display shows the set value and the measured value, readable from one metre.&rdquo;"],
        ["&ldquo;Must have a touchscreen&rdquo;", "A design choice, not a clinical need.", "&ldquo;Controls can be used with gloved hands and cleaned with standard disinfectant.&rdquo;"],
        ["&ldquo;Complies with international standards&rdquo;", "Does not say which standards, or what proof is needed.", "&ldquo;Meets IEC 60601-1 and the particular standard for this type of device. Test report attached.&rdquo;"],
    ],
)

spec_sections = table(
    ["Section", "What to write"],
    [
        ["Name, category and coding", "The generic name and a code from a recognised naming system, such as GMDN, so that every bidder understands the same device"],
        ["Purpose of use", "The clinical purpose, the level of care and the department where it will be used"],
        ["Technical characteristics", "What it must achieve, what it displays, and the settings a user can change"],
        ["Physical characteristics", "Parts, mobility and materials"],
        ["Utility requirements", "The electricity, water or gas supply the device needs"],
        ["Accessories, consumables and spare parts", "What must arrive with the device, and what it will use up"],
        ["Packaging", "Sterility on delivery, shelf life, transport, storage and labelling"],
        ["Environmental requirements", "The conditions the device must tolerate where it will work"],
        ["Training, installation and use", "Site preparation, approval at commissioning, and training for users"],
        ["Warranty and maintenance", "Warranty period, type of service contract, spare parts after the warranty, and upgrades"],
        ["Documentation", "The manuals and other documents to be supplied"],
        ["Decommissioning", "How long the device is expected to last"],
        ["Safety and standards", "Risk class, marketing authorisation and the standards that apply"],
    ],
)

spec = f"""    <div class="wrap">
      <header class="page-head">
        <h1>What should we ask for?</h1>
        <p class="lead">A specification decides what arrives at the facility. A good specification lets several manufacturers compete to supply a device that meets the clinical need. A poor one lets in equipment that does not work, or leaves only one supplier able to bid.</p>
{reviewed('guide-1')}
      </header>

{keypoints('1')}
      <div class="clauses">
{spec_clauses}
      </div>

      <h2 class="section-title">Rewriting a requirement</h2>
      <p class="section-lead">Four lines that often appear in specifications, and how to write each one better. The examples are illustrative.</p>
{spec_rewrite}

      <h2 class="section-title">A full specification, section by section</h2>
      <p class="section-lead">The World Health Organization publishes a <a href="https://www.who.int/publications/m/item/user-guide-who-technical-specification-for-medical-devices">template for technical specifications</a> with fifty fields in thirteen sections. If you use the same sections every time, nothing is forgotten and two specifications can be compared line by line.</p>
{spec_sections}

{related('1')}
{pager('specification.html')}
    </div>"""

# ------------------------------------------------------------------ Pricing

price_clauses = "\n".join([
    clause("2.1", "Agree what a price covers before you compare",
           ["Two prices for the same device can differ several times and both be fair, because they cover different things. One may be for the device alone, as it leaves the factory. Another may include delivery, installation and years of service. Write down what each price includes before you compare them."],
           "For every price you have, can you list what it includes and what it does not?",
           "Quote A: Rp150 million for the analyzer only. Quote B: Rp290 million including delivery, installation, training and two years of reagents. Quote B may be the better offer. (Illustrative figures.)"),
    clause("2.2", "Count the cost over the device's whole life",
           ["The purchase price is only part of the cost. Add delivery and installation, consumables and reagents, maintenance and spare parts, training, and disposal at the end. For laboratory analyzers, the reagents used over the years can cost more than the analyzer itself."],
           "What will this device cost each year once it is in use, and who will pay?",
           "A puskesmas that runs 20 tests a day, 250 days a year, uses reagents for 25,000 tests in five years. Multiply that by the reagent cost per test to see the real cost."),
    clause("2.3", "Use prices you can trace to a source",
           ["Build your reference price from sources that anyone can check. International catalogues such as the <a href=\"https://supply.unicef.org/\">UNICEF Supply Catalogue</a> publish indicative prices. Indonesia's national e-catalogue, <a href=\"https://katalog.inaproc.id/\">INAPROC Katalog Elektronik</a>, lists domestic offers. Past cost estimates (HPS) in tender notices, and contract award notices, show what other buyers expected and paid. The <a href=\"https://www.theglobalfund.org/en/sourcing-management/procurement-tools\">Global Fund</a> shows a good way to present reference prices and delivery times by product category."],
           "Could someone else trace every figure in your estimate back to its source?",
           "Record each price like this: source, item, price, currency, the date you read it, and what the price includes."),
    clause("2.4", "Compare prices on the same basis",
           ["Convert all prices to one currency, using the exchange rate of one stated date. Note the quantity each price was for, where the goods are delivered, and whether taxes and import duties are included. One unit collected from a warehouse and a thousand units delivered to remote facilities will not have the same unit price."],
           "Are all the prices in the same currency, from the same date, and for the same delivery point?",
           "Convert US dollar prices with the Bank Indonesia JISDOR rate on the day you prepare the estimate, and write that date next to the figure."),
    clause("2.5", "Explain why prices differ; do not average them",
           ["When two reliable prices are far apart, the reason is usually what they cover, the quantity, the level of specification or the after-sales service. Find out which. An average of prices that cover different things does not mean anything."],
           "For your highest and lowest prices, can you explain why they are different?",
           "Two infant warmer prices differ three times over. The higher one includes a resuscitation unit and a five-year service contract. Compare them only after taking those out."),
    clause("2.6", "Check whether you will be tied to one supplier",
           ["Some devices work only with the manufacturer's own reagents, consumables or software. Then a low purchase price can be followed by years of high running costs. Ask for the cost per test or per use, and for how long that price is guaranteed."],
           "After purchase, can you buy what the device uses from more than one supplier?",
           "A &ldquo;closed&rdquo; analyzer accepts only the manufacturer's reagent packs. An &ldquo;open&rdquo; analyzer can use reagents from other suppliers, which usually keeps the cost per test lower."),
])

price_layers = table(
    ["Part of the price", "What it adds", "Ask the seller"],
    [
        ["Device", "The equipment with its standard accessories", "Which accessories and first consumables are included?"],
        ["Freight and insurance", "Transport to Indonesia or to the central warehouse", "To which place is the price quoted?"],
        ["Delivery to the facility", "The final journey, which can cost the most for remote facilities", "Is delivery to every facility on the list included?"],
        ["Installation and commissioning", "Setting up, testing and handing over a working device", "Who installs it, and when is it counted as accepted?"],
        ["Training", "Teaching users to operate it and technicians to maintain it", "How many people, for how long, and where?"],
        ["Warranty and maintenance", "Repairs, spare parts and regular servicing for a set period", "How long is the cover, and how fast must the supplier respond?"],
        ["Consumables and reagents", "What the device uses up when it runs", "What is the cost per test or per use, and for how long is it fixed?"],
    ],
)

pricing = f"""    <div class="wrap">
      <header class="page-head">
        <h1>What should it cost?</h1>
        <p class="lead">A price means little until you know what it includes. A good reference price says what it covers and where each figure comes from, so you can explain it line by line.</p>
{reviewed('guide-2')}
      </header>

{keypoints('2')}
      <div class="clauses">
{price_clauses}
      </div>

      <h2 class="section-title">What a price can include</h2>
      <p class="section-lead">Each part adds cost. Before you compare two prices, find out which parts each one covers.</p>
{price_layers}

{related('2')}
{pager('pricing.html')}
    </div>"""

# ------------------------------------------------------------------ Process

proc_clauses = "\n".join([
    clause("3.1", "Size each lot so that several suppliers can bid",
           ["A lot is a part of a tender that is bid for and awarded separately. You can divide lots by type of device, by region, or both. Their size decides who can bid. A lot that is too large keeps out capable smaller suppliers. Lots that are too small mean many contracts and can raise prices."],
           "For each lot, can you name several suppliers who could deliver the full quantity to every site?",
           "Instead of one national lot of 200 infant warmers, five regional lots of about 40 also let regional distributors bid."),
    clause("3.2", "Choose national or international competition deliberately",
           ["A national tender suits devices that Indonesian suppliers can make or supply in the quantity needed. An international tender brings in more bidders when they cannot. The choice affects the language, currency, timetable and delivery terms of the whole tender."],
           "Do you know who makes this device, and where, before you decide who can bid?",
           "Before you decide, search Info Alkes for devices of this type with an AKD number, which means they are made in Indonesia."),
    clause("3.3", "Tell bidders how bids will be scored",
           ["Bidders need to know the rules before they bid. Either the contract goes to the lowest-priced bid that meets all the requirements, or bids are scored on quality as well as price. Put the criteria and their weights in the bidding document."],
           "Could a bidder work out, from the document alone, how the winner will be chosen?",
           "&ldquo;Price 70%, service response time 20%, training plan 10%.&rdquo; (Illustrative weights.)"),
    clause("3.4", "Give bidders enough time and clear answers",
           ["Three things help good suppliers prepare a correct bid. Hold a pre-bid meeting. Share written answers with all bidders. Issue a formal amendment whenever the document changes. After the last amendment, leave enough time for bidders to respond to it."],
           "After your last amendment, how many working days do bidders have left?",
           "If an amendment changes a technical requirement two days before the deadline, move the deadline."),
    clause("3.5", "Learn from bidders' questions",
           ["Questions from bidders show you where the document is weak. When several bidders ask about the same requirement, it is unclear, or narrower than you meant. Correct it before bids close, not after they are opened."],
           "Which requirement got the most questions, and what did you change because of it?",
           "If three bidders ask whether the warmer must have a built-in scale, the requirement is unclear or too narrow."),
    clause("3.6", "Plan what happens after the contract is signed",
           ["Signing the contract is the halfway point, not the end. Plan delivery, installation, acceptance testing, user training and the warranty in advance. Decide who will maintain the device after the warranty ends."],
           "Who is responsible for this device in the year after the warranty ends?",
           "Write down who keeps the service record, who calls the supplier when a warmer breaks down, and who budgets for spare parts after the warranty."),
    clause("3.7", "If a tender fails, find the cause before you repeat it",
           ["Too few bids, no bids that meet the requirements, and prices above the cost estimate (HPS) are three different failures with different causes. If you repeat the same tender without finding the cause, you will usually get the same result."],
           "Before you re-tender: what exactly failed, and which part of the document have you changed?",
           "No bid met the requirements because none had a test report for the particular standard. Before re-tendering, check that suppliers can provide one."),
])

fail_table = table(
    ["What happened", "Common causes", "Check first"],
    [
        ["Too few bids, or none", "The lot is too large, the timetable too short, or suppliers did not hear about it.", "Lot size compared with what suppliers can deliver, the number of days allowed, and where the notice was published."],
        ["Bids arrived, but none met the requirements", "A requirement is unclear, or only one product can meet it.", "The bidders' questions, and which requirement each bid missed."],
        ["Prices above the cost estimate (HPS)", "The estimate left out delivery, installation, service or other costs that bidders included.", "What the estimate covered, compared with what the document asked bidders to include."],
    ],
)

roles_table = table(
    ["Role", "Usual tasks", "Most useful guides"],
    [
        ["Clinical users (doctors, midwives, nurses, laboratory staff)", "Describe the clinical need, and check that the specification makes sense in practice", '<a href="specification.html">Specification</a>'],
        ["Technical and maintenance staff (for example IPSRS in hospitals)", "Check technical requirements, installation needs, maintenance and spare parts", '<a href="specification.html">Specification</a> and <a href="technology.html">Technology</a>'],
        ["PPK", "Sets the technical specification and the cost estimate (HPS), signs and manages the contract, and receives the goods at handover", '<a href="specification.html">Specification</a>, <a href="pricing.html">Pricing</a> and <a href="regulation.html">Regulation</a>'],
        ["Pokja Pemilihan", "Prepares the bidding document, runs the tender, answers bidders' questions and evaluates the bids", '<a href="process.html">Process</a> and <a href="regulation.html">Regulation</a>'],
        ["Supplier (<em>penyedia</em>)", "Submits a bid, then delivers, installs, trains and provides service under the contract", "&nbsp;"],
    ],
)

process = f"""    <div class="wrap">
      <header class="page-head">
        <h1>How do we buy it without a failed tender?</h1>
        <p class="lead">Many tenders fail because of decisions made before the tender opens. These include how the lots are divided, how bids will be scored, and how much time bidders get.</p>
{reviewed('guide-3')}
      </header>

{keypoints('3')}
      <div class="clauses">
{proc_clauses}
      </div>

      <h2 class="section-title">Who does what in a government tender</h2>
      <p class="section-lead">The usual roles under Presidential Regulation 16 of 2018 on government procurement, as amended. Your organisation may divide the work differently. Purchases from the e-catalogue are usually handled by the PPK or a procurement official (<em>Pejabat Pengadaan</em>), not by a Pokja.</p>
{roles_table}

      <h2 class="section-title">When a tender fails</h2>
      <p class="section-lead">Three common ways a tender fails, and the causes to check first. More than one can apply.</p>
{fail_table}

{related('3')}
{pager('process.html')}
    </div>"""

# ------------------------------------------------------------------ Regulation and standards

reg_clauses = "\n".join([
    clause("A.1", "Check the marketing authorisation (<em>izin edar</em>) first",
           ["A medical device needs a marketing authorisation, called <em>izin edar</em>, from the Ministry of Health before it can be sold in Indonesia. The number starts with AKD for a device made in Indonesia, and AKL for an imported one. Anyone can look up a product on the Ministry's <a href=\"https://infoalkes.kemkes.go.id/\">Info Alkes</a> website."],
           "Does the number in the offer match this exact product and model in the public database, and is it still valid?",
           "Search Info Alkes for the product. Check that the manufacturer, the model and the AKD or AKL number all match the offer."),
    clause("A.2", "Know the risk class",
           ["Devices are grouped into four classes, from A (low risk) to D (high risk), following the ASEAN Medical Device Directive. In vitro diagnostic devices (laboratory tests) use the same four letters. The higher the class, the more evidence the manufacturer had to provide for registration."],
           "Which class is this device, and do the documents in the offer match it?",
           "Ask the bidder to state the risk class, and check that the registration documents in the offer show the same class."),
    clause("A.3", "Check who made it, and how quality is controlled",
           ["Registration usually requires the manufacturer's ISO 13485 certificate, issued by an accredited body. Devices made in Indonesia also need a good manufacturing practice certificate, called CPAKB. These certificates show that the factory works under a controlled system. They do not prove that a particular device performs well."],
           "Is the manufacturer's quality certificate still valid, and does its scope cover this product?",
           "An ISO 13485 certificate that covers only patient monitors does not cover an infant warmer from the same factory. Read the scope written on the certificate."),
    clause("A.4", "Check who is selling it",
           ["Distributors must follow good distribution practice for medical devices, called CDAKB. The seller should also have a letter of authorisation from the manufacturer. This matters most after delivery, when you need spare parts and service."],
           "Can the seller show the manufacturer's authorisation, and does it cover service for the whole life of the device?",
           "A good letter names the distributor, the products and the period it covers, and is signed by the manufacturer."),
    clause("A.5", "Ask for standards, with proof",
           ["Standards make sure that buyer and seller agree on what &ldquo;safe&rdquo; means. Name the standards that apply to the device, with their edition, and ask for the test report. The table below lists the standards cited most often."],
           "For each standard in the offer: which edition, tested by whom, and on which model?",
           "&ldquo;Complies with IEC 60601-1&rdquo; is a claim. &ldquo;IEC 60601-1:2005+AMD1:2012+AMD2:2020, test report number &hellip;, from laboratory &hellip;, for model &hellip;&rdquo; is evidence."),
    clause("A.6", "Check local content (TKDN)",
           ["Government buyers must give priority to products made in Indonesia. The share of local content is certified as a percentage, called TKDN. If a domestic product with enough local content exists, you may not buy an imported one instead. The rules for calculating and certifying TKDN changed in 2025, so check the current rule before you rely on a figure."],
           "Is there a domestic product that meets the specification, and what does its TKDN certificate say?",
           "Before you decide that no domestic product qualifies, look up its TKDN certificate in the Ministry of Industry's TKDN database."),
    clause("A.7", "Budget for calibration every year",
           ["Every medical device used in a health facility must be tested or calibrated at least once a year by an authorised testing body. This is a cost and a task that repeat every year, starting the year after delivery."],
           "Who will calibrate this device each year, and is the cost in the budget?",
           "If you buy ten infant warmers this year, next year's budget needs ten calibrations."),
    clause("A.8", "Know how to report a problem",
           ["The Ministry of Health runs a national monitoring system for medical devices, called e-Watch Alkes. It also publishes guidance on reporting adverse events: incidents in which a device harms, or could harm, a patient. Staff who know how to report do it faster, and a fast report protects the next patient."],
           "If this device harmed a patient tomorrow, who in your facility would report it, and how?",
           "Name one person in each facility who reports device problems, and put the reporting steps up next to the device."),
])

standards_table = table(
    ["Standard", "What it covers", "When to name it"],
    [
        ["IEC 60601-1", "General safety and essential performance of medical electrical equipment", "Any medical device that uses mains power or a battery"],
        ["IEC 60601-1-2", "Electromagnetic compatibility: the device does not disturb other equipment, and is not disturbed by it", "The same devices, especially where several are used side by side"],
        ["IEC 60601-2 series", 'Extra requirements for one type of device. <a href="https://webstore.iec.ch/publication/64028">IEC 60601-2-21</a>, for example, covers infant radiant warmers', "Whenever a particular standard exists for the type of device"],
        ['<a href="https://www.iso.org/standard/59752.html">ISO 13485</a>', "The manufacturer's quality management system", "As evidence about the manufacturer, not about the device"],
        ["ISO 14971", "How the manufacturer finds and controls risks", "For higher-risk devices, together with the risk analysis"],
        ["IEC 62304", "How medical device software is developed and maintained", "Any device that depends on software"],
        ["IEC 62366-1", "Usability: design that prevents mistakes by users", "Devices whose safety depends on how the user operates them"],
    ],
)

regulation = f"""    <div class="wrap">
      <header class="page-head">
        <h1>What must a device comply with?</h1>
        <p class="lead">A medical device must meet Indonesian regulations before it can be sold or used, and a good device is built and tested to published standards. Knowing which documents to ask for is the quickest way to tell an offer that complies from one that only claims to.</p>
{reviewed('guide-a')}
      </header>

{keypoints('A')}
      <div class="clauses">
{reg_clauses}
      </div>

      <h2 class="section-title">Standards named most often</h2>
      <p class="section-lead">Standards are updated over time. Always give the edition, and check with the publisher which edition is current.</p>
{standards_table}

      <h2 class="section-title">Sources</h2>
      <div class="prose">
        <p>The rules on this page were checked on 11 October 2026. Regulations change, so confirm the current text before you rely on it.</p>
        <ul>
          <li><a href="https://jdih.kemkes.go.id/storage/documents/pdfs/2017permenkes062.pdf">Minister of Health Regulation 62 of 2017</a> on marketing authorisation for medical devices.</li>
          <li><a href="https://regalkes.kemkes.go.id/informasi_alkes/Indonesia%20Guideline%20for%20Evaluation%20of%20Medical%20Device%20and%20IVD%202020.pdf">Indonesia Guideline for Evaluation of Medical Device and IVD (2020)</a>, Ministry of Health.</li>
          <li><a href="https://regalkes.kemkes.go.id/informasi_alkes/TataCaraKlasifikasi1.pdf">Classification of medical devices by risk</a>, Ministry of Health.</li>
          <li><a href="https://farmalkes.kemkes.go.id/2024/07/bijak-memilih-dan-menggunakan-alkes-dan-pkrt/">How to check a marketing authorisation number</a>, Directorate General of Pharmaceuticals and Medical Devices (2024).</li>
          <li><a href="https://farmalkes.kemkes.go.id/unduh/modul-cara-distribusi-alat-kesehatan-yang-baik/">Good distribution practice for medical devices</a>, citing Minister of Health Regulation 4 of 2014.</li>
          <li><a href="https://peraturan.bpk.go.id/Download/107180/Permenkes%20Nomor%2054%20Tahun%202015.pdf">Minister of Health Regulation 54 of 2015</a> on testing and calibration of medical devices.</li>
          <li><a href="https://bbt.kemenperin.go.id/blog/menperin:-regulasi-baru-tkdn-prioritaskan-produk-lokal-dan-pacu-investasi">Ministry of Industry statement on the new TKDN rules</a> (October 2025).</li>
          <li><a href="https://farmalkes.kemkes.go.id/unduh/tata-cara-pelaporan-kejadian-tidak-diinginkan-ktd-alat-kesehatan/">Procedure for reporting adverse events involving medical devices</a>, Ministry of Health (2020).</li>
        </ul>
      </div>

{related('A')}
{pager('regulation.html')}
    </div>"""

# ------------------------------------------------------------------ Technology and research

tech_clauses = "\n".join([
    clause("B.1", "Understand how it works",
           ["Every device measures or delivers something physical, such as heat, pressure, light or an electrical signal. Knowing which one tells you what limits its accuracy, what it needs from its surroundings, and what usually breaks first."],
           "Can you explain in two sentences how this device does its job?",
           "A radiant warmer heats the baby from above with infrared heat, so staff can care for the baby without covering it. That is why it needs a skin temperature sensor to control the heat."),
    clause("B.2", "Separate what matters for the patient from extra features",
           ["The core technology decides how well the device works for the patient. Extra features add convenience, and often add cost. Two devices with the same core technology can have very different prices because of screens, connectivity or software that change nothing for the patient."],
           "Which of the listed features changes the result for the patient?",
           "For an analyzer, the measuring method decides how accurate the result is. A larger touchscreen or Wi-Fi does not."),
    clause("B.3", "Ask what evidence supports each claim",
           ["Some evidence is stronger than other evidence. An independent test report or a peer-reviewed study is stronger than the manufacturer's own data, and both are stronger than a brochure. A marketing authorisation shows that a device may be sold. It does not show that it is the right choice for you."],
           "For the main performance claim: who measured it, and were they independent of the seller?",
           "A brochure says &ldquo;highly accurate&rdquo;. An independent evaluation reports how close the results were to a reference method, and on how many samples."),
    clause("B.4", "Check its history in use",
           ["Find out how long the model has been sold, where it is used, and whether it has been recalled or named in a safety notice. Facilities that already use it are the best source of information, and they are usually willing to talk."],
           "Where is this model already in use, and what do those users say about it?",
           "Ask the seller for three facilities that have used the model for more than a year, and call at least one of them."),
    clause("B.5", "Match the technology to the level of care",
           ["The most advanced device is not the best choice for every facility. WHO, UNFPA and UNICEF publish a joint <a href=\"https://www.who.int/publications/i/item/9789241565028\">list of priority medical devices</a> for the health of mothers, newborns and children. It is arranged by level of care. WHO's <a href=\"https://medevis.who-healthtechnologies.org/\">MeDevIS</a> platform lists more than 2,300 types of device and the level of care each one suits. In Indonesia, a health technology assessment committee, set up by the Ministry of Health in 2014, reviews the evidence for technologies considered for JKN coverage."],
           "Was this technology designed for a facility like yours, with your staff and your number of patients?",
           "A fully automatic chemistry analyzer may suit a district hospital laboratory. A puskesmas may be better served by a smaller semi-automatic analyzer that its own staff can run and maintain."),
    clause("B.6", "Plan for the device's whole life",
           ["A device is used for many years after its warranty ends. Ask how long spare parts will be available. Ask how the software is updated, and who pays for updates. Ask when the manufacturer plans to stop supporting the model."],
           "For how many years does the manufacturer promise spare parts and software support?",
           "Ask the bidder to state in writing until which year spare parts for this model will be available."),
    clause("B.7", "Be careful with new technology",
           ["New technology can reach the market before there is evidence that it works well. If you buy early, you pay to discover its problems. For anything new, look for evaluations by people other than the manufacturer before you buy it for a whole district."],
           "Has this technology been evaluated by anyone who does not profit from selling it?",
           "Try a new rapid test in one facility, and compare its results with the laboratory, before you buy it for every puskesmas."),
])

evidence_table = table(
    ["Source", "What you find there", "Use it for"],
    [
        ['<a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a>', "Peer-reviewed studies of devices and the technology behind them", "Independent evidence on accuracy and clinical benefit"],
        ['<a href="https://medevis.who-healthtechnologies.org/">WHO MeDevIS</a>', "More than 2,300 types of medical device, with the level of care and infrastructure each one needs", "Checking that a device suits your type of facility before you write the specification"],
        ['<a href="https://www.who.int/publications/i/item/9789241565028">WHO, UNFPA and UNICEF interagency list</a>', "Priority medical devices for the health of mothers, newborns and children, by level of care", "Deciding whether a technology belongs in your type of facility"],
        ['<a href="https://supply.unicef.org/">UNICEF Supply Catalogue</a>', "Technical specifications and indicative prices for the devices UNICEF supplies", "A reference specification written for places with limited resources"],
        ['<a href="https://infoalkes.kemkes.go.id/">Info Alkes</a>', "Devices, manufacturers and distributors registered in Indonesia", "Confirming that a model has a marketing authorisation, and who supplies it"],
        ['<a href="https://e-watch-alkes.kemkes.go.id/">e-Watch Alkes</a>', "Indonesia's national monitoring system for medical devices", "Reporting a problem with a device"],
    ],
)

technology = f"""    <div class="wrap">
      <header class="page-head">
        <h1>How do we judge the technology?</h1>
        <p class="lead">You do not need to design a device to judge it. You need to know how it works, what evidence supports it, and whether it suits the place where it will be used.</p>
{reviewed('guide-b')}
      </header>

{keypoints('B')}
      <div class="clauses">
{tech_clauses}
      </div>

      <h2 class="section-title">Where to find the evidence</h2>
      <p class="section-lead">Public sources worth checking before any purchase. All are free to use.</p>
{evidence_table}

      <div class="prose">
        <h2>Technology notes</h2>
        <p>Short explanations of how specific types of device work will be published together with the dossiers. {IN_PREP}</p>
        <p>Sources for this page: an <a href="https://dara.ui.ac.id/research-output/0275fc74-f03e-4cc6-8a89-048e47c2f4a5">account of health technology assessment in Indonesia</a>, for the 2014 committee. The Ministry of Health's <a href="https://farmalkes.kemkes.go.id/unduh/tata-cara-pelaporan-kejadian-tidak-diinginkan-ktd-alat-kesehatan/">medical device services page</a>, for e&#8209;Watch Alkes.</p>
      </div>

{related('B')}
{pager('technology.html')}
    </div>"""

# ------------------------------------------------------------------ Dossiers

dossier_parts = table(
    ["Part", "Question it answers", "What it contains"],
    [
        ['<a href="specification.html">Specification</a>', "What should we ask for?", "A model specification that names no brand, the requirements that matter clinically, and the standards to name."],
        ['<a href="pricing.html">Pricing</a>', "What should it cost?", "Published reference prices, what each one includes, and why they differ."],
        ['<a href="process.html">Process</a>', "How do we buy it without a failed tender?", "How to divide the lots, how to score the bids, and the questions bidders usually ask."],
    ],
)

dossiers = f"""    <div class="wrap">
      <header class="page-head">
        <h1>Device dossiers</h1>
        <p class="lead">A dossier is a short report on one device. It answers all three questions for that device, in a few pages, for a team that has to buy it.</p>
      </header>

      <div class="prose">
        <h2>What a dossier contains</h2>
{dossier_parts}

        <h2>How a dossier is made</h2>
        <p>Every dossier follows the same six steps, so any two can be compared and every claim can be traced.</p>
        <ol class="steps">
          <li>Public sources are collected, and each one is recorded with its link and the date it was read.</li>
          <li>The specification is written using the <a href="specification.html">thirteen sections of the WHO template</a>, the same for every device.</li>
          <li>The reference price is built from cited figures, each with what it includes.</li>
          <li>The draft is checked against the two publication rules below.</li>
          <li>Someone who uses the device in clinical practice reads it before it is published.</li>
          <li>It is published with a version number and a date, and corrections are recorded on the page.</li>
        </ol>

        <h2>In preparation</h2>
{STATUS_TABLE}

        <h2>When a dossier is published</h2>
        <p>A dossier is published only when both of these are true:</p>
        <ul>
          <li>Everything in it comes from public documents, and each source is cited.</li>
          <li>It is not about a tender that is still being evaluated.</li>
        </ul>
        <p>Dossiers do not rate brands or recommend models. They describe what to ask for, what a fair price covers, and how to run the purchase.</p>
      </div>
    </div>"""

# ------------------------------------------------------------------ About

about = """    <div class="wrap">
      <header class="page-head">
        <h1>About SistemSehat</h1>
        <p class="lead">SistemSehat publishes independent guidance on buying medical equipment. It covers the technical specification, the price and the procurement process, with background on regulation, standards and the technology itself.</p>
      </header>

      <div class="prose">
        <h2>Who it is for</h2>
        <p>People in district health offices and public hospitals in Indonesia who take part in buying medical equipment:</p>
        <ul>
          <li>procurement officials, such as the PPK and the Pokja Pemilihan;</li>
          <li>clinicians who help write specifications and check what is delivered;</li>
          <li>technical and maintenance staff;</li>
          <li>planners who prepare budgets.</li>
        </ul>

        <h2>Why it exists</h2>
        <p>These teams are asked to specify and price complex equipment, often with little independent material to help them. Suppliers know their products in detail. Buyers need guidance that is just as careful, from someone with no product to sell.</p>

        <h2>Why the name</h2>
        <p><em>Sistem sehat</em> means &ldquo;healthy system&rdquo; in Indonesian. A health system depends on its equipment, and buying the right device at a fair price helps keep that system healthy.</p>

        <h2>Who is behind it</h2>
        <p>SistemSehat was started by Aminul Solihin, a biomedical engineer trained at Institut Teknologi Bandung. He led the development of three medical devices from prototype to market before moving into public procurement.</p>

        <h2>Disclosure</h2>
        <p>Aminul works in public-sector procurement in Indonesia. SistemSehat is a personal initiative. It is not linked to or endorsed by his employer, any government body or any lender, and nothing on this site represents their views.</p>

        <h2 id="how">How it works</h2>
        <ul>
          <li><strong>Public sources only.</strong> Every figure and requirement comes from a document anyone can download, and each one is cited.</li>
          <li><strong>No money from sellers.</strong> No funding, gifts or sponsored content from manufacturers or distributors.</li>
          <li><strong>No current tenders.</strong> Nothing is published about a tender that is still being evaluated.</li>
          <li><strong>No brand ratings.</strong> The guidance describes what to ask for and how to buy it, not which product to choose.</li>
          <li><strong>Public corrections.</strong> When something is wrong or outdated, it is corrected and the change is noted on the page.</li>
        </ul>

        <h2>Status</h2>
        <p>SistemSehat is a working project and is not yet a registered organisation. The aim is to make it a nonprofit.</p>
        <!-- CONTACT: add a line here with your email address or LinkedIn link before going live. -->
      </div>
    </div>"""

# ------------------------------------------------------------------ Dossier template (kept out of the published site)

template_body = """    <div class="wrap">
      <header class="page-head">
        <h1>DEVICE NAME</h1>
        <p class="lead">One or two sentences: what this device does, where it is used, and who this dossier is for.</p>
        <p class="reviewed">Version 1.0, published DATE. Sources are listed at the end and are all public.</p>
      </header>

      <div class="prose">
        <h2>At a glance</h2>
        <div class="table-wrap">
          <table>
            <thead>
              <tr><th scope="col">Item</th><th scope="col">For this device</th></tr>
            </thead>
            <tbody>
              <tr><th scope="row">Generic name and nomenclature code</th><td data-label="For this device">NAME, GMDN OR EMDN CODE</td></tr>
              <tr><th scope="row">Level of care</th><td data-label="For this device">WHERE IT IS MEANT TO BE USED</td></tr>
              <tr><th scope="row">Risk class in Indonesia</th><td data-label="For this device">A, B, C OR D</td></tr>
              <tr><th scope="row">Standards that apply</th><td data-label="For this device">STANDARD AND EDITION</td></tr>
            </tbody>
          </table>
        </div>

        <h2>1. What should we ask for?</h2>
        <p>The clinical need in two or three sentences. Then the model specification, using the thirteen sections of the WHO template. Keep every section, and write "not applicable" where one does not apply.</p>
        <div class="table-wrap">
          <table>
            <thead>
              <tr><th scope="col">Section</th><th scope="col">Requirement</th><th scope="col">How to check</th></tr>
            </thead>
            <tbody>
              <tr><th scope="row">Name, category and coding</th><td data-label="Requirement">TEXT</td><td data-label="How to check">EVIDENCE</td></tr>
              <tr><th scope="row">Purpose of use</th><td data-label="Requirement">TEXT</td><td data-label="How to check">EVIDENCE</td></tr>
              <tr><th scope="row">Technical characteristics</th><td data-label="Requirement">TEXT</td><td data-label="How to check">EVIDENCE</td></tr>
              <tr><th scope="row">Physical characteristics</th><td data-label="Requirement">TEXT</td><td data-label="How to check">EVIDENCE</td></tr>
              <tr><th scope="row">Utility requirements</th><td data-label="Requirement">TEXT</td><td data-label="How to check">EVIDENCE</td></tr>
              <tr><th scope="row">Accessories, consumables and spare parts</th><td data-label="Requirement">TEXT</td><td data-label="How to check">EVIDENCE</td></tr>
              <tr><th scope="row">Packaging</th><td data-label="Requirement">TEXT</td><td data-label="How to check">EVIDENCE</td></tr>
              <tr><th scope="row">Environmental requirements</th><td data-label="Requirement">TEXT</td><td data-label="How to check">EVIDENCE</td></tr>
              <tr><th scope="row">Training, installation and use</th><td data-label="Requirement">TEXT</td><td data-label="How to check">EVIDENCE</td></tr>
              <tr><th scope="row">Warranty and maintenance</th><td data-label="Requirement">TEXT</td><td data-label="How to check">EVIDENCE</td></tr>
              <tr><th scope="row">Documentation</th><td data-label="Requirement">TEXT</td><td data-label="How to check">EVIDENCE</td></tr>
              <tr><th scope="row">Decommissioning</th><td data-label="Requirement">TEXT</td><td data-label="How to check">EVIDENCE</td></tr>
              <tr><th scope="row">Safety and standards</th><td data-label="Requirement">TEXT</td><td data-label="How to check">EVIDENCE</td></tr>
            </tbody>
          </table>
        </div>

        <h2>2. What should it cost?</h2>
        <div class="table-wrap">
          <table>
            <thead>
              <tr><th scope="col">Source</th><th scope="col">Price</th><th scope="col">Date</th><th scope="col">What it includes</th></tr>
            </thead>
            <tbody>
              <tr><th scope="row"><a href="URL">SOURCE NAME</a></th><td data-label="Price">PRICE AND CURRENCY</td><td data-label="Date">DATE</td><td data-label="What it includes">SCOPE</td></tr>
            </tbody>
          </table>
        </div>
        <p>Why these prices differ.</p>

        <h2>3. How do we buy it without a failed tender?</h2>
        <p>How to divide the lots, how to score the bids, and the questions bidders usually ask about this device.</p>

        <h2>Sources</h2>
        <ul>
          <li><a href="URL">DOCUMENT TITLE</a>, publisher, date. Read on DATE.</li>
        </ul>

        <h2>Corrections</h2>
        <p>None yet.</p>
      </div>
    </div>"""

# ------------------------------------------------------------------ Checklist

checklist = f"""    <div class="wrap">
      <header class="page-head">
        <h1>The checklist</h1>
        <p class="lead">All the &ldquo;Ask yourself&rdquo; questions from the five guides, in one place. Tick them on screen, or print the list for your meeting.</p>
        <p class="reviewed">{len(S['registry'])} questions. Last reviewed {REVIEWED}. Under each question is a link to the rule it comes from.</p>
      </header>

      <div class="checklist">
{checklist_groups()}
      </div>
    </div>"""

# ------------------------------------------------------------------ Glossary
# (id, term, definition, patterns). The ids are shared with the Indonesian glossary.
# patterns find the term in running text; the first one on each page is linked here.

az, rows, n_terms = glossary_list([
    ("acceptance-test", "Acceptance test", "The check at delivery that the device works and meets the contract, before the buyer accepts it. In Indonesian: <em>uji terima</em>.", [r"(?i:\bacceptance test(?:ing|s)?\b)"]),
    ("adverse-event", "Adverse event", "An incident in which a device harms, or could harm, a patient or a user. In Indonesian: <em>kejadian tidak diinginkan</em> (KTD).", [r"(?i:\badverse events?\b)"]),
    ("akd-and-akl", "AKD and AKL", "The letters at the start of an Indonesian marketing authorisation number. AKD means the device is made in Indonesia; AKL means it is imported.", [r"\bAKD\b", r"\bAKL\b"]),
    ("alkes", "<em>Alkes</em>", "Short for <em>alat kesehatan</em>, the Indonesian term for medical devices.", [r"\bAlkes\b"]),
    ("amendment", "Amendment", "A formal change to a bidding document, sent to every bidder before the deadline. In Indonesian: <em>adendum</em>.", [r"(?i:\bamendments?\b)"]),
    ("asean", "ASEAN", "Association of Southeast Asian Nations. Its Medical Device Directive sets the A to D risk classes that Indonesia follows.", [r"\bASEAN\b"]),
    ("bidder", "Bidder", "A company that submits a bid in a tender. In Indonesian: <em>peserta</em>.", [r"(?i:\bbidders?\b)"]),
    ("calibration", "Calibration", "Checking a device's measurements against a known reference, and adjusting it if needed.", [r"(?i:\bcalibrat(?:e|ed|ion)\b)"]),
    ("cdakb", "CDAKB", "<em>Cara Distribusi Alat Kesehatan yang Baik</em>: good distribution practice for medical devices, which distributors in Indonesia must follow.", [r"\bCDAKB\b"]),
    ("commissioning", "Commissioning", "Setting up a newly installed device and testing that it works before it is used. In Indonesian: <em>uji fungsi</em>.", [r"(?i:\bcommissioning\b)"]),
    ("consumables", "Consumables", "Items a device uses up, such as reagents, sensors, filters or paper. In Indonesian: <em>bahan habis pakai</em>.", [r"(?i:\bconsumables\b)"]),
    ("cpakb", "CPAKB", "<em>Cara Pembuatan Alat Kesehatan yang Baik</em>: good manufacturing practice for medical devices, certified for manufacturers in Indonesia.", [r"\bCPAKB\b"]),
    ("e-watch-alkes", "e-Watch Alkes", "Indonesia's national monitoring system for medical devices, run by the Ministry of Health. Problems with devices are reported here.", [r"e(?:-|\u2011|&#8209;)Watch Alkes"]),
    ("ecri", "ECRI", "An independent nonprofit organisation in the United States that tests medical devices and reports on their safety.", [r"\bECRI\b"]),
    ("emdn", "EMDN", "European Medical Device Nomenclature: a system for naming types of device, used mostly in European countries.", [r"\bEMDN\b"]),
    ("gmdn", "GMDN", "Global Medical Device Nomenclature: a system for naming types of device, used by regulators in many countries.", [r"\bGMDN\b"]),
    ("hps", "HPS", "<em>Harga perkiraan sendiri</em>: the cost estimate a government buyer prepares before a tender. It is used to judge the prices offered.", [r"\bHPS\b"]),
    ("hta", "HTA", "Health technology assessment: a structured review of what a technology achieves and what it costs. It is used to decide whether a health system should pay for it.", [r"\bHTA\b", r"(?i:\bhealth technology assessment\b)"]),
    ("iec", "IEC", "International Electrotechnical Commission. It publishes safety standards for electrical medical equipment, such as IEC 60601-1.", [r"\bIEC\b"]),
    ("inaproc-katalog-elektronik", "INAPROC Katalog Elektronik", "Indonesia's national electronic catalogue for government purchasing, run by LKPP.", [r"INAPROC Katalog Elektronik"]),
    ("info-alkes", "Info Alkes", "The Ministry of Health's public database of registered medical devices, manufacturers and distributors.", [r"\bInfo Alkes\b"]),
    ("ipsrs", "IPSRS", "<em>Instalasi Pemeliharaan Sarana Rumah Sakit</em>: the hospital unit that maintains equipment and buildings.", [r"\bIPSRS\b"]),
    ("iso", "ISO", "International Organization for Standardization. It publishes standards such as ISO 13485 on quality management for device manufacturers.", [r"\bISO\b"]),
    ("ivd", "IVD", "In vitro diagnostic device: a device that tests samples taken from the body, such as blood or urine.", [r"\bIVD\b", r"(?i:\bin vitro diagnostic\b)"]),
    ("izin-edar", "<em>Izin edar</em>", "Marketing authorisation. A medical device needs one from the Ministry of Health before it can be sold in Indonesia.", [r"(?i:\bizin edar\b)", r"(?i:\bmarketing authorisation\b)"]),
    ("jisdor", "JISDOR", "Jakarta Interbank Spot Dollar Rate: the daily reference rate for the rupiah against the US dollar, published by Bank Indonesia.", [r"\bJISDOR\b"]),
    ("jkn", "JKN", "<em>Jaminan Kesehatan Nasional</em>: Indonesia's national health insurance, run by BPJS Kesehatan.", [r"\bJKN\b"]),
    ("lkpp", "LKPP", "<em>Lembaga Kebijakan Pengadaan Barang/Jasa Pemerintah</em>: Indonesia's government procurement policy agency.", [r"\bLKPP\b"]),
    ("lot", "Lot", "A part of a tender that is bid for and awarded separately, often one type of device or one region. In Indonesian: <em>paket</em>.", [r"(?i:\blots?\b)"]),
    ("model-specification", "Model specification", "A specification for a type of device that names no brand. It is a starting point that buyers adapt to their own needs.", [r"(?i:\bmodel specifications?\b)"]),
    ("particular-standard", "Particular standard", "A standard in the IEC 60601-2 series with extra requirements for one type of medical electrical equipment.", [r"(?i:\bparticular standards?\b)"]),
    ("pokja-pemilihan", "Pokja Pemilihan", "The selection working group that runs a government tender. It prepares the bidding document, answers bidders' questions and evaluates the bids.", [r"\bPokja Pemilihan\b", r"\bPokja\b"]),
    ("poned", "PONED", "<em>Pelayanan Obstetri Neonatal Emergensi Dasar</em>: basic emergency care for mothers and newborns, offered by designated puskesmas.", [r"\bPONED\b"]),
    ("ppk", "PPK", "<em>Pejabat Pembuat Komitmen</em>: the official who sets the technical specification and the cost estimate (HPS), and signs and manages the contract.", [r"\bPPK\b"]),
    ("pre-bid-meeting", "Pre-bid meeting", "A meeting where the buyer explains the tender and answers questions from possible bidders. In Indonesian: <em>pemberian penjelasan</em>.", [r"(?i:\bpre-bid meetings?\b)"]),
    ("puskesmas", "<em>Puskesmas</em>", "<em>Pusat kesehatan masyarakat</em>: the community health centre that provides primary care in Indonesia.", [r"(?i:\bpuskesmas\b)"]),
    ("rated-criteria", "Scoring on quality and price", "An evaluation method that gives points for the quality of a bid as well as its price. In Indonesian: <em>sistem nilai</em>.", [r"(?i:\bscored on quality\b)"]),
    ("reagent", "Reagent", "A chemical that a laboratory analyzer uses to carry out a test. Reagents are bought again and again.", [r"(?i:\breagents?\b)"]),
    ("reference-price", "Reference price", "A price range for a device, built from cited sources, each with what it includes. It is used to judge the prices offered.", [r"(?i:\breference prices?\b)"]),
    ("risk-class", "Risk class", "One of four classes, A to D, that group medical devices from low to high risk.", [r"(?i:\brisk class(?:es)?\b)"]),
    ("supplier", "Supplier", "A company that sells and delivers goods. In Indonesian government procurement: <em>penyedia</em>.", [r"(?i:\bsuppliers?\b)"]),
    ("test-report", "Test report", "A document from a testing laboratory showing that a device was tested against a standard, and the results.", [r"(?i:\btest reports?\b)"]),
    ("tkdn", "TKDN", "<em>Tingkat Komponen Dalam Negeri</em>: the certified share of local content in a product, as a percentage.", [r"\bTKDN\b"]),
    ("total-cost-of-ownership", "Total cost of ownership", "Everything a device costs over its working life: purchase, delivery, installation, consumables, maintenance, training and disposal.", [r"(?i:\btotal cost of ownership\b)"]),
    ("umdns", "UMDNS", "Universal Medical Device Nomenclature System: a system for naming types of device, maintained by ECRI.", [r"\bUMDNS\b"]),
    ("unfpa", "UNFPA", "United Nations Population Fund, the United Nations agency for sexual and reproductive health.", [r"\bUNFPA\b"]),
    ("unicef", "UNICEF", "United Nations Children's Fund. It buys medical equipment for many countries and publishes specifications and prices.", [r"\bUNICEF\b"]),
    ("ups", "UPS", "Uninterruptible power supply: a battery unit that keeps a device running during a power cut.", [r"\bUPS\b"]),
    ("who", "WHO", "World Health Organization, the United Nations agency for health.", [r"\bWHO\b", r"World Health Organization"]),
])

glossary = f"""    <div class="wrap">
      <header class="page-head">
        <h1>Glossary</h1>
        <p class="lead">Indonesian terms, procurement words and abbreviations used on this site, explained in plain English. In the guides, a term with a dotted underline links to its entry here.</p>
        <p class="reviewed">{n_terms} terms. Last reviewed {REVIEWED}.</p>
      </header>

      <div class="glossary-tools">
        <nav class="az" aria-label="Jump to a letter">
          <ul>{az}</ul>
        </nav>
        <div class="filter js-only">
          <label for="glossary-filter">Filter the glossary</label>
          <input id="glossary-filter" type="search" placeholder="For example: TKDN">
        </div>
      </div>
      <p id="glossary-count" class="reviewed" aria-live="polite"></p>

      <dl class="glossary">
{rows}
      </dl>
    </div>"""

# ------------------------------------------------------------------ Sources (library.html)

library = f"""    <div class="wrap">
      <header class="page-head">
        <h1>Sources</h1>
        <p class="lead">The public documents this site uses and learned from. Each one is good at one part of the job. All are free to read unless noted.</p>
        <p class="reviewed">Links checked {REVIEWED}.</p>
      </header>

      <div class="prose library">
{library_group("Specifications and lists of devices", [
    ['<a href="https://www.who.int/publications/m/item/user-guide-who-technical-specification-for-medical-devices">Technical specification template and user guide</a>', "World Health Organization", "A template of fifty fields in thirteen sections. Every dossier here uses this structure."],
    ['<a href="https://medevis.who-healthtechnologies.org/">MeDevIS</a>', "World Health Organization", "More than 2,300 types of device, which you can browse by level of care, health care unit and type."],
    ['<a href="https://supply.unicef.org/">UNICEF Supply Catalogue</a>', "UNICEF", "Full specifications, written for places with limited resources, with indicative prices."],
    ['<a href="https://www.nhsrcindia.org/sites/default/files/2021-05/Technical%20Specifications%20of%20Medical%20Devices%20for%20Special%20Neonatal%20Care%20Unit.pdf">Technical specifications for special neonatal care units</a>', "National Health Systems Resource Centre, India", "An example of a national set of model specifications, written with clinicians, engineers and manufacturers."],
    ['<a href="https://www.who.int/publications/i/item/9789241565028">Interagency list of priority medical devices</a>', "WHO, UNFPA and UNICEF", "Which devices belong at which level of care, for the health of mothers, newborns and children."],
])}
{library_group("Prices", [
    ['<a href="https://www.theglobalfund.org/en/sourcing-management/procurement-tools">Procurement tools and reference prices</a>', "The Global Fund", "Reference prices and delivery times by product category, and indicative costs for freight, insurance and quality checks."],
    ['<a href="https://katalog.inaproc.id/">INAPROC Katalog Elektronik</a>', "LKPP, Indonesia", "Offers from domestic suppliers in the national e-catalogue."],
])}
{library_group("Process and practice", [
    ['<a href="https://www.open-contracting.org/what-is-open-contracting/health/">Open contracting for health</a>', "Open Contracting Partnership", "Guides and country examples on publishing and using health procurement data."],
    ['<a href="https://www.newborntoolkit.org/">Implementation Toolkit for Small and Sick Newborn Care</a>', "NEST360 and UNICEF", "Practical guidance arranged by task, including a section on equipment and supplies."],
])}
{library_group("Evidence and safety", [
    ['<a href="https://home.ecri.org/">ECRI</a>', "ECRI, an independent nonprofit", "Device evaluations and a yearly list of health technology hazards. Evaluations are for members only."],
    ['<a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a>', "US National Library of Medicine", "Peer-reviewed studies of devices and the technology behind them."],
    ['<a href="https://infoalkes.kemkes.go.id/">Info Alkes</a>', "Ministry of Health, Indonesia", "Confirming that a device has a marketing authorisation in Indonesia, and who supplies it."],
    ['<a href="https://e-watch-alkes.kemkes.go.id/">e-Watch Alkes</a>', "Ministry of Health, Indonesia", "The national monitoring system for medical devices."],
])}
      </div>
    </div>"""

# ------------------------------------------------------------------ Guides

guide_cards_main = "\n".join(guide_card(g, "h2") for g in GUIDES[:3])
guide_cards_support = "\n".join(guide_card(g, "h2") for g in GUIDES[3:])

guides = f"""    <div class="wrap">
      <header class="page-head">
        <h1>Guides</h1>
        <p class="lead">Five guides with {len(S['registry'])} rules. Three follow the steps of a purchase. Two give the background that every purchase depends on.</p>
        <p class="reviewed">Each rule says what to do, gives an example, and ends with a question to ask yourself.</p>
      </header>

      <div class="section-head">
        <h2 class="section-title">Three questions every purchase must answer</h2>
      </div>
      <ul class="cards cards-3">
{guide_cards_main}
      </ul>

      <div class="section-head section-head-sub">
        <h2 class="section-title">Two guides that support all three</h2>
      </div>
      <ul class="cards cards-2">
{guide_cards_support}
      </ul>

      <section class="related related-spaced" aria-labelledby="related-title">
        <h2 id="related-title">Use the guides</h2>
        <ul class="link-list">
          <li><a href="checklist.html">Checklist</a><span>All the questions from the guides, to tick or print</span></li>
          <li><a href="glossary.html">Glossary</a><span>Terms and abbreviations used here, explained</span></li>
          <li><a href="library.html">Sources</a><span>The public documents behind the guides</span></li>
          <li><a href="search.html">Search</a><span>Find a rule or a term by keyword</span></li>
        </ul>
      </section>
    </div>"""

# ------------------------------------------------------------------ Search

search = f"""    <div class="wrap">
      <header class="page-head">
        <h1>Search</h1>
        <p class="lead">Search the {len(S['registry'])} rules, the glossary and the sources.</p>
      </header>

      <form class="search search-large" action="search.html" method="get" role="search" aria-label="New search">
        <label for="page-search">Search for</label>
        <div class="search-row">
          <input id="page-search" type="search" name="q">
          <button type="submit">Search</button>
        </div>
      </form>

      <p id="search-status" class="reviewed" aria-live="polite"></p>
      <ol id="results" class="results"></ol>

      <noscript>
        <p>Search needs JavaScript. Without it, browse the <a href="guides.html">guides</a>, the <a href="checklist.html">checklist</a> or the <a href="glossary.html">glossary</a>.</p>
      </noscript>

      <div id="search-help" class="prose">
        <h2>Try searching for</h2>
        <ul class="chips">
          <li><a href="search.html?q=calibration">calibration</a></li>
          <li><a href="search.html?q=warranty">warranty</a></li>
          <li><a href="search.html?q=lot">lot</a></li>
          <li><a href="search.html?q=TKDN">TKDN</a></li>
          <li><a href="search.html?q=standard">standard</a></li>
          <li><a href="search.html?q=reagents">reagents</a></li>
        </ul>
      </div>
    </div>"""

PAGES = [
    ("index.html", "SistemSehat: independent guidance on buying medical equipment",
     "Free, independent guidance on specifying, pricing and buying medical equipment for Indonesia's public health facilities.", home),
    ("guides.html", "Guides | SistemSehat",
     "Five guides on specifying, pricing and buying medical equipment, and on the regulation and technology behind them.", guides),
    ("specification.html", "What should we ask for? Specification guide | SistemSehat",
     "Seven rules, with examples, for writing a medical equipment specification that several manufacturers can meet.", spec),
    ("pricing.html", "What should it cost? Pricing guide | SistemSehat",
     "Six rules, with examples, for building a reference price for medical equipment that you can explain and defend.", pricing),
    ("process.html", "How do we buy it without a failed tender? Process guide | SistemSehat",
     "Seven rules, with examples, for running a medical equipment tender, from dividing lots to finding why a tender failed.", process),
    ("regulation.html", "What must a device comply with? Regulation guide | SistemSehat",
     "Eight rules, with examples, for checking a medical device against Indonesian regulations and international standards.", regulation),
    ("technology.html", "How do we judge the technology? Technology guide | SistemSehat",
     "Seven rules, with examples, for judging medical technology and the evidence behind it.", technology),
    ("checklist.html", "The checklist | SistemSehat",
     "All the questions from the SistemSehat guides in one checklist you can tick or print.", checklist),
    ("glossary.html", "Glossary | SistemSehat",
     "Indonesian terms, procurement words and abbreviations used on SistemSehat, explained in plain English.", glossary),
    ("library.html", "Sources | SistemSehat",
     "Public documents on medical device specifications, prices, procurement and evidence.", library),
    ("dossiers.html", "Device dossiers | SistemSehat",
     "What a SistemSehat device dossier contains, which ones are in preparation, and when one is published.", dossiers),
    ("about.html", "About | SistemSehat",
     "Who SistemSehat is for, who is behind it, and how it stays independent.", about),
    ("search.html", "Search | SistemSehat",
     "Search the SistemSehat rules, glossary and sources.", search),
]

INDEX_PAGES = [
    ("checklist.html", "The checklist", "All the questions from the five guides, to tick on screen or print."),
    ("dossiers.html", "Device dossiers", "What a dossier contains, how one is made and when it is published."),
    ("about.html", "About SistemSehat", "Who the site is for, who is behind it, and how it stays independent."),
]

TEMPLATE = ("DEVICE NAME dossier | SistemSehat", "ONE-SENTENCE SUMMARY OF THIS DOSSIER.",
            "DEVICE NAME", template_body, "dossier-template.html")
