import dns.resolver
import dns.reversename
import ipaddress


def get_dns_records(hostname: str):
    """
    Retrieves DNS records for a domain or reverse DNS information for an IP.

    Parameters:
        hostname (str): Domain name or IP address.

    Returns:
        dict: Dictionary containing DNS records.
    """

    records = {}

    # Check whether the input is an IP address
    try:
        ipaddress.ip_address(hostname)
        is_ip = True
    except ValueError:
        is_ip = False

    # Reverse DNS lookup for IP targets
    if is_ip:

        records["PTR"] = []

        try:
            reverse_name = dns.reversename.from_address(hostname)
            answers = dns.resolver.resolve(reverse_name, "PTR")

            records["PTR"] = [str(answer).rstrip(".") for answer in answers]

        except Exception:
            records["PTR"] = []

        return records

    # Normal DNS lookup for domain targets
    record_types = ["A", "AAAA", "MX", "NS", "TXT", "CNAME"]

    for record_type in record_types:

        try:
            answers = dns.resolver.resolve(hostname, record_type)

            records[record_type] = [str(answer) for answer in answers]

        except Exception:
            records[record_type] = []

    return records