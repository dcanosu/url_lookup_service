![Python CI](https://github.com/USUARIO/REPO/actions/workflows/main.yml/badge.svg)
# URL Lookup Service

A lightweight Flask service that checks if a requested URL is present in a malware database. This service is designed to be used by an HTTP proxy to block malicious traffic.

## Project Structure
- `app/`: Contains the Flask application logic and the malware database.
- `tests/`: Contains functional tests using `pytest`.
- `requirements.txt`: Lists Python dependencies.

## Setup Instructions

### 1. Prerequisites
- Python 3.x
- macOS or Linux

### 2. Installation
From the project root directory, create a virtual environment and install dependencies:
```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```
### 3. Running the Service
```bash
python3 -m app.main
```
### 4. Running the Tests
```bash
python3 -m pytest
```
## Design Decisions & Best Practices

- **Security First:** The lookup logic uses **Prefix Matching**. This ensures that blocking a root domain effectively blocks all subsequent paths and resources.
- **Input Sanitization:** All incoming requests are normalized (lowercased and stripped) to prevent common evasion tactics.
- **Performance:** For Part 1, we utilize an in-memory set. While the current prefix-search is $O(N)$, for Part 2 (Scale), I recommend migrating to a **Trie (Prefix Tree)** or **Redis with Scan** to maintain constant-time performance.
- **Observability:** Integrated Python's `logging` module to track blocked attempts, facilitating integration with SIEM tools or ELK stacks.


### Key Features
- **Health Check Endpoint:** Includes `/health` for container orchestration (Liveness/Readiness probes).
- **Graceful Error Handling:** Standardized JSON error responses.
- **Configurable Environment:** Support for dynamic port assignment via environment variables.
- **Structured Logging:** Ready for log aggregation services (like ELK or CloudWatch).
pip install flake8 black
pip install bandit
bandit -r app/
python3 -m pip install pre-commit
