# ARPWatch - ARP Spoofing Detector

## Student Information
- Student: Haziq
- Track: Network Defense and Detection
- Department: Cyber Security
- Instructor: Abdul Mannan
- Organization: PNY Trainings

## Project Overview
ARPWatch is a Python-based network monitoring and security learning project.
Its purpose is to study ARP traffic and understand how suspicious IP-to-MAC
mapping changes can be identified.

## Objectives
- Understand the Address Resolution Protocol (ARP).
- Learn IP-to-MAC mapping.
- Understand suspicious MAC address changes.
- Study Gratuitous ARP announcements.
- Learn Python dictionaries and sets.
- Practice alert formatting and logging.
- Understand command-line arguments.

## Technologies Used
- Python 3
- Scapy
- Kali Linux
- VMware Virtual Machines

## Project Features
1. ARP packet observation
2. IP-to-MAC mapping table
3. MAC-change comparison logic
4. Gratuitous ARP identification
5. MAC-to-IP reverse mapping
6. Timestamped logging
7. Command-line argument practice
8. Allowlist file handling

## Project Files
- step1.py - ARP observation practice
- step2.py - IP-to-MAC table
- step3.py - MAC comparison logic
- step4.py - Gratuitous ARP identification
- step5.py - MAC-to-IP reverse mapping
- step6.py - Alert logging
- step7.py - Command-line configuration
- allowlist.txt - Sample trusted mappings
- arpwatch.log - Sample alert log

## Testing
Each individual Python module was checked for syntax errors
and basic behavior using sample data.

These individual tests do not represent a complete end-to-end
network detection test.

## Limitations
- Individual modules are not yet integrated into one application.
- Sample data tests do not prove real network detection.
- Alerts may represent legitimate network changes.
- Further development and authorized lab validation are required.

## Safety
This project is intended for cybersecurity education and
authorized laboratory environments only.

## Author
Haziq
PNY Trainings - Cyber Security Department
