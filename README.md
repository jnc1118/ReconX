# ReconX

> **Automated Reconnaissance and Vulnerability Assessment Framework**

ReconX is a modular Python-based reconnaissance and vulnerability assessment framework developed as part of a Cyber Security Internship at IIIT Kottayam. It automates the initial stages of security assessment by validating targets, collecting DNS and WHOIS information, detecting network services using Nmap, correlating detected services with known CVEs, checking IP and domain reputation, and generating structured scan reports.

---

## Features

### Target Validation

- Domain validation
- IP address validation
- URL input support
- Automatic domain-to-IP resolution
- Identification of whether the original target is an IP address or domain

### DNS Lookup

For domain targets:

- A Records
- AAAA Records
- MX Records
- NS Records
- TXT Records
- CNAME Records

For IP targets:

- Reverse DNS / PTR lookup

### WHOIS Information

- Registrar information
- Organization
- Creation date
- Expiration date
- Updated date
- Country
- Name servers

### Nmap Scanning

- Fast port scanning
- Service detection
- Service version detection
- Structured parsing of Nmap results

### CVE Vulnerability Correlation

- Extracts detected services and versions from Nmap results
- Queries the National Vulnerability Database (NVD)
- Correlates detected software with known CVEs
- Displays CVE ID, severity, CVSS score, and applicability

### IP Reputation

- Checks the reputation of the target IP
- Displays blacklist status
- Displays malicious status
- Displays confidence score
- Displays number of reports
- Displays country and ISP information
- Displays last reported information

### Domain Reputation

- Checks domain reputation when the original target is a domain
- Displays malicious and suspicious engine results
- Displays overall reputation status
- Domain reputation is not performed automatically for IP inputs to avoid incorrectly treating a reverse-DNS hostname as the target domain

### Reporting

- Automated text report generation
- Target information
- DNS/PTR information
- WHOIS information
- Nmap results
- CVE vulnerability results
- IP reputation results
- Domain reputation results when applicable
- Scan timestamp
- Total scan time

### Terminal Interface

- Rich-based formatted tables
- Structured scan output
- Scan progress indication
- Scan summary

---

## Project Architecture

```text
                         +----------------+
                         |   User Input   |
                         +-------+--------+
                                 |
                                 v
                       +-------------------+
                       | Target Validation |
                       +---------+---------+
                                 |
                  +--------------+--------------+
                  |                             |
                  v                             v
            DNS / PTR Lookup              WHOIS Lookup
                  |                             |
                  +--------------+--------------+
                                 |
                                 v
                    +--------------------------+
                    | Nmap Service Detection   |
                    +------------+-------------+
                                 |
                                 v
                    +--------------------------+
                    | CVE Vulnerability        |
                    | Correlation               |
                    +------------+-------------+
                                 |
                  +--------------+--------------+
                  |                             |
                  v                             v
            IP Reputation                Domain Reputation
                                           (Domain Input Only)
                  |                             |
                  +--------------+--------------+
                                 |
                                 v
                    +--------------------------+
                    |    Report Generation     |
                    +------------+-------------+
                                 |
                                 v
                    +--------------------------+
                    |      Scan Summary        |
                    +--------------------------+
```

---

## IP and Domain Handling

ReconX handles IP and domain inputs differently to maintain accurate target identification.

### Domain Input

Example:

```text
scanme.nmap.org
```

ReconX:

1. Validates the domain
2. Resolves the domain to an IP address
3. Performs DNS enumeration
4. Performs WHOIS lookup
5. Performs Nmap scanning
6. Correlates detected services with CVEs
7. Checks IP reputation
8. Checks domain reputation
9. Generates the report

### IP Input

Example:

```text
162.241.216.11
```

ReconX:

1. Validates the IP address
2. Performs reverse DNS / PTR lookup when available
3. Performs Nmap scanning
4. Correlates detected services with CVEs
5. Checks IP reputation
6. Does not automatically perform domain reputation using the reverse-DNS hostname
7. Generates the report

This prevents a hosting provider's PTR hostname or another reverse-DNS record from being incorrectly treated as the domain being assessed.

---

## Tech Stack

- **Python 3**
- **Nmap**
- **Rich**
- **dnspython**
- **python-whois**
- **Requests**
- **NVD API**
- **IP Reputation API**
- **Domain Reputation API**
- **Git / GitHub**

---

## Project Structure

```text
ReconX/
│
├── core/
│   ├── banner.py
│   ├── validator.py
│   ├── target.py
│   └── report.py
│
├── modules/
│   ├── dns_lookup.py
│   ├── whois_lookup.py
│   ├── nmap_scan.py
│   ├── vulnerability_lookup.py
│   └── reputation_lookup.py
│
├── reports/
│   └── .gitkeep
│
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/jnc1118/ReconX.git
```

### 2. Move into the project directory

```bash
cd ReconX
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Linux / Kali Linux

```bash
source venv/bin/activate
```

#### Windows

```powershell
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Ensure Nmap is installed

On Kali Linux:

```bash
sudo apt install nmap
```

Verify the installation:

```bash
nmap --version
```

---

## Usage

Run the application:

```bash
python main.py
```

Enter an authorized domain or IP address when prompted.

### Domain Example

```text
Enter target: scanme.nmap.org
```

### IP Example

```text
Enter target: 162.241.216.11
```

ReconX will automatically:

- Validate the target
- Resolve domain-to-IP when applicable
- Perform DNS or reverse DNS lookup
- Retrieve WHOIS information
- Execute an Nmap service and version scan
- Correlate detected services with CVEs
- Check IP reputation
- Check domain reputation for domain targets
- Generate a structured report
- Display the scan summary

> **Use ReconX only against systems and networks for which you have permission to perform security testing.**

---

## Sample Workflow

```text
Enter target: scanme.nmap.org

        Target Information

Original Input : scanme.nmap.org
Hostname       : scanme.nmap.org
IP Address     : <resolved IP>
Scheme         : https

        DNS Records

A       <IP>
AAAA    ...
MX      ...
NS      ...
TXT     ...

        WHOIS Information

Registrar       ...
Organization    ...
Country         ...

        Nmap Scan Results

22/tcp   open    ssh     OpenSSH ...
80/tcp   open    http    Apache ...

        Vulnerability Results

22/tcp   ssh     CVE-...    MEDIUM    ...
80/tcp   http    CVE-...    HIGH      ...

        IP Reputation

Blacklisted       ...
Malicious         ...
Confidence Score  ...

        Domain Reputation

Reputation          Clean
Malicious Engines   0
Suspicious Engines  0

        ReconX Scan Summary

✓ Target Validation
✓ DNS Lookup
✓ WHOIS Lookup
✓ Nmap Scan
✓ CVE Correlation
✓ IP Reputation
✓ Domain Reputation
✓ Report Generation

Total Scan Time : XX.XX seconds
```

---

## Reports

ReconX automatically stores generated scan reports in:

```text
reports/
```

Each report contains:

```text
Target Information
DNS / PTR Records
WHOIS Information
Nmap Results
CVE Vulnerability Results
IP Reputation
Domain Reputation
Scan Time
```

Domain reputation is omitted from the active scan when the original target is an IP address.

---

## Current Scope

The current IIIT Kottayam implementation focuses on:

- Target validation
- DNS and reverse DNS lookup
- WHOIS information gathering
- Nmap service and version detection
- CVE correlation
- IP reputation analysis
- Domain reputation analysis
- Automated report generation

The framework uses a modular architecture so that additional reconnaissance and security assessment capabilities can be integrated in future versions.

---

## Future Enhancements

- GeoIP Lookup
- SSL/TLS Analysis
- HTTP Security Header Analysis
- Technology Detection
- Website Screenshot Capture
- HTML/PDF Report Generation
- Shodan Integration
- Multi-threaded Scanning
- Web Dashboard
- Advanced vulnerability correlation
- Additional reputation and threat-intelligence sources

---

## Author

**John Paul**

B.Tech Computer Science and Engineering

Mar Athanasius College of Engineering

Cyber Security Intern – IIIT Kottayam