from core.banner import show_banner
from core.validator import validate_target
from modules.dns_lookup import get_dns_records
from modules.whois_lookup import get_whois_info
from core.report import (show_target_info, show_dns_records, show_whois_info)


def main():
    show_banner()

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

        dns_records = get_dns_records(target.hostname)

        show_dns_records(dns_records)

        whois_info = get_whois_info(target.hostname)

        show_whois_info(whois_info)

    except ValueError as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()