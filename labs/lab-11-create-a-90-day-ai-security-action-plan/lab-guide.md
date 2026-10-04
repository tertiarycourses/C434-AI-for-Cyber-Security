# Lab 11: Create a 90-Day AI Security Action Plan

**Mapped outcome:** LO3
**Tools:** Python 3 · CSV · Hacklab: Ethical Hacking Lab Simulator

## Objective

Sequence architecture work packages, dependencies, acceptance evidence and regulatory review triggers.

## Deliverable

`action_plan.csv` and `roadmap.md`.

## Safety and privacy boundary

Use only the synthetic files in `data/` and `mock-data/`. Do not paste organisation logs, credentials, personal data, malware, or live incidents into any external AI service. Use the linked tool only as an education simulation or use a trainer-owned isolated Kali environment.

## Simulator or Kali-style practice

Open [tool-exercise.md](tool-exercise.md) for the controlled Hacklab: Ethical Hacking Lab Simulator exercise. The offline mock-data path is equivalent for lab evidence.

## Detailed procedure

### Step 1 - Import the target architecture work packages.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: No dependency cycles

### Step 2 - Assign owner, duration, dependency and acceptance evidence.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Every work package has evidence

### Step 3 - Detect missing or cyclic dependencies.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Critical path identified

### Step 4 - Calculate earliest start and critical path.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Change triggers recorded

### Step 5 - Add model/provider change and regulatory-review triggers.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Change triggers recorded

### Step 6 - Present the 30/60/90-day roadmap for approval.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Change triggers recorded

## Run the reference and tests

```bash
python3 solution/main.py
python3 -m pytest -q tests
```

## Acceptance checks

- [ ] No dependency cycles
- [ ] Every work package has evidence
- [ ] Critical path identified
- [ ] Change triggers recorded

## Troubleshooting

- `FileNotFoundError`: run from the lab folder and confirm `data/input.csv`.
- Missing package: create a virtual environment and install `requirements.txt`.
- Unexpected score: inspect types, nulls, baseline split and threshold direction.
- Too many alerts: state the capacity constraint before tuning the threshold.

## Reflection

Explain one limitation, one control and one condition that prevents production use.
