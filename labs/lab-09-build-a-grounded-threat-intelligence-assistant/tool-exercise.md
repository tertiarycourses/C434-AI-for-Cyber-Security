# Tool exercise - Lab 9: Build a Grounded Threat-Intelligence Assistant

**Training surface:** [Hacklab: Ethical Hacking Lab Simulator](https://alfredang.github.io/ethnicalhacking/)
**Module:** Reconnaissance scenario

## Scope and safety

The public site is an education-only simulation. Use only its built-in fictional scenario. Do not run scanners, password attacks or exploit traffic against the public site or any unrelated system.

If the trainer provides Kali, reproduce the exercise only against an isolated, trainer-owned target with written authorisation. The browser simulator is the default.

## Exercise

Capture simulated reconnaissance facts, convert them into approved local bulletins and test citation and abstention behaviour.

## Simulated terminal commands

Enter these commands only in the Hacklab browser terminal. They are listed to practise evidence interpretation, not to authorise live-system testing.

```text
whois megacorp.local
nslookup megacorp.local
theHarvester -d megacorp.local
```

## Evidence to capture

1. Record the fictional scenario or module used.
2. Copy only non-sensitive simulated observations into `evidence/tool-observations.md`.
3. Link each observation to a local file in `mock-data/`.
4. State one limitation and one human approval point.

## Offline fallback

If the site is unavailable, complete the same reasoning task with the files in `mock-data/`; the assessed lab remains fully runnable offline.
