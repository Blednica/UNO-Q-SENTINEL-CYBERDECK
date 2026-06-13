# UNO Q Sentinel

A lightweight cyberdeck-inspired system monitoring and incident response utility written in Python.

UNO Q Sentinel provides quick access to system information, network status, basic reconnaissance tools, logging capabilities, and forensic snapshot generation from a simple terminal interface.

---

## Features

### System Monitoring

* Display hostname
* Display local IP address
* Check internet connectivity
* View system status information
* Operating system identification

### Logging

* Save system status to a timestamped log file
* Record hostname, IP address, and network status

### Network Reconnaissance

* ARP table enumeration
* MAC address discovery of local network devices
* Basic network visibility

### Incident Response

* Generate forensic-style incident snapshots
* Collect:

  * Hostname
  * IP Address
  * Operating System
  * Active users
  * Running processes
  * Network connections
  * ARP cache data

### File Analysis

* SHA-256 file hashing
* Verify file integrity
* Generate hashes for evidence collection

---

## Requirements

Python 3.10+

Standard Python libraries:

```text
socket
subprocess
platform
hashlib
datetime
pathlib
```

No third-party packages are currently required.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/USERNAME/uno-q-sentinel.git
cd uno-q-sentinel
```

Run:

```bash
python3 sentinel.py
```

---

## Menu

```text
=== UNO Q SENTINEL CYBERDECK ===

1 - Show hostname
2 - Show IP
3 - Check internet
4 - Show status
5 - Save status log
6 - MAC / ARP scan
7 - Incident snapshot
8 - Hash file
9 - Exit
```

---

## Example Incident Snapshot

The Incident Snapshot feature generates a report containing:

```text
=== UNO Q SENTINEL INCIDENT SNAPSHOT ===

Timestamp
Hostname
IP Address
Operating System

ARP Table
Logged-in Users
Running Processes
Network Connections
```

Output:

```text
incident_snapshot_YYYYMMDD_HHMMSS.txt
```

---

## Log Format

Status logs are saved to:

```text
status.log
```

Example:

```text
2026-06-13 15:10:22    sentinel01    192.168.1.50    True
```

---

## Intended Use

UNO Q Sentinel is designed as a learning platform and cyberdeck utility for:

* Cybersecurity students
* DFIR practice
* Network visibility
* Incident response exercises
* System administration
* Security automation experimentation

---

## Roadmap

Planned features:

* System health dashboard
* RAM and disk monitoring
* Wi-Fi information
* Threat intelligence lookups
* Device inventory tracking
* Configuration profiles
* Exportable reports
* TUI dashboard mode
* OLED/LCD cyberdeck display support
* Raspberry Pi integration
* GPS support
* Portable forensic toolkit mode

---

## Disclaimer

This software is intended for educational, research, administrative, and defensive security purposes only. Users are responsible for complying with all applicable laws, regulations, and organizational policies.

---

Created for the UNO Q Cyberdeck Project.
