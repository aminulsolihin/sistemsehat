---
# A device dossier. Copy this file to dossiers/DEVICE-NAME.md, and drafts/dossier-template-id.md
# to id/dossiers/DEVICE-NAME.md (same file name). Replace every word in CAPITALS, in both.
# Keep every row of the specification table; write "not applicable" where one does not apply.
title: DEVICE NAME dossier | SistemSehat
description: ONE-SENTENCE SUMMARY OF THIS DOSSIER.
lang: en
layout: page
crumb: DEVICE NAME
heading: DEVICE NAME
lead: One or two sentences. What this device does, where it is used, and who this dossier is for.
note: Version 1.0, published DATE. Sources are listed at the end and are all public.
tables:
  glance:
    columns: [Item, For this device]
    rows:
      - [Generic name and nomenclature code, "NAME, GMDN OR EMDN CODE"]
      - [Level of care, WHERE IT IS MEANT TO BE USED]
      - [Risk class in Indonesia, "A, B, C OR D"]
      - [Standards that apply, STANDARD AND EDITION]
  specification:
    columns: [Section, Requirement, How to check]
    rows:
      - ["Name, category and coding", TEXT, EVIDENCE]
      - ["Purpose of use", TEXT, EVIDENCE]
      - ["Technical characteristics", TEXT, EVIDENCE]
      - ["Physical characteristics", TEXT, EVIDENCE]
      - ["Utility requirements", TEXT, EVIDENCE]
      - ["Accessories, consumables and spare parts", TEXT, EVIDENCE]
      - ["Packaging", TEXT, EVIDENCE]
      - ["Environmental requirements", TEXT, EVIDENCE]
      - ["Training, installation and use", TEXT, EVIDENCE]
      - ["Warranty and maintenance", TEXT, EVIDENCE]
      - ["Documentation", TEXT, EVIDENCE]
      - ["Decommissioning", TEXT, EVIDENCE]
      - ["Safety and standards", TEXT, EVIDENCE]
  prices:
    columns: [Source, Price, Date, What it includes]
    rows:
      - ["[SOURCE NAME](URL)", PRICE AND CURRENCY, DATE, SCOPE]
---

## At a glance

{% include table.html table=page.tables.glance %}

## 1. What should we ask for?

The clinical need in two or three sentences. Then the model specification, using the thirteen sections of the WHO template. Keep every section, and write "not applicable" where one does not apply.

{% include table.html table=page.tables.specification %}

## 2. What should it cost?

{% include table.html table=page.tables.prices %}

Why these prices differ.

## 3. How do we buy it without a failed tender?

How to divide the lots, how to score the bids, and the questions bidders usually ask about this device.

## Sources

- [DOCUMENT TITLE](URL), publisher, date. Read on DATE.

## Corrections

None yet.
