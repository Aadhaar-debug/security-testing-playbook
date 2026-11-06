# Security Testing Playbook

An industry-grade, standards-based **penetration-testing and software-testing playbook**, delivered as an Excel workbook.

**Files:**
- `Penetration_Testing_and_Software_Testing_Playbook.xlsx` — the working playbook (checklists, register, dashboard)
- `Security_Standards_and_Frameworks.pdf` — a 69-page companion handbook explaining each referenced standard and how it is brought into practice

> ⚠️ **Authorization first.** Penetration testing is performed **only** against systems you own or have explicit, written, signed authorization to test, and only within the agreed scope, window and Rules of Engagement. Every pentest checklist opens with **Authorization Gate** items that must be completed before any active testing. This workbook is a governance and checklist tool — it deliberately contains **no exploit code, payloads or attack instructions.**

## What's inside (15 tabs)

| Area | Tabs |
|------|------|
| Guidance | **README**, **Dashboard** (live roll-up of every assessment), **Assessment Register** (one row per engagement, with sign-offs) |
| Pentest method | **Pentest Methodology** (8 phases, PTES / NIST SP 800-115), **Rules of Engagement** (authorization checklist, RoE, comms templates) |
| Pentest checklists | **IT & Network**, **OT & ICS**, **IoT & Embedded**, **AI & ML Systems**, plus a generic **Pentest Template** to copy |
| Software testing | **Software Test Methodology** (8 phases, ISO/IEC 29119 / ISTQB), **Test Types & Techniques** (unit, integration, E2E, white/black/grey box, performance, security, UAT, the test pyramid) |
| Reference | **Standards & Frameworks**, **Severity & Risk** (CVSS v4.0 bands, risk matrix, remediation SLAs), **Reporting & Retest** |

## How to use it

1. Copy the matching domain tab (or `Pentest Template`), rename it for the engagement, and type the name into cell **C3**.
2. Add a row to the **Assessment Register** with the same name in column A.
3. Complete every **Authorization Gate** item first — the tab shows *Not Authorised* until they are done.
4. Work the 8 phases, setting Status, owner, completion date and an evidence link per item.
5. Rate findings on **Severity & Risk**, write them up via **Reporting & Retest**, retest, and collect the four sign-offs in the Register.

The **Dashboard** rolls up every tab automatically: phase progress, open blockers, authorization state and a single status (Not Authorised → In Progress → Needs Evidence → Ready for Sign-off → Signed Off).

## Standards referenced

PTES · NIST SP 800-115 · OSSTMM · OWASP WSTG / API / MASVS / IoT / LLM Top 10 · MITRE ATT&CK (Enterprise & ICS) · MITRE ATLAS · ISA/IEC 62443 · ETSI EN 303 645 · NIST AI RMF · NIST CSF 2.0 · CIS Benchmarks · CVSS v4.0 · ISO/IEC 29119 · ISTQB · ISO/IEC 27001

## Companion handbook (PDF)

`Security_Standards_and_Frameworks.pdf` gives a detailed breakdown of all 20 standards and frameworks the playbook references. Each chapter covers what the standard is, its structure, and how practitioners apply it. A final chapter walks through one engagement end to end, with a crosswalk table and a finding mapped to every framework. Appendices hold a quick-reference table and a glossary.

The HTML/CSS source and build script are in `book-source/`. To rebuild, run `python3 book-source/build.py` (it prints to PDF with headless Microsoft Edge and uses `pypdf` for the contents page numbers).

## Notes

- Severity bands, remediation SLAs and the review cycle are **proposed defaults** — align them with your own security and release policy.
- Role names are generic placeholders; replace them with your team's.
- Standards links were current as of 2026-11-06; confirm the live version before relying on a specific control.
