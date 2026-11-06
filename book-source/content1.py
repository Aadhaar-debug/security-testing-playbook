# -*- coding: utf-8 -*-
# Chapter content, part 1: testing methodologies and application-layer guides.

def glance(rows):
    out = '<table class="glance"><tbody>'
    for k, v in rows:
        out += f'<tr><th>{k}</th><td>{v}</td></tr>'
    return out + '</tbody></table>'

CHAPTERS = []

def ch(part, cid, title, subtitle, body):
    CHAPTERS.append(dict(part=part, id=cid, title=title, subtitle=subtitle, body=body))

# --------------------------------------------------------------------------
ch("Part I &middot; Penetration and Security Testing Methodologies", "ptes",
   "PTES", "The Penetration Testing Execution Standard",
glance([
 ("Area", "Penetration testing"),
 ("Type", "Community methodology (phase model + technical guidelines)"),
 ("Maintained by", "A volunteer group of practitioners; launched 2009, largely stable since"),
 ("Mandatory?", "No. Widely cited in statements of work and RFPs as the reference pentest flow"),
 ("Use it for", "Overall pentest methodology and phase structure"),
 ("Link", '<a href="http://www.pentest-standard.org/">pentest-standard.org</a>'),
]) + """
<h2>What it is</h2>
<p>PTES was created by a group of working penetration testers who were frustrated that "penetration test" meant
wildly different things depending on who sold it. Some vendors delivered an automated scan with a logo on it;
others delivered weeks of manual adversary simulation. PTES defines a common baseline: what a penetration test
<em>is</em>, what phases it moves through, and what a client should expect to receive at the end.</p>
<p>It has two layers. The <strong>main standard</strong> describes the seven phases at a level a client or manager
can understand. The <strong>technical guidelines</strong> go deeper, listing tools, techniques and the kinds of
information to collect in each phase. The technical guidelines are now dated in places (tool names change), but the
phase model has proven durable and is still the backbone of most consultancies' methodology documents.</p>

<h2>The seven phases</h2>
<table class="data">
<thead><tr><th>#</th><th>Phase</th><th>Purpose</th><th>Typical outputs</th></tr></thead>
<tbody>
<tr><td>1</td><td>Pre-engagement Interactions</td><td>Agree scope, goals, rules of engagement, legal authority, communication paths and emergency contacts.</td><td>Signed SOW, RoE, authorisation letter, scope list (IPs, URLs, apps), test windows, escalation tree.</td></tr>
<tr><td>2</td><td>Intelligence Gathering</td><td>Learn as much as possible about the target: OSINT, footprinting, infrastructure and people.</td><td>Asset inventory, domains/subdomains, employee and technology profile, exposed services.</td></tr>
<tr><td>3</td><td>Threat Modelling</td><td>Identify the assets that matter (business and data) and the threat actors and capabilities likely to target them.</td><td>Prioritised list of high-value assets and attack paths to pursue.</td></tr>
<tr><td>4</td><td>Vulnerability Analysis</td><td>Discover flaws through active and passive testing, then validate them to remove false positives.</td><td>Validated vulnerability list with evidence.</td></tr>
<tr><td>5</td><td>Exploitation</td><td>Bypass controls and gain access, choosing precise attacks rather than spraying exploits.</td><td>Proof of access, screenshots, compromised credentials, footholds.</td></tr>
<tr><td>6</td><td>Post Exploitation</td><td>Determine the value of the compromise: pivoting, privilege escalation, data access, persistence &mdash; within RoE.</td><td>Attack narrative showing business impact; data touched; cleanup log.</td></tr>
<tr><td>7</td><td>Reporting</td><td>Communicate results to executives and technical teams.</td><td>Executive summary, technical findings, risk ratings, remediation guidance.</td></tr>
</tbody></table>

<h2>Key ideas worth knowing</h2>
<ul>
<li><strong>Scoping is a phase, not paperwork.</strong> PTES treats pre-engagement as part of the test. A sloppy scope
causes most engagement failures: testing a third party's IP you had no right to touch, missing the asset the client
actually cared about, or running a destructive test during business hours.</li>
<li><strong>Threat modelling drives effort.</strong> PTES expects testers to spend their limited hours where real
attackers would gain the most, not to test everything equally. That is what separates a pentest from a vulnerability
scan.</li>
<li><strong>Exploitation should be precise.</strong> The standard explicitly discourages "throwing everything at the
wall". Each exploitation attempt should be justified by earlier analysis, which also reduces the chance of crashing
production systems.</li>
<li><strong>Post-exploitation proves impact.</strong> A shell on a server is a technical fact; showing that the shell
leads to the payroll database is a business fact. PTES insists on the second.</li>
</ul>

<h2>How it is brought into practice</h2>
<h3>1. Build your engagement lifecycle around the phases</h3>
<p>Most consultancies map their internal workflow directly onto PTES. A typical implementation:</p>
<ol>
<li><strong>Kick-off call and scoping questionnaire</strong> (phase 1). Questionnaires capture number of IPs, apps,
user roles, environments (prod vs. staging), cloud providers and third-party hosting. The output feeds a fixed-price
quote and a Rules of Engagement document.</li>
<li><strong>Authorisation.</strong> A signed letter from someone with authority over each asset. For cloud-hosted
assets, check the provider's testing policy (most major providers no longer need pre-approval for common services, but
prohibit things like DoS testing).</li>
<li><strong>Recon sprint</strong> (phase 2) &mdash; time-boxed, often 10&ndash;15% of total effort.</li>
<li><strong>Threat modelling workshop</strong> (phase 3) &mdash; even a 30-minute call with the client to ask "what
would hurt most?" makes the test far more valuable.</li>
<li><strong>Testing</strong> (phases 4&ndash;6), with daily status updates and immediate escalation of critical
findings rather than waiting for the report.</li>
<li><strong>Reporting and debrief</strong> (phase 7), followed by an optional retest window.</li>
</ol>

<h3>2. Write a Rules of Engagement document</h3>
<p>The RoE is the most important artefact PTES encourages. It should state at minimum:</p>
<ul>
<li>In-scope and explicitly out-of-scope targets.</li>
<li>Test dates and permitted hours; time zone.</li>
<li>Permitted techniques (social engineering? physical? DoS? password spraying limits?).</li>
<li>Data handling: what testers may view, copy or retain, and how evidence is destroyed afterwards.</li>
<li>Emergency stop procedure and 24/7 contacts on both sides.</li>
<li>Source IP addresses testers will use, so the blue team can distinguish them.</li>
</ul>

<h3>3. Pair PTES with asset-specific guides</h3>
<p>PTES tells you <em>when</em> to do things; it does not give you a detailed checklist for a web app or a mobile app.
In practice it is the outer frame, and inside phases 4&ndash;6 testers use OWASP WSTG (web), the API Security Top 10,
OWASP MASTG (mobile), the OWASP IoT guides, or the LLM Top 10. Findings are then scored with CVSS and mapped to
MITRE ATT&amp;CK and control frameworks in the reporting phase.</p>

<div class="callout"><strong>Practitioner tip.</strong> Keep a running <em>activity log</em> (timestamp, source IP,
target, action) throughout phases 4&ndash;6. If something breaks in production, the log lets the client correlate
quickly and proves what you did and did not do.</div>

<h2>Strengths and limitations</h2>
<table class="data two"><thead><tr><th>Strengths</th><th>Limitations</th></tr></thead><tbody><tr>
<td><ul><li>Clear, client-friendly phase model.</li><li>Strong emphasis on scoping and business impact.</li>
<li>Free and vendor-neutral.</li></ul></td>
<td><ul><li>Technical guidelines are dated; tool lists are stale.</li><li>No metrics or scoring model of its own.</li>
<li>Not a formal standard; not auditable or certifiable.</li></ul></td></tr></tbody></table>

<h2>Related frameworks</h2>
<p>NIST SP 800-115 (similar phases, more formal), OSSTMM (metric-driven alternative), CVSS (scoring findings),
MITRE ATT&amp;CK (describing attack paths in the report).</p>
""")

# --------------------------------------------------------------------------
ch("Part I &middot; Penetration and Security Testing Methodologies", "nist800115",
   "NIST SP 800-115", "Technical Guide to Information Security Testing and Assessment",
glance([
 ("Area", "Penetration testing and security assessment"),
 ("Type", "Government guidance (NIST Special Publication)"),
 ("Published by", "US National Institute of Standards and Technology, September 2008"),
 ("Mandatory?", "Not mandatory in itself, but routinely referenced by US federal programmes (e.g. FedRAMP, FISMA assessments) and by contracts worldwide"),
 ("Use it for", "A recognised reference for planning and running security tests"),
 ("Link", '<a href="https://csrc.nist.gov/pubs/sp/800/115/final">csrc.nist.gov/pubs/sp/800/115/final</a>'),
]) + """
<h2>What it is</h2>
<p>SP 800-115 is NIST's guide to <em>planning and conducting</em> technical security testing and assessment, analysing
the findings, and developing mitigation strategies. It is broader than penetration testing: it covers document and log
reviews, scanning, wireless assessment and password cracking as well as pentests. Its value lies in being an
authoritative, neutral reference that auditors, procurement teams and regulators recognise.</p>
<p>The publication dates from 2008, so its tool examples are old. The <em>process</em> guidance, however &mdash; how to
plan, what roles exist, how to handle data and how to report &mdash; remains sound. Check the CSRC page for the current
revision status before citing it in a contract.</p>

<h2>Structure: three families of technique</h2>
<table class="data"><thead><tr><th>Family</th><th>Techniques</th><th>Typical use</th></tr></thead><tbody>
<tr><td><strong>Review techniques</strong><br>(passive)</td><td>Documentation review, log review, ruleset review (firewalls, IDS), system configuration review, network sniffing, file integrity checking</td><td>Find policy and configuration gaps with no risk to systems.</td></tr>
<tr><td><strong>Target identification and analysis</strong></td><td>Network discovery, network port and service identification, vulnerability scanning, wireless scanning</td><td>Build an inventory and find candidate weaknesses.</td></tr>
<tr><td><strong>Target vulnerability validation</strong><br>(active)</td><td>Password cracking, penetration testing, social engineering</td><td>Prove that weaknesses are exploitable and show impact.</td></tr>
</tbody></table>

<h2>The four-phase penetration testing model</h2>
<p>Within validation, SP 800-115 describes penetration testing as four phases, with a feedback loop between Discovery
and Attack:</p>
<div class="flow"><span>Planning</span><span>Discovery</span><span>Attack</span><span>Reporting</span></div>
<ul>
<li><strong>Planning</strong> &mdash; rules are identified, management approval is finalised and documented, and goals are set. No testing occurs.</li>
<li><strong>Discovery</strong> &mdash; information gathering and scanning, then vulnerability analysis comparing discovered services against vulnerability databases.</li>
<li><strong>Attack</strong> &mdash; gaining access, escalating privileges, system browsing, installing additional tools. If new information is found, the tester loops back to Discovery.</li>
<li><strong>Reporting</strong> &mdash; occurs in parallel with the other phases and culminates in a report describing vulnerabilities, risk ratings and mitigation guidance.</li>
</ul>

<h2>Assessment planning and logistics</h2>
<p>A distinctive strength of SP 800-115 is its treatment of the "boring" parts that make testing safe and defensible:</p>
<ul>
<li><strong>Developing a security assessment policy</strong> at organisational level (who may authorise tests, how often, requirements for third parties).</li>
<li><strong>Prioritising and scheduling</strong> assessments based on risk and system categorisation.</li>
<li><strong>Selecting and customising techniques</strong> to the objective; not every assessment needs a pentest.</li>
<li><strong>Logistics</strong>: assessor selection and skills, location (internal/external), technical tools and resources.</li>
<li><strong>Assessment plan</strong> containing scope, rules, schedule, legal considerations and data handling.</li>
<li><strong>Data handling</strong>: collection, storage, transmission and destruction of assessment data, which is itself highly sensitive.</li>
</ul>

<h2>How it is brought into practice</h2>
<h3>Inside an organisation (testing programme owner)</h3>
<ol>
<li><strong>Write a security testing policy</strong> referencing SP 800-115: frequency (e.g. annual external pentest, quarterly scans), who approves, and minimum assessor qualifications.</li>
<li><strong>Build an assessment calendar</strong> prioritised by system criticality, change rate and regulatory exposure.</li>
<li><strong>Standardise the assessment plan template</strong> using SP 800-115's suggested contents, so every test, internal or external, is approved the same way.</li>
<li><strong>Define a findings workflow</strong>: from report, to risk register, to remediation tickets with SLAs, to retest. SP 800-115's post-testing section (root cause analysis, mitigation recommendations, reporting, remediation) is the template.</li>
</ol>
<h3>For a testing provider</h3>
<ul>
<li>Cite SP 800-115 in proposals as the reference methodology alongside PTES. Government and regulated clients frequently ask for it by name.</li>
<li>Structure deliverables around the three families: a configuration review section (review techniques), a scan and inventory section (identification), and a validated findings section (validation).</li>
<li>Adopt its data-handling guidance as your evidence retention policy (encrypt at rest, restrict access, destroy at engagement end with a certificate if requested).</li>
</ul>

<div class="callout"><strong>Where it fits.</strong> SP 800-115 is the "assessment programme" view; PTES is the
"engagement" view. Many teams quote both: SP 800-115 for governance and planning, PTES for the engagement flow, and
OWASP guides for the technical checklists.</div>

<h2>Strengths and limitations</h2>
<table class="data two"><thead><tr><th>Strengths</th><th>Limitations</th></tr></thead><tbody><tr>
<td><ul><li>Recognised by auditors and governments.</li><li>Covers the whole assessment programme, not just pentests.</li><li>Excellent on planning, legal and data-handling issues.</li></ul></td>
<td><ul><li>Published 2008; tool references and some techniques are dated.</li><li>Light on application, cloud, mobile and API testing.</li><li>No severity scoring model.</li></ul></td></tr></tbody></table>
""")

# --------------------------------------------------------------------------
ch("Part I &middot; Penetration and Security Testing Methodologies", "osstmm",
   "OSSTMM", "Open Source Security Testing Methodology Manual",
glance([
 ("Area", "Operational security testing (all channels)"),
 ("Type", "Scientific testing methodology with its own metrics"),
 ("Maintained by", "ISECOM (Institute for Security and Open Methodologies); version 3 published 2010"),
 ("Mandatory?", "No. Used where repeatability and measurable results are required"),
 ("Use it for", "Repeatable, metric-driven operational security testing"),
 ("Link", '<a href="https://www.isecom.org/OSSTMM.3.pdf">isecom.org/OSSTMM.3.pdf</a>'),
]) + """
<h2>What it is</h2>
<p>OSSTMM takes a very different philosophy from PTES. Rather than asking "can an attacker break in?", it asks
"<em>how much</em> operational security does this target actually have, and can we measure it the same way every time?"
It aims to produce fact-based, repeatable results that two different teams testing the same target would agree on.</p>
<p>OSSTMM avoids subjective risk language. Instead of saying a finding is "high risk", it measures how much of the
target is exposed, which controls are in place, and which limitations (flaws) exist, and combines them into a
numeric security value.</p>

<h2>Core concepts</h2>
<h3>Porosity: Visibility, Access, Trust</h3>
<p>OSSTMM views security as a separation between an asset and threats. Every point where that separation is broken
is a "pore". Pores are classified as:</p>
<ul>
<li><strong>Visibility</strong> &mdash; the target can be seen or detected (e.g. an IP that responds to probes).</li>
<li><strong>Access</strong> &mdash; an interaction point that allows a response (e.g. an open port, a reception desk).</li>
<li><strong>Trust</strong> &mdash; an interaction between targets that is accepted without authentication (e.g. one server trusting another's requests).</li>
</ul>

<h3>The ten operational controls</h3>
<table class="data"><thead><tr><th>Class A &mdash; Interactive controls</th><th>Class B &mdash; Process controls</th></tr></thead><tbody>
<tr><td>Authentication</td><td>Non-repudiation</td></tr>
<tr><td>Indemnification</td><td>Confidentiality</td></tr>
<tr><td>Resilience</td><td>Privacy</td></tr>
<tr><td>Subjugation</td><td>Integrity</td></tr>
<tr><td>Continuity</td><td>Alarm</td></tr>
</tbody></table>
<p>Class A controls directly influence interactions (e.g. authentication, or subjugation which forces interactions to
occur only under the owner's conditions). Class B controls protect assets once an interaction occurs.</p>

<h3>Limitations</h3>
<p>Rather than "vulnerabilities", OSSTMM classifies the flaws found into five limitation types: <strong>Vulnerability</strong>
(a flaw that denies access or allows privileged access), <strong>Weakness</strong> (a flaw in a Class A control),
<strong>Concern</strong> (a flaw in a Class B control), <strong>Exposure</strong> (an unjustifiable action or
information that gives visibility), and <strong>Anomaly</strong> (an unidentified or unknown element).</p>

<h3>The rav and the STAR</h3>
<p>Porosity, controls and limitations combine into the <strong>rav</strong> (risk assessment value), a measure of the
attack surface: the amount of uncontrolled interaction. A score near 100 rav indicates a balance between porosity and
controls ("perfect balance"); below means insufficient controls, above means more controls than needed. Results are
recorded in the <strong>STAR</strong> (Security Test Audit Report), a standard form that records what was tested, how,
and the quantified results.</p>

<h2>Channels and test types</h2>
<p>OSSTMM covers five channels grouped into three classes: <strong>PHYSSEC</strong> (Human and Physical),
<strong>SPECSEC</strong> (Wireless/spectrum) and <strong>COMSEC</strong> (Telecommunications and Data Networks). It also
defines six test types by how much the tester and target know in advance:</p>
<table class="data"><thead><tr><th>Type</th><th>Tester knows</th><th>Target knows</th></tr></thead><tbody>
<tr><td>Blind</td><td>Nothing</td><td>Everything (expects the test)</td></tr>
<tr><td>Double Blind</td><td>Nothing</td><td>Nothing</td></tr>
<tr><td>Gray Box</td><td>Limited</td><td>Everything</td></tr>
<tr><td>Double Gray Box</td><td>Limited</td><td>Scope and time frame only</td></tr>
<tr><td>Tandem</td><td>Everything</td><td>Everything</td></tr>
<tr><td>Reversal</td><td>Everything</td><td>Nothing (tests the defenders' response)</td></tr>
</tbody></table>

<h2>The test process</h2>
<p>OSSTMM's Four Point Process structures each test: <strong>Induction</strong> (learn about the target from the
environment), <strong>Inquest</strong> (investigate emanations from the target), <strong>Interaction</strong> (probe
the target directly) and <strong>Intervention</strong> (change resources the target depends on to see how it reacts).
Within each channel, a set of modules runs from posture review and logistics through visibility audit, access
verification, trust verification and controls verification, to alert and log review.</p>

<h2>How it is brought into practice</h2>
<ol>
<li><strong>Define the scope as a vector and channel.</strong> E.g. "Data Networks channel, external vector, from the internet into the DMZ." OSSTMM requires each vector to be tested separately.</li>
<li><strong>Choose the test type</strong> (blind, gray box, tandem&hellip;) and document it, because results are only comparable between tests of the same type.</li>
<li><strong>Run the modules systematically</strong>, recording each pore (visibility, access, trust), each control observed, and each limitation.</li>
<li><strong>Calculate the rav</strong> using ISECOM's spreadsheet or calculator.</li>
<li><strong>Complete the STAR</strong> and attach it to the narrative report.</li>
<li><strong>Repeat after change.</strong> Because the method is repeatable, you can retest after remediation or annually and compare rav values, which shows measurable improvement to management.</li>
</ol>
<div class="callout"><strong>When to choose OSSTMM.</strong> It shines when you need to compare security over time or
across sites (e.g. 40 retail branches), when physical and human channels are in scope, or when clients want metrics
instead of opinions. Many teams borrow its concepts (porosity, test types, STAR) even if they do not compute rav.</div>

<h2>Strengths and limitations</h2>
<table class="data two"><thead><tr><th>Strengths</th><th>Limitations</th></tr></thead><tbody><tr>
<td><ul><li>Repeatable and measurable.</li><li>Covers human, physical, wireless and telecom as well as networks.</li><li>Clear vocabulary for test types.</li></ul></td>
<td><ul><li>Steep learning curve; dense language.</li><li>rav is unfamiliar to most executives and not comparable with CVSS.</li><li>Version 3 dates from 2010; v4 has been long in development.</li></ul></td></tr></tbody></table>
""")

# --------------------------------------------------------------------------
ch("Part II &middot; Application, API, Mobile and IoT Security", "wstg",
   "OWASP WSTG", "Web Security Testing Guide",
glance([
 ("Area", "Web applications"),
 ("Type", "Testing methodology and test-case catalogue"),
 ("Maintained by", "OWASP Foundation (community project); v4.2 stable, with a rolling development version"),
 ("Mandatory?", "No, but the de facto reference for web application testing"),
 ("Use it for", "The reference methodology for web application testing"),
 ("Link", '<a href="https://owasp.org/www-project-web-security-testing-guide/">owasp.org/www-project-web-security-testing-guide</a>'),
]) + """
<h2>What it is</h2>
<p>The WSTG is a comprehensive guide to testing the security of web applications and web services. Where the OWASP
Top 10 is an <em>awareness</em> document listing the most critical risk categories, the WSTG is the
<em>how-to</em>: hundreds of pages describing what to test, why, and how, with tools and example payloads. Every test
has a stable identifier, which makes it easy to build checklists and to reference tests in reports.</p>

<h2>Structure</h2>
<p>The guide opens with a testing framework (how testing fits into the SDLC: before development, during definition
and design, during development, during deployment, and during maintenance) and then lists tests in categories. Each
test ID follows the pattern <code>WSTG-&lt;CATEGORY&gt;-&lt;NN&gt;</code>:</p>
<table class="data"><thead><tr><th>Code</th><th>Category</th><th>Example tests</th></tr></thead><tbody>
<tr><td>INFO</td><td>Information Gathering</td><td>Fingerprint web server; review webpage content for leakage; map application architecture</td></tr>
<tr><td>CONF</td><td>Configuration and Deployment Management</td><td>Test HTTP methods; HSTS; file extension handling; cloud storage; subdomain takeover</td></tr>
<tr><td>IDNT</td><td>Identity Management</td><td>Role definitions; user registration; account enumeration</td></tr>
<tr><td>ATHN</td><td>Authentication</td><td>Default credentials; lockout; bypass; weak password policy; MFA weaknesses</td></tr>
<tr><td>ATHZ</td><td>Authorization</td><td>Directory traversal; privilege escalation; insecure direct object references (IDOR)</td></tr>
<tr><td>SESS</td><td>Session Management</td><td>Cookie attributes; session fixation; CSRF; logout; session timeout; JWT</td></tr>
<tr><td>INPV</td><td>Input Validation</td><td>Reflected/stored XSS; SQL injection; command injection; SSRF; SSTI; HTTP request smuggling</td></tr>
<tr><td>ERRH</td><td>Error Handling</td><td>Improper error handling; stack traces</td></tr>
<tr><td>CRYP</td><td>Cryptography</td><td>Weak TLS; padding oracle; sensitive data over unencrypted channels; weak encryption</td></tr>
<tr><td>BUSL</td><td>Business Logic</td><td>Data validation; request forgery; integrity checks; process timing; workflow circumvention; file upload</td></tr>
<tr><td>CLNT</td><td>Client-side</td><td>DOM XSS; JavaScript execution; HTML injection; open redirect; CORS; clickjacking; WebSockets; browser storage</td></tr>
<tr><td>APIT</td><td>API Testing</td><td>GraphQL testing (expanded in later development versions)</td></tr>
</tbody></table>
<p>For example, <code>WSTG-INPV-05</code> is Testing for SQL Injection, and <code>WSTG-ATHZ-04</code> is Testing for
Insecure Direct Object References. Because IDs can shift between versions, always cite the version (e.g. "WSTG v4.2").</p>

<h2>How it is brought into practice</h2>
<h3>1. Build a test checklist from the WSTG</h3>
<p>OWASP publishes a checklist spreadsheet derived from the guide. Teams typically fork it and add columns for
<em>status</em> (Not started / Pass / Fail / N/A), <em>tester</em>, <em>evidence reference</em> and <em>notes</em>.
Marking tests explicitly as N/A (with a reason) is as important as marking failures: it proves coverage.</p>
<h3>2. Run the engagement in a sensible order</h3>
<ol>
<li><strong>INFO</strong> and <strong>CONF</strong> first: map the app, its entry points, roles and technology stack. Spider and proxy every function through an intercepting proxy (e.g. Burp Suite, OWASP ZAP).</li>
<li><strong>IDNT, ATHN, SESS</strong>: understand who users are and how they log in and stay logged in.</li>
<li><strong>ATHZ</strong>: with at least two accounts per role, test horizontal and vertical access control on every object and function. This is where the most serious real-world findings usually live.</li>
<li><strong>INPV, CLNT</strong>: injection and client-side tests across all inputs, combining automated scanning with manual payload work.</li>
<li><strong>BUSL</strong>: business logic tests, which cannot be automated &mdash; skip steps in a workflow, replay discount codes, race a payment.</li>
<li><strong>ERRH, CRYP</strong>: sweep for leakage and transport/crypto weaknesses.</li>
</ol>
<h3>3. Embed it into the SDLC</h3>
<ul>
<li><strong>Requirements</strong>: reference the OWASP ASVS (the sister "verification standard") for what the app must do; the WSTG tells you how to test it.</li>
<li><strong>CI/CD</strong>: automate the subset of WSTG tests that are automatable (DAST baseline scans, header checks, TLS checks) on every build.</li>
<li><strong>Pre-release</strong>: manual WSTG-based pentest for major releases or high-risk features.</li>
<li><strong>Reporting</strong>: tag each finding with its WSTG ID, a CWE, and a CVSS score so developers can look up the test and reproduce it.</li>
</ul>
<div class="callout"><strong>WSTG vs. ASVS vs. Top 10.</strong> The <em>Top 10</em> raises awareness of risk
categories; <em>ASVS</em> defines verifiable security requirements at three levels; <em>WSTG</em> describes how to test.
A mature programme uses all three: ASVS for requirements, WSTG for testing, Top 10 for training and executive
communication.</div>

<h2>Strengths and limitations</h2>
<table class="data two"><thead><tr><th>Strengths</th><th>Limitations</th></tr></thead><tbody><tr>
<td><ul><li>Extremely comprehensive and free.</li><li>Stable test IDs ideal for checklists and reports.</li><li>Practical: payloads, tools and examples.</li></ul></td>
<td><ul><li>Not a compliance standard; no pass/fail levels (use ASVS for that).</li><li>Release cadence is slow; newest techniques may only be in the development version.</li><li>Coverage of modern SPAs and APIs is still evolving.</li></ul></td></tr></tbody></table>
""")

# --------------------------------------------------------------------------
ch("Part II &middot; Application, API, Mobile and IoT Security", "apitop10",
   "OWASP API Security Top 10", "The most critical API-specific risks (2023 edition)",
glance([
 ("Area", "APIs (REST, GraphQL, gRPC and others)"),
 ("Type", "Risk awareness list"),
 ("Maintained by", "OWASP API Security Project; first edition 2019, current edition 2023"),
 ("Mandatory?", "No. Widely used in procurement, testing scopes and API gateway product features"),
 ("Use it for", "Scoping and checklist for API testing"),
 ("Link", '<a href="https://owasp.org/API-Security/">owasp.org/API-Security</a>'),
]) + """
<h2>What it is</h2>
<p>APIs are now the main attack surface of most applications. They expose business logic and data directly, are
consumed by machines rather than browsers, and often lack the protective layers a web front-end provides. The API
Security Top 10 exists because the classic OWASP Top 10 under-represents the risks that dominate API breaches &mdash;
above all, broken authorisation.</p>

<h2>The 2023 list</h2>
<table class="data"><thead><tr><th>ID</th><th>Risk</th><th>In plain terms</th></tr></thead><tbody>
<tr><td>API1</td><td>Broken Object Level Authorization (BOLA)</td><td>Change an ID in the request (<code>/orders/1001</code> &rarr; <code>/orders/1002</code>) and get someone else's data.</td></tr>
<tr><td>API2</td><td>Broken Authentication</td><td>Weak token handling, credential stuffing, missing brute-force protection, unsigned or poorly validated JWTs.</td></tr>
<tr><td>API3</td><td>Broken Object Property Level Authorization (BOPLA)</td><td>Excessive data exposure and mass assignment: reading or writing fields you should not (e.g. setting <code>"isAdmin": true</code>).</td></tr>
<tr><td>API4</td><td>Unrestricted Resource Consumption</td><td>No limits on rate, payload size, pagination or expensive operations, leading to DoS or cost blow-ups (SMS, AI tokens).</td></tr>
<tr><td>API5</td><td>Broken Function Level Authorization (BFLA)</td><td>A normal user can call admin functions, e.g. <code>DELETE /users/42</code> or <code>/admin/</code> endpoints.</td></tr>
<tr><td>API6</td><td>Unrestricted Access to Sensitive Business Flows</td><td>Automating a legitimate flow at scale: ticket scalping, mass account creation, referral abuse.</td></tr>
<tr><td>API7</td><td>Server Side Request Forgery (SSRF)</td><td>The API fetches a user-supplied URL, letting attackers reach internal services or cloud metadata.</td></tr>
<tr><td>API8</td><td>Security Misconfiguration</td><td>Verbose errors, permissive CORS, missing TLS, unnecessary HTTP methods, default configs.</td></tr>
<tr><td>API9</td><td>Improper Inventory Management</td><td>Forgotten old versions (<code>/v1/</code>), undocumented debug endpoints, shadow APIs, unclear data flows to third parties.</td></tr>
<tr><td>API10</td><td>Unsafe Consumption of APIs</td><td>Trusting data from third-party APIs too much; following their redirects; not validating their responses.</td></tr>
</tbody></table>

<h2>How it is brought into practice</h2>
<h3>Scoping an API test</h3>
<ol>
<li><strong>Get the specification</strong>: OpenAPI/Swagger file, GraphQL schema, Postman collection or gRPC protobufs. Without one, testing becomes partly reverse engineering (traffic capture from the mobile or web client).</li>
<li><strong>Inventory the endpoints</strong> (API9): list every version, host and environment. Compare documentation to reality &mdash; undocumented endpoints are findings in their own right.</li>
<li><strong>Request multiple identities</strong>: at least two users per role and one per privilege level, plus tenants if multi-tenant. BOLA/BFLA testing is impossible without them.</li>
<li><strong>Agree rate-limit testing boundaries</strong> (API4/API6) so that resource-consumption tests do not cause real outages or costs.</li>
</ol>
<h3>Turning the list into a test plan</h3>
<table class="data"><thead><tr><th>Risk</th><th>Core test activity</th></tr></thead><tbody>
<tr><td>API1 BOLA</td><td>For every endpoint taking an object ID, replay User A's request with User B's token. Automate with an authorisation-matrix tool or proxy extension.</td></tr>
<tr><td>API2</td><td>Test token lifetime, revocation on logout/password change, JWT algorithm confusion (<code>alg: none</code>, key confusion), brute-force and credential-stuffing protections.</td></tr>
<tr><td>API3</td><td>Compare response fields with what the UI needs; try adding undocumented properties in POST/PUT/PATCH bodies.</td></tr>
<tr><td>API4 / API6</td><td>Measure rate limits per user, IP and token; send large page sizes and nested GraphQL queries; script business flows.</td></tr>
<tr><td>API5</td><td>Call every admin or privileged function with low-privilege tokens; try HTTP method switching.</td></tr>
<tr><td>API7</td><td>Supply internal and metadata URLs to every URL-accepting parameter (webhooks, image fetchers, importers).</td></tr>
<tr><td>API8 / API9 / API10</td><td>Configuration review, endpoint discovery and version enumeration, and review of how third-party data is validated.</td></tr>
</tbody></table>
<h3>Beyond testing: building it into development</h3>
<ul>
<li>Enforce authorisation in a central policy layer rather than per-endpoint code, and write unit tests that assert "User B cannot read User A's object".</li>
<li>Generate contract tests from the OpenAPI spec and reject requests with unexpected properties (mitigates mass assignment).</li>
<li>Use an API gateway for authentication, rate limiting and inventory; feed its traffic into discovery tooling to find shadow APIs.</li>
<li>Track each Top 10 item as a recurring threat in your threat model template for every new API.</li>
</ul>
<div class="callout"><strong>Note.</strong> The Top 10 is a list of risk categories, not a full methodology. For
detailed test cases combine it with WSTG (especially Authorization, Session and Input Validation tests and the API
testing section) and with the OWASP ASVS API requirements.</div>
""")

# --------------------------------------------------------------------------
ch("Part II &middot; Application, API, Mobile and IoT Security", "masvs",
   "OWASP MASVS / MASTG", "Mobile Application Security Verification Standard and Testing Guide",
glance([
 ("Area", "Mobile apps (Android and iOS)"),
 ("Type", "Requirements standard (MASVS) + testing guide (MASTG) + weakness list (MASWE)"),
 ("Maintained by", "OWASP Mobile Application Security (MAS) project"),
 ("Mandatory?", "No, but the basis of many certification schemes, including app-store-related assessment programmes"),
 ("Use it for", "Mobile app security requirements and tests"),
 ("Link", '<a href="https://mas.owasp.org/">mas.owasp.org</a>'),
]) + """
<h2>What it is</h2>
<p>The OWASP MAS project provides three linked resources:</p>
<ul>
<li><strong>MASVS</strong> &mdash; the <em>standard</em>: what a secure mobile app must achieve, expressed as high-level control groups and controls.</li>
<li><strong>MASTG</strong> &mdash; the <em>testing guide</em>: detailed, platform-specific techniques and test cases (static and dynamic) to verify each control, plus tooling guidance and demo apps.</li>
<li><strong>MASWE</strong> &mdash; the <em>weakness enumeration</em>: specific weaknesses that link MASVS controls to MASTG tests, similar in spirit to CWE.</li>
</ul>
<p>MASVS v2 (2023) simplified the earlier standard: the old L1/L2/R "levels" were moved out of the standard into
<strong>MAS testing profiles</strong>, and the control list became more concise.</p>

<h2>MASVS control groups</h2>
<table class="data"><thead><tr><th>Group</th><th>Focus</th></tr></thead><tbody>
<tr><td>MASVS-STORAGE</td><td>Secure storage of sensitive data on the device; preventing leakage via logs, backups, keyboard caches, screenshots.</td></tr>
<tr><td>MASVS-CRYPTO</td><td>Use of strong, current cryptography and correct key management (Android Keystore, iOS Keychain/Secure Enclave).</td></tr>
<tr><td>MASVS-AUTH</td><td>Secure authentication and authorisation, including biometric and local authentication done properly.</td></tr>
<tr><td>MASVS-NETWORK</td><td>Secure network communication: TLS everywhere, certificate validation, pinning where justified.</td></tr>
<tr><td>MASVS-PLATFORM</td><td>Secure interaction with the platform and other apps: IPC, intents, deep links, WebViews, UI.</td></tr>
<tr><td>MASVS-CODE</td><td>Secure coding: input validation, up-to-date dependencies, enforced updates, platform version support.</td></tr>
<tr><td>MASVS-RESILIENCE</td><td>Resistance to reverse engineering and tampering: obfuscation, root/jailbreak detection, anti-debugging, integrity checks.</td></tr>
<tr><td>MASVS-PRIVACY</td><td>Privacy controls: data minimisation, transparency, user control (added in v2.1).</td></tr>
</tbody></table>

<h2>Testing profiles</h2>
<ul>
<li><strong>L1</strong> &mdash; baseline security for all apps.</li>
<li><strong>L2</strong> &mdash; defence in depth for apps handling sensitive data (banking, health).</li>
<li><strong>R</strong> &mdash; resilience against reverse engineering and tampering, for apps protecting IP or high-value logic (games, DRM, payments).</li>
<li><strong>P</strong> &mdash; privacy-focused tests.</li>
</ul>

<h2>How it is brought into practice</h2>
<h3>For development teams</h3>
<ol>
<li><strong>Select the profile</strong> during design based on the data the app handles and its threat model (a retail app might be L1; a banking app L2+R).</li>
<li><strong>Turn MASVS controls into user stories / acceptance criteria</strong>, e.g. "Auth tokens are stored only in the Keychain with <code>kSecAttrAccessibleWhenUnlockedThisDeviceOnly</code>."</li>
<li><strong>Automate static checks</strong> in CI (e.g. MobSF or semgrep rules) for obvious issues: hard-coded secrets, insecure WebView settings, cleartext traffic allowed.</li>
<li><strong>Schedule a MASTG-based assessment</strong> before major releases.</li>
</ol>
<h3>For testers: a typical MASTG workflow</h3>
<ol>
<li><strong>Set up the lab</strong>: rooted Android device or emulator, jailbroken iOS device (or Corellium-type virtualisation), intercepting proxy, Frida/objection, jadx/Ghidra, MobSF.</li>
<li><strong>Static analysis</strong>: decompile the APK/IPA; review manifest/Info.plist (exported components, ATS exceptions, permissions); search for secrets, endpoints, insecure crypto.</li>
<li><strong>Dynamic analysis</strong>: install, intercept traffic (bypassing pinning if necessary to test the backend), inspect files written to the sandbox, logs and backups, exercise IPC and deep links.</li>
<li><strong>Resilience testing</strong> (profile R): attempt to bypass root/jailbreak detection, hook functions, repackage the app.</li>
<li><strong>Backend testing</strong>: the API behind the app is tested with the API Top 10 and WSTG &mdash; mobile clients often expose APIs never meant to be called directly.</li>
<li><strong>Report</strong> each finding against its MASVS control and MASWE/MASTG test ID.</li>
</ol>
<div class="callout"><strong>Common pitfall.</strong> Treating client-side resilience as a security boundary.
Obfuscation and root detection slow attackers down; they never replace server-side authorisation. MASVS-RESILIENCE
is explicitly an add-on, not a substitute for the other groups.</div>
""")
