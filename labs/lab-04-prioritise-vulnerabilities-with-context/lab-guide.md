# Lab 4: Prioritise Vulnerabilities with Context

**Mapped outcome:** LO1
**Tools:** Python 3 · pandas · Hacklab: Ethical Hacking Lab Simulator

## Objective

Rank vulnerabilities using severity, exploit likelihood, exposure, asset criticality and compensating controls.

## Deliverable

`prioritised_vulnerabilities.csv` and `sla-rationale.md`.

## Safety and privacy boundary

Use only the synthetic files in `data/` and `mock-data/`. Do not paste organisation logs, credentials, personal data, malware, or live incidents into any external AI service. Use the linked tool only as an education simulation or use a trainer-owned isolated Kali environment.

## Simulator or Kali-style practice

Open [tool-exercise.md](tool-exercise.md) for the controlled Hacklab: Ethical Hacking Lab Simulator exercise. The offline mock-data path is equivalent for lab evidence.

## Detailed procedure

### Step 1 - Inspect the synthetic CVE inventory and verify source/retrieval dates.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: CVSS and EPSS remain separate fields

### Step 2 - Calculate a transparent contextual priority score.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Internet exposure changes priority

### Step 3 - Compare the result with a CVSS-only sort.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Every row keeps source and retrieval_date

### Step 4 - Assign remediation SLAs by policy bands.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: SLA is policy-derived

### Step 5 - Record one case where a lower-CVSS item moves ahead.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: SLA is policy-derived

### Step 6 - Run tests for score bounds and required provenance.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: SLA is policy-derived

## Run the reference and tests

```bash
python3 solution/main.py
python3 -m pytest -q tests
```

## Acceptance checks

- [ ] CVSS and EPSS remain separate fields
- [ ] Internet exposure changes priority
- [ ] Every row keeps source and retrieval_date
- [ ] SLA is policy-derived

## Troubleshooting

- `FileNotFoundError`: run from the lab folder and confirm `data/input.csv`.
- Missing package: create a virtual environment and install `requirements.txt`.
- Unexpected score: inspect types, nulls, baseline split and threshold direction.
- Too many alerts: state the capacity constraint before tuning the threshold.

## Reflection

Explain one limitation, one control and one condition that prevents production use.
