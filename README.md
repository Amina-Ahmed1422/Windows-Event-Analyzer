**Windows Event Analyzer
## Overview
Windows Event Analyzer is a Python-based Blue Team security tool designed to analyze Windows Security Event Logs and identify suspicious authentication activity.

The project focuses on detecting failed login attempts, analyzing Windows security events, identifying possible brute-force activity, classifying risk levels, and generating an automated security report.
## Features
-Analyze Windows Security Event Logs
-Detect Event ID 4624 — Successful Logon
-Detect Event ID 4625 — Failed Logon
-Detect Event ID 4672 — Special Privileges Assigned
-Count authentication events
-Extract usernames from failed login events
-Extract source IP addresses when available
-Detect possible brute-force activity
-Classify activity as LOW, MEDIUM, or HIGH risk
-Generate an automated security report

## Technologies
-Python
-PowerShell
-Windows Event Logs
-Regular Expressions
-Git & GitHub
## Detection Logic
The analyzer focuses on several Windows Security Event IDs:
Event ID   Description
4624       Successful Logon
4625       Failed Logon
4672      Special Privileges Assigned

For training purposes, repeated failed login attempts are used as an indicator of possible brute-force activity.

The project uses a threshold-based approach:
-0–4 failed attempts → LOW
-5–9 failed attempts → MEDIUM
-10+ failed attempts → HIGH

These thresholds are simplified rules for this educational project and should not be treated as definitive evidence of an attack.
Project Structure
Windows-Event-Analyzer/
│
├── event_analyzer.py
├── README.md
├── requirements.txt
│
└── results/
    └── security_report.txt
## How to Run
Open PowerShell or the VS Code Terminal inside the project directory.
Run:

python event_analyzer.py

The analyzer will collect Windows Security Events and display the results in the terminal.
A security report will also be generated automatically:

results/security_report.txt

## Example Output
WINDOWS EVENT ANALYZER

Successful Logons (Event ID 4624)
Events found: 20

Failed Logons (Event ID 4625)
Events found: 7

Special Privileges Assigned (Event ID 4672)
Events found: 3

SECURITY ASSESSMENT

Failed Login Attempts: 7
Risk Level: MEDIUM

Brute Force Assessment:
POSSIBLE BRUTE-FORCE ACTIVITY DETECTED

## Security Use Case
This project demonstrates basic Security Operations Center (SOC) concepts, including:
-Authentication monitoring
-Windows event analysis
-Detection of suspicious login activity
-Basic threat detection
-Alert generation
-Security reporting

It can be used as a learning project for Blue Team and Security Analyst skills.
## Future Improvements

Possible future enhancements include:
-Detecting multiple failed logins from the same IP within a specific time window
-Adding Event ID 4648 analysis
-Exporting results to CSV
-Creating a graphical dashboard
-Adding email or alert notifications
-Integrating the tool with a SIEM
-Adding more advanced detection rules
## Disclaimer
This project is intended for educational and defensive cybersecurity purposes.
The detection rules are simplified and should be validated before being used in a real production environment.