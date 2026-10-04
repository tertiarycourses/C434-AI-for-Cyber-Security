# Lab 12: Monitor Model Effectiveness and Produce Advice

**Mapped outcome:** LO4
**Tools:** Python 3 · pandas · scikit-learn metrics · Cryptography Toolkit

## Objective

Measure detection quality, identify drift and control failures, then issue evidence-backed adoption advice.

## Deliverable

monitoring_report.json and advisory_report.md.

## Safety and privacy boundary

Use only the synthetic files in `data/` and `mock-data/`. Do not paste organisation logs, credentials, personal data, malware, or live incidents into any external AI service. Use the linked tool only as an education simulation or use a trainer-owned isolated Kali environment.

## Simulator or Kali-style practice

Open [tool-exercise.md](tool-exercise.md) for the controlled Cryptography Toolkit exercise. The offline mock-data path is equivalent for lab evidence.

## Detailed procedure

### Step 1 - Build the confusion matrix from labelled outcomes.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Metrics include class prevalence

### Step 2 - Calculate precision, recall, F1 and false-positive rate.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Drift is diagnostic, not automatic retraining

### Step 3 - Compare feature distributions with the reference window.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Advice separates fact/inference/recommendation

### Step 4 - Review prompt-injection, citation and permission tests.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Each action has owner and measure

### Step 5 - Map findings to NIST CSF/AI RMF control outcomes.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Each action has owner and measure

### Step 6 - Write a recommendation with options, limitations, owner, metric and 30/60/90-day follow-up.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Each action has owner and measure

## Run the reference and tests

```bash
python3 solution/main.py
python3 -m pytest -q tests
```

## Acceptance checks

- [ ] Metrics include class prevalence
- [ ] Drift is diagnostic, not automatic retraining
- [ ] Advice separates fact/inference/recommendation
- [ ] Each action has owner and measure

## Troubleshooting

- `FileNotFoundError`: run from the lab folder and confirm `data/input.csv`.
- Missing package: create a virtual environment and install `requirements.txt`.
- Unexpected score: inspect types, nulls, baseline split and threshold direction.
- Too many alerts: state the capacity constraint before tuning the threshold.

## Reflection

Explain one limitation, one control and one condition that prevents production use.
