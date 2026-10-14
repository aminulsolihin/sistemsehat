{%- comment -%} Placeholders in the words of _data/*/ui.yml {%- endcomment -%}
{%- assign ph_label = "{label}" -%}
{%- assign ph_label_lower = "{label_lower}" -%}
{%- comment -%}
  The search index for one language: guides, rules, glossary terms, sources and a few pages.
  Built from the same files as the pages, so it is never out of date. Used by search.html.
{%- endcomment -%}
{%- assign lang = include.lang -%}
{%- assign t = site.data[lang].ui -%}
{%- assign guides = site.pages | where: "lang", lang | where: "layout", "guide" | sort: "order" -%}
window.SISTEMSEHAT_INDEX = [
{%- for g in guides %}
{%- assign href = g.name | replace: '.md', '.html' %}
{%- assign label_lower = g.label | downcase %}
{%- assign kind = t.k_rule | replace: ph_label_lower, label_lower | replace: ph_label, g.label %}
 {"t": {{ g.question | jsonify }}, "x": {{ g.summary | jsonify }}, "u": {{ href | jsonify }}, "k": {{ t.k_guide | jsonify }}},
{%- for r in g.rules %}
{%- capture title %}{{ r.number }} {{ r.heading | markdownify | strip_html | normalize_whitespace | strip }}{% endcapture %}
{%- capture text %}{{ r.explanation | markdownify | strip_html }} {{ r.example | markdownify | strip_html }} {{ r.ask | markdownify | strip_html }}{% endcapture %}
 {"t": {{ title | jsonify }}, "x": {{ text | normalize_whitespace | strip | jsonify }}, "u": "{{ href }}#rule-{{ r.number | downcase | replace: '.', '-' }}", "k": {{ kind | jsonify }}},
{%- endfor %}
{%- endfor %}
{%- assign terms = site.data[lang].glossary | sort_natural: "term" %}
{%- for e in terms %}
 {"t": {{ e.term | jsonify }}, "x": {{ e.definition | markdownify | strip_html | normalize_whitespace | strip | jsonify }}, "u": "glossary.html#{{ e.id }}", "k": {{ t.labels["glossary.html"] | jsonify }}},
{%- endfor %}
{%- for group in site.data[lang].sources %}
{%- for s in group.items %}
{%- capture text %}{{ s.publisher | markdownify | strip_html | strip }}. {{ s.use | markdownify | strip_html | strip }}{% endcapture %}
 {"t": {{ s.title | markdownify | strip_html | strip | jsonify }}, "x": {{ text | normalize_whitespace | jsonify }}, "u": "library.html", "k": {{ t.labels["library.html"] | jsonify }}},
{%- endfor %}
{%- endfor %}
{%- assign articles = site.posts | where: "lang", lang %}
{%- for a in articles %}
 {"t": {{ a.title | jsonify }}, "x": {{ a.description | append: " " | append: a.content | strip_html | normalize_whitespace | jsonify }}, "u": "articles/{{ a.url | split: '/' | last }}", "k": {{ t.k_article | jsonify }}},
{%- endfor %}
{%- assign extra = site.pages | where: "lang", lang | sort: "name" %}
{%- for p in extra %}{% if p.search %}
 {"t": {{ p.search.title | jsonify }}, "x": {{ p.search.text | jsonify }}, "u": {{ p.name | replace: '.md', '.html' | jsonify }}, "k": {{ t.k_page | jsonify }}},
{%- endif %}{% endfor %}
];
