# ARPWatch - Test Report

## Project
ARPWatch - ARP Spoofing Detector

## Environment
- OS: Kali Linux
- Language: Python 3
- Project Type: Network Defense and Detection

## Test 1 - IP to MAC Mapping
Result: Tested with sample data.
Status: PASS

## Test 2 - MAC Change Comparison
Result: Tested comparison logic with sample values.
Status: PASS

## Test 3 - Gratuitous ARP Identification
Result: Checked using sample packet fields.
Status: PASS

## Test 4 - MAC to IP Reverse Mapping
Result: Tested with sample records.
Status: PASS

## Test 5 - Alert Logging
Result: Checked timestamp formatting and file logging.
Status: PASS

## Test 6 - Allowlist Configuration
Result: Tested allowlist parsing with sample file.
Status: PASS

## Test 7 - Command Line Arguments
Result: Checked default and custom argument values.
Status: PASS

## Overall Result
Individual modules were tested with sample data.
The modules have not been integrated into a complete application.
No end-to-end network detection test is claimed.

## Safety
Testing is intended for an isolated, authorized lab environment.
