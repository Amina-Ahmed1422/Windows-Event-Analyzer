import subprocess 
import os 
from datetime import datetime

print("=" * 50) 
print("       WINDOWS EVENT ANALYZER") 
print("=" * 50)

print("\n[+] Collecting Windows Security Events...")

event_ids = { 
    4624: "Successful Logon", 
    4625: "Failed Logon", 
    4672: "Special Privileges Assigned" 
}
event_counts = {}

for event_id, event_name in event_ids.items():
    command = [
    "powershell",
    "-Command",
    f"@(Get-WinEvent -FilterHashtable "
    f"@{{LogName='Security'; Id={event_id}}} "
    f"-MaxEvents 50).Count"
]

result = subprocess.run(
    command,
    capture_output=True,
    text=True
)

try:
    count = int(result.stdout.strip())
except ValueError:
    count = 0

event_counts[event_id] = count

print(f"\n{event_name} (Event ID {event_id})")
print(f"Events found: {count}")

failed_logins = event_counts.get(4625, 0)

if failed_logins >= 10:
     risk_level = "HIGH" 
     recommendation = ( 
         "Investigate possible brute-force activity " 
         "and review the source IP addresses." 
    )
elif failed_logins >= 5: 
    risk_level = "MEDIUM" 
    recommendation = ( 
        "Monitor failed login activity and investigate " 
        "repeated authentication failures." 
    )
else:
    risk_level = "LOW" 
    recommendation = ( 
    "Continue monitoring Windows authentication events." 
    )

os.makedirs("results", exist_ok=True)

report_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
report = f""" 
WINDOWS SECURITY ANALYSIS REPORT
=====================================
Analysis Time: 
{report_time}
EVENT SUMMARY
----------------------
Successful Logons (4624): 
{event_counts.get(4624, 0)}

Failed Logons (4625): 
{event_counts.get(4625, 0)}

Special Privileges (4672): 
{event_counts.get(4672, 0)}

SECURITY ASSESSMENT
------------------------

Failed Login Attempts: 
{failed_logins}

Risk Level: 
{risk_level}

Recommendation: 
{recommendation}

ANALYST NOTE
----------------
This report was generated automatically by the Windows Event Analyzer project. 
"""
report_path = os.path.join( 
    "results", 
    "security_report.txt" 
    )
with open(report_path, "w", encoding="utf-8") as file: 
    file.write(report)

print("\n" + "=" * 50) 
print("           SECURITY REPORT") 
print("=" * 50)
print(f"\n[+] Risk Level: {risk_level}") 
print(f"[+] Report saved to: {report_path}")

print("\n[+] Analysis completed.")