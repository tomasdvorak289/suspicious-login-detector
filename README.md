# Suspicious Login Detector

A simple Python cybersecurity project that detects suspicious IP addresses based on failed login attempts.

## Features

- Loads login records from CSV files.
- Counts failed login attempts for each IP address.
- Identifies suspicious IP addresses based on a configurable threshold.
- Uses a modular Python project structure.

## Technologies

- Python 3
- CSV
- Git & GitHub

## Installation

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the project:

```bash
python3 -m pip install -e .
```

## Usage

Run the detector from the project root:

```bash
python3 -m tests.test_detector
```

Example output:

```text
['192.168.1.1']
```

The default detection threshold is 3 failed login attempts.

## Future Improvements

- Automated testing with pytest
- Advanced login analysis
- Machine learning for anomaly detection
- REST API using FastAPI
- Docker support

## Status

Version 0.1.0 — Work in progress.