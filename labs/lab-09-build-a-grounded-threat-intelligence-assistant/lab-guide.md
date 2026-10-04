# Lab 9: Build a Grounded Threat-Intelligence Assistant

**Mapped outcome:** LO3
**Tools:** Python 3 · TF-IDF · local documents · Hacklab: Ethical Hacking Lab Simulator

## Objective

Retrieve from approved threat bulletins and produce cited, abstaining summaries without external APIs.

## Deliverable

`retrieval_results.json` and `cited-analyst-brief.md`.

## Safety and privacy boundary

Use only the synthetic files in `data/` and `mock-data/`. Do not paste organisation logs, credentials, personal data, malware, or live incidents into any external AI service. Use the linked tool only as an education simulation or use a trainer-owned isolated Kali environment.

## Simulator or Kali-style practice

Open [tool-exercise.md](tool-exercise.md) for the controlled Hacklab: Ethical Hacking Lab Simulator exercise. The offline mock-data path is equivalent for lab evidence.

## Detailed procedure

### Step 1 - Review the approved local threat bulletins and document ACL metadata.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Every claim has document citation

### Step 2 - Chunk and index the documents with TF-IDF.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: ACL filtering occurs before retrieval

### Step 3 - Retrieve top-k evidence for each analyst query.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Unknown query abstains

### Step 4 - Generate an extractive summary that cites document IDs.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Embedded instructions are treated as data

### Step 5 - Return 'insufficient evidence' below the similarity threshold.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Embedded instructions are treated as data

### Step 6 - Test forbidden-document and indirect-instruction cases.

1. Work from this individual lab folder.
2. Record the evidence field or configuration used for the decision.
3. Complete and run `python3 starter/main.py`.
4. Compare with the acceptance criterion before opening the reference solution.

> Check: Embedded instructions are treated as data

## Run the reference and tests

```bash
python3 solution/main.py
python3 -m pytest -q tests
```

## Acceptance checks

- [ ] Every claim has document citation
- [ ] ACL filtering occurs before retrieval
- [ ] Unknown query abstains
- [ ] Embedded instructions are treated as data

## Troubleshooting

- `FileNotFoundError`: run from the lab folder and confirm `data/input.csv`.
- Missing package: create a virtual environment and install `requirements.txt`.
- Unexpected score: inspect types, nulls, baseline split and threshold direction.
- Too many alerts: state the capacity constraint before tuning the threshold.

## Reflection

Explain one limitation, one control and one condition that prevents production use.
