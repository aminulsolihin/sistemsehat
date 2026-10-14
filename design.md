---
title: How do we design the right device? Design guide | SistemSehat
description: >-
  Seven rules, with examples, for designing a medical device from a clinical need: the product profile, the setting, risk, usability and software.
lang: en
layout: guide
pillar: build
reviewed: 14 October 2026
order: 6
number: "C"
label: Design
question: How do we design the right device?
summary: >-
  Many devices fail because they solve the wrong problem, or ignore the place where they will be
  used. Seven rules for designing a device from a clinical need.
icon: bulb
lead: >-
  A device succeeds when it solves a real problem, works where it will be used, and can be shown to
  be safe. These rules apply whether you work in a university, a hospital or a company.

rules:
  - number: "C.1"
    heading: Start from a need you have seen
    explanation: >-
      Watch the work before you invent anything. Spend time where care is given, and write down the
      problems you see, not solutions. A good need statement names the problem, the patients and the
      change you want, and no technology.
    example: >-
      Weak: "A cheaper incubator." Better: "A way to keep low-birth-weight babies warm during
      transfer from a puskesmas to the district hospital."
    ask: Can you state the need without naming any technology?

  - number: "C.2"
    heading: Write down what the device must achieve
    explanation: >-
      A target product profile lists what the finished product must do: its intended use, users,
      setting, performance and price. WHO gives two values for each line: the minimum that is
      acceptable, and the result you would prefer. Agree the profile with clinicians and buyers
      before you start designing.
    example: >-
      For a transport warmer, the minimum is to keep the baby's skin temperature in the safe range
      for a two-hour journey. The preferred result is four hours on its battery. (Illustrative
      figures.)
    ask: For each line of your profile, what is the minimum acceptable value, and who agreed it?

  - number: "C.3"
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

  - number: "C.4"
    heading: Manage risk from the first sketch
    explanation: >-
      List what could harm a patient or user, how likely it is, and how severe. Then design the risk
      out, add a protection, or warn the user, in that order. ISO 14971 describes this process, and
      regulators expect to see its record.
    example: >-
      An infant warmer could overheat a baby. Design: limit the heater's power. Protection: a
      separate cut-out that switches off at a set temperature. Warning: an alarm and a label.
    ask: For each hazard you listed, which design change, protection or warning controls it?

  - number: "C.5"
    heading: Test with real users, early and often
    explanation: >-
      Many problems with devices are use errors: the design leads a tired or busy user into a
      mistake. IEC 62366-1 describes how to find and remove them. Let nurses, midwives or technicians
      try a prototype in realistic conditions, and watch without helping.
    example: >-
      Ask three midwives to set the temperature with gloved hands, in a dim room, without the manual.
      Note every hesitation and every wrong press.
    ask: Which use errors did you see in testing, and what did you change because of them?

  - number: "C.6"
    heading: Treat software as part of the device
    explanation: >-
      Software that controls a device, or that supports a diagnosis or treatment decision, is
      usually regulated as a medical device. IEC 62304 sets out how to develop and maintain it. Plan
      for updates, security and records from the start.
    example: >-
      An app that calculates a medicine dose from a child's weight is medical device software, even
      when it runs on an ordinary phone.
    ask: Which of your software's functions could harm a patient if they gave a wrong result?

  - number: "C.7"
    heading: Record design decisions as you go
    explanation: >-
      Keep a design file: the requirements, how each one was checked, and why each decision was
      made. ISO 13485 calls this design and development control. Rebuilding the file later is slow,
      and registering the device ([Guide D](to-market.html)) depends on it.
    example: >-
      For each requirement, keep one line: the requirement, the test method, the result, the date,
      and who checked it.
    ask: Could someone outside your team trace each requirement to a test result?

tables:
  stages:
    columns:
      - Stage
      - What you should have
      - Standards and tools that help
    rows:
      - - Find the need
        - A need statement, agreed with the people who give care
        - The biodesign process (identify, invent, implement)
      - - Define the product
        - A target product profile with minimum and preferred values
        - WHO target product profiles
      - - Design and prototype
        - Requirements, a risk file and a design file
        - ISO 14971, ISO 13485
      - - Test
        - Bench, usability and safety test reports
        - IEC 60601-1, IEC 62366-1, IEC 62304
      - - Prepare for market
        - The evidence and documents for registration
        - '[Guide D](to-market.html)'
---

## From idea to device

What to have at each stage. Each stage builds on the one before, and gaps found late cost the most to fix.

{% include table.html table=page.tables.stages %}

## Sources

These are the public documents behind this guide. The standards themselves are sold by ISO and IEC; their summary pages are free.

- Stanford Byers Center for Biodesign, [the biodesign process](https://biodesign.stanford.edu/about-us/process.html): identify, invent, implement.
- World Health Organization, [target product profiles](https://www.who.int/observatories/global-observatory-on-health-research-and-development/analyses-and-syntheses/target-product-profile/who-target-product-profiles): minimum and preferred characteristics.
- World Health Organization, [compendium of innovative health technologies for low-resource settings, 2024](https://www.who.int/publications/i/item/9789240095212).
- [ISO 14971:2019](https://www.iso.org/standard/72704.html), application of risk management to medical devices.
- [IEC 62366-1:2015](https://www.iso.org/standard/63179.html), application of usability engineering to medical devices.
- [IEC 62304:2006](https://www.iso.org/standard/38421.html), medical device software life cycle processes.
- [ISO 13485:2016](https://www.iso.org/standard/59752.html), quality management systems for medical devices.
