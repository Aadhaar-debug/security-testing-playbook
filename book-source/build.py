# -*- coding: utf-8 -*-
import os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import content1, content2, content3  # noqa: registers chapters
from content1 import CHAPTERS

ORDER = ["ptes", "nist800115", "osstmm", "wstg", "apitop10", "masvs", "iottop10", "etsi303645",
         "llmtop10", "atlas", "airmf", "attack", "attackics", "iec62443",
         "csf", "cis", "cvss", "iso27001", "iso29119", "istqb"]
byid = {c["id"]: c for c in CHAPTERS}
chapters = [byid[i] for i in ORDER]
assert len(chapters) == len(CHAPTERS)

EDGE = "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"
OUT_DIR = os.path.join(HERE, "out")
os.makedirs(OUT_DIR, exist_ok=True)

CSS = open(os.path.join(HERE, "book.css")).read()

QUICKREF = [
 ("PTES","Penetration Testing","Penetration Testing Execution Standard: end-to-end pentest phases.","Overall pentest methodology and phase structure.","http://www.pentest-standard.org/"),
 ("NIST SP 800-115","Penetration Testing","Technical Guide to Information Security Testing and Assessment.","A recognised reference for planning and running security tests.","https://csrc.nist.gov/pubs/sp/800/115/final"),
 ("OSSTMM","Security Testing","Open Source Security Testing Methodology Manual.","Repeatable, metric-driven operational security testing.","https://www.isecom.org/OSSTMM.3.pdf"),
 ("OWASP WSTG","Web Apps","Web Security Testing Guide.","The reference methodology for web application testing.","https://owasp.org/www-project-web-security-testing-guide/"),
 ("OWASP API Security Top 10","APIs","Top risks specific to APIs.","Scoping and checklist for API testing.","https://owasp.org/API-Security/"),
 ("OWASP MASVS / MASTG","Mobile","Mobile App Security Verification Standard and testing guide.","Mobile app security requirements and tests.","https://mas.owasp.org/"),
 ("OWASP IoT Top 10","IoT","Top IoT security risks.","Scoping and checklist for IoT device assessments.","https://owasp.org/www-project-internet-of-things/"),
 ("ETSI EN 303 645","IoT","Cyber security for consumer IoT baseline.","Baseline security requirements for consumer IoT.","https://www.etsi.org/standards"),
 ("OWASP LLM Top 10","AI","Top risks for LLM applications.","Scoping and checklist for AI / LLM testing.","https://genai.owasp.org/"),
 ("MITRE ATLAS","AI","Adversarial Threat Landscape for AI Systems.","Adversary techniques against AI/ML, for threat modelling.","https://atlas.mitre.org/"),
 ("NIST AI RMF","AI","AI Risk Management Framework.","Governance and risk framework for AI systems.","https://www.nist.gov/itl/ai-risk-management-framework"),
 ("MITRE ATT&amp;CK (Enterprise)","IT","Adversary tactics and techniques for IT.","Threat modelling and mapping findings to detections.","https://attack.mitre.org/"),
 ("MITRE ATT&amp;CK (ICS)","OT","Adversary techniques for industrial control systems.","Threat modelling for OT/ICS assessments.","https://attack.mitre.org/techniques/ics/"),
 ("ISA/IEC 62443","OT","Security for industrial automation and control systems.","Zones/conduits model and OT security requirements.","https://www.isa.org/standards-and-publications/isa-standards"),
 ("NIST CSF 2.0","Governance","Cybersecurity Framework.","Framing findings against Govern/Identify/Protect/Detect/Respond/Recover.","https://www.nist.gov/cyberframework"),
 ("CIS Benchmarks / Controls","Hardening","Configuration benchmarks and prioritised controls.","Baseline for configuration and hardening reviews.","https://www.cisecurity.org/"),
 ("CVSS v4.0","Rating","Common Vulnerability Scoring System.","Consistent technical severity scoring of findings.","https://www.first.org/cvss/"),
 ("ISO/IEC 29119","Software Testing","International software testing standard.","Framework, processes and documentation for software testing.","https://www.iso.org/standard/81291.html"),
 ("ISTQB","Software Testing","Testing body of knowledge and glossary.","Common vocabulary and test design techniques.","https://www.istqb.org/"),
 ("ISO/IEC 27001","Governance","Information security management system.","Organisational security governance context.","https://www.iso.org/standard/27001"),
]

def marker(key):
    return f'<span class="mk">@@{key}@@</span>'

# ---------------------------------------------------------------- front matter
cover = """
<section class="cover">
  <div class="cover-band"></div>
  <div class="cover-inner">
    <div class="cover-kicker">A practitioner&rsquo;s handbook</div>
    <h1 class="cover-title">Security Standards<br>and Frameworks</h1>
    <div class="cover-sub">A detailed breakdown of twenty methodologies, standards and frameworks &mdash;
    what each one is, how it is structured, and how it is brought into practice.</div>
    <div class="cover-list">PTES &middot; NIST SP 800-115 &middot; OSSTMM &middot; OWASP WSTG &middot; OWASP API Top 10 &middot;
    OWASP MASVS/MASTG &middot; OWASP IoT Top 10 &middot; ETSI EN 303 645 &middot; OWASP LLM Top 10 &middot; MITRE ATLAS &middot;
    NIST AI RMF &middot; MITRE ATT&amp;CK Enterprise &amp; ICS &middot; ISA/IEC 62443 &middot; NIST CSF 2.0 &middot;
    CIS Benchmarks &amp; Controls &middot; CVSS v4.0 &middot; ISO/IEC 27001 &middot; ISO/IEC/IEEE 29119 &middot; ISTQB</div>
    <div class="cover-foot">Edition: November 2026</div>
  </div>
</section>
"""

intro = marker("intro") + """
<section class="chapter front" id="intro">
<div class="ch-part">Introduction</div>
<h1 class="ch-title">How to Use This Book</h1>
<p class="lead">Security work runs on shared reference points. A client asks for a "PTES-aligned" penetration test;
an auditor asks how a finding maps to ISO/IEC 27001; a SOC lead asks which ATT&amp;CK techniques the red team used; a
product team needs to know whether their smart doorbell meets ETSI EN 303 645. This book gives you a working
understanding of the twenty standards and frameworks you will meet most often, and &mdash; more importantly &mdash; how
practitioners actually apply them.</p>

<h2>Four kinds of document</h2>
<p>The documents in this book are often lumped together as "frameworks", but they do very different jobs. Knowing
which kind you are holding tells you how to use it.</p>
<table class="data"><thead><tr><th>Kind</th><th>What it gives you</th><th>Examples in this book</th></tr></thead><tbody>
<tr><td><strong>Methodology</strong></td><td>A process: the phases and activities of doing a test or assessment.</td><td>PTES, NIST SP 800-115, OSSTMM, OWASP WSTG, OWASP MASTG</td></tr>
<tr><td><strong>Risk list / taxonomy</strong></td><td>A catalogue of what goes wrong or what attackers do; used for scoping, checklists and shared vocabulary.</td><td>OWASP API, IoT and LLM Top 10s; MITRE ATT&amp;CK (Enterprise and ICS); MITRE ATLAS</td></tr>
<tr><td><strong>Requirements standard</strong></td><td>Statements a system, product or organisation must meet; often assessable or certifiable.</td><td>OWASP MASVS, ETSI EN 303 645, ISA/IEC 62443, ISO/IEC 27001, CIS Benchmarks</td></tr>
<tr><td><strong>Governance / measurement framework</strong></td><td>A structure for managing risk, measuring severity or organising a programme.</td><td>NIST CSF 2.0, NIST AI RMF, CIS Controls, CVSS v4.0, ISO/IEC/IEEE 29119, ISTQB</td></tr>
</tbody></table>

<h2>The layered model</h2>
<p>In practice these documents stack. A single security test usually touches every layer:</p>
<div class="layers">
<div class="layer l1"><b>Governance</b><span>Why we test and how results drive decisions &mdash; ISO/IEC 27001, NIST CSF 2.0, NIST AI RMF, ISA/IEC 62443-2-1</span></div>
<div class="layer l2"><b>Engagement methodology</b><span>How a test is planned, run and reported &mdash; PTES, NIST SP 800-115, OSSTMM, ISO/IEC/IEEE 29119</span></div>
<div class="layer l3"><b>Technical test guides</b><span>What to test on a given asset &mdash; WSTG, API Top 10, MASVS/MASTG, IoT Top 10, ETSI EN 303 645, LLM Top 10</span></div>
<div class="layer l4"><b>Adversary models</b><span>How real attackers behave &mdash; MITRE ATT&amp;CK Enterprise, ATT&amp;CK for ICS, ATLAS</span></div>
<div class="layer l5"><b>Baselines and ratings</b><span>What "good" looks like and how bad a finding is &mdash; CIS Benchmarks/Controls, ISA/IEC 62443-3-3, CVSS v4.0</span></div>
<div class="layer l6"><b>Testing discipline</b><span>Shared vocabulary and test design &mdash; ISTQB, ISO/IEC/IEEE 29119-4</span></div>
</div>

<h2>How each chapter is organised</h2>
<p>Every chapter opens with an <strong>at-a-glance</strong> panel (area, type, owner, whether it is mandatory, what to
use it for, and the official link). It then explains <strong>what it is</strong>, breaks down its
<strong>structure</strong> in detail, and spends most of its length on <strong>how it is brought into practice</strong>
&mdash; the concrete steps, artefacts and habits practitioners use. Part VII then pulls everything together into a
single worked engagement and a crosswalk you can reuse.</p>

<div class="callout"><strong>A note on versions.</strong> Standards evolve. This book reflects the versions current
at the time of writing (for example CVSS v4.0, NIST CSF 2.0, ISO/IEC 27001:2022, OWASP API Security Top 10 2023,
OWASP Top 10 for LLM Applications 2025, MASVS v2). Identifiers such as test IDs and technique numbers occasionally
change between releases &mdash; always cite the version you used and check the official link before relying on a
specific clause in a contract or audit.</div>
</section>
"""

# ---------------------------------------------------------------- chapters
def chapter_html(i, c):
    return marker(c["id"]) + f"""
<section class="chapter" id="{c['id']}">
<div class="ch-part">{c['part']}</div>
<div class="ch-num">Chapter {i}</div>
<h1 class="ch-title">{c['title']}</h1>
<div class="ch-sub">{c['subtitle']}</div>
{c['body']}
</section>
"""

# ---------------------------------------------------------------- synthesis
synthesis = marker("together") + """
<section class="chapter" id="together">
<div class="ch-part">Part VII &middot; Bringing It All Together</div>
<div class="ch-num">Chapter 21</div>
<h1 class="ch-title">Integrating the Frameworks</h1>
<div class="ch-sub">One engagement, every layer &mdash; and a crosswalk you can reuse</div>

<p class="lead">No single framework covers a real engagement. This chapter walks through a realistic assessment and
shows exactly where each standard is used, then gives a crosswalk table and a reporting template that link them.</p>

<h2>Scenario</h2>
<p>A mid-sized health-tech company, certified to ISO/IEC 27001, offers a patient-facing web portal, a REST API, iOS and
Android apps, a connected blood-pressure monitor, and a new LLM-powered assistant that answers questions using the
patient's records (RAG). It commissions an annual security assessment.</p>

<h2>Walkthrough</h2>
<table class="data"><thead><tr><th>Stage</th><th>What happens</th><th>Frameworks used</th></tr></thead><tbody>
<tr><td>1. Programme context</td><td>The ISMS requires annual independent testing (Annex A 5.35, 8.8, 8.29). The CISO frames objectives in CSF terms: improve ID.RA and DE.CM.</td><td>ISO/IEC 27001, NIST CSF 2.0</td></tr>
<tr><td>2. Test planning</td><td>A test plan names security as a test type, defines risks, environments, entry/exit criteria and deliverables.</td><td>ISO/IEC/IEEE 29119-2/3, NIST SP 800-115 (planning, data handling)</td></tr>
<tr><td>3. Pre-engagement</td><td>Scope, rules of engagement, authorisation letters, emergency contacts, test accounts for every role.</td><td>PTES phase 1</td></tr>
<tr><td>4. Threat modelling</td><td>Workshop identifies crown jewels (patient records), likely threat actors (financially motivated groups), and AI-specific threats.</td><td>PTES phase 3, MITRE ATT&amp;CK, MITRE ATLAS, NIST AI RMF (MAP)</td></tr>
<tr><td>5. Web portal</td><td>Checklist-driven manual testing.</td><td>OWASP WSTG</td></tr>
<tr><td>6. API</td><td>Authorisation matrix testing across roles and tenants; rate limiting; inventory of versions.</td><td>OWASP API Security Top 10, WSTG</td></tr>
<tr><td>7. Mobile apps</td><td>Static and dynamic analysis against L2 profile.</td><td>OWASP MASVS / MASTG</td></tr>
<tr><td>8. Connected device</td><td>Hardware, firmware, BLE and companion-app testing; check regulatory baseline.</td><td>OWASP IoT Top 10, ETSI EN 303 645</td></tr>
<tr><td>9. LLM assistant</td><td>Direct and indirect prompt injection, RAG permission filtering, output handling, tool agency.</td><td>OWASP LLM Top 10, MITRE ATLAS</td></tr>
<tr><td>10. Infrastructure</td><td>Cloud and server configuration review; internal attack path from a compromised laptop.</td><td>CIS Benchmarks, MITRE ATT&amp;CK</td></tr>
<tr><td>11. Rating</td><td>Each finding scored with a full vector.</td><td>CVSS v4.0 (CVSS-BT)</td></tr>
<tr><td>12. Reporting</td><td>Findings mapped to controls and functions; executive heat map by CSF function; detection gaps by ATT&amp;CK technique.</td><td>PTES phase 7, NIST CSF 2.0, ISO/IEC 27001 Annex A, CIS Controls</td></tr>
<tr><td>13. Remediation and retest</td><td>Findings enter the ISMS risk register; regression tests written; retest closes findings.</td><td>ISO/IEC 27001 clauses 6, 8, 10; ISTQB test techniques; 29119 completion report</td></tr>
</tbody></table>

<h2>A fully mapped finding</h2>
<div class="example"><div class="ex-h">Finding HT-07: Patient records accessible across accounts via API (BOLA)</div>
<table class="glance"><tbody>
<tr><th>Description</th><td>The endpoint <code>GET /api/v2/patients/{id}/readings</code> returns blood-pressure readings for any patient ID when called with a valid token for a different patient.</td></tr>
<tr><th>Test reference</th><td>OWASP API Security Top 10 2023 &mdash; API1 BOLA; OWASP WSTG v4.2 &mdash; WSTG-ATHZ-04 (IDOR)</td></tr>
<tr><th>Weakness</th><td>CWE-639 Authorization Bypass Through User-Controlled Key</td></tr>
<tr><th>Severity</th><td><code>CVSS:4.0/AV:N/AC:L/AT:N/PR:L/UI:N/VC:H/VI:N/VA:N/SC:N/SI:N/SA:N</code> &rarr; High (CVSS-B 7.1)</td></tr>
<tr><th>Adversary view</th><td>MITRE ATT&amp;CK T1190 Exploit Public-Facing Application &rarr; Collection of patient data</td></tr>
<tr><th>Control gap</th><td>ISO/IEC 27001:2022 A.8.3 Information access restriction; A.8.26/8.28 Application security requirements / secure coding</td></tr>
<tr><th>Governance view</th><td>NIST CSF 2.0 PR.AA-05 (access permissions and authorisations managed); PR.DS-01 (data-at-rest protected)</td></tr>
<tr><th>Baseline control</th><td>CIS Controls v8.1 &mdash; Control 16 Application Software Security; Control 6 Access Control Management</td></tr>
<tr><th>Remediation</th><td>Enforce object-level authorisation in a central policy layer; add a decision-table regression test (ISTQB) asserting cross-patient access returns 403; review all endpoints taking object IDs.</td></tr>
</tbody></table></div>

<h2>Crosswalk: which framework answers which question?</h2>
<table class="data"><thead><tr><th>Question</th><th>Primary reference</th><th>Supporting</th></tr></thead><tbody>
<tr><td>How do we run a pentest end-to-end?</td><td>PTES</td><td>NIST SP 800-115, OSSTMM</td></tr>
<tr><td>How do we run a security testing programme?</td><td>NIST SP 800-115</td><td>ISO/IEC/IEEE 29119, ISO/IEC 27001 (8.8, 8.29)</td></tr>
<tr><td>How do we measure security repeatably over time?</td><td>OSSTMM</td><td>NIST CSF profiles, CIS-CAT scores</td></tr>
<tr><td>What do we test in a web app?</td><td>OWASP WSTG</td><td>OWASP ASVS</td></tr>
<tr><td>What do we test in an API?</td><td>OWASP API Security Top 10</td><td>WSTG</td></tr>
<tr><td>What must a mobile app meet, and how do we verify it?</td><td>OWASP MASVS / MASTG</td><td>API Top 10 for the backend</td></tr>
<tr><td>What do we test in an IoT product?</td><td>OWASP IoT Top 10</td><td>ETSI EN 303 645 (+ TS 103 701), MASTG, API Top 10</td></tr>
<tr><td>Is our consumer IoT product compliant?</td><td>ETSI EN 303 645</td><td>UK PSTI, EU RED/EN 18031, EU CRA</td></tr>
<tr><td>What do we test in an LLM app?</td><td>OWASP LLM Top 10</td><td>MITRE ATLAS</td></tr>
<tr><td>How do we govern AI risk?</td><td>NIST AI RMF (+ AI 600-1)</td><td>ISO/IEC 42001, EU AI Act</td></tr>
<tr><td>How do attackers behave, and can we detect them?</td><td>MITRE ATT&amp;CK</td><td>ATLAS (AI), ATT&amp;CK for ICS (OT)</td></tr>
<tr><td>How do we secure an industrial site?</td><td>ISA/IEC 62443</td><td>ATT&amp;CK for ICS</td></tr>
<tr><td>How do we explain results to the board?</td><td>NIST CSF 2.0</td><td>ISO/IEC 27001</td></tr>
<tr><td>What is a secure configuration?</td><td>CIS Benchmarks</td><td>CIS Controls (4), ISO/IEC 27001 A.8.9</td></tr>
<tr><td>How severe is this finding?</td><td>CVSS v4.0</td><td>EPSS, CISA KEV, SSVC</td></tr>
<tr><td>How do we formalise testing processes and documents?</td><td>ISO/IEC/IEEE 29119</td><td>ISTQB</td></tr>
<tr><td>How do we design good test cases and share vocabulary?</td><td>ISTQB</td><td>ISO/IEC/IEEE 29119-4</td></tr>
<tr><td>How do we run security as a certifiable management system?</td><td>ISO/IEC 27001</td><td>NIST CSF 2.0, CIS Controls</td></tr>
</tbody></table>

<h2>Recommended report fields</h2>
<p>A finding template that carries the mappings above makes a single report useful to engineers, the SOC, the ISMS
manager and the board at once:</p>
<ul class="cols2">
<li>ID and title</li><li>Affected asset(s)</li><li>Description and evidence</li><li>Reproduction steps</li>
<li>Test reference (WSTG / MASTG / API / LLM / IoT ID)</li><li>Weakness (CWE)</li>
<li>CVSS v4.0 vector, score and nomenclature</li><li>Business risk rating (with method)</li>
<li>ATT&amp;CK / ATLAS / ICS technique(s)</li><li>Detection opportunity</li>
<li>Control mapping (ISO 27001 Annex A, CIS Control, 62443 SR)</li><li>CSF 2.0 subcategory</li>
<li>Remediation and owner</li><li>Retest status and date</li>
</ul>

<h2>A maturity roadmap for adopting the frameworks</h2>
<table class="data"><thead><tr><th>Stage</th><th>Focus</th><th>Adopt</th></tr></thead><tbody>
<tr><td>1. Foundations</td><td>Know your assets, harden them, fix the obvious.</td><td>CIS Controls IG1, CIS Benchmarks Level 1, CVSS for prioritisation, annual PTES-style pentest.</td></tr>
<tr><td>2. Structured testing</td><td>Asset-specific testing in the SDLC.</td><td>WSTG, API Top 10, MASVS/MASTG, IoT/LLM Top 10 as relevant; ISTQB skills; security in test plans.</td></tr>
<tr><td>3. Threat-informed</td><td>Test and detect what real adversaries do.</td><td>MITRE ATT&amp;CK (and ATLAS/ICS), purple teaming, detection coverage metrics.</td></tr>
<tr><td>4. Governed</td><td>Board-level risk management and certification.</td><td>NIST CSF 2.0 profiles, ISO/IEC 27001 certification, NIST AI RMF, ISA/IEC 62443 for OT, ISO/IEC/IEEE 29119 for audited test processes.</td></tr>
<tr><td>5. Measured and adaptive</td><td>Continuous improvement driven by metrics.</td><td>OSSTMM-style repeatable measurement, CSF Tier 3&ndash;4, CVSS-BTE with threat intelligence, regular profile reassessment.</td></tr>
</tbody></table>
</section>
"""

# ---------------------------------------------------------------- appendices
qr_rows = "".join(
    f"<tr><td><strong>{n}</strong></td><td>{a}</td><td>{w}</td><td>{u}</td><td class='url'>{l}</td></tr>"
    for n, a, w, u, l in QUICKREF)
appendix_a = marker("appA") + f"""
<section class="chapter" id="appA">
<div class="ch-part">Appendices</div>
<div class="ch-num">Appendix A</div>
<h1 class="ch-title">Quick Reference</h1>
<div class="ch-sub">All twenty standards and frameworks at a glance</div>
<table class="data qr"><thead><tr><th>Standard / Framework</th><th>Area</th><th>What it is</th><th>Use it for</th><th>Link</th></tr></thead>
<tbody>{qr_rows}</tbody></table>
</section>
"""

GLOSS = [
 ("ASVS", "OWASP Application Security Verification Standard: verifiable security requirements for web apps at three levels."),
 ("Attack path", "A sequence of steps (often mapped to ATT&amp;CK techniques) by which an attacker reaches an objective."),
 ("BOLA / IDOR", "Broken Object Level Authorization / Insecure Direct Object Reference: accessing another user's object by changing its identifier."),
 ("Conduit", "ISA/IEC 62443: a logical grouping of communication channels connecting two or more zones."),
 ("CWE", "Common Weakness Enumeration: MITRE's catalogue of software and hardware weakness types."),
 ("EPSS", "Exploit Prediction Scoring System (FIRST): the probability a vulnerability will be exploited in the next 30 days."),
 ("Indirect prompt injection", "Instructions hidden in content an LLM reads (documents, web pages, emails) that alter its behaviour."),
 ("ISMS", "Information Security Management System: the management system defined by ISO/IEC 27001."),
 ("KEV", "CISA Known Exploited Vulnerabilities catalogue."),
 ("Porosity", "OSSTMM: the openings (visibility, access, trust) between an asset and threats."),
 ("Profile", "NIST CSF / AI RMF: a description of current or target outcomes tailored to an organisation, sector or use case."),
 ("Purdue model", "Reference architecture dividing industrial networks into levels from field devices (0) to enterprise (4&ndash;5)."),
 ("RAG", "Retrieval-Augmented Generation: supplying an LLM with retrieved documents as context for its answer."),
 ("rav", "OSSTMM risk assessment value: a quantitative measure of attack surface."),
 ("Rules of Engagement (RoE)", "The document defining what testers may and may not do during an engagement."),
 ("SBOM", "Software Bill of Materials: an inventory of software components in a product."),
 ("Security Level (SL)", "ISA/IEC 62443 measure (0&ndash;4) of protection against increasingly capable attackers; SL-T, SL-C, SL-A."),
 ("SoA", "Statement of Applicability: the ISO/IEC 27001 document listing Annex A controls, their applicability and status."),
 ("SSVC", "Stakeholder-Specific Vulnerability Categorization: a decision-tree method for prioritising vulnerability response."),
 ("STAR", "OSSTMM Security Test Audit Report."),
 ("Tactic / Technique", "ATT&amp;CK/ATLAS: the adversary's goal (tactic) and the means of achieving it (technique)."),
 ("Test basis", "ISTQB: the body of knowledge (requirements, specs, code) used as the basis for test analysis and design."),
 ("Test oracle", "ISTQB: a source used to determine the expected results of a test."),
 ("Zone", "ISA/IEC 62443: a grouping of logical or physical assets that share common security requirements."),
]
appendix_b = marker("appB") + """
<section class="chapter" id="appB">
<div class="ch-num">Appendix B</div>
<h1 class="ch-title">Glossary</h1>
<dl class="gloss">""" + "".join(f"<dt>{t}</dt><dd>{d}</dd>" for t, d in GLOSS) + """</dl>
</section>
"""

# ---------------------------------------------------------------- TOC
def toc_html(pages):
    def p(k): return str(pages.get(k, "")) if pages else ""
    rows = [f'<div class="toc-row front"><a href="#intro">How to Use This Book</a><span class="dots"></span><span class="pg">{p("intro")}</span></div>']
    last_part = None
    for i, c in enumerate(chapters, 1):
        if c["part"] != last_part:
            rows.append(f'<div class="toc-part">{c["part"]}</div>')
            last_part = c["part"]
        rows.append(f'<div class="toc-row"><span class="n">{i}</span><a href="#{c["id"]}">{c["title"]}</a><span class="dots"></span><span class="pg">{p(c["id"])}</span></div>')
    rows.append('<div class="toc-part">Part VII &middot; Bringing It All Together</div>')
    rows.append(f'<div class="toc-row"><span class="n">21</span><a href="#together">Integrating the Frameworks</a><span class="dots"></span><span class="pg">{p("together")}</span></div>')
    rows.append('<div class="toc-part">Appendices</div>')
    rows.append(f'<div class="toc-row"><span class="n">A</span><a href="#appA">Quick Reference</a><span class="dots"></span><span class="pg">{p("appA")}</span></div>')
    rows.append(f'<div class="toc-row"><span class="n">B</span><a href="#appB">Glossary</a><span class="dots"></span><span class="pg">{p("appB")}</span></div>')
    return '<section class="toc"><h1 class="ch-title">Contents</h1>' + "".join(rows) + "</section>"

def build_html(pages, markers=True):
    body = cover + toc_html(pages) + intro
    body += "".join(chapter_html(i, c) for i, c in enumerate(chapters, 1))
    body += synthesis + appendix_a + appendix_b
    body = re.sub(r'(<span class="mk">@@\w+@@</span>)\s*(<section[^>]*>)', r'\2\1', body)
    if not markers:
        body = re.sub(r'<span class="mk">@@\w+@@</span>', '', body)
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<title>Security Standards and Frameworks</title><style>{CSS}</style></head><body>{body}</body></html>"""

def render(html, pdf):
    hp = os.path.join(OUT_DIR, "book.html")
    open(hp, "w").write(html)
    subprocess.run([EDGE, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    "--generate-pdf-document-outline", f"--print-to-pdf={pdf}",
                    "file://" + hp], check=True, capture_output=True, timeout=180)

def find_pages(pdf):
    from pypdf import PdfReader
    r = PdfReader(pdf)
    pages = {}
    for idx, pg in enumerate(r.pages, 1):
        for k in re.findall(r"@@(\w+)@@", pg.extract_text() or ""):
            pages.setdefault(k, idx)
    return pages, len(r.pages)

if __name__ == "__main__":
    tmp = os.path.join(OUT_DIR, "pass1.pdf")
    # Pass 1 with placeholder page numbers of same width
    render(build_html({k: "00" for k in ["intro","together","appA","appB"] + ORDER}), tmp)
    pages, n = find_pages(tmp)
    print("pages:", n, pages)
    final = os.path.join(OUT_DIR, "Security_Standards_and_Frameworks.pdf")
    chk = os.path.join(OUT_DIR, "pass2.pdf")
    render(build_html(pages), chk)
    pages2, n2 = find_pages(chk)
    assert pages2 == pages, (pages, pages2)
    render(build_html(pages, markers=False), final)
    print("final ok", n2)
