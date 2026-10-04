# AI for Cyber Security - Learner Guide

**Course code:** C434
**Duration:** 2 days · 15 hours (9:30am – 5:30pm)
**Version:** v1.0 · 4 October 2026

## Learning outcomes

- LO1: Identify security risks, threats, and assess gaps in controls impacting business processes.
- LO2: Translate security objectives into specific programmes considering security programme design techniques.
- LO3: Develop a detailed action plan for security programmes in line with information security architectures.
- LO4: Deliver advice for adoption of security architectures, monitoring their effectiveness against standards.

## Responsible use boundary

AI output is a hypothesis. Preserve raw evidence, protect sensitive data, state confidence and limitations, and require human approval for high-impact actions.

## Topic 1: AI-Assisted Security Risk, Threat and Control-Gap Analysis

**Alignment:** LO1

Telemetry contracts · detection models · business impact · analyst evidence

### Security telemetry is a governed evidence pipeline

**Runtime mechanism:** Collect → Normalize → Enrich → Score → Retain

**Concrete contract**

- `event_time: UTC timestamp`
- `principal.id: stable identity`
- `asset.criticality: 1-5`
- `action/outcome: attempted result`

**Decision analysis**

- Schema-first features survive tool changes
- Late events need event-time windows
- Asset context changes the same alert's risk
- Raw evidence remains immutable

**Failure and control**

- Failure: Clock skew creates false sequences
  Control/evidence: Parse success >= 99%
- Failure: Missing identity joins hide lateral movement
  Control/evidence: Field null rates tracked
- Failure: PII copied into prompts
  Control/evidence: Lineage links score to raw event
- Failure: Silent parser failures
  Control/evidence: Retention matches policy

Lab bridge: Lab 1 provides implementation and evidence checks.

### Risk scoring joins threat likelihood to business impact

**Runtime mechanism:** Threat → Exposure → Control gap → Impact → Decision

**Concrete contract**

- `risk = likelihood x impact`
- `likelihood = exploitability x exposure`
- `residual = inherent x (1-control_effectiveness)`
- `owner + due_date + evidence`

**Decision analysis**

- CVSS measures severity, not organisational priority
- EPSS estimates exploitation probability
- Criticality weights business consequence
- Confidence must travel with the score

**Failure and control**

- Failure: Single-number theatre
  Control/evidence: Top risks trace to assets
- Failure: Unbounded AI-generated severity
  Control/evidence: Sensitivity analysis recorded
- Failure: No risk owner
  Control/evidence: Human approves priority band
- Failure: No exception expiry
  Control/evidence: Exceptions expire automatically

Lab bridge: Lab 1 provides implementation and evidence checks.

### Anomaly detection models normal behaviour, not malicious intent

**Runtime mechanism:** Baseline → Feature vector → Distance score → Threshold → Analyst review

**Concrete contract**

- `window=15m`
- `features=[failures,new_device,bytes_out]`
- `score = model.decision_function(x)`
- `alert if score < threshold`

**Decision analysis**

- Isolation Forest isolates sparse points
- Z-score assumes a stable distribution
- Seasonality needs peer/time baselines
- Threshold controls workload and misses

**Failure and control**

- Failure: Novel but benign deployment
  Control/evidence: Backtest on labelled window
- Failure: Poisoned baseline
  Control/evidence: Report precision and recall
- Failure: Feature drift
  Control/evidence: Analyst disposition captured
- Failure: Rare user treated as hostile
  Control/evidence: Threshold reviewed monthly

Lab bridge: Lab 2 provides implementation and evidence checks.

### Phishing detection combines header, URL and language evidence

**Runtime mechanism:** Parse mail → Extract features → Classify → Explain → Quarantine/review

**Concrete contract**

- `spf/dkim/dmarc result`
- `reply_to mismatch`
- `url_domain_age_days`
- `language urgency score`

**Decision analysis**

- Header authentication is stronger than tone alone
- URL structure adds campaign signal
- Text models require multilingual evaluation
- Explanations should cite observed fields

**Failure and control**

- Failure: Attacker prompt text manipulates an LLM
  Control/evidence: Evidence cites exact header/URL
- Failure: Legitimate urgent mail
  Control/evidence: No auto-delete at low confidence
- Failure: Image-only lure
  Control/evidence: False positives sampled weekly
- Failure: Domain reputation delay
  Control/evidence: Protected sandbox for links

Lab bridge: Lab 3 provides implementation and evidence checks.

### Malware triage separates static signals from behavioural proof

**Runtime mechanism:** Hash/type → Static features → Sandbox → Classifier → Disposition

**Concrete contract**

- `sha256 + file_type`
- `imports/entropy/sections`
- `process/network/file behaviours`
- `family confidence + evidence`

**Decision analysis**

- Static ML scales pre-screening
- Behaviour reveals packed samples
- Family labels are noisy
- Unknown stays unknown

**Failure and control**

- Failure: Adversarial packing
  Control/evidence: No live malware in training
- Failure: Sandbox evasion
  Control/evidence: Hash and provenance recorded
- Failure: Training labels from one vendor
  Control/evidence: Confidence threshold documented
- Failure: Executing samples outside isolation
  Control/evidence: Analyst confirms containment

Lab bridge: Lab 4 provides implementation and evidence checks.

### Vulnerability prioritisation is a multi-signal ranking problem

**Runtime mechanism:** Inventory → Severity → Exploit likelihood → Exposure → Business context

**Concrete contract**

- `asset_id + owner`
- `CVSS base/vector`
- `EPSS probability`
- `internet_exposed + compensating_control`

**Decision analysis**

- Known exploitation outranks theoretical severity
- Exposure time affects urgency
- Compensating controls lower residual risk
- AI summarises evidence; policy sets SLA

**Failure and control**

- Failure: Hallucinated CVE details
  Control/evidence: Source URL and retrieval date
- Failure: Stale inventory
  Control/evidence: Reachability evidence
- Failure: Dependency not reachable
  Control/evidence: Priority rationale stored
- Failure: SLA ignores business owner
  Control/evidence: SLA breach dashboard

Lab bridge: Lab 5 provides implementation and evidence checks.

### UEBA needs peer groups, identity joins and privacy controls

**Runtime mechanism:** Identity graph → Peer baseline → Session features → Risk aggregation → Investigation

**Concrete contract**

- `principal.id + role`
- `device.id + managed`
- `geo_velocity_kmh`
- `privilege_change + data_access`

**Decision analysis**

- Peer grouping reduces role-driven noise
- Risk accumulates across weak signals
- Identity resolution precedes analytics
- Privacy purpose limits remain

**Failure and control**

- Failure: Shared accounts
  Control/evidence: Purpose documented
- Failure: Role change not reflected
  Control/evidence: Access restricted
- Failure: Bias against remote workers
  Control/evidence: Appeal/correction route
- Failure: Excessive employee surveillance
  Control/evidence: Alert evidence reproducible

Lab bridge: Lab 2 provides implementation and evidence checks.

### Threat-intelligence extraction produces structured, confidence-scored objects

**Runtime mechanism:** Source → Extract → Normalise → Correlate → Operationalise

**Concrete contract**

- `indicator.type/value`
- `valid_from/valid_until`
- `confidence 0-100`
- `source + relationship`

**Decision analysis**

- NLP accelerates entity extraction
- STIX-like structure enables joins
- Confidence depends on source and corroboration
- Expiry prevents permanent blocks

**Failure and control**

- Failure: Defanged indicators parsed wrongly
  Control/evidence: Schema validation
- Failure: Duplicate aliases
  Control/evidence: Provenance retained
- Failure: Untrusted report instructions
  Control/evidence: Human approves blocking
- Failure: IOC without context
  Control/evidence: Expired indicators removed

Lab bridge: Lab 6 provides implementation and evidence checks.

### Lab 1: Build an AI-Assisted Cyber Risk Register

**Mapped outcome:** LO1

Join asset criticality, threat likelihood, control effectiveness and evidence into a transparent residual-risk ranking.

**Controlled tool practice:** [Cybersecurity Threat Simulation Lab](https://alfredang.github.io/cybersecuritysimulator/) · Threat Dashboard

Use the lab's `tool-exercise.md` and fictional files in `mock-data/`. Observe the simulated threat categories and translate three observations into risk-register evidence references and control-gap notes.

#### Detailed step-by-step guide

1. Review the asset, threat and control columns in data/input.csv.
   - Evidence: record the input field/configuration and generated output.
   - Check: All rows have owner and evidence_ref
2. Run the starter script and inspect its deliberately incomplete residual-risk calculation.
   - Evidence: record the input field/configuration and generated output.
   - Check: Residual scores are 0-25
3. Implement likelihood x impact and control-effectiveness reduction without overwriting raw evidence.
   - Evidence: record the input field/configuration and generated output.
   - Check: Ranking changes when asset criticality changes
4. Rank the risks, assign owners and record a confidence note for each row.
   - Evidence: record the input field/configuration and generated output.
   - Check: Output JSON records the scoring formula
5. Compare the ranking with the business-process impact column and document one changed priority.
   - Evidence: record the input field/configuration and generated output.
   - Check: Output JSON records the scoring formula
6. Run the smoke test and verify that every output row retains asset_id and evidence_ref.
   - Evidence: record the input field/configuration and generated output.
   - Check: Output JSON records the scoring formula

Run from the individual lab folder:

```bash
cd labs/lab-01-build-an-ai-assisted-cyber-risk-register
python3 solution/main.py
python3 -m pytest -q tests
```

Troubleshoot schema/type errors before changing thresholds. Keep sensitive organisation data outside the exercise.

### Lab 2: Detect Authentication Anomalies

**Mapped outcome:** LO1

Create a peer-aware anomaly score from failed logins, new-device state and impossible-travel indicators.

**Controlled tool practice:** [FauxBank Cybersecurity Training Simulation](https://pentest-fauxbank.vercel.app/) · Fictional sign-in and account activity

Use the lab's `tool-exercise.md` and fictional files in `mock-data/`. Compare weak-credential and account-behaviour observations with the local authentication baseline; treat the site as a reversible education sandbox only.

#### Detailed step-by-step guide

1. Inspect the authentication schema and identify event-time, identity and device fields.
   - Evidence: record the input field/configuration and generated output.
   - Check: Model trained only on baseline rows
2. Create 15-minute features per user.
   - Evidence: record the input field/configuration and generated output.
   - Check: Output includes anomaly_score and reason fields
3. Fit IsolationForest only on the baseline rows.
   - Evidence: record the input field/configuration and generated output.
   - Check: Queue has at most three alerts
4. Score the evaluation rows and preserve reason features.
   - Evidence: record the input field/configuration and generated output.
   - Check: Threshold and model random_state are recorded
5. Tune the percentile threshold to a maximum review queue of three alerts.
   - Evidence: record the input field/configuration and generated output.
   - Check: Threshold and model random_state are recorded
6. Record false-positive risks and run the tests.
   - Evidence: record the input field/configuration and generated output.
   - Check: Threshold and model random_state are recorded

Run from the individual lab folder:

```bash
cd labs/lab-02-detect-authentication-anomalies
python3 solution/main.py
python3 -m pytest -q tests
```

Troubleshoot schema/type errors before changing thresholds. Keep sensitive organisation data outside the exercise.

### Lab 3: Explain a Phishing Risk Score

**Mapped outcome:** LO1

Combine email authentication, reply-to mismatch, URL and language features into an explainable phishing triage score.

**Controlled tool practice:** [Cybersecurity Threat Simulation Lab](https://alfredang.github.io/cybersecuritysimulator/) · Phishing simulator and URL analyser

Use the lab's `tool-exercise.md` and fictional files in `mock-data/`. Classify the fictional messages and URL indicators, then compare the simulator rationale with locally generated reason codes.

#### Detailed step-by-step guide

1. Review the safely simulated email feature table.
   - Evidence: record the input field/configuration and generated output.
   - Check: No raw email body leaves the lab
2. Assign weights to SPF/DKIM failure, reply-to mismatch, young domains and urgency.
   - Evidence: record the input field/configuration and generated output.
   - Check: Every score has at least one reason code
3. Calculate a 0-100 risk score.
   - Evidence: record the input field/configuration and generated output.
   - Check: Low-confidence mail is review-only
4. Generate reason codes from observed fields only.
   - Evidence: record the input field/configuration and generated output.
   - Check: Thresholds are documented
5. Apply review/quarantine thresholds with human approval for destructive action.
   - Evidence: record the input field/configuration and generated output.
   - Check: Thresholds are documented
6. Test a legitimate urgent message and document the false-positive control.
   - Evidence: record the input field/configuration and generated output.
   - Check: Thresholds are documented

Run from the individual lab folder:

```bash
cd labs/lab-03-explain-a-phishing-risk-score
python3 solution/main.py
python3 -m pytest -q tests
```

Troubleshoot schema/type errors before changing thresholds. Keep sensitive organisation data outside the exercise.

### Lab 4: Prioritise Vulnerabilities with Context

**Mapped outcome:** LO1

Rank vulnerabilities using severity, exploit likelihood, exposure, asset criticality and compensating controls.

**Controlled tool practice:** [Hacklab: Ethical Hacking Lab Simulator](https://alfredang.github.io/ethnicalhacking/) · Vulnerability assessment scenario

Use the lab's `tool-exercise.md` and fictional files in `mock-data/`. Use the simulated terminal to collect vulnerability evidence, then combine it with criticality and compensating-control data before setting remediation priority.

#### Detailed step-by-step guide

1. Inspect the synthetic CVE inventory and verify source/retrieval dates.
   - Evidence: record the input field/configuration and generated output.
   - Check: CVSS and EPSS remain separate fields
2. Calculate a transparent contextual priority score.
   - Evidence: record the input field/configuration and generated output.
   - Check: Internet exposure changes priority
3. Compare the result with a CVSS-only sort.
   - Evidence: record the input field/configuration and generated output.
   - Check: Every row keeps source and retrieval_date
4. Assign remediation SLAs by policy bands.
   - Evidence: record the input field/configuration and generated output.
   - Check: SLA is policy-derived
5. Record one case where a lower-CVSS item moves ahead.
   - Evidence: record the input field/configuration and generated output.
   - Check: SLA is policy-derived
6. Run tests for score bounds and required provenance.
   - Evidence: record the input field/configuration and generated output.
   - Check: SLA is policy-derived

Run from the individual lab folder:

```bash
cd labs/lab-04-prioritise-vulnerabilities-with-context
python3 solution/main.py
python3 -m pytest -q tests
```

Troubleshoot schema/type errors before changing thresholds. Keep sensitive organisation data outside the exercise.

## Topic 2: Designing AI-Powered Cybersecurity Programmes

**Alignment:** LO2

Objectives · use-case selection · governance · human oversight · operating model

### Programme design starts with an outcome, not an AI product

**Runtime mechanism:** Security objective → Decision → Evidence → Control → Metric

**Concrete contract**

- `problem statement`
- `decision owner`
- `baseline + target`
- `automation ceiling`

**Decision analysis**

- Use cases compete on value, feasibility and risk
- Baseline defines improvement
- Decision rights prevent shadow automation
- Kill criteria stop sunk-cost escalation

**Failure and control**

- Failure: Technology-first purchase
  Control/evidence: Named owner
- Failure: No measurable baseline
  Control/evidence: Baseline frozen
- Failure: Unowned alerts
  Control/evidence: Success/stop thresholds
- Failure: Pilot becomes production silently
  Control/evidence: Review date

Lab bridge: Lab 7 provides implementation and evidence checks.

### Control gaps translate into programme epics and guardrails

**Runtime mechanism:** Current control → Gap evidence → Security objective → Programme epic → Acceptance

**Concrete contract**

- `control_id`
- `current_state/evidence`
- `target_state`
- `owner/milestone/dependency`

**Decision analysis**

- A gap is an evidence-backed delta
- Objectives state the desired security outcome
- Epics group related controls
- Acceptance criteria remain testable

**Failure and control**

- Failure: Vague 'improve security' objective
  Control/evidence: Gap references audit/log
- Failure: AI invents missing evidence
  Control/evidence: Target has date
- Failure: Control owner excluded
  Control/evidence: Owner accepts scope
- Failure: No dependency map
  Control/evidence: Test plan exists

Lab bridge: Lab 7 provides implementation and evidence checks.

### Data governance is part of the security control plane

**Runtime mechanism:** Classify → Minimise → Authorise → Protect → Delete

**Concrete contract**

- `data class`
- `allowed purpose`
- `retention`
- `region`
- `model/provider use`

**Decision analysis**

- Sensitive telemetry can identify people
- Prompts are data transfers
- Training use must be explicit
- Deletion must cover caches and indexes

**Failure and control**

- Failure: Secrets in prompts
  Control/evidence: DLP test
- Failure: Unbounded retention
  Control/evidence: Access log
- Failure: Cross-border transfer
  Control/evidence: Deletion evidence
- Failure: Vendor trains on customer data
  Control/evidence: Vendor contract control

Lab bridge: Lab 8 provides implementation and evidence checks.

### Automation levels define where humans must decide

**Runtime mechanism:** Recommend → Draft → Approve → Execute → Reverse

**Concrete contract**

- `confidence threshold`
- `action allow-list`
- `approval role`
- `rollback command`

**Decision analysis**

- Low-impact enrichment can be automatic
- Containment needs bounded targets
- High-impact identity actions need approval
- Reversibility lowers operational risk

**Failure and control**

- Failure: Model blocks a critical account
  Control/evidence: Dry-run default
- Failure: Approval fatigue
  Control/evidence: Two-person approval for destructive action
- Failure: No rollback
  Control/evidence: Full audit trail
- Failure: Action scope expands via tool permissions
  Control/evidence: Quarterly access review

Lab bridge: Lab 9 provides implementation and evidence checks.

### Threat modelling covers both AI use and the AI system

**Runtime mechanism:** Assets → Trust boundaries → Abuse cases → Controls → Tests

**Concrete contract**

- `model/data/tool identities`
- `prompt/retrieval/tool boundaries`
- `STRIDE + ATLAS techniques`
- `security test case`

**Decision analysis**

- AI can strengthen defence and create attack paths
- Tool permissions are a primary boundary
- Indirect prompt injection travels through content
- Model supply chain needs provenance

**Failure and control**

- Failure: Prompt injection
  Control/evidence: Abuse case mapped
- Failure: Training-data poisoning
  Control/evidence: Control owner
- Failure: Model theft
  Control/evidence: Test evidence
- Failure: Unsafe tool invocation
  Control/evidence: Residual risk accepted

Lab bridge: Lab 8 provides implementation and evidence checks.

### Build-versus-buy decisions depend on control and evidence

**Runtime mechanism:** Requirements → Market scan → Evidence request → Risk decision → Contract

**Concrete contract**

- `data use/retention`
- `model update notice`
- `tenant isolation`
- `incident notification`

**Decision analysis**

- Embedded AI reduces integration effort
- Custom models increase ownership burden
- Benchmarks must match local data
- Exit plans prevent lock-in

**Failure and control**

- Failure: Benchmark without dataset details
  Control/evidence: Proof-of-value dataset
- Failure: No audit logs
  Control/evidence: Security questionnaire
- Failure: Unannounced model changes
  Control/evidence: Contractual controls
- Failure: Provider dependency
  Control/evidence: Export/delete test

Lab bridge: Lab 8 provides implementation and evidence checks.

### Secure adoption applies least privilege to models, tools and people

**Runtime mechanism:** Authenticate → Authorise → Constrain tools → Monitor → Review

**Concrete contract**

- `service identity`
- `scoped retrieval index`
- `tool allow-list`
- `per-action audit event`

**Decision analysis**

- The model is not an identity
- Every tool call uses a governed principal
- Retrieval permissions filter before generation
- Logs capture inputs, decisions and actions

**Failure and control**

- Failure: Shared API key
  Control/evidence: RBAC test
- Failure: Cross-tenant retrieval
  Control/evidence: Tenant-isolation test
- Failure: Over-privileged plugin
  Control/evidence: Secret scan
- Failure: Sensitive log content exposed
  Control/evidence: Access recertification

Lab bridge: Lab 9 provides implementation and evidence checks.

### The operating model links people, process and technology

**Runtime mechanism:** Govern → Product owner → SOC operations → Model risk → Audit

**Concrete contract**

- `RACI`
- `change window`
- `incident route`
- `model card + runbook`

**Decision analysis**

- Product ownership outlives the pilot
- SOC owns operational disposition
- Model risk owns validation
- Audit needs evidence independent of the vendor

**Failure and control**

- Failure: Nobody owns false positives
  Control/evidence: RACI approved
- Failure: Change bypasses CAB
  Control/evidence: On-call route tested
- Failure: Runbook lacks fallback
  Control/evidence: Fallback exercised
- Failure: Audit depends on screenshots
  Control/evidence: Evidence pack reproducible

Lab bridge: Lab 7 provides implementation and evidence checks.

### Lab 5: Select and Scope an AI Security Use Case

**Mapped outcome:** LO2

Score candidate use cases on value, data readiness, integration effort, operating risk and human-oversight requirements.

**Controlled tool practice:** [Cybersecurity Threat Simulation Lab](https://alfredang.github.io/cybersecuritysimulator/) · Threat Dashboard and scenario modules

Use the lab's `tool-exercise.md` and fictional files in `mock-data/`. Identify candidate AI-support opportunities from the simulated scenarios, then score value, readiness, integration effort and operating risk.

#### Detailed step-by-step guide

1. Define the security outcome and decision owner.
   - Evidence: record the input field/configuration and generated output.
   - Check: Selected use case has measurable baseline
2. Score each use case against the provided rubric.
   - Evidence: record the input field/configuration and generated output.
   - Check: Decision owner named
3. Apply a risk penalty for high-impact autonomous action.
   - Evidence: record the input field/configuration and generated output.
   - Check: Automation ceiling explicit
4. Select one pilot and state the baseline and target.
   - Evidence: record the input field/configuration and generated output.
   - Check: Stop criteria included
5. Set automation ceiling, stop criteria and review date.
   - Evidence: record the input field/configuration and generated output.
   - Check: Stop criteria included
6. Peer-review the charter against LO2.
   - Evidence: record the input field/configuration and generated output.
   - Check: Stop criteria included

Run from the individual lab folder:

```bash
cd labs/lab-05-select-and-scope-an-ai-security-use-case
python3 solution/main.py
python3 -m pytest -q tests
```

Troubleshoot schema/type errors before changing thresholds. Keep sensitive organisation data outside the exercise.

### Lab 6: Threat-Model an AI SOC Assistant

**Mapped outcome:** LO2

Map assets, trust boundaries and AI-specific abuse cases, then turn them into programme guardrails.

**Controlled tool practice:** [Hacklab: Ethical Hacking Lab Simulator](https://alfredang.github.io/ethnicalhacking/) · Malware analysis scenario

Use the lab's `tool-exercise.md` and fictional files in `mock-data/`. Collect static-analysis observations from the fictional sample and model how untrusted evidence could manipulate an AI SOC assistant.

#### Detailed step-by-step guide

1. Draw the user-model-retrieval-tool-target trust boundaries.
   - Evidence: record the input field/configuration and generated output.
   - Check: At least four trust boundaries
2. Identify direct and indirect prompt-injection paths.
   - Evidence: record the input field/configuration and generated output.
   - Check: Every abuse case has a control owner
3. Map data leakage, unsafe tool invocation and poisoned feedback risks.
   - Evidence: record the input field/configuration and generated output.
   - Check: Tool actions are allow-listed
4. Assign preventive, detective and recovery controls.
   - Evidence: record the input field/configuration and generated output.
   - Check: Residual risk is stated
5. Name control owners and acceptance tests.
   - Evidence: record the input field/configuration and generated output.
   - Check: Residual risk is stated
6. Validate the JSON schema and peer-review residual risk.
   - Evidence: record the input field/configuration and generated output.
   - Check: Residual risk is stated

Run from the individual lab folder:

```bash
cd labs/lab-06-threat-model-an-ai-soc-assistant
python3 solution/main.py
python3 -m pytest -q tests
```

Troubleshoot schema/type errors before changing thresholds. Keep sensitive organisation data outside the exercise.

### Lab 7: Build the AI Security Programme Charter

**Mapped outcome:** LO2

Translate assessed control gaps into governed programme epics, metrics, owners and decision gates.

**Controlled tool practice:** [FauxBank Cybersecurity Training Simulation](https://pentest-fauxbank.vercel.app/) · Guided findings and report generator

Use the lab's `tool-exercise.md` and fictional files in `mock-data/`. Turn the fictional application findings into programme epics, accountable ownership, metrics and decision gates.

#### Detailed step-by-step guide

1. Select the highest-priority control gaps from the lab data.
   - Evidence: record the input field/configuration and generated output.
   - Check: Every epic traces to a gap
2. Write outcome-based objectives and measurable targets.
   - Evidence: record the input field/configuration and generated output.
   - Check: Metric has baseline and target
3. Group work into data, model, integration, people and assurance epics.
   - Evidence: record the input field/configuration and generated output.
   - Check: RACI has one accountable owner
4. Create RACI assignments and an escalation route.
   - Evidence: record the input field/configuration and generated output.
   - Check: Retirement/exit gate exists
5. Define pilot, production and retirement gates.
   - Evidence: record the input field/configuration and generated output.
   - Check: Retirement/exit gate exists
6. Run the charter checklist and resolve missing owners.
   - Evidence: record the input field/configuration and generated output.
   - Check: Retirement/exit gate exists

Run from the individual lab folder:

```bash
cd labs/lab-07-build-the-ai-security-programme-charter
python3 solution/main.py
python3 -m pytest -q tests
```

Troubleshoot schema/type errors before changing thresholds. Keep sensitive organisation data outside the exercise.

## Topic 3: Developing AI-Driven Security Architecture and Action Plans

**Alignment:** LO3

SOC architecture · data pipeline · guarded automation · delivery roadmap

### An AI-enhanced SOC separates evidence, inference and action

**Runtime mechanism:** Telemetry → Security lake/SIEM → Analytics → Case → Guarded response

**Concrete contract**

- `immutable event store`
- `feature/model service`
- `case evidence bundle`
- `SOAR approval gate`

**Decision analysis**

- Evidence remains queryable without the model
- Inference is versioned
- Cases preserve human disposition
- Response uses scoped service accounts

**Failure and control**

- Failure: LLM directly queries production
  Control/evidence: Replay creates same result
- Failure: No model version
  Control/evidence: Model/version logged
- Failure: Alert overwrites raw evidence
  Control/evidence: Case links raw events
- Failure: SOAR action lacks approval
  Control/evidence: Rollback tested

Lab bridge: Lab 9 provides implementation and evidence checks.

### Feature pipelines prevent training-serving skew

**Runtime mechanism:** Raw events → Transform → Feature store → Train → Serve

**Concrete contract**

- `feature name/type`
- `window and timezone`
- `default/null policy`
- `owner/version`

**Decision analysis**

- One definition serves training and inference
- Point-in-time joins prevent leakage
- Feature freshness is monitored
- Backfills are versioned

**Failure and control**

- Failure: Future data leaks into training
  Control/evidence: Offline/online parity test
- Failure: Different parser in production
  Control/evidence: Feature freshness SLO
- Failure: Null default changes
  Control/evidence: Schema contract test
- Failure: Stale enrichment
  Control/evidence: Backfill audit

Lab bridge: Lab 10 provides implementation and evidence checks.

### SIEM plus ML uses rules and models as complementary detectors

**Runtime mechanism:** Rule match → Model score → Correlation → Case severity → Disposition

**Concrete contract**

- `rule_id + version`
- `model_id + threshold`
- `entity graph`
- `reason codes`

**Decision analysis**

- Rules encode known policy
- Models surface weak novel patterns
- Correlation reduces isolated noise
- Disposition feeds both tuning loops

**Failure and control**

- Failure: Model replaces high-confidence rule
  Control/evidence: Detection-as-code test
- Failure: Duplicate alerts
  Control/evidence: Duplicate suppression
- Failure: Correlation window too wide
  Control/evidence: Latency SLO
- Failure: Feedback label leakage
  Control/evidence: Tuning change record

Lab bridge: Lab 10 provides implementation and evidence checks.

### RAG grounds an analyst assistant in approved evidence

**Runtime mechanism:** Curate → Chunk → Retrieve → Generate → Cite

**Concrete contract**

- `document_id/version`
- `chunk + ACL`
- `top_k + similarity`
- `answer + citations`

**Decision analysis**

- Retrieval narrows evidence
- ACL filtering precedes generation
- Citations enable verification
- Abstention is a valid output

**Failure and control**

- Failure: Indirect prompt injection
  Control/evidence: Citation precision
- Failure: Stale runbook
  Control/evidence: Forbidden-document test
- Failure: Cross-case retrieval
  Control/evidence: Freshness check
- Failure: Confident uncited answer
  Control/evidence: Abstention threshold

Lab bridge: Lab 10 provides implementation and evidence checks.

### Identity boundaries control every AI-to-tool transition

**Runtime mechanism:** User → Application → Model → Tool broker → Target system

**Concrete contract**

- `user/session claims`
- `workload identity`
- `delegated scope`
- `policy decision + audit`

**Decision analysis**

- The tool broker mediates calls
- Delegation cannot exceed the user
- Secrets stay outside prompts
- Break-glass is separate

**Failure and control**

- Failure: Model holds admin token
  Control/evidence: Token scope test
- Failure: Confused deputy
  Control/evidence: Denied-action test
- Failure: Long-lived secret
  Control/evidence: Secret rotation
- Failure: Unlogged break-glass
  Control/evidence: Break-glass review

Lab bridge: Lab 9 provides implementation and evidence checks.

### Guarded SOAR uses policy gates and reversible actions

**Runtime mechanism:** Enrich → Recommend → Simulate → Approve → Execute/rollback

**Concrete contract**

- `action type`
- `target scope`
- `precondition`
- `approval`
- `rollback`

**Decision analysis**

- Simulation checks blast radius
- Preconditions prevent stale actions
- Approval follows impact tier
- Rollback is part of the playbook

**Failure and control**

- Failure: Race condition
  Control/evidence: Dry-run output
- Failure: Wrong entity
  Control/evidence: Approval record
- Failure: Partial execution
  Control/evidence: Post-action verification
- Failure: Rollback dependency unavailable
  Control/evidence: Rollback exercise

Lab bridge: Lab 11 provides implementation and evidence checks.

### An action plan converts architecture into sequenced delivery

**Runtime mechanism:** Current state → Target state → Work packages → Dependencies → Milestones

**Concrete contract**

- `epic/control`
- `owner`
- `start/end`
- `dependency`
- `acceptance evidence`

**Decision analysis**

- Architecture decisions constrain work
- Critical path exposes sequencing
- Pilot and production have different gates
- Regulatory changes trigger backlog review

**Failure and control**

- Failure: Roadmap has dates but no dependencies
  Control/evidence: Dependency review
- Failure: Control evidence deferred
  Control/evidence: Milestone evidence
- Failure: No decommission task
  Control/evidence: Risk burn-down
- Failure: Owner changes silently
  Control/evidence: Change log

Lab bridge: Lab 11 provides implementation and evidence checks.

### Resilience assumes models and providers can fail

**Runtime mechanism:** Detect failure → Degrade safely → Fallback → Recover → Learn

**Concrete contract**

- `availability/latency SLO`
- `manual/rule fallback`
- `backup configuration`
- `recovery objective`

**Decision analysis**

- Security fundamentals remain available
- Fail-closed is not always safe
- Fallback needs equivalent audit
- Recovery includes model and index versions

**Failure and control**

- Failure: Provider outage
  Control/evidence: Game-day exercise
- Failure: Corrupt vector index
  Control/evidence: Manual queue works
- Failure: Rate-limit spike
  Control/evidence: Restore checksum
- Failure: Bad model rollout
  Control/evidence: Post-incident action

Lab bridge: Lab 11 provides implementation and evidence checks.

### Lab 8: Design an AI-Enhanced SOC Architecture

**Mapped outcome:** LO3

Design a layered architecture that separates evidence, inference, case management and guarded action.

**Controlled tool practice:** [Cryptography Toolkit](https://alfredang.github.io/cryptography-toolkit/) · ECDSA sign and verify

Use the lab's `tool-exercise.md` and fictional files in `mock-data/`. Sign a fictional architecture decision record and verify it after a controlled text change to demonstrate integrity evidence, not identity assurance by itself.

#### Detailed step-by-step guide

1. Inventory telemetry sources and owners.
   - Evidence: record the input field/configuration and generated output.
   - Check: Raw evidence is immutable
2. Define immutable evidence and normalized event stores.
   - Evidence: record the input field/configuration and generated output.
   - Check: Model and prompt versions logged
3. Place rule, ML and LLM services behind explicit interfaces.
   - Evidence: record the input field/configuration and generated output.
   - Check: Tool actions use scoped identity
4. Add case-management evidence links and a tool-broker approval gate.
   - Evidence: record the input field/configuration and generated output.
   - Check: Manual fallback documented
5. Document identity, logging, fallback and recovery paths.
   - Evidence: record the input field/configuration and generated output.
   - Check: Manual fallback documented
6. Validate the architecture against the provided control checklist.
   - Evidence: record the input field/configuration and generated output.
   - Check: Manual fallback documented

Run from the individual lab folder:

```bash
cd labs/lab-08-design-an-ai-enhanced-soc-architecture
python3 solution/main.py
python3 -m pytest -q tests
```

Troubleshoot schema/type errors before changing thresholds. Keep sensitive organisation data outside the exercise.

### Lab 9: Build a Grounded Threat-Intelligence Assistant

**Mapped outcome:** LO3

Retrieve from approved threat bulletins and produce cited, abstaining summaries without external APIs.

**Controlled tool practice:** [Hacklab: Ethical Hacking Lab Simulator](https://alfredang.github.io/ethnicalhacking/) · Reconnaissance scenario

Use the lab's `tool-exercise.md` and fictional files in `mock-data/`. Capture simulated reconnaissance facts, convert them into approved local bulletins and test citation and abstention behaviour.

#### Detailed step-by-step guide

1. Review the approved local threat bulletins and document ACL metadata.
   - Evidence: record the input field/configuration and generated output.
   - Check: Every claim has document citation
2. Chunk and index the documents with TF-IDF.
   - Evidence: record the input field/configuration and generated output.
   - Check: ACL filtering occurs before retrieval
3. Retrieve top-k evidence for each analyst query.
   - Evidence: record the input field/configuration and generated output.
   - Check: Unknown query abstains
4. Generate an extractive summary that cites document IDs.
   - Evidence: record the input field/configuration and generated output.
   - Check: Embedded instructions are treated as data
5. Return 'insufficient evidence' below the similarity threshold.
   - Evidence: record the input field/configuration and generated output.
   - Check: Embedded instructions are treated as data
6. Test forbidden-document and indirect-instruction cases.
   - Evidence: record the input field/configuration and generated output.
   - Check: Embedded instructions are treated as data

Run from the individual lab folder:

```bash
cd labs/lab-09-build-a-grounded-threat-intelligence-assistant
python3 solution/main.py
python3 -m pytest -q tests
```

Troubleshoot schema/type errors before changing thresholds. Keep sensitive organisation data outside the exercise.

### Lab 10: Design a Guarded SOAR Playbook

**Mapped outcome:** LO3

Build a reversible, approval-gated response playbook for suspicious account activity.

**Controlled tool practice:** [FauxBank Cybersecurity Training Simulation](https://pentest-fauxbank.vercel.app/) · Simulated scanner and report generator

Use the lab's `tool-exercise.md` and fictional files in `mock-data/`. Convert selected fictional findings into guarded response cases; keep all actions in dry-run or submit-for-approval mode.

#### Detailed step-by-step guide

1. Define trigger evidence and entity-resolution preconditions.
   - Evidence: record the input field/configuration and generated output.
   - Check: Default mode is dry-run
2. Add enrichment and confidence checks.
   - Evidence: record the input field/configuration and generated output.
   - Check: Target identity is verified
3. Simulate account containment and calculate blast radius.
   - Evidence: record the input field/configuration and generated output.
   - Check: Approval recorded
4. Require approval for identity-impacting actions.
   - Evidence: record the input field/configuration and generated output.
   - Check: Rollback and post-check exist
5. Define rollback and post-action verification.
   - Evidence: record the input field/configuration and generated output.
   - Check: Rollback and post-check exist
6. Run safe dry-run tests; no real accounts are modified.
   - Evidence: record the input field/configuration and generated output.
   - Check: Rollback and post-check exist

Run from the individual lab folder:

```bash
cd labs/lab-10-design-a-guarded-soar-playbook
python3 solution/main.py
python3 -m pytest -q tests
```

Troubleshoot schema/type errors before changing thresholds. Keep sensitive organisation data outside the exercise.

### Lab 11: Create a 90-Day AI Security Action Plan

**Mapped outcome:** LO3

Sequence architecture work packages, dependencies, acceptance evidence and regulatory review triggers.

**Controlled tool practice:** [Hacklab: Ethical Hacking Lab Simulator](https://alfredang.github.io/ethnicalhacking/) · Network scanning scenario

Use the lab's `tool-exercise.md` and fictional files in `mock-data/`. Use simulated discovery evidence to sequence work packages, dependencies, owners and acceptance gates in a 90-day plan.

#### Detailed step-by-step guide

1. Import the target architecture work packages.
   - Evidence: record the input field/configuration and generated output.
   - Check: No dependency cycles
2. Assign owner, duration, dependency and acceptance evidence.
   - Evidence: record the input field/configuration and generated output.
   - Check: Every work package has evidence
3. Detect missing or cyclic dependencies.
   - Evidence: record the input field/configuration and generated output.
   - Check: Critical path identified
4. Calculate earliest start and critical path.
   - Evidence: record the input field/configuration and generated output.
   - Check: Change triggers recorded
5. Add model/provider change and regulatory-review triggers.
   - Evidence: record the input field/configuration and generated output.
   - Check: Change triggers recorded
6. Present the 30/60/90-day roadmap for approval.
   - Evidence: record the input field/configuration and generated output.
   - Check: Change triggers recorded

Run from the individual lab folder:

```bash
cd labs/lab-11-create-a-90-day-ai-security-action-plan
python3 solution/main.py
python3 -m pytest -q tests
```

Troubleshoot schema/type errors before changing thresholds. Keep sensitive organisation data outside the exercise.

## Topic 4: Monitoring, Evaluating and Governing AI Security Solutions

**Alignment:** LO4

Metrics · drift · adversarial testing · standards · advisory reporting

### Confusion-matrix metrics connect detection to operations

**Runtime mechanism:** Labels → Predictions → TP/FP/FN/TN → Metrics → Operating point

**Concrete contract**

- `precision=TP/(TP+FP)`
- `recall=TP/(TP+FN)`
- `FPR=FP/(FP+TN)`
- `cost = FP*c_fp + FN*c_fn`

**Decision analysis**

- Accuracy hides class imbalance
- Precision measures alert usefulness
- Recall measures missed-threat exposure
- Cost weights business consequence

**Failure and control**

- Failure: Evaluation set not representative
  Control/evidence: Frozen test set
- Failure: Labels from same detector
  Control/evidence: Class prevalence reported
- Failure: Metric without confidence interval
  Control/evidence: Operating threshold approved
- Failure: Threshold changed without review
  Control/evidence: Metric tied to workload

Lab bridge: Lab 12 provides implementation and evidence checks.

### Drift monitoring compares live distributions and outcomes

**Runtime mechanism:** Reference → Live window → Feature drift → Performance drift → Response

**Concrete contract**

- `PSI = Σ(actual-expected) ln(actual/expected)`
- `feature null rate`
- `score distribution`
- `confirmed precision`

**Decision analysis**

- Input drift is an early warning
- Performance needs delayed labels
- Seasonality needs matched baselines
- Retraining is not the only response

**Failure and control**

- Failure: Alert fatigue from noisy drift
  Control/evidence: Drift thresholds
- Failure: Silent schema change
  Control/evidence: Schema-change alert
- Failure: Poisoned feedback
  Control/evidence: Label quality sample
- Failure: Automatic retraining on attacks
  Control/evidence: Rollback/recalibrate decision

Lab bridge: Lab 12 provides implementation and evidence checks.

### Grounding and citation tests manage hallucination risk

**Runtime mechanism:** Question → Retrieve evidence → Answer → Cite → Verify/abstain

**Concrete contract**

- `claim span`
- `source document/version`
- `entailment result`
- `abstention reason`

**Decision analysis**

- Faithfulness differs from usefulness
- Citation presence is not citation correctness
- Unsupported claims can be blocked
- High-impact advice requires review

**Failure and control**

- Failure: Fabricated IOC
  Control/evidence: Claim-level citation test
- Failure: Citation points to irrelevant paragraph
  Control/evidence: Freshness SLO
- Failure: Stale policy
  Control/evidence: Known-unanswerable set
- Failure: Answer exceeds source
  Control/evidence: Analyst sign-off

Lab bridge: Lab 10 provides implementation and evidence checks.

### Adversarial testing follows attacker goals and trust boundaries

**Runtime mechanism:** Threat model → Test cases → Execute → Observe → Remediate/retest

**Concrete contract**

- `ATLAS technique`
- `precondition`
- `payload/source`
- `expected control`
- `evidence`

**Decision analysis**

- Direct injection targets user input
- Indirect injection arrives via retrieved content
- Evasion perturbs model features
- Poisoning targets training/feedback

**Failure and control**

- Failure: Testing production destructively
  Control/evidence: Isolated test tenant
- Failure: No data exfiltration canary
  Control/evidence: Canary secret
- Failure: Tool-call side effect
  Control/evidence: Tool dry-run
- Failure: Payloads retained in logs
  Control/evidence: Retest closes finding

Lab bridge: Lab 12 provides implementation and evidence checks.

### Privacy and data-loss controls apply before, during and after inference

**Runtime mechanism:** Discover → Classify → Redact → Authorise → Monitor/delete

**Concrete contract**

- `secret/PII detectors`
- `token-level redaction`
- `purpose + consent`
- `retention/deletion receipt`

**Decision analysis**

- Prevention starts before the prompt
- Outputs can reconstruct inputs
- Logs may be more sensitive than prompts
- Deletion spans provider and local stores

**Failure and control**

- Failure: Prompt contains API key
  Control/evidence: Secret canary blocked
- Failure: Model memorisation
  Control/evidence: Output DLP test
- Failure: Sensitive output
  Control/evidence: Log access review
- Failure: Debug log leakage
  Control/evidence: Deletion proof

Lab bridge: Lab 8 provides implementation and evidence checks.

### Standards mapping turns principles into evidence

**Runtime mechanism:** Requirement → Control → Implementation → Evidence → Finding

**Concrete contract**

- `framework/function/category`
- `control owner`
- `test frequency`
- `evidence location`

**Decision analysis**

- NIST CSF structures cyber outcomes
- AI RMF covers AI-specific governance
- ISO-style controls support assurance
- Mapping avoids duplicate evidence

**Failure and control**

- Failure: Checkbox mapping
  Control/evidence: Sample evidence
- Failure: No test frequency
  Control/evidence: Independent test
- Failure: Vendor assertion only
  Control/evidence: Exception record
- Failure: Conflicting control owners
  Control/evidence: Management review

Lab bridge: Lab 12 provides implementation and evidence checks.

### Continuous assurance combines technical tests and operational review

**Runtime mechanism:** Control test → Detection test → Scenario exercise → Metric review → Improvement

**Concrete contract**

- `test id/version`
- `expected result`
- `observed evidence`
- `owner/due date`

**Decision analysis**

- Unit tests catch contract drift
- Purple-team tests validate detections
- Tabletops validate decisions
- Metrics expose operating degradation

**Failure and control**

- Failure: Tests never fail
  Control/evidence: Failure injection
- Failure: Synthetic scenario unlike production
  Control/evidence: Independent review
- Failure: Finding closed without evidence
  Control/evidence: Retest evidence
- Failure: No retest
  Control/evidence: Backlog trend

Lab bridge: Lab 12 provides implementation and evidence checks.

### Advisory reporting separates facts, inference and recommendations

**Runtime mechanism:** Executive outcome → Evidence → Risk → Options → Recommendation

**Concrete contract**

- `finding + source`
- `confidence/limitations`
- `decision owner`
- `action/measure/date`

**Decision analysis**

- Facts remain reproducible
- Inference is labelled
- Options expose trade-offs
- Recommendation has owner and metric

**Failure and control**

- Failure: AI-generated certainty
  Control/evidence: Source appendix
- Failure: No limitation statement
  Control/evidence: Assumption register
- Failure: Recommendation without cost
  Control/evidence: Management decision
- Failure: No follow-up measure
  Control/evidence: 30/60/90-day readback

Lab bridge: Lab 12 provides implementation and evidence checks.

### Lab 12: Monitor Model Effectiveness and Produce Advice

**Mapped outcome:** LO4

Measure detection quality, identify drift and control failures, then issue evidence-backed adoption advice.

**Controlled tool practice:** [Cryptography Toolkit](https://alfredang.github.io/cryptography-toolkit/) · ECDSA sign and verify

Use the lab's `tool-exercise.md` and fictional files in `mock-data/`. Sign the fictional advisory report, verify the original, then alter one statement and record the expected verification failure as integrity evidence.

#### Detailed step-by-step guide

1. Build the confusion matrix from labelled outcomes.
   - Evidence: record the input field/configuration and generated output.
   - Check: Metrics include class prevalence
2. Calculate precision, recall, F1 and false-positive rate.
   - Evidence: record the input field/configuration and generated output.
   - Check: Drift is diagnostic, not automatic retraining
3. Compare feature distributions with the reference window.
   - Evidence: record the input field/configuration and generated output.
   - Check: Advice separates fact/inference/recommendation
4. Review prompt-injection, citation and permission tests.
   - Evidence: record the input field/configuration and generated output.
   - Check: Each action has owner and measure
5. Map findings to NIST CSF/AI RMF control outcomes.
   - Evidence: record the input field/configuration and generated output.
   - Check: Each action has owner and measure
6. Write a recommendation with options, limitations, owner, metric and 30/60/90-day follow-up.
   - Evidence: record the input field/configuration and generated output.
   - Check: Each action has owner and measure

Run from the individual lab folder:

```bash
cd labs/lab-12-monitor-model-effectiveness-and-produce-advice
python3 solution/main.py
python3 -m pytest -q tests
```

Troubleshoot schema/type errors before changing thresholds. Keep sensitive organisation data outside the exercise.


## References

Retrieval date: 28 August 2026.

- ACSC et al. (2026). [Opportunities for AI in cyber defence](https://www.cyber.gov.au/business-government/secure-design/artificial-intelligence/opportunities-for-ai-in-cyber-defence)
- NIST (2024). [Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework)
- NIST (2023). [AI Risk Management Framework 1.0](https://www.nist.gov/itl/ai-risk-management-framework)
- NIST (2025). [Adversarial Machine Learning Taxonomy and Terminology](https://csrc.nist.gov/pubs/ai/100/2/e2025/final)
- MITRE. [ATLAS: Adversarial Threat Landscape for AI Systems](https://atlas.mitre.org/)
- OWASP. [Top 10 for Large Language Model Applications](https://genai.owasp.org/llm-top-10/)
- CISA. [Secure by Design](https://www.cisa.gov/securebydesign)
- Google Cloud. [AI for Security](https://cloud.google.com/security/ai)
- IBM. [AI cybersecurity solutions](https://www.ibm.com/solutions/ai-cybersecurity)
- Red Hat. [Four use cases for AI in cyber security](https://www.redhat.com/en/blog/4-use-cases-ai-cyber-security)
- Alfred Ang. [Cybersecurity Threat Simulation Lab](https://alfredang.github.io/cybersecuritysimulator/)
- Alfred Ang. [Hacklab: Ethical Hacking Lab Simulator](https://alfredang.github.io/ethnicalhacking/)
- Tertiary Infotech Academy. [FauxBank Cybersecurity Training Simulation](https://pentest-fauxbank.vercel.app/)
- Alfred Ang. [Cryptography Toolkit](https://alfredang.github.io/cryptography-toolkit/)
