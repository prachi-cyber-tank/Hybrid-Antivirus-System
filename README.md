# Hybrid-Antivirus-System

# Hybrid Signature + Heuristic Antivirus System

## Overview
This project is a Windows-based Hybrid Antivirus Prototype developed in Python.
It combines Signature-Based Detection and Heuristic Analysis to identify malicious or suspicious files.

## Features
- SHA-256 based file hashing
- Signature-based malware detection
- Heuristic keyword-based detection
- Automatic file quarantine system
- Timestamp-based logging
- Scan summary reporting
- File type filtering (.py, .exe, .txt, .bat)
- Command Line Interface (CLI)

## How It Works
1. The system scans files inside a specified folder.
2. A SHA-256 hash is generated for each file.
3. The hash is compared against a malware signature database.
4. If matched → File marked INFECTED and moved to quarantine.
5. If suspicious keywords are detected → File marked SUSPICIOUS.
6. All results are logged with timestamps.
7. A scan summary is displayed.

## Project Structure
- main.py → CLI interface
- scanner.py → Detection engine
- hash_utils.py → Hash generation
- quarantine.py → File isolation
- signatures.txt → Malware database
- scan_log.txt → Scan logs

## Limitations
- Cannot detect zero-day malware fully
- No real-time background monitoring
- Heuristic detection is keyword-based only

## Future Improvements
- GUI interface
- Real-time file monitoring
- Machine learning-based detection
- Cloud signature updates

## Author
Prachi Tank
