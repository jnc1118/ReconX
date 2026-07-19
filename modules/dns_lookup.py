import dns.resolver


def get_dns_records(hostname: str):
    """
    Retrieves DNS records for a given hostname.

    Parameters:
        hostname (str): Domain name (e.g., google.com)

    Returns:
        dict: Dictionary containing different DNS records.
    """

    records = {}

    record_types = ["A", "AAAA", "MX", "NS", "TXT", "CNAME"]

    for record_type in record_types:

        try:
            answers = dns.resolver.resolve(hostname, record_type)

            records[record_type] = [str(answer) for answer in answers]

        except Exception:
            records[record_type] = []

    return records