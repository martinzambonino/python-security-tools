# Python Security Tools

![GitHub Actions Status](https://img.shields.io/github/actions/workflow/status/martinzambonino/python-security-tools/ci.yml?branch=main)
![License](https://img.shields.io/github/license/martinzambonino/python-security-tools)

## What It Does

A collection of Python-based security utilities designed for educational exploration of common cybersecurity tasks:

- **Port Scanner:** TCP connect and SYN scan implementations for network reconnaissance in controlled environments.
- **Password Strength Analyzer:** Evaluates password entropy, common patterns, and dictionary-based weaknesses.
- **Hash Verifier:** Computes and compares cryptographic hashes (SHA-256, SHA-512, BLAKE2) for file integrity verification.
- **Log Parser:** Parses and analyzes system/application logs to detect anomalous patterns (failed logins, privilege escalations).

## Skills Demonstrated

| Skill | Details |
|---|---|
| Python 3 | OOP, type hints, standard library, CLI design |
| Security Scripting | Network sockets, hashlib, log analysis |
| Automation | Argparse CLI, structured output (JSON/CSV) |
| DevSecOps | SAST with Bandit, linting with Ruff, CI/CD |

## How to Run

```bash
# Clone the repository
git clone https://github.com/martinzambonino/python-security-tools.git
cd python-security-tools

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Run a tool (example)
python src/port_scanner.py --help
```

## Methodology

- **OWASP Testing Guide:** Reference for network and application security testing patterns.
- **NIST SP 800-115:** Technical Guide to Information Security Testing and Assessment.
- **CWE/SANS Top 25:** Common vulnerability patterns addressed by the tools.

## Limitations

- Tools are designed for **educational use only** in controlled lab environments.
- Port scanning capabilities are deliberately simplified and must **never** be used against systems without explicit written authorization.
- Password analysis uses publicly available wordlists (e.g., `rockyou` subsets) — no real credential data is processed.
- Log parsing works with synthetic log data generated via Faker.

## ⚖️ Ethical & Legal Disclaimer

> [!WARNING]
> **This repository is strictly for academic and educational purposes.**
> The tools provided must **not** be used against systems, networks, or data without explicit, written authorization from the owner.
> Unauthorized use of these tools may violate local, national, and international laws.
> The author assumes no liability for misuse.

### 🇪🇨 Compliance Note (Ecuador — LOPDP/SPDP)

This project adheres to Privacy by Design and Default principles.
**No real personal data is used, stored, or processed.** All datasets are purely synthetic (generated via `Faker`) or officially public academic datasets. This is compliant with the *Ley Orgánica de Protección de Datos Personales (LOPDP)* and auditable by the *Superintendencia de Protección de Datos Personales (SPDP)*.
