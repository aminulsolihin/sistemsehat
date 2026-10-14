---
title: How do we design the right device? Design guide | SistemSehat
description: >-
  Seven rules, with examples, for turning a concept into a safe, usable medical device: setting, risk, usability, software, testing and manufacture.
lang: en
layout: guide
pillar: build
reviewed: 14 October 2026
order: 7
number: "D"
label: Design
question: How do we design the right device?
summary: >-
  A good idea still fails if the device is unsafe, hard to use or impossible to make. Seven rules
  for turning a chosen concept into a device.
icon: pencil
lead: >-
  Once you have a need and a concept ([Guide C](identify.html)), make the device safe, usable and
  buildable, and prove it. These rules apply whether you work in a university,
  a hospital or a company.

rules:
  - number: "D.1"
    heading: Design for the place where it will be used
    explanation: >-
      Find out the power supply, heat, humidity and dust where the device will work, and who will
      use, clean and repair it. Buyers check the same points when they write a specification
      ([rule 1.5](specification.html#rule-1-5)). A device that needs what the facility lacks will not
      be bought, or will not be used.
    example: >-
      If the puskesmas has frequent power cuts, design for battery operation, and use parts that a
      district technician can buy and replace.
    ask: Would your device still work in the least-equipped facility you want to serve?

  - number: "D.2"
    heading: Manage risk from the first sketch
    explanation: >-
      List what could harm a patient or user, how likely it is, and how severe. Then design the risk
      out, add a protection, or warn the user, in that order. ISO 14971 describes this process, and
      regulators expect to see its record.
    example: >-
      An infant warmer could overheat a baby. Design: limit the heater's power. Protection: a
      separate cut-out that switches off at a set temperature. Warning: an alarm and a label.
    ask: For each hazard you listed, which design change, protection or warning controls it?

  - number: "D.3"
    heading: Test usability with the people who will use it
    explanation: >-
      Many problems with devices are use errors: the design leads a tired or busy user into a
      mistake. IEC 62366-1 describes how to find and remove them, ending with a test of the final
      design. Let nurses, midwives or technicians use it in realistic conditions, and watch without
      helping.
    example: >-
      Ask three midwives to set the temperature with gloved hands, in a dim room, without the manual.
      Note every hesitation and every wrong press.
    ask: Which use errors did you see in testing, and what did you change because of them?

  - number: "D.4"
    heading: Treat software as part of the device
    explanation: >-
      Software that controls a device, or that supports a diagnosis or treatment decision, is
      usually regulated as a medical device. IEC 62304 sets out how to develop and maintain it. Plan
      for updates, security and records from the start.
    example: >-
      An app that calculates a medicine dose from a child's weight is medical device software, even
      when it runs on an ordinary phone.
    ask: Which of your software's functions could harm a patient if they gave a wrong result?

  - number: "D.5"
    heading: Record design decisions as you go
    explanation: >-
      Keep a design file: the requirements, how each one was checked, and why each decision was
      made. ISO 13485 calls this design and development control. Rebuilding the file later is slow,
      and registering the device ([Guide E](to-market.html)) depends on it.
    example: >-
      For each requirement, keep one line: the requirement, the test method, the result, the date,
      and who checked it.
    ask: Could someone outside your team trace each requirement to a test result?

  - number: "D.6"
    heading: Verify the design, then validate the device
    explanation: >-
      Verification shows that you built the device right: every requirement is met, by test.
      Validation shows that you built the right device: it meets the need, with real users, in
      realistic conditions. You need both before you apply for registration.
    example: >-
      Verification: a bench test shows the heater holds the set temperature within its tolerance.
      Validation: midwives use the warmer in simulated transfers with a newborn manikin, and judge
      whether it meets the need.
    ask: Which test shows each requirement is met, and which shows that the device meets the need?

  - number: "D.7"
    heading: Design for manufacture and supply
    explanation: >-
      A prototype that one engineer can build is not yet a product. Choose parts and processes you
      can source reliably, in the volume and at the cost your need criteria allow. Plan who will make
      it, and under which quality system.
    example: >-
      Replace a hand-machined heater housing with a moulded one, and confirm two suppliers for each
      critical part, preferably in Indonesia.
    ask: Can the device be made at the volume and cost you need, from parts you can buy reliably?

tables:
  stages:
    columns:
      - Stage
      - What you should have
      - Where to look
    rows:
      - - Find and choose the need
        - A need statement and need criteria, agreed with the people who give care
        - '[Guide C](identify.html), rules C.1 to C.4'
      - - Choose and prototype a concept
        - Concepts screened against the criteria, and prototypes that answered your questions
        - '[Guide C](identify.html), rules C.5 to C.7'
      - - Design
        - Requirements, a risk file, usability results and a design file
        - Rules D.1 to D.5; ISO 14971, IEC 62366-1, IEC 62304, ISO 13485
      - - Verify and validate
        - Bench, safety and usability test reports, and evidence that the device meets the need
        - Rule D.6; IEC 60601-1 and the particular standard
      - - Prepare to make and sell it
        - A manufacturer with a quality system, suppliers, and the documents for registration
        - Rule D.7; [Guide E](to-market.html)
---

## From idea to device

What to have at each stage. Each stage builds on the one before, and gaps found late cost the most to fix.

{% include table.html table=page.tables.stages %}

## Sources

These are the public documents behind this guide. The standards themselves are sold by ISO and IEC; their summary pages are free.

- Paul Yock, Stefanos Zenios, Josh Makower and others, *Biodesign: The Process of Innovating Medical Technologies*, 2nd edition, Cambridge University Press, 2015. See chapters 4.5 (concept exploration and testing), 5.2 (R&D strategy) and 5.5 (quality management).
- [ISO 14971:2019](https://www.iso.org/standard/72704.html), application of risk management to medical devices.
- [IEC 62366-1:2015](https://www.iso.org/standard/63179.html), application of usability engineering to medical devices.
- [IEC 62304:2006](https://www.iso.org/standard/38421.html), medical device software life cycle processes.
- [ISO 13485:2016](https://www.iso.org/standard/59752.html), quality management systems for medical devices.
- World Health Organization, [compendium of innovative health technologies for low-resource settings, 2024](https://www.who.int/publications/i/item/9789240095212).
