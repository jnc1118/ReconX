import whois


def get_whois_info(domain):
    """
    Retrieve WHOIS information for a domain.

    Returns:
        dict
    """

    try:
        w = whois.whois(domain)

        return {
            "Registrar": w.registrar,
            "Organization": w.org,
            "Creation Date": w.creation_date,
            "Expiration Date": w.expiration_date,
            "Updated Date": w.updated_date,
            "Country": w.country,
            "Name Servers": w.name_servers,
        }

    except Exception as e:
        return {
            "Error": str(e)
        }