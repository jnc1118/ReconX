from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from datetime import datetime
import os

console = Console()


def show_target_info(target_info):

    table = Table(title="\nTarget Information")

    table.add_column("Field", style="cyan", no_wrap=True)
    table.add_column("Value", style="green")

    table.add_row("Original Input", target_info["original"])
    table.add_row("Hostname", target_info["hostname"])
    table.add_row("IP Address", target_info["ip"])
    table.add_row("Scheme", target_info["scheme"])

    console.print(table)


def show_dns_records(dns_records):

    table = Table(title="\nDNS Records")

    table.add_column("Record Type", style="cyan", no_wrap=True)
    table.add_column("Value", style="green")

    for record_type, values in dns_records.items():

        if values:
            for value in values:
                table.add_row(record_type, value)
        else:
            table.add_row(record_type, "[red]No records found[/red]")

    console.print(table)

def show_whois_info(whois_info):

    table = Table(title="\nWHOIS Information")

    table.add_column("Field", style="cyan", no_wrap=True)
    table.add_column("Value", style="green")

    for key, value in whois_info.items():

        if isinstance(value, list):
            value = "\n".join(str(v) for v in value)

        table.add_row(str(key), str(value))

    console.print(table)

def show_nmap_results(scan_results):

    table = Table(title="\nNmap Scan Results")

    table.add_column("Port", style="cyan", no_wrap=True)
    table.add_column("State", style="green")
    table.add_column("Service", style="yellow")
    table.add_column("Version", style="magenta")

    if not scan_results:
        console.print("[red]No scan results available.[/red]")
        return

    for port, info in scan_results.items():

        table.add_row(
            port,
            info["state"],
            info["service"],
            info["version"]
        )

    console.print(table)

def show_vulnerability_results(vulnerabilities):

    table = Table(title="\nVulnerability Results")

    table.add_column("Port", style="cyan", no_wrap=True)
    table.add_column("Service", style="yellow")
    table.add_column("CVE", style="red")
    table.add_column("Severity", style="magenta")
    table.add_column("CVSS", style="green")
    table.add_column("Applicability", style="blue")

    if not vulnerabilities:
        console.print("[green]No potential vulnerabilities found.[/green]")
        return

    for vuln in vulnerabilities:

        table.add_row(
            vuln["port"],
            vuln["service"],
            vuln["cve"],
            vuln["severity"],
            str(vuln["cvss_score"]),
            vuln["applicability"]
        )

    console.print(table)

def save_report(target, dns_records, whois_info, nmap_results, vulnerabilities,ip_reputation, domain_reputation):

    os.makedirs("reports", exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    filename = f"reports/{target.hostname}_{timestamp}.txt"

    with open(filename, "w") as report:

        report.write("=" * 60 + "\n")
        report.write("ReconX Scan Report\n")
        report.write("=" * 60 + "\n\n")

        report.write(f"Scan Time : {datetime.now()}\n")
        report.write(f"Target    : {target.original_input}\n")
        report.write(f"Hostname  : {target.hostname}\n")
        report.write(f"IP        : {target.ip}\n")
        report.write(f"Scheme    : {target.scheme}\n\n")

        report.write("=" * 60 + "\n")
        report.write("DNS RECORDS\n")
        report.write("=" * 60 + "\n")

        for record_type, values in dns_records.items():

            report.write(f"\n{record_type}:\n")

            if values:
                for value in values:
                    report.write(f"  - {value}\n")
            else:
                report.write("  No records found\n")

        report.write("\n")
        report.write("=" * 60 + "\n")
        report.write("WHOIS INFORMATION\n")
        report.write("=" * 60 + "\n")

        for key, value in whois_info.items():

            if isinstance(value, list):
                value = ", ".join(str(v) for v in value)

            report.write(f"{key}: {value}\n")

        report.write("\n")
        report.write("=" * 60 + "\n")
        report.write("NMAP RESULTS\n")
        report.write("=" * 60 + "\n")

        for port, info in nmap_results.items():

            report.write(
                f"{port} | "
                f"{info['state']} | "
                f"{info['service']} | "
                f"{info['version']}\n"
            )

        report.write("\n")
        report.write("=" * 60 + "\n")
        report.write("VULNERABILITY RESULTS\n")
        report.write("=" * 60 + "\n")

        if vulnerabilities:

            for vuln in vulnerabilities:

                report.write(f"\nPort          : {vuln['port']}\n")
                report.write(f"Service       : {vuln['service']}\n")
                report.write(f"Version       : {vuln['version']}\n")
                report.write(f"CVE           : {vuln['cve']}\n")
                report.write(f"Severity      : {vuln['severity']}\n")
                report.write(f"CVSS Score    : {vuln['cvss_score']}\n")
                report.write(f"Applicability : {vuln['applicability']}\n")
                report.write(f"Description   : {vuln['description']}\n")
                report.write("-" * 60 + "\n")

        else:
            report.write("\nNo potential vulnerabilities found.\n")

        report.write("\n")
        report.write("=" * 60 + "\n")
        report.write("IP REPUTATION\n")
        report.write("=" * 60 + "\n")

        for key, value in ip_reputation.items():
            report.write(f"{key}: {value}\n")

        report.write("\n")
        report.write("=" * 60 + "\n")
        report.write("DOMAIN REPUTATION\n")
        report.write("=" * 60 + "\n")

        for key, value in domain_reputation.items():
            report.write(f"{key}: {value}\n")

        report.write("\n")
        report.write("=" * 60 + "\n")
        report.write("Generated by ReconX\n")
        report.write("=" * 60 + "\n")

    return filename

def show_reputation_results(reputation):

    table = Table(title="\nIP Reputation")

    table.add_column("Field", style="cyan", no_wrap=True)
    table.add_column("Value", style="green")

    if reputation.get("status") != "success":
        table.add_row(
            "Status",
            reputation.get("message", "Reputation lookup unavailable.")
        )

        console.print(table)
        return

    table.add_row("IP Address", reputation["ip"])

    blacklisted = (
        "[red]Yes[/red]"
        if reputation["blacklisted"]
        else "[green]No[/green]"
    )

    malicious = (
        "[red]Yes[/red]"
        if reputation["malicious"]
        else "[green]No[/green]"
    )

    table.add_row("Blacklisted", blacklisted)
    table.add_row(
        "Malicious",
        malicious
    )

    table.add_row(
        "Confidence Score",
        f"{reputation['confidence_score']}%"
    )

    table.add_row(
        "Total Reports",
        str(reputation["total_reports"])
    )

    table.add_row(
        "Country",
        str(reputation["country"])
    )

    table.add_row(
        "ISP",
        str(reputation["isp"])
    )

    table.add_row(
        "Domain",
        str(reputation["domain"])
    )

    table.add_row(
        "Last Reported",
        str(reputation["last_reported"])
    )

    console.print(table)

def show_domain_reputation_results(reputation):

    table = Table(title="\nDomain Reputation")

    table.add_column("Field", style="cyan", no_wrap=True)
    table.add_column("Value", style="green")

    if reputation.get("status") != "success":
        table.add_row(
            "Status",
            reputation.get("message", "Domain reputation unavailable.")
        )
        console.print(table)
        return

    table.add_row("Domain", reputation["domain"])

    blacklisted = (
        "[red]Yes[/red]"
        if reputation["blacklisted"]
        else "[green]No[/green]"
    )

    malicious = (
        "[red]Yes[/red]"
        if reputation["malicious"]
        else "[green]No[/green]"
    )

    table.add_row("Blacklisted", blacklisted)
    table.add_row("Malicious", malicious)
    table.add_row("Reputation", reputation["reputation"])
    table.add_row(
        "Malicious Engines",
        str(reputation["malicious_engines"])
    )
    table.add_row(
        "Suspicious Engines",
        str(reputation["suspicious_engines"])
    )
    table.add_row(
        "Total Engines",
        str(reputation["total_engines"])
    )

    console.print(table)

def show_scan_summary(scan_time):

    summary = (
        "✓ Target Validation\n"
        "✓ DNS Lookup\n"
        "✓ WHOIS Lookup\n"
        "✓ Nmap Scan\n"
        "✓ Report Generation\n\n"
        f"Total Scan Time : {scan_time:.2f} seconds"
    )

    console.print(
        Panel(
            summary,
            title="[bold green]ReconX Scan Summary[/bold green]",
            border_style="green"
        )
    )