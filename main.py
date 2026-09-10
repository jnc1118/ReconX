from core import target
from core.banner import show_banner
from core.validator import validate_target
from modules.dns_lookup import get_dns_records
from modules.whois_lookup import get_whois_info
from modules.nmap_scan import run_nmap_scan
from modules.vulnerability_lookup import correlate_vulnerabilities
from modules.reputation_lookup import check_ip_reputation, check_domain_reputation
from rich.console import Console
from core.report import (show_target_info, show_dns_records, show_whois_info, show_nmap_results, show_vulnerability_results, show_reputation_results, show_domain_reputation_results, save_report, show_scan_summary)
import time


def main():
    show_banner()
    start_time = time.time()
    target_input = input("\nEnter target: ")

    try:
        target = validate_target(target_input)

        target_info = {
            "original": target.original_input,
            "hostname": target.hostname,
            "ip": target.ip,
            "scheme": target.scheme
        }

        show_target_info(target_info)

        if target.hostname:
            dns_records = get_dns_records(target.hostname)
            show_dns_records(dns_records)

            whois_info = get_whois_info(target.hostname)
            show_whois_info(whois_info)

        else:
            dns_records = {}
            whois_info = {}
            print("\nNo domain name found through reverse DNS.")

        console = Console()
        with console.status(
            "[bold green]Running Nmap Service Detection..."
        ):
            scan_results = run_nmap_scan(target.ip)
        console.print("\n[green]✓ Nmap scan completed![/green]")
        show_nmap_results(scan_results)

        vulnerabilities = correlate_vulnerabilities(scan_results, 3)
        show_vulnerability_results(vulnerabilities)
    
        ip_reputation = check_ip_reputation(target.ip)
        domain_reputation = check_domain_reputation(target.hostname)

        show_reputation_results(ip_reputation)
        show_domain_reputation_results(domain_reputation)

        report_path = save_report(target,dns_records,whois_info,scan_results,vulnerabilities,ip_reputation,domain_reputation)
        end_time = time.time()
        elapsed_time = end_time - start_time
        show_scan_summary(elapsed_time)
        print(f"\nReport saved successfully!")
        print(f"Location: {report_path}")

    except ValueError as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()