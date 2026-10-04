# Lab 7: Build the AI Security Programme Charter

**Mapped outcome:** LO2
**Tools:** Markdown · CSV · policy template · FauxBank Cybersecurity Training Simulation

## Objective

Translate assessed control gaps into governed programme epics, metrics, owners and decision gates.

## Deliverable

programme_charter.md and RACI.csv.

## Safety and privacy boundary

Use only the synthetic files in `data/` and `mock-data/`. Do not paste organisation logs, credentials, personal data, malware, or live incidents into any external AI service. Use the linked tool only as an education simulation or use a trainer-owned isolated Kali environment.

## Simulator or Kali-style practice

Open [tool-exercise.md](tool-exercise.md) for the controlled FauxBank Cybersecurity Training Simulation exercise. The offline mock-data path is equivalent for lab evidence.

## Detailed procedure

### Step 1 - Select the highest-priority control gaps from the lab data.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Every epic traces to a gap

### Step 2 - Write outcome-based objectives and measurable targets.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Metric has baseline and target

### Step 3 - Group work into data, model, integration, people and assurance epics.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: RACI has one accountable owner

### Step 4 - Create RACI assignments and an escalation route.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Retirement/exit gate exists

### Step 5 - Define pilot, production and retirement gates.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Retirement/exit gate exists

### Step 6 - Run the charter checklist and resolve missing owners.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Retirement/exit gate exists

## Run the reference and tests

```bash
python3 solution/main.py
python3 -m pytest -q tests
```

## Acceptance checks

- [ ] Every epic traces to a gap
- [ ] Metric has baseline and target
- [ ] RACI has one accountable owner
- [ ] Retirement/exit gate exists

## Troubleshooting

- `FileNotFoundError`: run from the lab folder and confirm `data/input.csv`.
- Missing package: create a virtual environment and install `requirements.txt`.
- Unexpected score: inspect types, nulls, baseline split and threshold direction.
- Too many alerts: state the capacity constraint before tuning the threshold.

## Reflection

Explain one limitation, one control and one condition that prevents production use.
