# Lab 10: Design a Guarded SOAR Playbook

**Mapped outcome:** LO3
**Tools:** Python 3 · JSON · FauxBank Cybersecurity Training Simulation

## Objective

Build a reversible, approval-gated response playbook for suspicious account activity.

## Deliverable

playbook.json and dry_run_report.json.

## Safety and privacy boundary

Use only the synthetic files in `data/` and `mock-data/`. Do not paste organisation logs, credentials, personal data, malware, or live incidents into any external AI service. Use the linked tool only as an education simulation or use a trainer-owned isolated Kali environment.

## Simulator or Kali-style practice

Open [tool-exercise.md](tool-exercise.md) for the controlled FauxBank Cybersecurity Training Simulation exercise. The offline mock-data path is equivalent for lab evidence.

## Detailed procedure

### Step 1 - Define trigger evidence and entity-resolution preconditions.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Default mode is dry-run

### Step 2 - Add enrichment and confidence checks.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Target identity is verified

### Step 3 - Simulate account containment and calculate blast radius.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Approval recorded

### Step 4 - Require approval for identity-impacting actions.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Rollback and post-check exist

### Step 5 - Define rollback and post-action verification.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Rollback and post-check exist

### Step 6 - Run safe dry-run tests; no real accounts are modified.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Rollback and post-check exist

## Run the reference and tests

```bash
python3 solution/main.py
python3 -m pytest -q tests
```

## Acceptance checks

- [ ] Default mode is dry-run
- [ ] Target identity is verified
- [ ] Approval recorded
- [ ] Rollback and post-check exist

## Troubleshooting

- `FileNotFoundError`: run from the lab folder and confirm `data/input.csv`.
- Missing package: create a virtual environment and install `requirements.txt`.
- Unexpected score: inspect types, nulls, baseline split and threshold direction.
- Too many alerts: state the capacity constraint before tuning the threshold.

## Reflection

Explain one limitation, one control and one condition that prevents production use.
