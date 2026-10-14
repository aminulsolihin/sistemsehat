---
title: What should we ask for? Specification guide | SistemSehat
description: >-
  Seven rules, with examples, for writing a medical equipment specification that several
  manufacturers can meet.
lang: en
layout: guide
order: 1
number: "1"
label: Specification
question: What should we ask for?
summary: >-
  A specification decides what arrives at the facility. Seven rules for writing one that several
  manufacturers can meet and clinicians can use.
icon: doc
lead: >-
  A specification decides what arrives at the facility. A good specification lets several
  manufacturers compete to supply a device that meets the clinical need. A poor one lets in
  equipment that does not work, or leaves only one supplier able to bid.

rules:
  - number: "1.1"
    heading: Start from the clinical need
    explanation: >-
      Before you list any features, write down what the device must do, for which patients, and
      in which type of facility. A device for a district hospital ward and one for a village
      health post may have the same name but need very different specifications.
    example: >-
      For an infant warmer: "Keeps a newborn warm during resuscitation and the first hours after
      birth, in the delivery room of a PONED puskesmas."
    ask: >-
      Can a clinician who will use the device explain, in one sentence, why each requirement is
      needed?

  - number: "1.2"
    heading: Describe what it must do, not which product to buy
    explanation: >-
      State the range, accuracy, capacity or output you need. Do not name a brand or model. Do
      not copy a design detail that only one manufacturer uses. A requirement copied from one
      brochure usually fits only one product.
    example: >-
      Write "heater output controlled automatically by a skin temperature sensor, with a manual
      mode", not the model name of the warmer you used before.
    ask: Can more than one manufacturer meet this requirement as written?

  - number: "1.3"
    heading: Separate "must have" from "nice to have"
    explanation: >-
      A "must have" is something without which the device is unsafe or useless, because a bid
      that lacks it is rejected. Everything else is "nice to have". If the evaluation method
      allows it, give extra points for "nice to have" items instead of rejecting bids without
      them.
    example: >-
      For an infant warmer, an alarm when the temperature goes out of range is a must have. A
      built-in baby scale is nice to have.
    ask: If a bid did not meet this line, would you really want to reject it?

  - number: "1.4"
    heading: Name the right standards
    explanation: >-
      Medical electrical equipment must meet the general safety standard IEC 60601-1. Many types
      of device also have a particular standard of their own. For example, IEC 60601-2-21 covers
      infant radiant warmers. Name the standards that apply, and ask for proof such as a test
      report, not just a statement that the device complies.
    example: >-
      Weak: "Meets international standards." Strong: "Meets IEC 60601-1 and IEC 60601-2-21.
      Attach the test report."
    ask: Does each standard you name actually apply to this type of device?

  - number: "1.5"
    heading: Choose for the place where it will be used
    explanation: >-
      The device must keep working where it is used. Think about the electricity supply and the
      climate: heat, humidity and dust. Think also about the journey to remote facilities, the
      skills of the staff who will use it, and who will maintain it.
    example: >-
      A laboratory analyzer for a puskesmas with frequent power cuts may need a UPS, and
      reagents that can be stored without a refrigerator.
    ask: >-
      Would this device still work in the facility on the delivery list with the fewest
      resources?

  - number: "1.6"
    heading: List everything that must come with the device
    explanation: >-
      A device is not ready to use without its accessories, its first supply of consumables and
      a manual its users can read. Include these, and also training, the warranty period, spare
      parts, and how fast the supplier must respond to a breakdown.
    example: >-
      For a laboratory analyzer: the first reagents, control and calibration materials, printer
      paper, and training for the laboratory staff.
    ask: On delivery day, will everything needed to treat the first patient be there?

  - number: "1.7"
    heading: Make every requirement checkable
    explanation: >-
      For each requirement, say what evidence the bidder must submit, and how you will check it
      when the device is delivered. If you cannot check a requirement, you cannot enforce it.
    example: >-
      Requirement: temperature control within the range you set. Evidence in the bid: the test
      report. Check at delivery: measure with a calibrated thermometer during the acceptance
      test.
    ask: 'For each line: which document proves it, and which check confirms it at delivery?'

tables:
  rewrite:
    columns:
      - Often written
      - The problem
      - Better
    rows:
      - - '"Brand X or equivalent"'
        - Names a product, and does not say what "equivalent" means.
        - State what the device must achieve, with the range and accuracy needed.
      - - '"High-quality display"'
        - Cannot be checked, so it cannot be enforced.
        - '"Display shows the set value and the measured value, readable from one metre."'
      - - '"Must have a touchscreen"'
        - A design choice, not a clinical need.
        - '"Controls can be used with gloved hands and cleaned with standard disinfectant."'
      - - '"Complies with international standards"'
        - Does not say which standards, or what proof is needed.
        - >-
          "Meets IEC 60601-1 and the particular standard for this type of device. Test report
          attached."
  sections:
    columns:
      - Section
      - What to write
    rows:
      - - Name, category and coding
        - >-
          The generic name and a code from a recognised naming system, such as GMDN, so that
          every bidder understands the same device
      - - Purpose of use
        - The clinical purpose, the level of care and the department where it will be used
      - - Technical characteristics
        - What it must achieve, what it displays, and the settings a user can change
      - - Physical characteristics
        - Parts, mobility and materials
      - - Utility requirements
        - The electricity, water or gas supply the device needs
      - - Accessories, consumables and spare parts
        - What must arrive with the device, and what it will use up
      - - Packaging
        - Sterility on delivery, shelf life, transport, storage and labelling
      - - Environmental requirements
        - The conditions the device must tolerate where it will work
      - - Training, installation and use
        - Site preparation, approval at commissioning, and training for users
      - - Warranty and maintenance
        - >-
          Warranty period, type of service contract, spare parts after the warranty, and
          upgrades
      - - Documentation
        - The manuals and other documents to be supplied
      - - Decommissioning
        - How long the device is expected to last
      - - Safety and standards
        - Risk class, marketing authorisation and the standards that apply
---

## Rewriting a requirement

Four lines that often appear in specifications, and how to write each one better. The examples are illustrative.

{% include table.html table=page.tables.rewrite %}

## A full specification, section by section

The World Health Organization publishes a [template for technical specifications](https://www.who.int/publications/m/item/user-guide-who-technical-specification-for-medical-devices) with fifty fields in thirteen sections. If you use the same sections every time, nothing is forgotten and two specifications can be compared line by line.

{% include table.html table=page.tables.sections %}
