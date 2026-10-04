# Lab 3: Explain a Phishing Risk Score

**Mapped outcome:** LO1
**Tools:** Python 3 · pandas · Cybersecurity Threat Simulation Lab

## Objective

Combine email authentication, reply-to mismatch, URL and language features into an explainable phishing triage score.

## Deliverable

phishing_triage.csv with evidence-based reason codes.

## Safety and privacy boundary

Use only the synthetic files in `data/` and `mock-data/`. Do not paste organisation logs, credentials, personal data, malware, or live incidents into any external AI service. Use the linked tool only as an education simulation or use a trainer-owned isolated Kali environment.

## Simulator or Kali-style practice

Open [tool-exercise.md](tool-exercise.md) for the controlled Cybersecurity Threat Simulation Lab exercise. The offline mock-data path is equivalent for lab evidence.

## Detailed procedure

### Step 1 - Review the safely simulated email feature table.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: No raw email body leaves the lab

### Step 2 - Assign weights to SPF/DKIM failure, reply-to mismatch, young domains and urgency.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Every score has at least one reason code

### Step 3 - Calculate a 0-100 risk score.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Low-confidence mail is review-only

### Step 4 - Generate reason codes from observed fields only.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Thresholds are documented

### Step 5 - Apply review/quarantine thresholds with human approval for destructive action.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Thresholds are documented

### Step 6 - Test a legitimate urgent message and document the false-positive control.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Thresholds are documented

## Run the reference and tests

```bash
python3 solution/main.py
python3 -m pytest -q tests
```

## Acceptance checks

- [ ] No raw email body leaves the lab
- [ ] Every score has at least one reason code
- [ ] Low-confidence mail is review-only
- [ ] Thresholds are documented

## Troubleshooting

- `FileNotFoundError`: run from the lab folder and confirm `data/input.csv`.
- Missing package: create a virtual environment and install `requirements.txt`.
- Unexpected score: inspect types, nulls, baseline split and threshold direction.
- Too many alerts: state the capacity constraint before tuning the threshold.

## Reflection

Explain one limitation, one control and one condition that prevents production use.
