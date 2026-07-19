from core.banner import show_banner
from core.validator import validate_target
from modules.dns_lookup import get_dns_records


def main():
    show_banner()

    target_input = input("\nEnter target: ")

    try:
        target = validate_target(target_input)

        print("\nTarget Information")
        print("-" * 40)
        print(f"Original Input : {target.original_input}")
        print(f"Hostname       : {target.hostname}")
        print(f"IP Address     : {target.ip}")
        print(f"Scheme         : {target.scheme}")

    except ValueError as e:
        print(f"\nError: {e}")

    dns_records = get_dns_records(target.hostname)

    print("\nDNS Records")
    print("-" * 40)

    for record_type, values in dns_records.items():

        print(f"\n{record_type} Records:")

        if values:
            for value in values:
                print(f"  • {value}")
        else:
            print("  No records found.")


if __name__ == "__main__":
    main()