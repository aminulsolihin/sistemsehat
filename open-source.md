---
title: How do we use open-source technology? Open source guide | SistemSehat
description: >-
  Seven rules, with examples, for using and sharing open-source medical hardware and software: licences, approval, evidence and patient data.
lang: en
layout: guide
pillar: build
reviewed: 14 October 2026
order: 8
number: "E"
label: Open source
question: How do we use and share open-source technology?
summary: >-
  Open designs and software can save years of work, but open does not mean approved or safe. Seven
  rules for using and sharing them.
icon: share
lead: >-
  Open-source hardware and software let anyone study, use, change and share a design. In health
  care, that freedom comes with the same duties as any other device: evidence, quality, and someone
  responsible for it.

rules:
  - number: "E.1"
    heading: Read the licence before you use anything
    explanation: >-
      The licence says what you may do with a design or with code. Permissive licences, such as MIT
      or BSD, let you reuse it almost freely. Reciprocal licences, such as GNU GPL or CERN-OHL-S,
      require you to share your changes under the same licence.
    example: >-
      SIMRS Khanza is free to use, but its licence forbids selling it. The Open Source Initiative
      does not count a licence with that restriction as open source.
    ask: What does the licence require if you change the design and then distribute it?

  - number: "E.2"
    heading: An open design is not an approved device
    explanation: >-
      Regulators approve a device made by a responsible manufacturer, not a design file. Whoever
      makes and supplies a device in Indonesia needs a marketing authorisation (*izin edar*), as for
      any other device. Being free or open changes none of the steps in [Guide D](to-market.html).
    example: >-
      The OpenFlexure project states that its microscope is not certified as a medical device. It
      also notes that certification is issued to a manufacturer, not to a design.
    ask: Who will be the manufacturer of record for the device you build from this design?

  - number: "E.3"
    heading: Check the evidence, not the enthusiasm
    explanation: >-
      Open projects are often well known before they are well tested. A 2020 review of open-source
      ventilators found that tested designs lacked full documentation, and documented designs were
      only basically tested, if at all. Ask for test reports and published evaluations, as for any
      device.
    example: >-
      Before adapting an open ventilator design, look for a test report against the ventilator
      standards, not only videos of it working.
    ask: Who tested this design, against which standard, and where are the results?

  - number: "E.4"
    heading: Check that the project is alive
    explanation: >-
      Hardware and software need fixes long after their first release. Look at when the last version
      came out, how many people maintain it, and how security problems are reported and fixed. A
      project with one maintainer can stop at any time.
    example: >-
      You plan to install an open image server in a hospital. First check the date of its last
      release, and whether security fixes were published in the past year.
    ask: If a serious fault were found tomorrow, who would fix it, and how would you hear about it?

  - number: "E.5"
    heading: Check that you can build it from the documents
    explanation: >-
      A design is only open in practice if someone else can make it. Look for the design files, the
      list of parts, assembly and calibration instructions, and the source code of any firmware.
      Missing pieces usually mean you still depend on the original team.
    example: >-
      Before you commit to a design, try to order every part on its list from suppliers in
      Indonesia.
    ask: Could a technician on your team build, calibrate and repair one unit using only the published documents?

  - number: "E.6"
    heading: Protect patient data
    explanation: >-
      Software that stores patient data must meet the Personal Data Protection Law (Law 27 of 2022),
      which treats health data as sensitive. Health facilities must also keep electronic medical
      records that connect to the Ministry of Health's SATUSEHAT platform. Check both before you
      choose open software for patient records.
    example: >-
      Before using an open medical record system, check that it controls who can see each record,
      logs every access, and can exchange data with SATUSEHAT.
    ask: Who can see patient data in this system, and can you show a record of who did?

  - number: "E.7"
    heading: Choose a licence when you share your own work
    explanation: >-
      If you publish a design, choose its licence deliberately. For hardware, CERN-OHL version 2 has
      strongly reciprocal, weakly reciprocal and permissive variants. For software, the main choice
      is between reciprocal licences such as GNU GPL and permissive ones such as MIT or Apache 2.0.
    example: >-
      A team that wants companies to share their improvements to its warmer design chooses
      CERN-OHL-S. A team that wants the widest possible use chooses CERN-OHL-P.
    ask: What do you want others to be able to do with your design, and does your licence say so?

tables:
  licences:
    columns:
      - Licence
      - Type
      - If you distribute a changed version
      - Often used for
    rows:
      - - MIT, BSD, Apache 2.0
        - Permissive
        - Keep the original notice. You may use any licence for your version.
        - Software
      - - Mozilla Public License 2.0
        - Weakly reciprocal
        - Share the changed files under the same licence. New files can use other terms.
        - Software
      - - GNU GPL version 3
        - Strongly reciprocal
        - Share the source code of the whole work under the GPL.
        - Software
      - - CERN-OHL-P version 2
        - Permissive
        - Keep the original notice. You may use any licence for your version.
        - Hardware
      - - CERN-OHL-W version 2
        - Weakly reciprocal
        - Share changes to the licensed design. Parts you add can stay under other terms.
        - Hardware
      - - CERN-OHL-S version 2
        - Strongly reciprocal
        - Share the whole changed design under the same licence.
        - Hardware
      - - Creative Commons Attribution (CC BY)
        - Permissive
        - Credit the original author.
        - Documentation and images
---

## Common licences

What each licence asks of you when you distribute a changed version. This is a summary: read the licence itself before you rely on it.

{% include table.html table=page.tables.licences %}

## Examples

The [Innovation](innovation.html#hardware) page lists open-source medical hardware and software, with the licence each one uses and what its own documents say about medical use.

## Sources

- CERN, [CERN Open Hardware Licence version 2](https://ohwr.org/project/cernohl/wikis/Documents/CERN-OHL-version-2), with its three variants.
- Open Source Initiative, [the Open Source Definition and approved licences](https://opensource.org/licenses).
- Open Source Hardware Association, [open source hardware certification](https://certification.oshwa.org/).
- Joshua M. Pearce, [a review of open source ventilators for COVID-19 and future pandemics](https://f1000research.com/articles/9-218/v2), F1000Research, 2020.
- OpenFlexure, [medical devices](https://openflexure.org/about/medical-devices): what an open design can and cannot claim.
- [Law 27 of 2022 on personal data protection](https://peraturan.bpk.go.id/Details/229798).
- [Minister of Health Regulation 24 of 2022 on medical records](https://peraturan.bpk.go.id/Details/245544).
