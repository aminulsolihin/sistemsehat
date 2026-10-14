/* SistemSehat: small behaviours, in English or Indonesian to match the page.
   The site works without this file. With it: glossary terms link to their definitions, the language switch keeps your place and offers
   Indonesian to visitors whose browser asks for it, the phone menu folds away, "/" jumps to search,
   the guide tabs show when more are off-screen, long pages get a back-to-top button,
   checklist ticks are kept, the glossary can be filtered, and search runs with highlighted matches. */
(function () {
  "use strict";

  var root = document.documentElement;
  root.classList.add("js"); // normally already set by the inline script in <head>

  /* ---- Messages in the page's language ---- */
  var LANG = root.lang === "id" ? "id" : "en";
  var T = LANG === "id" ? {
    menu: "Menu", close: "Tutup", top: "Kembali ke atas",
    ticked: function (n, of) { return n + " dari " + of + " dicentang"; },
    notKept: "Centang tidak disimpan setelah Anda meninggalkan halaman ini.",
    noTerms: "Tidak ada istilah yang cocok. Coba kata yang lebih pendek.",
    terms: function (n) { return n + " istilah ditampilkan"; },
    noResults: function (q) { return "Tidak ada hasil untuk “" + q + "”. Coba satu kata yang lebih pendek, atau telusuri panduan."; },
    results: function (n, q) { return n + " hasil untuk “" + q + "”"; }
  } : {
    menu: "Menu", close: "Close", top: "Back to top",
    ticked: function (n, of) { return n + " of " + of + " ticked"; },
    notKept: "Ticks are not kept when you leave this page.",
    noTerms: "No terms match. Try a shorter word.",
    terms: function (n) { return n + (n === 1 ? " term" : " terms") + " shown"; },
    noResults: function (q) { return "Nothing found for “" + q + "”. Try one shorter word, or browse the guides."; },
    results: function (n, q) { return n + (n === 1 ? " result" : " results") + " for “" + q + "”"; }
  };

  /* Storage can be missing or blocked (private windows, strict settings); everything still works without it. */
  var store = null;
  try {
    store = window.localStorage;
    store.setItem("sistemsehat-test", "1");
    store.removeItem("sistemsehat-test");
  } catch (e) { store = null; }
  function load(key) { try { return store ? store.getItem(key) : null; } catch (e) { return null; } }
  function save(key, value) { try { if (store) { store.setItem(key, value); } } catch (e) { /* full or blocked */ } }

  /* ---- Glossary terms: the first use of each term on a page links to its definition ----
     The terms come from assets/terms-LANG.js, built from the glossary. Text in links, headings,
     labels, buttons and table headers is left alone. At each place in the text the longest match
     wins, so "Info Alkes" is linked as a whole and never yields a separate link on "Alkes". */
  (function linkTerms() {
    var terms = window.SISTEMSEHAT_TERMS;
    var main = document.getElementById("main");
    var glossaryLink = document.querySelector('.site-footer a[href$="glossary.html"]');
    if (!terms || !main || !glossaryLink) { return; }
    var glossary = glossaryLink.getAttribute("href");
    var finders = [];
    terms.forEach(function (term) {
      (term.f || []).forEach(function (words) {
        var source = words.replace(/[.*+?^${}()|[\]\\]/g, "\\$&").replace(/-/g, "[-\u2011]").replace(/ /g, "\\s+");
        var exact = words !== words.toLowerCase(); // with capitals the case must match; all lowercase matches any case
        finders.push({ rx: new RegExp("\\b" + source + "\\b", exact ? "g" : "gi"), term: term });
      });
    });
    var SKIP = /^(A|H1|H2|H3|H4|H5|H6|LABEL|BUTTON|THEAD|SUMMARY|SCRIPT|STYLE|NOSCRIPT|TEXTAREA|SELECT|svg)$/;
    var walker = document.createTreeWalker(main, NodeFilter.SHOW_TEXT, {
      acceptNode: function (node) {
        if (!/\S/.test(node.nodeValue)) { return NodeFilter.FILTER_REJECT; }
        for (var el = node.parentNode; el && el !== main; el = el.parentNode) {
          if (SKIP.test(el.nodeName) || (el.classList && (el.classList.contains("crumbs") || el.classList.contains("guide-tabs")))) {
            return NodeFilter.FILTER_REJECT;
          }
        }
        return NodeFilter.FILTER_ACCEPT;
      }
    });
    var nodes = [];
    while (walker.nextNode()) { nodes.push(walker.currentNode); }
    var used = {};
    nodes.forEach(function (node) {
      var text = node.nodeValue, i = 0, frag = null, last = 0;
      for (;;) {
        var best = null;
        finders.forEach(function (f) {
          f.rx.lastIndex = i;
          var m = f.rx.exec(text);
          if (m && (!best || m.index < best.m.index || (m.index === best.m.index && m[0].length > best.m[0].length))) {
            best = { m: m, term: f.term };
          }
        });
        if (!best) { break; }
        var start = best.m.index, end = start + best.m[0].length;
        if (!used[best.term.id]) {
          used[best.term.id] = true;
          frag = frag || document.createDocumentFragment();
          frag.appendChild(document.createTextNode(text.slice(last, start)));
          var a = document.createElement("a");
          a.className = "term";
          a.href = glossary + "#" + best.term.id;
          a.title = best.term.d;
          a.textContent = best.m[0];
          frag.appendChild(a);
          last = end;
        }
        i = end;
      }
      if (frag) {
        frag.appendChild(document.createTextNode(text.slice(last)));
        node.parentNode.replaceChild(frag, node);
      }
    });
  })();

  /* ---- Language switch: the other-language link always points at the same spot ---- */
  var LANG_KEY = "sistemsehat-lang";
  var langLinks = Array.prototype.slice.call(document.querySelectorAll(".lang-switch a"));
  function syncLangLinks() {
    langLinks.forEach(function (link) {
      if (!link.dataset.base) { link.dataset.base = link.getAttribute("href"); }
      link.setAttribute("href", link.dataset.base + window.location.search + window.location.hash);
    });
  }
  syncLangLinks();
  window.addEventListener("hashchange", syncLangLinks);
  langLinks.forEach(function (link) {
    link.addEventListener("click", function () { save(LANG_KEY, link.getAttribute("hreflang")); });
  });

  /* Visitors whose browser asks for Indonesian are offered the Indonesian page. Never a redirect:
     the choice is theirs, and it is remembered. */
  var toIndonesian = langLinks.filter(function (l) { return l.getAttribute("hreflang") === "id"; })[0];
  if (LANG === "en" && toIndonesian) {
    var wanted = load(LANG_KEY);
    var browserId = (navigator.languages || [navigator.language || ""]).some(function (l) { return /^id\b/i.test(l); });
    if (wanted === "id" || (wanted === null && browserId)) {
      var hint = document.createElement("div");
      hint.className = "lang-hint";
      hint.setAttribute("role", "region");
      hint.setAttribute("aria-label", "Pilihan bahasa");
      hint.lang = "id";
      hint.innerHTML = '<p>Halaman ini tersedia dalam Bahasa Indonesia.</p>' +
        '<div class="lang-hint-actions"><a class="button" hreflang="id"></a>' +
        '<button type="button" class="lang-hint-close" aria-label="Tetap dalam bahasa Inggris" title="Tetap dalam bahasa Inggris">×</button></div>';
      var go = hint.querySelector("a");
      go.textContent = "Buka versi Indonesia";
      go.setAttribute("href", toIndonesian.getAttribute("href"));
      go.addEventListener("click", function () {
        save(LANG_KEY, "id");
        go.setAttribute("href", toIndonesian.getAttribute("href")); // keeps the current #rule
      });
      hint.querySelector("button").addEventListener("click", function () {
        save(LANG_KEY, "en");
        hint.parentNode.removeChild(hint);
        root.classList.remove("has-lang-hint");
      });
      // first in reading order for keyboard and screen-reader users; shown at the bottom of the screen
      var skip = document.querySelector(".skip");
      document.body.insertBefore(hint, skip ? skip.nextSibling : document.body.firstChild);
      root.classList.add("has-lang-hint");
    }
  }

  /* ---- Menu button on narrow screens ---- */
  var button = document.querySelector(".menu-button");
  var menu = document.getElementById("site-menu");
  var label = button ? button.querySelector(".menu-label") : null;

  function setMenu(open) {
    menu.classList.toggle("is-open", open);
    button.setAttribute("aria-expanded", open ? "true" : "false");
    if (label) { label.textContent = open ? T.close : T.menu; }
  }

  function narrow() {
    return button && window.getComputedStyle(button).display !== "none";
  }

  if (button && menu) {
    button.hidden = false;
    button.addEventListener("click", function () {
      setMenu(!menu.classList.contains("is-open"));
    });
    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape" && menu.classList.contains("is-open")) {
        setMenu(false);
        button.focus();
      }
    });
  }

  /* ---- Search: phone shortcut, and "/" to jump to the search box ---- */
  var pageSearch = document.getElementById("page-search");
  var headerSearch = document.getElementById("header-search");

  function focusSearch() {
    if (pageSearch) {
      pageSearch.focus();
      pageSearch.select();
    } else if (headerSearch) {
      if (menu && narrow()) { setMenu(true); }
      headerSearch.focus();
    }
  }

  var searchLink = document.querySelector(".search-link");
  if (searchLink) {
    searchLink.addEventListener("click", function (event) {
      if (pageSearch || (headerSearch && menu && narrow())) {
        event.preventDefault();
        focusSearch();
      }
    });
  }

  document.addEventListener("keydown", function (event) {
    if (event.key !== "/" || event.ctrlKey || event.metaKey || event.altKey || event.defaultPrevented) { return; }
    var t = event.target;
    if (t && (t.isContentEditable || /^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName))) { return; }
    event.preventDefault();
    focusSearch();
  });

  /* ---- Guide tabs: keep the current tab in view, fade the side with more tabs ---- */
  var tabs = document.querySelector(".guide-tabs");
  if (tabs) {
    var strip = tabs.querySelector("ul");
    var current = tabs.querySelector("[aria-current]");
    var markEdges = function () {
      var max = strip.scrollWidth - strip.clientWidth;
      tabs.classList.toggle("more-left", strip.scrollLeft > 4);
      tabs.classList.toggle("more-right", strip.scrollLeft < max - 4);
    };
    if (current && strip.scrollWidth > strip.clientWidth) {
      var item = current.parentNode;
      strip.scrollLeft = item.offsetLeft - (strip.clientWidth - item.offsetWidth) / 2;
    }
    markEdges();
    strip.addEventListener("scroll", markEdges, { passive: true });
    window.addEventListener("resize", markEdges);
  }

  /* ---- Back to top on long pages ---- */
  var main = document.getElementById("main");
  if (main && "requestAnimationFrame" in window) {
    var topButton = document.createElement("button");
    topButton.type = "button";
    topButton.className = "to-top";
    topButton.hidden = true;
    topButton.setAttribute("aria-label", T.top);
    topButton.innerHTML = '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" ' +
      'stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">' +
      '<path d="M12 19V5M5 12l7-7 7 7"/></svg>';
    document.body.appendChild(topButton);
    var ticking = false;
    var place = function () {
      ticking = false;
      var long = root.scrollHeight > window.innerHeight * 3;
      topButton.hidden = !(long && window.pageYOffset > window.innerHeight * 1.5);
    };
    window.addEventListener("scroll", function () {
      if (!ticking) { ticking = true; window.requestAnimationFrame(place); }
    }, { passive: true });
    window.addEventListener("resize", place);
    topButton.addEventListener("click", function () {
      window.scrollTo(0, 0);
      main.setAttribute("tabindex", "-1");
      main.focus({ preventScroll: true });
    });
    place();
  }

  /* ---- Checklist: keep ticks in this browser, show progress ---- */
  var checklist = document.querySelector(".checklist");
  if (checklist) {
    var boxes = Array.prototype.slice.call(checklist.querySelectorAll('input[type="checkbox"]'));
    var KEY = "sistemsehat-checklist";
    var saved = [];
    try { saved = JSON.parse(load(KEY) || "[]"); } catch (e) { saved = []; }
    if (!Array.isArray(saved)) { saved = []; }
    boxes.forEach(function (box) { box.checked = saved.indexOf(box.id) !== -1; });

    // the bar is already in the page, so filling it in moves nothing
    var count = document.getElementById("check-count");
    var note = document.getElementById("check-note");
    var clear = document.getElementById("check-clear");
    if (!store) { note.textContent = T.notKept; }

    var update = function () {
      var ticked = boxes.filter(function (box) { return box.checked; });
      count.textContent = T.ticked(ticked.length, boxes.length);
      clear.disabled = ticked.length === 0;
      save(KEY, JSON.stringify(ticked.map(function (box) { return box.id; })));
    };
    checklist.addEventListener("change", update);
    clear.addEventListener("click", function () {
      boxes.forEach(function (box) { box.checked = false; });
      update();
    });
    update();
  }

  /* ---- Glossary filter ---- */
  var filter = document.getElementById("glossary-filter");
  if (filter) {
    var terms = Array.prototype.slice.call(document.querySelectorAll(".glossary > div"));
    var termCount = document.getElementById("glossary-count");
    filter.addEventListener("input", function () {
      var q = filter.value.trim().toLowerCase();
      var shown = 0;
      terms.forEach(function (term) {
        var match = q === "" || term.textContent.toLowerCase().indexOf(q) !== -1;
        term.hidden = !match;
        if (match) { shown += 1; }
      });
      if (termCount) {
        termCount.textContent = q === "" ? "" : (shown === 0 ? T.noTerms : T.terms(shown));
      }
    });
  }

  /* ---- Search page ---- */

  /* Append text to a node with every match of the query words wrapped in <mark>. Text only, never HTML. */
  function appendMarked(node, text, words) {
    var lower = text.toLowerCase();
    var i = 0;
    while (i < text.length) {
      var next = -1, len = 0;
      for (var w = 0; w < words.length; w += 1) {
        var at = lower.indexOf(words[w], i);
        if (at !== -1 && (next === -1 || at < next || (at === next && words[w].length > len))) { next = at; len = words[w].length; }
      }
      if (next === -1) { node.appendChild(document.createTextNode(text.slice(i))); return; }
      if (next > i) { node.appendChild(document.createTextNode(text.slice(i, next))); }
      var mark = document.createElement("mark");
      mark.textContent = text.slice(next, next + len);
      node.appendChild(mark);
      i = next + len;
    }
  }

  /* About 190 characters around the first match, cut at word boundaries. */
  function snippet(text, words) {
    var LIMIT = 190;
    if (text.length <= LIMIT) { return text; }
    var lower = text.toLowerCase();
    var first = -1;
    words.forEach(function (w) { var at = lower.indexOf(w); if (at !== -1 && (first === -1 || at < first)) { first = at; } });
    var start = first <= 60 ? 0 : first - 60;
    if (start > 0) { start = text.indexOf(" ", start) + 1 || start; }
    var end = Math.min(text.length, start + LIMIT);
    if (end < text.length) { var cut = text.lastIndexOf(" ", end); if (cut > start) { end = cut; } }
    return (start > 0 ? "…" : "") + text.slice(start, end) + (end < text.length ? "…" : "");
  }

  var results = document.getElementById("results");
  var index = window.SISTEMSEHAT_INDEX;
  if (results && index) {
    var status = document.getElementById("search-status");
    var help = document.getElementById("search-help");
    var query = (new URLSearchParams(window.location.search).get("q") || "").trim();
    if (pageSearch) { pageSearch.value = query; }
    if (query !== "") {
      var words = query.toLowerCase().split(/\s+/).filter(Boolean);
      // highlight the whole phrase where it appears intact, single words elsewhere
      var marks = words.length > 1 ? [words.join(" ")].concat(words) : words;
      var found = [];
      index.forEach(function (entry) {
        var title = entry.t.toLowerCase();
        var body = entry.x.toLowerCase();
        var score = 0;
        for (var i = 0; i < words.length; i += 1) {
          var inTitle = title.indexOf(words[i]) !== -1;
          if (!inTitle && body.indexOf(words[i]) === -1) { return; }
          score += inTitle ? 3 : 1;
        }
        found.push({ entry: entry, score: score });
      });
      found.sort(function (a, b) { return b.score - a.score; });

      found.forEach(function (hit) {
        var li = document.createElement("li");
        var type = document.createElement("span");
        type.className = "result-type";
        type.textContent = hit.entry.k;
        var link = document.createElement("a");
        link.href = hit.entry.u;
        appendMarked(link, hit.entry.t, marks);
        var p = document.createElement("p");
        appendMarked(p, snippet(hit.entry.x, words), marks);
        li.appendChild(type);
        li.appendChild(link);
        li.appendChild(p);
        results.appendChild(li);
      });

      if (status) {
        status.textContent = found.length === 0 ? T.noResults(query) : T.results(found.length, query);
      }
      if (help && found.length > 0) { help.hidden = true; }
    }
  }
})();
