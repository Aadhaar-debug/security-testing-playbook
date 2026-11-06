# -*- coding: utf-8 -*-
# Chapter content, part 3: governance, hardening, rating, software testing.
from content1 import ch, glance

ch("Part V &middot; Governance, Hardening and Risk Rating", "csf",
   "NIST CSF 2.0", "The NIST Cybersecurity Framework, version 2.0",
glance([
 ("Area", "Governance and cybersecurity risk management"),
 ("Type", "Voluntary outcome-based framework"),
 ("Published by", "NIST; v1.0 2014, v1.1 2018, v2.0 February 2024"),
 ("Mandatory?", "Voluntary for most organisations, but referenced by US regulators, insurers and boards worldwide"),
 ("Use it for", "Framing findings against Govern / Identify / Protect / Detect / Respond / Recover"),
 ("Link", '<a href="https://www.nist.gov/cyberframework">nist.gov/cyberframework</a>'),
]) + """
<h2>What it is</h2>
<p>The CSF is a taxonomy of high-level cybersecurity <em>outcomes</em> that any organisation, of any size or sector,
can use to understand, assess, prioritise and communicate its cybersecurity efforts. It does not tell you how to
achieve outcomes; it points to other standards (informative references) for that. Version 2.0 expanded the scope beyond
critical infrastructure to all organisations and added a sixth function, <strong>Govern</strong>, putting governance at
the centre.</p>

<h2>The CSF Core: functions, categories, subcategories</h2>
<p>The Core has 6 functions, 22 categories and 106 subcategories.</p>
<table class="data"><thead><tr><th>Function</th><th>Categories</th></tr></thead><tbody>
<tr><td><strong>GOVERN (GV)</strong><br>Strategy, expectations and policy are established, communicated and monitored.</td><td>GV.OC Organizational Context; GV.RM Risk Management Strategy; GV.RR Roles, Responsibilities and Authorities; GV.PO Policy; GV.OV Oversight; GV.SC Cybersecurity Supply Chain Risk Management</td></tr>
<tr><td><strong>IDENTIFY (ID)</strong><br>Current cybersecurity risks are understood.</td><td>ID.AM Asset Management; ID.RA Risk Assessment; ID.IM Improvement</td></tr>
<tr><td><strong>PROTECT (PR)</strong><br>Safeguards to manage risks are used.</td><td>PR.AA Identity Management, Authentication and Access Control; PR.AT Awareness and Training; PR.DS Data Security; PR.PS Platform Security; PR.IR Technology Infrastructure Resilience</td></tr>
<tr><td><strong>DETECT (DE)</strong><br>Possible attacks and compromises are found and analysed.</td><td>DE.CM Continuous Monitoring; DE.AE Adverse Event Analysis</td></tr>
<tr><td><strong>RESPOND (RS)</strong><br>Actions regarding a detected incident are taken.</td><td>RS.MA Incident Management; RS.AN Incident Analysis; RS.CO Incident Response Reporting and Communication; RS.MI Incident Mitigation</td></tr>
<tr><td><strong>RECOVER (RC)</strong><br>Affected assets and operations are restored.</td><td>RC.RP Incident Recovery Plan Execution; RC.CO Incident Recovery Communication</td></tr>
</tbody></table>
<p>Subcategories are specific outcome statements, for example <code>PR.AA-01</code>: identities and credentials for
authorised users, services and hardware are managed by the organisation; <code>ID.RA-01</code>: vulnerabilities in
assets are identified, validated and recorded.</p>

<h2>Profiles and tiers</h2>
<ul>
<li><strong>Organizational Profiles</strong> describe a <em>Current Profile</em> (outcomes achieved today) and a <em>Target Profile</em> (outcomes desired). The gap between them drives an action plan. <strong>Community Profiles</strong> provide sector baselines.</li>
<li><strong>Tiers</strong> characterise the rigour of risk governance and management practices: Tier 1 Partial, Tier 2 Risk Informed, Tier 3 Repeatable, Tier 4 Adaptive. Tiers are not a maturity model to "max out"; organisations choose the tier appropriate to their risk.</li>
</ul>
<p>NIST supports the Core with online resources: <strong>Implementation Examples</strong> for each subcategory,
<strong>Informative References</strong> (mappings to SP 800-53, ISO/IEC 27001, CIS Controls and more), and
<strong>Quick-Start Guides</strong> for small businesses, enterprise risk management and supply chain.</p>

<h2>How it is brought into practice</h2>
<h3>Building a programme with CSF</h3>
<ol>
<li><strong>Scope</strong>: whole organisation or a business unit / system.</li>
<li><strong>Gather information</strong>: policies, risk registers, previous audits, pentest reports.</li>
<li><strong>Create the Current Profile</strong>: assess each subcategory (e.g. on a 0&ndash;5 scale, or Not/Partially/Largely/Fully achieved) with evidence.</li>
<li><strong>Create the Target Profile</strong> driven by risk appetite, regulation and threat landscape.</li>
<li><strong>Gap analysis and action plan</strong>: prioritise, cost and assign owners.</li>
<li><strong>Implement and repeat</strong>: re-assess annually; report progress to the board using the six functions as the storyline.</li>
</ol>
<h3>Framing technical findings with CSF</h3>
<p>Security testers use CSF to translate technical findings into governance language. Each finding (or root cause)
is mapped to the subcategory it shows is not being achieved:</p>
<table class="data"><thead><tr><th>Finding</th><th>CSF subcategory</th></tr></thead><tbody>
<tr><td>Unpatched internet-facing server with known exploitable CVE</td><td>ID.RA-01 (vulnerabilities identified) and PR.PS-02 (software maintained)</td></tr>
<tr><td>No MFA on VPN</td><td>PR.AA-03 (users, services and hardware are authenticated)</td></tr>
<tr><td>Red team activity not detected for 5 days</td><td>DE.CM-01 (networks monitored) and DE.AE-02 (adverse events analysed)</td></tr>
<tr><td>Backups reachable and deletable from domain admin account</td><td>PR.DS-11 (backups created, protected, maintained and tested)</td></tr>
<tr><td>Unknown shadow cloud tenant discovered</td><td>ID.AM-02 (inventories of software, services and systems)</td></tr>
</tbody></table>
<p>Summed across a report, this produces a function-level heat map ("most findings are in PROTECT and DETECT") that
executives can act on.</p>
""")

# --------------------------------------------------------------------------
ch("Part V &middot; Governance, Hardening and Risk Rating", "cis",
   "CIS Benchmarks and CIS Controls", "Configuration baselines and prioritised security safeguards",
glance([
 ("Area", "Hardening and baseline security controls"),
 ("Type", "Consensus configuration benchmarks + prioritised control set"),
 ("Maintained by", "Center for Internet Security (CIS), a non-profit; Controls v8.1 (2024)"),
 ("Mandatory?", "Voluntary, but referenced by PCI DSS, cyber insurance questionnaires, regulators and many contracts as an acceptable hardening standard"),
 ("Use it for", "Baseline for configuration and hardening reviews"),
 ("Link", '<a href="https://www.cisecurity.org/">cisecurity.org</a>'),
]) + """
<h2>What they are</h2>
<p>CIS publishes two closely related but distinct resources:</p>
<ul>
<li><strong>CIS Benchmarks</strong>: detailed, prescriptive configuration guides for specific technologies &mdash; over 100 products, including Windows, Linux distributions, macOS, cloud platforms (AWS, Azure, GCP), Kubernetes, Docker, databases, browsers, network devices and Microsoft 365. Each recommendation states the setting, rationale, audit procedure and remediation.</li>
<li><strong>CIS Critical Security Controls</strong> (CIS Controls): a prioritised set of 18 controls containing safeguards that defend against the most common attacks. They answer "what should we do first?".</li>
</ul>

<h2>CIS Controls v8.1</h2>
<table class="data"><thead><tr><th>#</th><th>Control</th><th>#</th><th>Control</th></tr></thead><tbody>
<tr><td>1</td><td>Inventory and Control of Enterprise Assets</td><td>10</td><td>Malware Defenses</td></tr>
<tr><td>2</td><td>Inventory and Control of Software Assets</td><td>11</td><td>Data Recovery</td></tr>
<tr><td>3</td><td>Data Protection</td><td>12</td><td>Network Infrastructure Management</td></tr>
<tr><td>4</td><td>Secure Configuration of Enterprise Assets and Software</td><td>13</td><td>Network Monitoring and Defense</td></tr>
<tr><td>5</td><td>Account Management</td><td>14</td><td>Security Awareness and Skills Training</td></tr>
<tr><td>6</td><td>Access Control Management</td><td>15</td><td>Service Provider Management</td></tr>
<tr><td>7</td><td>Continuous Vulnerability Management</td><td>16</td><td>Application Software Security</td></tr>
<tr><td>8</td><td>Audit Log Management</td><td>17</td><td>Incident Response Management</td></tr>
<tr><td>9</td><td>Email and Web Browser Protections</td><td>18</td><td>Penetration Testing</td></tr>
</tbody></table>
<p>The controls contain 153 safeguards, each tagged to an <strong>Implementation Group</strong>:</p>
<ul>
<li><strong>IG1</strong> &mdash; "essential cyber hygiene": the minimum for every organisation (56 safeguards); typically small organisations with limited IT expertise.</li>
<li><strong>IG2</strong> &mdash; adds safeguards for organisations with multiple departments and sensitive data.</li>
<li><strong>IG3</strong> &mdash; all safeguards, for organisations facing sophisticated attacks or with significant regulatory exposure.</li>
</ul>
<p>Version 8.1 also aligned the safeguards with NIST CSF 2.0 security functions, including a Govern function.</p>

<h2>Benchmark profiles</h2>
<ul>
<li><strong>Level 1</strong>: practical, prudent settings that provide clear security benefit with minimal impact on functionality.</li>
<li><strong>Level 2</strong>: defence in depth for high-security environments; may reduce functionality or performance.</li>
<li>Some benchmarks also offer a <strong>STIG</strong> profile aligned with US DoD requirements, and BitLocker or Next Generation Windows Security profiles.</li>
</ul>

<h2>How they are brought into practice</h2>
<h3>Hardening programme with Benchmarks</h3>
<ol>
<li><strong>Select the benchmark and profile</strong> for each platform (e.g. "CIS Microsoft Windows Server 2022 Benchmark, Level 1 &mdash; Member Server").</li>
<li><strong>Tailor</strong>: test the baseline in a lab, document exceptions with business justification and compensating controls.</li>
<li><strong>Codify</strong>: implement via Group Policy, Intune, Ansible, Chef, Terraform policy, or start from CIS Hardened Images in the cloud.</li>
<li><strong>Measure</strong>: scan compliance using CIS-CAT Pro or benchmark-aligned policies in vulnerability scanners, cloud security posture management (CSPM) and Kubernetes tools.</li>
<li><strong>Monitor drift</strong> and remediate continuously.</li>
</ol>
<h3>Configuration reviews in security testing</h3>
<p>In a build/configuration review, testers run benchmark audits and report the compliance percentage, the failed
recommendations that matter most, and the risk of each. Good reviews do not just paste hundreds of failed checks; they
group them into themes (e.g. "legacy authentication protocols enabled", "insufficient audit logging") and prioritise.</p>
<h3>Security programme with Controls</h3>
<ul>
<li>Perform a CIS Controls self-assessment (CIS provides the free CIS Controls Self Assessment Tool, CSAT).</li>
<li>Achieve IG1 first, then progress to IG2/IG3 based on risk.</li>
<li>Use CIS mappings to other frameworks (NIST CSF, ISO/IEC 27001, PCI DSS) so one assessment serves several compliance needs.</li>
<li>Use the CIS Community Defense Model, which maps safeguards to ATT&amp;CK techniques, to show how each safeguard reduces exposure to common attack types (ransomware, web app hacking, insider misuse).</li>
</ul>
""")

# --------------------------------------------------------------------------
ch("Part V &middot; Governance, Hardening and Risk Rating", "cvss",
   "CVSS v4.0", "Common Vulnerability Scoring System, version 4.0",
glance([
 ("Area", "Vulnerability severity rating"),
 ("Type", "Open scoring standard"),
 ("Maintained by", "FIRST (Forum of Incident Response and Security Teams); v4.0 published November 2023"),
 ("Mandatory?", "De facto standard; used by NVD, CNAs and vendors for CVE scoring and by PCI DSS and many policies for remediation SLAs"),
 ("Use it for", "Consistent technical severity scoring of findings"),
 ("Link", '<a href="https://www.first.org/cvss/">first.org/cvss</a>'),
]) + """
<h2>What it is</h2>
<p>CVSS captures the principal characteristics of a vulnerability and produces a numerical score from 0.0 to 10.0
reflecting its <strong>severity</strong>, plus a textual <strong>vector string</strong> recording exactly how the score
was derived. It provides a shared, reproducible language: two analysts scoring the same vulnerability with the same
information should arrive at the same vector.</p>
<p>A key point FIRST emphasises in v4.0: <strong>CVSS measures severity, not risk</strong>. Risk also depends on the
likelihood of exploitation and the business value of the affected asset, which the Base score alone does not capture.</p>

<h2>Metric groups</h2>
<table class="data"><thead><tr><th>Group</th><th>Metrics</th><th>Set by</th></tr></thead><tbody>
<tr><td><strong>Base</strong> &mdash; Exploitability</td><td>Attack Vector (AV: Network, Adjacent, Local, Physical); Attack Complexity (AC: Low, High); <em>Attack Requirements</em> (AT: None, Present) &mdash; new in v4; Privileges Required (PR: None, Low, High); User Interaction (UI: None, Passive, Active)</td><td>Vendor / analyst</td></tr>
<tr><td><strong>Base</strong> &mdash; Impact</td><td>Vulnerable System Confidentiality, Integrity, Availability (VC/VI/VA); Subsequent System Confidentiality, Integrity, Availability (SC/SI/SA). Each High, Low or None.</td><td>Vendor / analyst</td></tr>
<tr><td><strong>Threat</strong></td><td>Exploit Maturity (E: Attacked, Proof-of-Concept, Unreported)</td><td>Consumer, using threat intelligence</td></tr>
<tr><td><strong>Environmental</strong></td><td>Confidentiality/Integrity/Availability Requirements (CR/IR/AR) and Modified Base metrics</td><td>Consumer (asset owner)</td></tr>
<tr><td><strong>Supplemental</strong></td><td>Safety (S), Automatable (AU), Recovery (R), Value Density (V), Vulnerability Response Effort (RE), Provider Urgency (U). These do <em>not</em> change the score but add context.</td><td>Vendor / consumer</td></tr>
</tbody></table>

<h2>What changed from v3.1</h2>
<ul>
<li>The confusing <strong>Scope</strong> metric was removed and replaced by separate impact metrics for the vulnerable system and subsequent systems.</li>
<li><strong>Attack Requirements</strong> (AT) separates "conditions the attacker cannot control" (e.g. a race condition, specific deployment configuration) from Attack Complexity.</li>
<li><strong>User Interaction</strong> gained granularity (Passive vs. Active).</li>
<li>Temporal metrics were simplified into the <strong>Threat</strong> group, with only Exploit Maturity.</li>
<li>Scores are computed from <strong>equivalence classes (macrovectors)</strong> derived from expert ranking, rather than a single formula; use FIRST's calculator or a reference library.</li>
<li>New nomenclature makes it explicit which groups were used: <strong>CVSS-B</strong> (Base), <strong>CVSS-BT</strong> (Base + Threat), <strong>CVSS-BE</strong> (Base + Environmental), <strong>CVSS-BTE</strong> (all).</li>
</ul>

<h2>Qualitative severity scale</h2>
<table class="data"><thead><tr><th>Rating</th><th>Score</th></tr></thead><tbody>
<tr><td>None</td><td>0.0</td></tr><tr><td>Low</td><td>0.1 &ndash; 3.9</td></tr><tr><td>Medium</td><td>4.0 &ndash; 6.9</td></tr><tr><td>High</td><td>7.0 &ndash; 8.9</td></tr><tr><td>Critical</td><td>9.0 &ndash; 10.0</td></tr>
</tbody></table>

<div class="example"><div class="ex-h">Worked example: unauthenticated SQL injection in a public web app</div>
<p>Network-reachable (AV:N), no special conditions (AC:L, AT:N), no login (PR:N), no user interaction (UI:N), full read
and write of the database and potential service disruption on the vulnerable system (VC:H/VI:H/VA:H), no direct impact
on other systems (SC:N/SI:N/SA:N).</p>
<p><code>CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N</code> &rarr; <strong>9.3 Critical (CVSS-B)</strong></p>
<p>If the tester also knows a public exploit is being used in the wild, add <code>E:A</code> (CVSS-BT). If the asset
owner states that the database holds only public marketing content, Environmental requirements (e.g. <code>CR:L</code>)
can lower the CVSS-BTE score for that organisation.</p></div>

<h2>How it is brought into practice</h2>
<h3>In penetration test reports</h3>
<ul>
<li>Provide the <strong>full vector string</strong> for every finding, not just a number &mdash; it makes the rating auditable and lets clients rescore.</li>
<li>State which nomenclature you used (usually CVSS-B or CVSS-BT from a tester; the client adds Environmental).</li>
<li>Score the <strong>individual vulnerability</strong>, not the whole attack chain. Use the narrative and ATT&amp;CK mapping to explain chained impact.</li>
<li>Some firms separate "CVSS severity" from an overall "risk rating" that adds likelihood and business context. This is good practice, but explain the method.</li>
</ul>
<h3>In vulnerability management</h3>
<ul>
<li>Define remediation SLAs by severity (e.g. Critical 7 days, High 30 days), but <strong>prioritise with threat data</strong>: combine CVSS with EPSS (Exploit Prediction Scoring System, also by FIRST), the CISA Known Exploited Vulnerabilities catalogue, and asset criticality. Frameworks such as SSVC (Stakeholder-Specific Vulnerability Categorization) provide decision trees for this.</li>
<li>Re-score with Environmental metrics for your crown-jewel systems.</li>
</ul>
""")

# --------------------------------------------------------------------------
ch("Part VI &middot; Software Testing Foundations", "iso29119",
   "ISO/IEC/IEEE 29119", "Software and systems engineering &mdash; Software testing",
glance([
 ("Area", "Software testing"),
 ("Type", "International standard series"),
 ("Published by", "ISO/IEC JTC 1/SC 7 with IEEE; first parts 2013, major revision 2021&ndash;2022"),
 ("Mandatory?", "Voluntary; used in regulated and safety-related industries, government contracts and organisations formalising their test process"),
 ("Use it for", "Framework, processes and documentation for software testing"),
 ("Link", '<a href="https://www.iso.org/standard/81291.html">iso.org/standard/81291.html</a> (Part 1: General concepts)'),
]) + """
<h2>What it is</h2>
<p>ISO/IEC/IEEE 29119 is an internationally agreed set of standards for software testing that can be used within any
software development lifecycle (waterfall, V-model, agile, DevOps) and by any organisation. It replaced earlier
standards such as IEEE 829 (test documentation) and BS 7925 (component testing). Its aim is to give a common basis for
test processes, documentation and techniques, so that testing can be planned, managed and audited consistently.</p>
<p>Security testing is a type of testing; 29119 provides the <em>process and documentation discipline</em> within which
security tests (penetration tests, security functional tests, fuzzing) can be managed like any other test activity.</p>

<h2>Parts of the series</h2>
<table class="data"><thead><tr><th>Part</th><th>Title</th><th>Content</th></tr></thead><tbody>
<tr><td>29119-1</td><td>General concepts</td><td>Vocabulary and concepts: test levels, types, practices, risk-based testing.</td></tr>
<tr><td>29119-2</td><td>Test processes</td><td>A three-layer process model (below).</td></tr>
<tr><td>29119-3</td><td>Test documentation</td><td>Templates and content for test documents, with examples for agile and traditional contexts.</td></tr>
<tr><td>29119-4</td><td>Test techniques</td><td>Specification-based, structure-based and experience-based techniques with coverage measures.</td></tr>
<tr><td>29119-5</td><td>Keyword-driven testing</td><td>Framework for keyword-driven test automation.</td></tr>
<tr><td>Other parts / TRs</td><td>&mdash;</td><td>Guidance for agile projects, testing AI-based systems (TR 29119-11), test models, and others.</td></tr>
</tbody></table>

<h2>The three-layer process model (Part 2)</h2>
<ol>
<li><strong>Organisational test process</strong> &mdash; creates and maintains organisation-wide test specifications: the <em>test policy</em> and <em>organisational test practices</em> (formerly "test strategy").</li>
<li><strong>Test management processes</strong> &mdash; <em>test planning</em>, <em>test monitoring and control</em>, and <em>test completion</em>, applied to a project or to a test level/type.</li>
<li><strong>Dynamic test processes</strong> &mdash; <em>test design and implementation</em>, <em>test environment and data management</em>, <em>test execution</em>, and <em>test incident reporting</em>.</li>
</ol>
<p>The process is <strong>risk-based</strong>: test planning identifies product and project risks and uses them to
decide what to test, how much and with which techniques.</p>

<h2>Key documents (Part 3)</h2>
<table class="data two"><thead><tr><th>Organisational and management</th><th>Dynamic testing</th></tr></thead><tbody><tr>
<td><ul><li>Test policy</li><li>Organisational test practices</li><li>Test plan</li><li>Test status report</li><li>Test completion report</li></ul></td>
<td><ul><li>Test model specification (test design)</li><li>Test case specification</li><li>Test procedure specification</li><li>Test data requirements / readiness report</li><li>Test environment requirements / readiness report</li><li>Test execution log</li><li>Test incident report</li></ul></td></tr></tbody></table>

<h2>How it is brought into practice</h2>
<ul>
<li><strong>Tailoring is expected.</strong> Organisations claim either <em>full</em> or <em>tailored</em> conformance. Agile teams map documents to lightweight artefacts: the test plan becomes a page in the wiki; test cases live in the test management tool; incident reports are tickets.</li>
<li><strong>Security as a test type in the test plan.</strong> A 29119-style test plan lists security testing alongside functional and performance testing, with its own risks, techniques (e.g. penetration testing per PTES/WSTG, SAST/DAST, fuzzing), entry/exit criteria, environments and responsibilities.</li>
<li><strong>Pentest reports as test completion reports.</strong> Mapping a pentest to 29119 gives it an auditable place in the project's evidence: scope (test plan), test cases (WSTG checklist), execution log (activity log), incidents (findings) and completion report (final report and retest).</li>
<li><strong>Test techniques for security.</strong> Part 4 techniques apply directly: boundary value analysis for input validation, state transition testing for authentication and session flows, decision tables for authorisation rules, and experience-based "error guessing" which underlies much of manual pentesting.</li>
</ul>
<div class="callout"><strong>Context.</strong> 29119 has critics in parts of the testing community who argue it is too
document-heavy for context-driven testing. The 2021&ndash;2022 revisions added much more agile guidance. Use it as a
reference model to tailor, not a bureaucracy to copy.</div>
""")

# --------------------------------------------------------------------------
ch("Part VI &middot; Software Testing Foundations", "istqb",
   "ISTQB", "International Software Testing Qualifications Board &mdash; body of knowledge and glossary",
glance([
 ("Area", "Software testing"),
 ("Type", "Certification scheme, syllabi (body of knowledge) and glossary"),
 ("Maintained by", "ISTQB, a not-for-profit association of national member boards; Foundation Level v4.0 (2023)"),
 ("Mandatory?", "No. One of the most widely held testing certifications worldwide; frequently requested in job descriptions"),
 ("Use it for", "Common vocabulary and test design techniques"),
 ("Link", '<a href="https://www.istqb.org/">istqb.org</a>'),
]) + """
<h2>What it is</h2>
<p>ISTQB defines a structured body of knowledge for software testing, delivered through syllabi at Foundation,
Advanced and Expert levels, plus specialist modules. Its <strong>Glossary</strong> is a widely used reference for testing
terminology. For security professionals, ISTQB matters because it supplies the shared vocabulary and systematic test
design techniques that make security testing integrate cleanly with QA teams.</p>

<h2>The certification structure (simplified)</h2>
<ul>
<li><strong>Foundation Level (CTFL)</strong> &mdash; the core: fundamentals, testing in the SDLC, static testing, test analysis and design, test management, tools.</li>
<li><strong>Core Advanced</strong> &mdash; Test Analyst, Technical Test Analyst, Test Manager.</li>
<li><strong>Specialist</strong> &mdash; including <strong>Security Tester (CT-SEC)</strong>, Performance Testing, Automotive, AI Testing, Mobile Application Testing, Test Automation Engineering, and others.</li>
<li><strong>Agile</strong> &mdash; Agile Tester and related modules.</li>
<li><strong>Expert</strong> &mdash; improving the test process, test management.</li>
</ul>

<h2>The seven testing principles</h2>
<ol>
<li><strong>Testing shows the presence, not the absence, of defects.</strong> A clean pentest does not prove a system is secure.</li>
<li><strong>Exhaustive testing is impossible.</strong> Prioritise by risk &mdash; the same logic as PTES threat modelling.</li>
<li><strong>Early testing saves time and money</strong> ("shift left"): threat modelling and design review find flaws cheapest.</li>
<li><strong>Defects cluster together.</strong> Where you find one injection flaw, look harder nearby.</li>
<li><strong>Tests wear out</strong> (the "pesticide paradox"): rotating testers and updating test cases keeps finding new issues.</li>
<li><strong>Testing is context dependent.</strong> A medical device and a marketing site need different testing.</li>
<li><strong>Absence-of-defects fallacy.</strong> A defect-free system can still fail to meet user needs or be insecure by design.</li>
</ol>

<h2>Test design techniques</h2>
<table class="data"><thead><tr><th>Category</th><th>Technique</th><th>Security application</th></tr></thead><tbody>
<tr><td rowspan="4">Black-box</td><td>Equivalence partitioning</td><td>Group inputs (valid, invalid, malicious classes) so one payload represents each class.</td></tr>
<tr><td>Boundary value analysis</td><td>Test lengths and numeric limits: buffer sizes, max upload sizes, integer overflows.</td></tr>
<tr><td>Decision table testing</td><td>Verify authorisation rules: role &times; resource &times; action combinations.</td></tr>
<tr><td>State transition testing</td><td>Authentication flows, MFA, password reset, session lifecycle, workflow bypass.</td></tr>
<tr><td rowspan="2">White-box</td><td>Statement and branch testing</td><td>Measure coverage during fuzzing; ensure error-handling branches are exercised.</td></tr>
<tr><td>(Value of white-box testing)</td><td>Supports code review and SAST triage.</td></tr>
<tr><td rowspan="3">Experience-based</td><td>Error guessing</td><td>Applying knowledge of common vulnerabilities (the core of manual pentesting).</td></tr>
<tr><td>Exploratory testing</td><td>Time-boxed, charter-driven security exploration of a feature.</td></tr>
<tr><td>Checklist-based testing</td><td>Using WSTG, MASTG or API Top 10 checklists.</td></tr>
</tbody></table>
<p>The CTFL v4.0 syllabus also covers collaboration-based approaches (user stories, acceptance criteria,
acceptance test-driven development), which is where security acceptance criteria belong.</p>

<h2>How it is brought into practice</h2>
<ul>
<li><strong>Common language between QA and security.</strong> Use ISTQB glossary terms (defect, failure, test basis, test oracle, test level, regression testing) in security test plans so QA teams can absorb security tests into their regression suites.</li>
<li><strong>Training path.</strong> CTFL gives testers fundamentals; CT-SEC adds security testing; developers and pentesters gain systematic test design skills that reduce missed cases.</li>
<li><strong>Security regression.</strong> After a pentest, convert each finding into an automated regression test case using the techniques above (e.g. a decision-table test that User B receives 403 on User A's resources).</li>
<li><strong>Process alignment.</strong> ISTQB's test process (planning, monitoring and control, analysis, design, implementation, execution, completion) aligns with ISO/IEC/IEEE 29119, so organisations often adopt both: ISTQB for skills and vocabulary, 29119 for formal process and documentation.</li>
</ul>
""")

# --------------------------------------------------------------------------
ch("Part V &middot; Governance, Hardening and Risk Rating", "iso27001",
   "ISO/IEC 27001", "Information security management systems &mdash; Requirements (2022 edition)",
glance([
 ("Area", "Governance: information security management"),
 ("Type", "International certifiable management-system standard"),
 ("Published by", "ISO/IEC JTC 1/SC 27; current edition ISO/IEC 27001:2022 (with Amendment 1:2024)"),
 ("Mandatory?", "Voluntary, but certification is a common contractual requirement, especially for SaaS, outsourcing and B2B suppliers"),
 ("Use it for", "Organisational security governance context"),
 ("Link", '<a href="https://www.iso.org/standard/27001">iso.org/standard/27001</a>'),
]) + """
<h2>What it is</h2>
<p>ISO/IEC 27001 specifies requirements for establishing, implementing, maintaining and continually improving an
<strong>Information Security Management System (ISMS)</strong>: a systematic, risk-based approach to managing sensitive
information across people, processes and technology. Unlike most frameworks in this book, organisations can be
<strong>certified</strong> against it by accredited certification bodies.</p>
<p>The standard has two parts: the <strong>management system clauses</strong> (4&ndash;10), which are mandatory, and
<strong>Annex A</strong>, a reference list of information security controls that must be considered against identified
risks. ISO/IEC 27002 provides detailed implementation guidance for each Annex A control.</p>

<h2>Clauses 4&ndash;10 (mandatory)</h2>
<table class="data"><thead><tr><th>Clause</th><th>Topic</th><th>Key requirements</th></tr></thead><tbody>
<tr><td>4</td><td>Context of the organisation</td><td>Internal/external issues, interested parties and their requirements, ISMS scope.</td></tr>
<tr><td>5</td><td>Leadership</td><td>Top management commitment, information security policy, roles and responsibilities.</td></tr>
<tr><td>6</td><td>Planning</td><td>Risk assessment and risk treatment process, Statement of Applicability, security objectives, planning of changes.</td></tr>
<tr><td>7</td><td>Support</td><td>Resources, competence, awareness, communication, documented information.</td></tr>
<tr><td>8</td><td>Operation</td><td>Operational planning and control; performing risk assessments and risk treatment.</td></tr>
<tr><td>9</td><td>Performance evaluation</td><td>Monitoring and measurement, internal audit, management review.</td></tr>
<tr><td>10</td><td>Improvement</td><td>Continual improvement, nonconformity and corrective action.</td></tr>
</tbody></table>

<h2>Annex A (2022): 93 controls in four themes</h2>
<table class="data"><thead><tr><th>Theme</th><th>Count</th><th>Examples</th></tr></thead><tbody>
<tr><td>5 Organisational</td><td>37</td><td>Policies; roles; threat intelligence (5.7); asset inventory; access control; supplier security; cloud services (5.23); incident management; ICT readiness for business continuity (5.30); legal requirements; independent review (5.35)</td></tr>
<tr><td>6 People</td><td>8</td><td>Screening; terms of employment; awareness and training; disciplinary process; remote working</td></tr>
<tr><td>7 Physical</td><td>14</td><td>Perimeters; entry controls; physical security monitoring (7.4); equipment; clear desk; secure disposal</td></tr>
<tr><td>8 Technological</td><td>34</td><td>Endpoint devices; privileged access; authentication; malware protection; management of technical vulnerabilities (8.8); configuration management (8.9); information deletion; data masking; data leakage prevention; backup; logging; monitoring activities (8.16); web filtering; cryptography; secure development; secure coding (8.28); security testing in development and acceptance (8.29)</td></tr>
</tbody></table>
<p>The 2022 revision introduced 11 new controls, including threat intelligence, cloud services security, ICT readiness
for business continuity, physical security monitoring, configuration management, information deletion, data masking,
data leakage prevention, monitoring activities, web filtering and secure coding. Controls can also be tagged with
attributes (control type, security properties, cybersecurity concepts aligned to Identify/Protect/Detect/Respond/Recover,
operational capabilities and security domains).</p>

<h2>How it is brought into practice</h2>
<h3>Implementation roadmap</h3>
<ol>
<li><strong>Secure management commitment</strong> and define the ISMS scope (e.g. "the SaaS platform and supporting functions in London and Bengaluru").</li>
<li><strong>Define the risk methodology</strong> (asset- or scenario-based, likelihood &times; impact scale, risk acceptance criteria).</li>
<li><strong>Perform the risk assessment</strong> and decide treatments.</li>
<li><strong>Produce the Statement of Applicability (SoA)</strong>: all 93 Annex A controls, whether each is applicable, justification, and implementation status.</li>
<li><strong>Implement controls</strong> and write required documented information (policy, risk process, SoA, objectives, competence evidence, operational procedures, monitoring results, audit programme, management review minutes, nonconformities).</li>
<li><strong>Operate</strong> for a period (often 3+ months) to generate evidence; run internal audit and management review.</li>
<li><strong>Certification audit</strong>: Stage 1 (documentation and readiness) and Stage 2 (implementation effectiveness). Then annual surveillance audits and recertification every three years.</li>
</ol>
<h3>Where security testing fits</h3>
<ul>
<li><strong>8.8 Management of technical vulnerabilities</strong> &mdash; vulnerability scanning, pentesting and patch SLAs provide evidence.</li>
<li><strong>8.29 Security testing in development and acceptance</strong> &mdash; WSTG/MASTG/API testing, SAST/DAST in the pipeline.</li>
<li><strong>5.35 Independent review of information security</strong> and <strong>clause 9</strong> performance evaluation &mdash; independent pentests and assessments feed management review.</li>
<li><strong>8.9 Configuration management</strong> &mdash; CIS Benchmarks are a common way to define and evidence secure baselines.</li>
<li><strong>Risk treatment</strong> &mdash; pentest findings become risks in the register with owners, treatment plans and acceptance decisions (clause 6.1.3 and 8.3).</li>
</ul>
<div class="callout"><strong>Tip for testers.</strong> When writing reports for ISO 27001-certified clients, add an
"ISO/IEC 27001:2022 Annex A reference" field to each finding. Auditors and ISMS managers can then trace findings
directly to controls and nonconformities.</div>
""")
