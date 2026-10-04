# Lab 1: Build an AI-Assisted Cyber Risk Register

**Mapped outcome:** LO1
**Tools:** Python 3 · CSV · JSON · Cybersecurity Threat Simulation Lab

## Objective

Join asset criticality, threat likelihood, control effectiveness and evidence into a transparent residual-risk ranking.

## Deliverable

risk_register.csv and risk_summary.json with traceable scoring rationale.

## Safety and privacy boundary

Use only the synthetic files in `data/` and `mock-data/`. Do not paste organisation logs, credentials, personal data, malware, or live incidents into any external AI service. Use the linked tool only as an education simulation or use a trainer-owned isolated Kali environment.

## Simulator or Kali-style practice

Open [tool-exercise.md](tool-exercise.md) for the controlled Cybersecurity Threat Simulation Lab exercise. The offline mock-data path is equivalent for lab evidence.

## Detailed procedure

### Step 1 - Review the asset, threat and control columns in data/input.csv.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: All rows have owner and evidence_ref

### Step 2 - Run the starter script and inspect its deliberately incomplete residual-risk calculation.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Residual scores are 0-25

### Step 3 - Implement likelihood x impact and control-effectiveness reduction without overwriting raw evidence.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Ranking changes when asset criticality changes

### Step 4 - Rank the risks, assign owners and record a confidence note for each row.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Output JSON records the scoring formula

### Step 5 - Compare the ranking with the business-process impact column and document one changed priority.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Output JSON records the scoring formula

### Step 6 - Run the smoke test and verify that every output row retains asset_id and evidence_ref.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Output JSON records the scoring formula

## Run the reference and tests

```bash
python3 solution/main.py
python3 -m pytest -q tests
```

## Acceptance checks

- [ ] All rows have owner and evidence_ref
- [ ] Residual scores are 0-25
- [ ] Ranking changes when asset criticality changes
- [ ] Output JSON records the scoring formula

## Troubleshooting

- `FileNotFoundError`: run from the lab folder and confirm `data/input.csv`.
- Missing package: create a virtual environment and install `requirements.txt`.
- Unexpected score: inspect types, nulls, baseline split and threshold direction.
- Too many alerts: state the capacity constraint before tuning the threshold.

## Reflection

Explain one limitation, one control and one condition that prevents production use.
