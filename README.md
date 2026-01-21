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


pip install flake8 black
pip install bandit
bandit -r app/