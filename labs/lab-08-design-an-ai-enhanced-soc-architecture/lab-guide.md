# Lab 8: Design an AI-Enhanced SOC Architecture

**Mapped outcome:** LO3
**Tools:** JSON · architecture template · Cryptography Toolkit

## Objective

Design a layered architecture that separates evidence, inference, case management and guarded action.

## Deliverable

`soc_architecture.json` and `ADR-001.md`.

## Safety and privacy boundary

Use only the synthetic files in `data/` and `mock-data/`. Do not paste organisation logs, credentials, personal data, malware, or live incidents into any external AI service. Use the linked tool only as an education simulation or use a trainer-owned isolated Kali environment.

## Simulator or Kali-style practice

Open [tool-exercise.md](tool-exercise.md) for the controlled Cryptography Toolkit exercise. The offline mock-data path is equivalent for lab evidence.

## Detailed procedure

### Step 1 - Inventory telemetry sources and owners.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Raw evidence is immutable

### Step 2 - Define immutable evidence and normalized event stores.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Model and prompt versions logged

### Step 3 - Place rule, ML and LLM services behind explicit interfaces.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Tool actions use scoped identity

### Step 4 - Add case-management evidence links and a tool-broker approval gate.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Manual fallback documented

### Step 5 - Document identity, logging, fallback and recovery paths.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Manual fallback documented

### Step 6 - Validate the architecture against the provided control checklist.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Manual fallback documented

## Run the reference and tests

```bash
python3 solution/main.py
python3 -m pytest -q tests
```

## Acceptance checks

- [ ] Raw evidence is immutable
- [ ] Model and prompt versions logged
- [ ] Tool actions use scoped identity
- [ ] Manual fallback documented

## Troubleshooting

- `FileNotFoundError`: run from the lab folder and confirm `data/input.csv`.
- Missing package: create a virtual environment and install `requirements.txt`.
- Unexpected score: inspect types, nulls, baseline split and threshold direction.
- Too many alerts: state the capacity constraint before tuning the threshold.

## Reflection

Explain one limitation, one control and one condition that prevents production use.
