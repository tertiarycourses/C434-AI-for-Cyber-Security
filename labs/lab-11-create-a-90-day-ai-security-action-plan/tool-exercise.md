# Tool exercise - Lab 11: Create a 90-Day AI Security Action Plan

**Training surface:** [Hacklab: Ethical Hacking Lab Simulator](https://alfredang.github.io/ethnicalhacking/)
**Module:** Network scanning scenario

## Scope and safety

The public site is an education-only simulation. Use only its built-in fictional scenario. Do not run scanners, password attacks or exploit traffic against the public site or any unrelated system.

If the trainer provides Kali, reproduce the exercise only against an isolated, trainer-owned target with written authorisation. The browser simulator is the default.

## Exercise

Use simulated discovery evidence to sequence work packages, dependencies, owners and acceptance gates in a 90-day plan.

## Simulated terminal commands

Enter these commands only in the Hacklab browser terminal. They are listed to practise evidence interpretation, not to authorise live-system testing.

```text
nmap -sn 10.10.10.0/24
nmap -sS 10.10.10.5
nmap -O 10.10.10.5
```

## Evidence to capture

1. Record the fictional scenario or module used.
2. Copy only non-sensitive simulated observations into `evidence/tool-observations.md`.
3. Link each observation to a local file in `mock-data/`.
4. State one limitation and one human approval point.

## Offline fallback

If the site is unavailable, complete the same reasoning task with the files in `mock-data/`; the assessed lab remains fully runnable offline.
