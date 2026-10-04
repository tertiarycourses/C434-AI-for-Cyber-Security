# Lab 5: Select and Scope an AI Security Use Case

**Mapped outcome:** LO2
**Tools:** Python 3 · CSV · Markdown · Cybersecurity Threat Simulation Lab

## Objective

Score candidate use cases on value, data readiness, integration effort, operating risk and human-oversight requirements.

## Deliverable

`use_case_scorecard.csv` and `pilot-charter.md`.

## Safety and privacy boundary

Use only the synthetic files in `data/` and `mock-data/`. Do not paste organisation logs, credentials, personal data, malware, or live incidents into any external AI service. Use the linked tool only as an education simulation or use a trainer-owned isolated Kali environment.

## Simulator or Kali-style practice

Open [tool-exercise.md](tool-exercise.md) for the controlled Cybersecurity Threat Simulation Lab exercise. The offline mock-data path is equivalent for lab evidence.

## Detailed procedure

### Step 1 - Define the security outcome and decision owner.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Selected use case has measurable baseline

### Step 2 - Score each use case against the provided rubric.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Decision owner named

### Step 3 - Apply a risk penalty for high-impact autonomous action.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Automation ceiling explicit

### Step 4 - Select one pilot and state the baseline and target.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Stop criteria included

### Step 5 - Set automation ceiling, stop criteria and review date.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Stop criteria included

### Step 6 - Peer-review the charter against LO2.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Stop criteria included

## Run the reference and tests

```bash
python3 solution/main.py
python3 -m pytest -q tests
```

## Acceptance checks

- [ ] Selected use case has measurable baseline
- [ ] Decision owner named
- [ ] Automation ceiling explicit
- [ ] Stop criteria included

## Troubleshooting

- `FileNotFoundError`: run from the lab folder and confirm `data/input.csv`.
- Missing package: create a virtual environment and install `requirements.txt`.
- Unexpected score: inspect types, nulls, baseline split and threshold direction.
- Too many alerts: state the capacity constraint before tuning the threshold.

## Reflection

Explain one limitation, one control and one condition that prevents production use.
