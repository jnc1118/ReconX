# ReconX

> **Automated Reconnaissance Framework for Cybersecurity**

ReconX is a modular Python-based reconnaissance framework developed as part of a Cyber Security Internship at IIIT Kottayam to automate the initial reconnaissance phase of security assessments. It streamlines the collection of target information such as DNS records, WHOIS information, and network services using Nmap, and generates structured reports for analysis.

---

## Features

- Target validation (Domain, IP Address, URL)
- DNS Enumeration
  - A Records
  - AAAA Records
  - MX Records
  - NS Records
  - TXT Records
  - CNAME Records
- WHOIS Information Lookup
- Nmap Service & Version Detection
- Rich Terminal Interface
- Automatic Report Generation
- Scan Summary
- Total Scan Time Display

---

## Project Architecture

```
                +----------------+
                |    User Input  |
                +--------+-------+
                         |
                         v
               Target Validation
                         |
                         v
          +--------------+--------------+
          |                             |
          v                             v
     DNS Lookup                  WHOIS Lookup
          |                             |
          +--------------+--------------+
                         |
                         v
                   Nmap Scanning
                         |
                         v
                  Report Generation
                         |
                         v
                  Scan Summary
```

---

## Tech Stack

- Python 3
- Rich
- dnspython
- python-whois
- Nmap

---

## Project Structure

```
ReconX/
│
├── core/
│   ├── banner.py
│   ├── validator.py
│   └── report.py
│
├── modules/
│   ├── dns_lookup.py
│   ├── whois_lookup.py
│   └── nmap_scan.py
│
├── reports/
│
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/ReconX.git
```

Move into the project directory

```bash
cd ReconX
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

Linux

```bash
source venv/bin/activate
```

Windows

```powershell
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

Run the application

```bash
python main.py
```

Example

```
Enter Target:

google.com
```

ReconX will automatically

- Validate the target
- Perform DNS enumeration
- Retrieve WHOIS information
- Execute an Nmap scan
- Generate a report
- Display the scan summary

---

## Sample Output

```
✓ Target Validated

DNS Lookup Completed

WHOIS Lookup Completed

Running Nmap Scan...

Nmap Scan Completed

Report Generated

Total Scan Time: 18.42 seconds
```

---

## Future Enhancements

- GeoIP Lookup
- SSL/TLS Analysis
- HTTP Security Headers
- Technology Detection
- Subdomain Enumeration
- Website Screenshot Capture
- HTML/PDF Report Generation
- Shodan Integration
- VirusTotal Integration
- CVE Mapping
- Multi-threaded Scanning
- Web Dashboard

---

## Author

**John Paul**

B.Tech Computer Science and Engineering

Mar Athanasius College of Engineering

Cyber Security Intern – IIIT Kottayam