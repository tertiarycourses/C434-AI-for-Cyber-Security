# Lab 2: Detect Authentication Anomalies

**Mapped outcome:** LO1
**Tools:** Python 3 · pandas · scikit-learn · FauxBank Cybersecurity Training Simulation

## Objective

Create a peer-aware anomaly score from failed logins, new-device state and impossible-travel indicators.

## Deliverable

`anomalies.csv` and `threshold-decision.md`.

## Safety and privacy boundary

Use only the synthetic files in `data/` and `mock-data/`. Do not paste organisation logs, credentials, personal data, malware, or live incidents into any external AI service. Use the linked tool only as an education simulation or use a trainer-owned isolated Kali environment.

## Simulator or Kali-style practice

Open [tool-exercise.md](tool-exercise.md) for the controlled FauxBank Cybersecurity Training Simulation exercise. The offline mock-data path is equivalent for lab evidence.

## Detailed procedure

### Step 1 - Inspect the authentication schema and identify event-time, identity and device fields.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Model trained only on baseline rows

### Step 2 - Create 15-minute features per user.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Output includes anomaly_score and reason fields

### Step 3 - Fit IsolationForest only on the baseline rows.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Queue has at most three alerts

### Step 4 - Score the evaluation rows and preserve reason features.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Threshold and model random_state are recorded

### Step 5 - Tune the percentile threshold to a maximum review queue of three alerts.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Threshold and model random_state are recorded

### Step 6 - Record false-positive risks and run the tests.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Threshold and model random_state are recorded

## Run the reference and tests

```bash
python3 solution/main.py
python3 -m pytest -q tests
```

## Acceptance checks

- [ ] Model trained only on baseline rows
- [ ] Output includes anomaly_score and reason fields
- [ ] Queue has at most three alerts
- [ ] Threshold and model random_state are recorded

## Troubleshooting

- `FileNotFoundError`: run from the lab folder and confirm `data/input.csv`.
- Missing package: create a virtual environment and install `requirements.txt`.
- Unexpected score: inspect types, nulls, baseline split and threshold direction.
- Too many alerts: state the capacity constraint before tuning the threshold.

## Reflection

Explain one limitation, one control and one condition that prevents production use.
