# -*- coding: utf-8 -*-
# Chapter content, part 2: IoT, AI, threat frameworks, OT.
from content1 import ch, glance

ch("Part II &middot; Application, API, Mobile and IoT Security", "iottop10",
   "OWASP IoT Top 10", "The top security risks for Internet of Things devices (2018)",
glance([
 ("Area", "IoT devices and their ecosystems"),
 ("Type", "Risk awareness list"),
 ("Maintained by", "OWASP Internet of Things Project; current list 2018"),
 ("Mandatory?", "No. Used for scoping assessments and as a design checklist"),
 ("Use it for", "Scoping and checklist for IoT device assessments"),
 ("Link", '<a href="https://owasp.org/www-project-internet-of-things/">owasp.org/www-project-internet-of-things</a>'),
]) + """
<h2>What it is</h2>
<p>An IoT product is never just a device. It is an <em>ecosystem</em>: the hardware and firmware, the companion mobile
app, the cloud backend and APIs, the update infrastructure, and local network protocols (Wi-Fi, BLE, Zigbee, MQTT).
The OWASP IoT Top 10 highlights the ten things that most often go wrong across that ecosystem. Although the list
dates from 2018, it remains an accurate description of the issues found in assessments today, and it directly
influenced later regulation.</p>

<h2>The list</h2>
<table class="data"><thead><tr><th>ID</th><th>Risk</th><th>Typical example</th></tr></thead><tbody>
<tr><td>I1</td><td>Weak, Guessable, or Hardcoded Passwords</td><td>Default <code>admin/admin</code>, the same password on every unit, backdoor accounts in firmware.</td></tr>
<tr><td>I2</td><td>Insecure Network Services</td><td>Telnet or debug services exposed; UPnP opening ports to the internet.</td></tr>
<tr><td>I3</td><td>Insecure Ecosystem Interfaces</td><td>Weak authorisation in the cloud API or mobile app that controls the device.</td></tr>
<tr><td>I4</td><td>Lack of Secure Update Mechanism</td><td>Unsigned firmware, updates over HTTP, no rollback protection, no update notifications.</td></tr>
<tr><td>I5</td><td>Use of Insecure or Outdated Components</td><td>Old BusyBox, OpenSSL or Linux kernels; vulnerable third-party SDKs.</td></tr>
<tr><td>I6</td><td>Insufficient Privacy Protection</td><td>Personal data collected and stored without need or consent.</td></tr>
<tr><td>I7</td><td>Insecure Data Transfer and Storage</td><td>Cleartext protocols, unencrypted secrets in flash.</td></tr>
<tr><td>I8</td><td>Lack of Device Management</td><td>No asset tracking, monitoring, decommissioning or update management at fleet level.</td></tr>
<tr><td>I9</td><td>Insecure Default Settings</td><td>Insecure out-of-the-box configuration that users cannot change or harden.</td></tr>
<tr><td>I10</td><td>Lack of Physical Hardening</td><td>Exposed UART/JTAG headers, readable flash chips, no secure boot.</td></tr>
</tbody></table>

<h2>How it is brought into practice</h2>
<h3>Scoping an IoT assessment</h3>
<p>Use the ten items as scoping questions. Each maps to a part of the ecosystem and therefore a test workstream:</p>
<ul>
<li><strong>Hardware workstream</strong> (I10, I1, I7): teardown, identify debug ports, dump flash, extract firmware, look for secrets.</li>
<li><strong>Firmware workstream</strong> (I1, I4, I5, I9): unpack with binwalk or similar, review filesystem, generate an SBOM and match components to CVEs, emulate services, analyse the update process.</li>
<li><strong>Network workstream</strong> (I2, I7): port scan, protocol analysis, radio testing (BLE, Zigbee, sub-GHz) where in scope.</li>
<li><strong>Ecosystem workstream</strong> (I3, I6, I8): test mobile app (MASTG), cloud APIs (API Top 10), web portal (WSTG), and privacy flows.</li>
</ul>
<h3>Practical test plan tips</h3>
<ol>
<li>Ask the vendor for <strong>at least two units</strong> (one may be destroyed in hardware testing) and for firmware images.</li>
<li>Test the <strong>update path end-to-end</strong>: can you install modified firmware? Can you downgrade to a vulnerable version?</li>
<li>Check whether <strong>secrets are per-device or global</strong> &mdash; a global key extracted from one unit compromises the whole fleet.</li>
<li>Map findings to the <strong>regulatory baseline</strong> the product must meet (ETSI EN 303 645, UK PSTI, EU Cyber Resilience Act / RED delegated act). The IoT Top 10 is not itself a compliance standard, but most items line up with mandatory provisions.</li>
</ol>
<div class="callout"><strong>Going deeper.</strong> OWASP also maintains the <em>IoT Security Testing Guide (ISTG)</em> and
the <em>Firmware Security Testing Methodology (FSTM)</em>, which provide step-by-step test cases. Use the Top 10 to
scope and communicate; use those guides to execute.</div>
""")

# --------------------------------------------------------------------------
ch("Part II &middot; Application, API, Mobile and IoT Security", "etsi303645",
   "ETSI EN 303 645", "Cyber Security for Consumer Internet of Things: Baseline Requirements",
glance([
 ("Area", "Consumer IoT products"),
 ("Type", "European Standard (EN) with mandatory and recommended provisions"),
 ("Published by", "ETSI Technical Committee CYBER; first EN 2020 (v2.1.1), revised since"),
 ("Mandatory?", "Voluntary as a standard, but forms the basis of law: the UK PSTI regime mirrors its top provisions, and it feeds EU requirements and many national labelling schemes"),
 ("Use it for", "Baseline security requirements for consumer IoT"),
 ("Link", '<a href="https://www.etsi.org/standards">etsi.org/standards</a>'),
]) + """
<h2>What it is</h2>
<p>EN 303 645 is the first globally applicable baseline for consumer IoT security. It covers products such as smart
cameras, speakers, TVs, wearables, home assistants, connected appliances, door locks and baby monitors. It is designed
to be <strong>outcome-focused</strong> (it says what must be achieved, not how) and <strong>achievable</strong> for
manufacturers of any size. Its companion specification, <strong>ETSI TS 103 701</strong>, defines how to assess
conformance.</p>

<h2>The thirteen provision groups</h2>
<table class="data"><thead><tr><th>Clause</th><th>Provision</th><th>What it means in practice</th></tr></thead><tbody>
<tr><td>5.1</td><td>No universal default passwords</td><td>Passwords must be unique per device or set by the user. Brute-force protections required.</td></tr>
<tr><td>5.2</td><td>Implement a means to manage reports of vulnerabilities</td><td>Publish a vulnerability disclosure policy with a contact point and timelines.</td></tr>
<tr><td>5.3</td><td>Keep software updated</td><td>Secure, authenticated updates; publish the defined support period.</td></tr>
<tr><td>5.4</td><td>Securely store sensitive security parameters</td><td>No hard-coded critical credentials in firmware; use secure storage.</td></tr>
<tr><td>5.5</td><td>Communicate securely</td><td>Best-practice cryptography for security-relevant communications.</td></tr>
<tr><td>5.6</td><td>Minimise exposed attack surfaces</td><td>Disable unused interfaces and services; least privilege; no exposed debug.</td></tr>
<tr><td>5.7</td><td>Ensure software integrity</td><td>Secure boot or equivalent integrity verification.</td></tr>
<tr><td>5.8</td><td>Ensure that personal data is secure</td><td>Protect personal data in transit and at rest.</td></tr>
<tr><td>5.9</td><td>Make systems resilient to outages</td><td>Keep working locally when network or power is lost; recover cleanly.</td></tr>
<tr><td>5.10</td><td>Examine system telemetry data</td><td>If telemetry is collected, check it for security anomalies.</td></tr>
<tr><td>5.11</td><td>Make it easy for users to delete user data</td><td>Simple factory reset and data deletion, including in the cloud.</td></tr>
<tr><td>5.12</td><td>Make installation and maintenance of devices easy</td><td>Secure setup with minimal steps and clear guidance.</td></tr>
<tr><td>5.13</td><td>Validate input data</td><td>Validate data from user interfaces, APIs and networks.</td></tr>
</tbody></table>
<p>Clause 6 adds data protection provisions: tell users what personal data is processed and why, obtain valid
consent where needed, and let users withdraw it. Each provision is marked as <strong>mandatory</strong> (M),
<strong>recommended</strong> (R), or <strong>conditional</strong> (applies only when a feature exists, e.g. if the
device has an update mechanism).</p>

<h2>Regulatory connections</h2>
<ul>
<li><strong>UK Product Security and Telecommunications Infrastructure (PSTI) regime</strong> (in force since April 2024) legally requires the essence of 5.1, 5.2 and 5.3 for consumer connectable products sold in the UK. Conformance with the corresponding EN 303 645 provisions is accepted as a route to compliance.</li>
<li><strong>EU</strong>: the Radio Equipment Directive delegated act (with the harmonised EN 18031 series) and the Cyber Resilience Act raise the bar further; EN 303 645 is a strong foundation for both.</li>
<li><strong>Labelling schemes</strong> in several countries (e.g. Finland, Singapore, Germany) build on EN 303 645.</li>
</ul>

<h2>How it is brought into practice</h2>
<h3>For a manufacturer</h3>
<ol>
<li><strong>Gap analysis</strong>: list every provision, decide whether it applies (conditional provisions), and record current status.</li>
<li><strong>Implementation conformance statement (ICS)</strong>: TS 103 701 expects the manufacturer to declare, per provision, whether it is supported and how, and to justify any recommended provision not implemented.</li>
<li><strong>Engineering work</strong>: typical changes are per-device passwords printed on labels, a signed update pipeline, secure boot, closing debug ports, and a published support period.</li>
<li><strong>Process work</strong>: a vulnerability disclosure policy and a team to triage reports (5.2); a defined security update policy (5.3).</li>
<li><strong>Assessment</strong>: self-assessment or third-party lab testing against TS 103 701, often leading to a certificate or label.</li>
</ol>
<h3>For a tester</h3>
<p>Use TS 103 701's test cases as the conformance checklist and the OWASP IoT Top 10 / ISTG as the technical
attack-driven complement. Report findings with both references, e.g. "Hard-coded root password in firmware &mdash; OWASP
I1; fails EN 303 645 provisions 5.1-1 and 5.4-3".</p>
<div class="callout"><strong>Tip.</strong> Always check the current version on the ETSI portal; provision numbering
is stable but wording and the set of conditional provisions have been refined across releases.</div>
""")

# --------------------------------------------------------------------------
ch("Part III &middot; Artificial Intelligence Security and Risk", "llmtop10",
   "OWASP Top 10 for LLM Applications", "The top risks for applications built on large language models (2025 edition)",
glance([
 ("Area", "AI / LLM applications, including RAG systems and agents"),
 ("Type", "Risk awareness list with mitigations"),
 ("Maintained by", "OWASP GenAI Security Project; first edition 2023, current edition 2025"),
 ("Mandatory?", "No. Rapidly becoming the standard scoping document for AI application tests"),
 ("Use it for", "Scoping and checklist for AI / LLM testing"),
 ("Link", '<a href="https://genai.owasp.org/">genai.owasp.org</a>'),
]) + """
<h2>What it is</h2>
<p>LLM applications introduce a new kind of attack surface: the model treats instructions and data as the same
thing (natural language), its output is non-deterministic, and it is increasingly connected to tools, data stores
and other systems. The OWASP Top 10 for LLM Applications lists the most critical risks for systems that use LLMs,
covering not just the model but the surrounding application: prompts, retrieval pipelines, plugins/tools, and output
handling.</p>

<h2>The 2025 list</h2>
<table class="data"><thead><tr><th>ID</th><th>Risk</th><th>In plain terms</th></tr></thead><tbody>
<tr><td>LLM01</td><td>Prompt Injection</td><td>User input (direct) or content the model reads, such as web pages, emails or documents (indirect), overrides the intended instructions.</td></tr>
<tr><td>LLM02</td><td>Sensitive Information Disclosure</td><td>The model or app reveals personal data, secrets, proprietary data or other users' content.</td></tr>
<tr><td>LLM03</td><td>Supply Chain</td><td>Compromised or untrustworthy models, datasets, fine-tuning adapters, or libraries.</td></tr>
<tr><td>LLM04</td><td>Data and Model Poisoning</td><td>Manipulated training, fine-tuning or embedding data introduces backdoors or bias.</td></tr>
<tr><td>LLM05</td><td>Improper Output Handling</td><td>Model output is passed to browsers, shells, SQL or other systems without validation (XSS, RCE, injection).</td></tr>
<tr><td>LLM06</td><td>Excessive Agency</td><td>The LLM has too many tools, too much permission or too much autonomy, so a manipulated model can do real damage.</td></tr>
<tr><td>LLM07</td><td>System Prompt Leakage</td><td>The system prompt is extracted and reveals secrets, logic or guardrail details (system prompts should never contain secrets).</td></tr>
<tr><td>LLM08</td><td>Vector and Embedding Weaknesses</td><td>RAG weaknesses: cross-tenant leakage in vector stores, poisoned documents, embedding inversion.</td></tr>
<tr><td>LLM09</td><td>Misinformation</td><td>Confident but false output (hallucination) that users or systems rely on.</td></tr>
<tr><td>LLM10</td><td>Unbounded Consumption</td><td>Uncontrolled inference cost or resource use: denial of wallet, model extraction via mass querying.</td></tr>
</tbody></table>

<h2>How it is brought into practice</h2>
<h3>Scoping an LLM application test</h3>
<ol>
<li><strong>Draw the data flow</strong>: user &rarr; app &rarr; system prompt + retrieved context &rarr; model &rarr; output &rarr; tools/downstream systems. Every arrow where untrusted text enters is a prompt injection point.</li>
<li><strong>List tools and permissions</strong> the model can invoke (email, file access, code execution, database queries, payments). This defines the blast radius for LLM06.</li>
<li><strong>Identify trust boundaries in RAG</strong>: who can write documents that end up in the index? Is retrieval filtered by the user's permissions? (LLM08, LLM02)</li>
<li><strong>Agree on cost limits</strong> for testing (LLM10) and on whether testers may attempt jailbreaks that produce harmful content.</li>
</ol>
<h3>Testing activities by risk</h3>
<ul>
<li><strong>LLM01</strong>: direct jailbreak and instruction-override attempts; indirect injection by planting instructions in documents, web pages, emails or tool outputs the model will read; test whether injected instructions can trigger tools.</li>
<li><strong>LLM02/LLM07</strong>: attempt extraction of system prompts, other users' conversation data, and data from documents the user should not see.</li>
<li><strong>LLM05</strong>: make the model emit HTML/JavaScript, Markdown image links (data exfiltration), SQL or shell syntax and see whether downstream components execute it.</li>
<li><strong>LLM06</strong>: chain injection with tool use: can a malicious document make the agent send an email or delete a file? Is there human approval for sensitive actions?</li>
<li><strong>LLM08</strong>: test tenant isolation in the vector store; plant poisoned documents and see if they surface for other users.</li>
<li><strong>LLM10</strong>: test rate limits, maximum context sizes and per-user cost caps.</li>
</ul>
<h3>Defensive implementation</h3>
<ul>
<li>Treat <strong>all model output as untrusted user input</strong>: encode, validate and sandbox it.</li>
<li>Apply <strong>least privilege</strong> to tools; require human confirmation for high-impact actions; scope credentials per user, not per app.</li>
<li>Enforce <strong>authorisation outside the model</strong>: filter retrieval results by the caller's permissions before they reach the prompt.</li>
<li>Use layered guardrails (input/output classifiers), but never as the only control: prompt injection has no complete fix today.</li>
<li>Build an <strong>evaluation suite</strong> of adversarial prompts mapped to Top 10 IDs and run it in CI whenever prompts, models or tools change.</li>
</ul>
<div class="callout"><strong>Related.</strong> The OWASP GenAI Security Project also publishes guidance for agentic AI
systems (threats such as tool misuse, memory poisoning and identity abuse in autonomous agents). Use it alongside the
Top 10 when the application is an agent rather than a chatbot. Map attack techniques to MITRE ATLAS and govern overall
AI risk with the NIST AI RMF.</div>
""")

# --------------------------------------------------------------------------
ch("Part III &middot; Artificial Intelligence Security and Risk", "atlas",
   "MITRE ATLAS", "Adversarial Threat Landscape for Artificial-Intelligence Systems",
glance([
 ("Area", "AI / ML systems"),
 ("Type", "Knowledge base of adversary tactics, techniques and case studies"),
 ("Maintained by", "MITRE, with industry and government collaborators"),
 ("Mandatory?", "No. Used for threat modelling, red teaming and detection engineering"),
 ("Use it for", "Adversary techniques against AI/ML, for threat modelling"),
 ("Link", '<a href="https://atlas.mitre.org/">atlas.mitre.org</a>'),
]) + """
<h2>What it is</h2>
<p>ATLAS does for AI systems what ATT&amp;CK does for enterprise IT: it catalogues <em>how</em> real adversaries attack
AI-enabled systems, organised as tactics (the adversary's goal) and techniques (how they achieve it), backed by real-world
and red-team <strong>case studies</strong>. It deliberately reuses ATT&amp;CK's structure and many of its tactics so that
security teams can extend existing threat models to cover AI components.</p>

<h2>Structure</h2>
<p>ATLAS tactics include the familiar ATT&amp;CK ones &mdash; Reconnaissance, Resource Development, Initial Access,
Execution, Persistence, Privilege Escalation, Defense Evasion, Credential Access, Discovery, Collection, Command and
Control, Exfiltration and Impact &mdash; plus AI-specific tactics:</p>
<ul>
<li><strong>AI Model Access</strong> &mdash; how the adversary gains access to the model: via an inference API, an AI-enabled product, physical environment access, or full model access.</li>
<li><strong>AI Attack Staging</strong> &mdash; preparing the attack: training proxy (surrogate) models, crafting adversarial data, backdooring models, verifying attacks offline.</li>
</ul>
<p>Techniques have IDs prefixed <code>AML.T</code>. Examples:</p>
<table class="data"><thead><tr><th>Technique</th><th>Description</th></tr></thead><tbody>
<tr><td>LLM Prompt Injection (AML.T0051)</td><td>Crafting inputs that cause an LLM to ignore its instructions; direct and indirect variants.</td></tr>
<tr><td>LLM Jailbreak</td><td>Bypassing model safety controls to produce restricted output.</td></tr>
<tr><td>Poison Training Data (AML.T0020)</td><td>Inserting malicious samples to degrade or backdoor a model.</td></tr>
<tr><td>Craft Adversarial Data (AML.T0043)</td><td>Inputs perturbed to cause misclassification (e.g. evading a malware or fraud classifier).</td></tr>
<tr><td>Exfiltration via AI Inference API (AML.T0024)</td><td>Model inversion, membership inference, or model extraction by querying the API.</td></tr>
<tr><td>Discover AI Model Ontology / Family</td><td>Learning what model and outputs a system uses to tailor attacks.</td></tr>
<tr><td>Publish Poisoned Models / Datasets</td><td>Supply-chain attacks via public model hubs and datasets.</td></tr>
</tbody></table>
<p class="small">Technique names and IDs evolve between ATLAS releases; always reference the current matrix.</p>
<p>ATLAS also lists <strong>mitigations</strong> (e.g. limit model query rate, sanitise training data, use ensemble
methods, control access to model artefacts) and <strong>case studies</strong> of real incidents and research
demonstrations, which are valuable for convincing stakeholders that a threat is real.</p>

<h2>How it is brought into practice</h2>
<h3>Threat modelling AI systems</h3>
<ol>
<li><strong>Decompose the AI system</strong>: data sources, training pipeline, model registry, serving infrastructure, application layer, and users.</li>
<li><strong>Walk the ATLAS matrix</strong> left to right for each component and ask "is this technique possible here?". Record plausible techniques with likelihood and impact.</li>
<li><strong>Combine with ATT&amp;CK</strong> for the conventional infrastructure (an attacker who compromises the training cluster via phishing is using ATT&amp;CK techniques to reach an ATLAS goal).</li>
<li><strong>Select mitigations</strong> from ATLAS and from your control frameworks (e.g. NIST AI RMF, ISO/IEC 27001 and AI-specific controls).</li>
</ol>
<h3>AI red teaming</h3>
<ul>
<li>Use ATLAS tactics to structure the red team plan and the report narrative, just as ATT&amp;CK structures conventional red team reports.</li>
<li>Tag every finding with ATLAS technique IDs, and with OWASP LLM Top 10 IDs where it is an LLM application flaw. ATLAS describes <em>adversary behaviour</em>; the OWASP list describes <em>application weaknesses</em>. The two are complementary.</li>
<li>Re-use case studies as attack scenarios for exercises.</li>
</ul>
<h3>Detection engineering</h3>
<p>For deployed models, map telemetry (query logs, input distribution monitoring, abnormal query volumes) to ATLAS
techniques it can detect, and identify gaps. For example, high-volume systematic querying can indicate model
extraction (exfiltration via inference API).</p>
""")

# --------------------------------------------------------------------------
ch("Part III &middot; Artificial Intelligence Security and Risk", "airmf",
   "NIST AI RMF", "Artificial Intelligence Risk Management Framework (AI RMF 1.0)",
glance([
 ("Area", "AI governance and risk management"),
 ("Type", "Voluntary risk management framework with Playbook and profiles"),
 ("Published by", "NIST, January 2023 (NIST AI 100-1); Generative AI Profile (NIST AI 600-1) July 2024"),
 ("Mandatory?", "Voluntary. Widely referenced by US agencies, regulators and enterprises; complements ISO/IEC 42001 and the EU AI Act"),
 ("Use it for", "Governance and risk framework for AI systems"),
 ("Link", '<a href="https://www.nist.gov/itl/ai-risk-management-framework">nist.gov/itl/ai-risk-management-framework</a>'),
]) + """
<h2>What it is</h2>
<p>The AI RMF helps organisations manage the risks of designing, developing, deploying and using AI systems. It is
broader than security: it covers any way an AI system can harm people, organisations or society, and frames these
risks around building <strong>trustworthy AI</strong>. It is non-sector-specific, use-case agnostic and voluntary.</p>

<h2>Trustworthiness characteristics</h2>
<p>The framework defines seven characteristics of trustworthy AI, used as the lens for identifying and measuring risk:</p>
<ul>
<li><strong>Valid and reliable</strong> (the foundation for the others)</li>
<li><strong>Safe</strong></li>
<li><strong>Secure and resilient</strong></li>
<li><strong>Accountable and transparent</strong></li>
<li><strong>Explainable and interpretable</strong></li>
<li><strong>Privacy-enhanced</strong></li>
<li><strong>Fair, with harmful bias managed</strong></li>
</ul>

<h2>The four core functions</h2>
<table class="data"><thead><tr><th>Function</th><th>Purpose</th><th>Example outcomes</th></tr></thead><tbody>
<tr><td><strong>GOVERN</strong></td><td>Cultivate a culture of risk management; cross-cutting, informs all other functions.</td><td>AI policies and accountability; roles and training; risk tolerance defined; processes for third-party AI; workforce diversity considered.</td></tr>
<tr><td><strong>MAP</strong></td><td>Establish context and identify risks for a specific AI system.</td><td>Intended purpose and context documented; categorisation of the system; benefits and costs; impacts on individuals and groups identified.</td></tr>
<tr><td><strong>MEASURE</strong></td><td>Analyse, assess, benchmark and monitor risks and trustworthiness.</td><td>Metrics selected; system evaluated for trustworthiness (including security testing and red teaming); mechanisms for tracking risks over time.</td></tr>
<tr><td><strong>MANAGE</strong></td><td>Prioritise and act on risks based on projected impact.</td><td>Risk responses (mitigate, transfer, avoid, accept); third-party risks monitored; incident response and recovery; decommissioning plans.</td></tr>
</tbody></table>
<p>Each function is broken into categories and subcategories (e.g. GOVERN 1.1, MAP 2.3), and the companion
<strong>AI RMF Playbook</strong> suggests concrete actions, documentation and references for each subcategory.</p>

<h2>Profiles</h2>
<p>Profiles tailor the framework to a sector, technology or use case. The most important is the
<strong>Generative AI Profile (NIST AI 600-1)</strong>, which identifies risks that are unique to or exacerbated by
generative AI &mdash; such as confabulation, information integrity, information security (including prompt injection and
data poisoning), harmful bias, data privacy, intellectual property, and value chain/component integration &mdash; and maps
suggested actions to the AI RMF subcategories.</p>

<h2>How it is brought into practice</h2>
<h3>Step 1: Govern &mdash; set up the programme</h3>
<ul>
<li>Create an AI policy and an AI risk committee (or extend an existing risk committee).</li>
<li>Build an <strong>AI inventory</strong>: every model and AI-enabled product in use or development, including third-party SaaS features.</li>
<li>Define risk tolerance and approval gates (e.g. high-impact uses need committee sign-off).</li>
</ul>
<h3>Step 2: Map &mdash; for each AI system</h3>
<ul>
<li>Complete an AI impact assessment template: purpose, users, affected people, data sources, model provenance, deployment context, failure modes.</li>
<li>Categorise the system (e.g. low/medium/high impact) to determine the depth of measurement required.</li>
</ul>
<h3>Step 3: Measure</h3>
<ul>
<li>Define metrics for each relevant trustworthiness characteristic: accuracy and robustness benchmarks, bias metrics, privacy tests.</li>
<li>Commission <strong>security testing and red teaming</strong>: this is where the OWASP LLM Top 10 and MITRE ATLAS plug in as the technical methods.</li>
<li>Set up production monitoring (drift, abuse, incidents).</li>
</ul>
<h3>Step 4: Manage</h3>
<ul>
<li>Record risks in the risk register with owners and treatment decisions.</li>
<li>Implement mitigations; document residual risk acceptance.</li>
<li>Integrate AI incidents into incident response; plan for model rollback and decommissioning.</li>
</ul>
<div class="callout"><strong>Crosswalks.</strong> NIST publishes crosswalks from the AI RMF to ISO/IEC 42001 (AI
management systems), ISO/IEC 23894 (AI risk management) and the EU AI Act. Organisations already certified to ISO/IEC
27001 often implement AI RMF practices inside their existing ISMS and then pursue ISO/IEC 42001 certification.</div>
""")

# --------------------------------------------------------------------------
ch("Part IV &middot; Adversary Behaviour and Operational Technology", "attack",
   "MITRE ATT&amp;CK for Enterprise", "Adversarial Tactics, Techniques and Common Knowledge",
glance([
 ("Area", "Enterprise IT: Windows, macOS, Linux, cloud, network, containers, identity"),
 ("Type", "Knowledge base of real-world adversary behaviour"),
 ("Maintained by", "MITRE; public since 2015, updated twice a year"),
 ("Mandatory?", "No. The common language of threat intelligence, red teaming and detection engineering"),
 ("Use it for", "Threat modelling and mapping findings to detections"),
 ("Link", '<a href="https://attack.mitre.org/">attack.mitre.org</a>'),
]) + """
<h2>What it is</h2>
<p>ATT&amp;CK is a curated knowledge base of tactics and techniques that adversaries have actually used, built from
public threat intelligence and incident reporting. It answers the question "<em>how</em> do attackers operate once they
target us?" in a structured, shared vocabulary. Instead of saying "the attacker moved around the network", teams can say
"T1021.002 &mdash; Remote Services: SMB/Windows Admin Shares", and everyone from the threat intel analyst to the SOC
engineer to the auditor knows exactly what is meant.</p>

<h2>Structure</h2>
<ul>
<li><strong>Tactics</strong> (the "why"): the adversary's tactical goal. Enterprise ATT&amp;CK has 14: Reconnaissance, Resource Development, Initial Access, Execution, Persistence, Privilege Escalation, Defense Evasion, Credential Access, Discovery, Lateral Movement, Collection, Command and Control, Exfiltration, Impact.</li>
<li><strong>Techniques and sub-techniques</strong> (the "how"): e.g. T1566 Phishing &rarr; T1566.001 Spearphishing Attachment.</li>
<li><strong>Procedures</strong>: specific examples of how a named group or malware implemented a technique.</li>
<li><strong>Groups</strong> (threat actors, e.g. APT29), <strong>Software</strong> (malware and tools) and <strong>Campaigns</strong>.</li>
<li><strong>Mitigations</strong> (e.g. M1032 Multi-factor Authentication) and <strong>detection</strong> guidance (data sources and, in recent versions, detection strategies and analytics).</li>
</ul>
<p class="small">Tactic and technique sets change between releases (MITRE publishes new versions roughly every six
months). Always cite the ATT&amp;CK version you used.</p>

<h2>How it is brought into practice</h2>
<h3>1. Threat-informed defence and threat modelling</h3>
<ol>
<li>Identify threat groups relevant to your sector and geography (using ATT&amp;CK Groups and your threat intelligence).</li>
<li>Load their techniques into <strong>ATT&amp;CK Navigator</strong> to create a heat-map layer of "techniques used against organisations like us".</li>
<li>Overlay a second layer showing your detection and prevention coverage. The gaps are your priorities.</li>
</ol>
<h3>2. Detection engineering</h3>
<ul>
<li>Tag every SIEM/EDR detection rule with the techniques it covers (Sigma rules support ATT&amp;CK tags natively).</li>
<li>Track coverage per technique as a KPI, but measure <em>quality</em> (tested, low false positive rate) rather than counting rules.</li>
<li>Validate detections with <strong>atomic tests</strong> (e.g. Atomic Red Team) and purple-team exercises mapped to technique IDs.</li>
</ul>
<h3>3. Red teaming and penetration testing</h3>
<ul>
<li>Plan adversary emulation around a chosen threat group's technique set (MITRE's adversary emulation plans and the Center for Threat-Informed Defense resources help here).</li>
<li>In pentest reports, describe the attack path as a sequence of ATT&amp;CK techniques. This lets the blue team check, technique by technique, whether they saw the activity.</li>
<li>For each finding, add "detection opportunity" notes using the technique's detection guidance.</li>
</ul>
<div class="example"><div class="ex-h">Example: an internal pentest attack path mapped to ATT&amp;CK</div>
<table class="data"><thead><tr><th>Step</th><th>Activity</th><th>Technique</th><th>Detected?</th></tr></thead><tbody>
<tr><td>1</td><td>Phishing email with macro document</td><td>T1566.001 Spearphishing Attachment</td><td>Yes (mail gateway)</td></tr>
<tr><td>2</td><td>Macro launches PowerShell</td><td>T1059.001 PowerShell</td><td>No</td></tr>
<tr><td>3</td><td>LLMNR/NBT-NS poisoning captures hashes</td><td>T1557.001 LLMNR/NBT-NS Poisoning</td><td>No</td></tr>
<tr><td>4</td><td>Kerberoasting service account</td><td>T1558.003 Kerberoasting</td><td>No</td></tr>
<tr><td>5</td><td>Lateral movement via admin shares</td><td>T1021.002 SMB/Windows Admin Shares</td><td>Alert, not triaged</td></tr>
<tr><td>6</td><td>Dump credentials from LSASS</td><td>T1003.001 LSASS Memory</td><td>Yes (EDR blocked first attempt)</td></tr>
</tbody></table></div>
<h3>4. Security architecture and control mapping</h3>
<p>MITRE and the Center for Threat-Informed Defense publish mappings from ATT&amp;CK techniques to NIST SP 800-53
controls, CIS Controls, cloud-native security services and more. These let you answer "which controls actually stop the
techniques our adversaries use?" and justify investment in board-level language.</p>
""")

# --------------------------------------------------------------------------
ch("Part IV &middot; Adversary Behaviour and Operational Technology", "attackics",
   "MITRE ATT&amp;CK for ICS", "Adversary tactics and techniques against industrial control systems",
glance([
 ("Area", "Operational technology (OT) and industrial control systems (ICS)"),
 ("Type", "Knowledge base of adversary behaviour in ICS environments"),
 ("Maintained by", "MITRE; launched 2020"),
 ("Mandatory?", "No. Widely used by OT security vendors, asset owners and ICS-CERT style advisories"),
 ("Use it for", "Threat modelling for OT/ICS assessments"),
 ("Link", '<a href="https://attack.mitre.org/techniques/ics/">attack.mitre.org/techniques/ics</a>'),
]) + """
<h2>What it is</h2>
<p>Industrial environments differ fundamentally from enterprise IT. The ultimate targets are physical processes:
turbines, valves, pumps, robots, chemical reactors. Attacks aim to cause unsafe conditions, damage or loss of
production, not just data theft. ATT&amp;CK for ICS captures adversary behaviour specific to these environments, based
on real incidents such as attacks on Ukrainian power grids, TRITON/TRISIS against safety instrumented systems,
Stuxnet, and Industroyer.</p>

<h2>Structure</h2>
<p>ATT&amp;CK for ICS has its own set of tactics, including two that have no direct enterprise equivalent:</p>
<table class="data"><thead><tr><th>Tactic</th><th>Adversary goal</th></tr></thead><tbody>
<tr><td>Initial Access</td><td>Get into the ICS environment (e.g. via engineering workstation, remote access, supply chain).</td></tr>
<tr><td>Execution</td><td>Run code or commands, e.g. through the controller's native interfaces.</td></tr>
<tr><td>Persistence</td><td>Maintain access, e.g. modify controller program or firmware.</td></tr>
<tr><td>Privilege Escalation</td><td>Gain higher-level permissions.</td></tr>
<tr><td>Evasion</td><td>Avoid detection, e.g. spoof reporting messages, rootkits on controllers.</td></tr>
<tr><td>Discovery</td><td>Locate PLCs, RTUs, HMIs; enumerate I/O and points.</td></tr>
<tr><td>Lateral Movement</td><td>Move through the ICS network, often via default credentials or program download.</td></tr>
<tr><td>Collection</td><td>Gather process knowledge: point and tag identification, program upload, screen capture.</td></tr>
<tr><td>Command and Control</td><td>Communicate with compromised systems, often over standard industrial protocols.</td></tr>
<tr><td><strong>Inhibit Response Function</strong></td><td>Prevent safety, protection and quality functions from responding: block alarms, disable safety systems, put devices in an unrecoverable state.</td></tr>
<tr><td><strong>Impair Process Control</strong></td><td>Manipulate, disable or damage physical control: modify parameters, send unauthorised command messages, spoof I/O.</td></tr>
<tr><td>Impact</td><td>The end effect: damage to property, loss of control, loss of view, loss of safety, loss of productivity and revenue.</td></tr>
</tbody></table>
<p>Example techniques: <em>Unauthorized Command Message</em> (T0855), <em>Modify Parameter</em> (T0836), <em>Modify
Program</em> (T0889), <em>Device Restart/Shutdown</em> (T0816), <em>Manipulation of View</em> (T0832). The matrix also
models <strong>assets</strong> (PLC, HMI, engineering workstation, safety controller, historian, RTU) so each technique
can be tied to the asset types it affects.</p>

<h2>How it is brought into practice</h2>
<h3>Threat modelling OT sites</h3>
<ol>
<li><strong>Build the asset inventory and network model</strong>, typically aligned to the Purdue reference model levels (0 field devices, 1 controllers, 2 supervisory, 3 site operations, 3.5 DMZ, 4&ndash;5 enterprise).</li>
<li><strong>Identify crown-jewel processes</strong> and the "consequences that matter" (e.g. a toxic release, an explosion, a city blackout), an approach known as consequence-driven engineering.</li>
<li><strong>Trace attack paths</strong> using enterprise ATT&amp;CK to reach the OT boundary and ICS ATT&amp;CK inside it, focusing on paths that end in Inhibit Response Function and Impair Process Control.</li>
<li><strong>Map controls</strong> (ISA/IEC 62443 requirements, network segmentation, monitoring) to each technique.</li>
</ol>
<h3>Safe OT assessments</h3>
<p>Testing in OT is very different from IT. Active scanning can crash fragile controllers. Good practice:</p>
<ul>
<li>Prefer <strong>passive</strong> techniques (traffic capture, configuration review, architecture review) on production.</li>
<li>Perform active testing on <strong>test benches, spares or digital twins</strong>, or during planned outages.</li>
<li>Involve the asset owner's operations and safety engineers in planning and during testing.</li>
<li>Report findings with their ICS technique and the physical consequence they could enable.</li>
</ul>
<h3>Detection in OT</h3>
<p>OT network monitoring platforms map alerts (e.g. unexpected program download to a PLC, new Modbus write function
codes) to ICS techniques. Asset owners use the matrix to assess monitoring coverage, just as IT SOCs do with Enterprise
ATT&amp;CK.</p>
""")

# --------------------------------------------------------------------------
ch("Part IV &middot; Adversary Behaviour and Operational Technology", "iec62443",
   "ISA/IEC 62443", "Security for Industrial Automation and Control Systems",
glance([
 ("Area", "Operational technology / industrial automation and control systems (IACS)"),
 ("Type", "International standards series (requirements, processes, certification)"),
 ("Published by", "ISA99 committee and IEC TC65; adopted as IEC standards"),
 ("Mandatory?", "Voluntary internationally, but required by many asset owners in procurement, referenced by regulators, and the basis of ISASecure and IECEE certification"),
 ("Use it for", "Zones/conduits model and OT security requirements"),
 ("Link", '<a href="https://www.isa.org/standards-and-publications/isa-standards">isa.org/standards-and-publications/isa-standards</a>'),
]) + """
<h2>What it is</h2>
<p>ISA/IEC 62443 is the reference set of standards for securing industrial automation and control systems. Its key
idea is that OT security is a <strong>shared responsibility</strong> across three roles &mdash; the <em>asset owner</em>
(who runs the plant), the <em>system integrator / service provider</em> (who designs, builds and maintains the system),
and the <em>product supplier</em> (who builds the components) &mdash; and it gives each role its own requirements.</p>

<h2>Structure of the series</h2>
<table class="data"><thead><tr><th>Group</th><th>Key documents</th><th>Who it is for</th></tr></thead><tbody>
<tr><td>1 &mdash; General</td><td>62443-1-1 Concepts and models; terminology; metrics</td><td>Everyone</td></tr>
<tr><td>2 &mdash; Policies and procedures</td><td>62443-2-1 Security programme requirements for asset owners; 2-3 Patch management; 2-4 Requirements for IACS service providers</td><td>Asset owners, service providers</td></tr>
<tr><td>3 &mdash; System</td><td>62443-3-2 Security risk assessment and system design (zones and conduits); 3-3 System security requirements and security levels</td><td>Asset owners, integrators</td></tr>
<tr><td>4 &mdash; Component</td><td>62443-4-1 Secure product development lifecycle; 4-2 Technical security requirements for components</td><td>Product suppliers</td></tr>
</tbody></table>

<h2>Core concepts</h2>
<h3>Zones and conduits</h3>
<p>A <strong>zone</strong> is a grouping of assets that share the same security requirements (e.g. "Line 3 safety
system", "Control room HMIs"). A <strong>conduit</strong> is a grouping of communication channels between zones (e.g.
"historian replication from control zone to DMZ"). Security requirements are defined per zone and conduit, so you
protect the boundaries and the most critical zones most strongly. This is the OT equivalent of network segmentation
design, but driven by risk assessment.</p>
<h3>Seven foundational requirements (FRs)</h3>
<ol>
<li><strong>FR1</strong> Identification and authentication control</li>
<li><strong>FR2</strong> Use control</li>
<li><strong>FR3</strong> System integrity</li>
<li><strong>FR4</strong> Data confidentiality</li>
<li><strong>FR5</strong> Restricted data flow</li>
<li><strong>FR6</strong> Timely response to events</li>
<li><strong>FR7</strong> Resource availability</li>
</ol>
<p>62443-3-3 (systems) and 62443-4-2 (components) break each FR into detailed system requirements (SRs) / component
requirements (CRs) and requirement enhancements.</p>
<h3>Security levels (SL)</h3>
<table class="data"><thead><tr><th>SL</th><th>Protection against&hellip;</th></tr></thead><tbody>
<tr><td>SL 0</td><td>No specific requirements</td></tr>
<tr><td>SL 1</td><td>Casual or coincidental violation</td></tr>
<tr><td>SL 2</td><td>Intentional violation using simple means, low resources, generic skills, low motivation</td></tr>
<tr><td>SL 3</td><td>Intentional violation using sophisticated means, moderate resources, IACS-specific skills, moderate motivation</td></tr>
<tr><td>SL 4</td><td>Intentional violation using sophisticated means, extended resources, IACS-specific skills, high motivation (e.g. nation states)</td></tr>
</tbody></table>
<p>Three variants are used: <strong>SL-T</strong> (target, what a zone needs), <strong>SL-C</strong> (capability, what a
component or system can deliver) and <strong>SL-A</strong> (achieved, what is actually in place). The design goal is
SL-A &ge; SL-T for every zone and conduit. 62443-4-1 additionally defines <strong>maturity levels</strong> for a
supplier's development process.</p>

<h2>How it is brought into practice</h2>
<h3>Asset owner journey (62443-2-1 and 3-2)</h3>
<ol>
<li><strong>Establish the cybersecurity management system</strong> for OT (policy, roles, training, supplier requirements) per 62443-2-1.</li>
<li><strong>Inventory and define the System under Consideration (SuC)</strong>.</li>
<li><strong>High-level risk assessment</strong> to identify worst-case consequences.</li>
<li><strong>Partition into zones and conduits</strong>; draw the zone and conduit diagram.</li>
<li><strong>Detailed risk assessment</strong> per zone and conduit; assign an SL-T.</li>
<li><strong>Document cybersecurity requirements specification (CRS)</strong> for each zone/conduit.</li>
<li><strong>Procure</strong> systems and components with SL-C that meets SL-T (ask suppliers for 62443-4-1/4-2 certification and integrators for 2-4 compliance).</li>
<li><strong>Verify</strong> SL-A through assessments and testing, then operate, monitor and patch (62443-2-3).</li>
</ol>
<h3>Product supplier journey (62443-4-1 and 4-2)</h3>
<ul>
<li>Implement a secure development lifecycle: security requirements, secure design, secure implementation, verification and validation testing, defect management, patch management, product end-of-life, and security guidelines for users.</li>
<li>Design components to meet CRs at a target SL and obtain certification (e.g. ISASecure CSA/SDLA or IECEE schemes).</li>
</ul>
<h3>Assessors and testers</h3>
<p>OT assessments are often structured as a 62443 gap assessment: zone and conduit review, FR-by-FR evaluation of
SR compliance, and SL-A estimation. Technical testing results (ideally on non-production equipment) are mapped to FRs and
to ATT&amp;CK for ICS techniques.</p>
""")
