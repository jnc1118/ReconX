import whois
import io
import contextlib

def get_whois_info(domain):
    """
    Retrieve WHOIS information for a domain.

    Returns:
        dict
    """

    try:
        with contextlib.redirect_stderr(io.StringIO()):
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