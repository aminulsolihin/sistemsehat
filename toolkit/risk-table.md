---
title: "Risk table template | SistemSehat"
description: "A printable risk table for a medical device: each hazard, the harm it could cause, and how it is controlled."
lang: en
layout: page
parent: toolkit.html
crumb: "Risk table"
heading: "Risk table"
lead: "Each hazard, the harm it could cause, and how you control it. Goes with [rule D.2](../design.html#rule-d-2). ISO 14971 describes the full process."
note: "Print this page, or copy the table into your own document."
search:
  title: "Risk table"
  text: "A printable risk table for a medical device: each hazard, the harm it could cause, and how it is controlled."
tables:
  risks:
    columns: ["No.", "Hazard", "Harm it could cause", "Likelihood (low, medium, high)", "Severity (low, medium, high)", "Control: design, protection or warning", "Checked by which test"]
    rows:
      - ["1", "", "", "", "", "", ""]
      - ["2", "", "", "", "", "", ""]
      - ["3", "", "", "", "", "", ""]
      - ["4", "", "", "", "", "", ""]
      - ["5", "", "", "", "", "", ""]
      - ["6", "", "", "", "", "", ""]
      - ["7", "", "", "", "", "", ""]
      - ["8", "", "", "", "", "", ""]
---

## How to use it

1. List every way the device could harm a patient or a user: heat, electricity, wrong readings, use errors.
2. Rate how likely and how severe each harm is.
3. Choose the control in this order: change the design, add a protection, then warn the user.
4. For each control, name the test that shows it works ([rule D.5](../design.html#rule-d-5)).
{: .steps}

## An example row

An infant warmer could overheat a baby (hazard: too much heat; harm: burns). Control by design: limit the heater's power. Protection: a separate cut-out. Warning: an alarm. Checked by: the temperature test in IEC 60601-2-21.

## The table

{% include table.html table=page.tables.risks %}
