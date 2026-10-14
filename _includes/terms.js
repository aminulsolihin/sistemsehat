{%- comment -%}
  Glossary terms for linking: site.js links the first use of each term on a page to the glossary,
  with the definition as a tooltip. Built from _data/LANGUAGE/glossary.yml.
{%- endcomment -%}
{%- assign terms = site.data[include.lang].glossary | sort_natural: "term" -%}
window.SISTEMSEHAT_TERMS = [
{%- for e in terms %}
 {"id": {{ e.id | jsonify }}, "d": {{ e.definition | markdownify | strip_html | normalize_whitespace | strip | jsonify }}, "f": {{ e.find | jsonify }}},
{%- endfor %}
];
