import os
import requests
from dotenv import load_dotenv

load_dotenv()

ABUSEIPDB_API_URL = "https://api.abuseipdb.com/api/v2/check"
VIRUSTOTAL_API_URL = "https://www.virustotal.com/api/v3/domains"

def check_ip_reputation(ip):
    """
    Check the reputation of an IP address using AbuseIPDB.

    Returns structured reputation information.
    """

    api_key = os.getenv("ABUSEIPDB_API_KEY")

    if not api_key:
        return {
            "status": "unavailable",
            "message": "AbuseIPDB API key not configured."
        }

    headers = {
        "Accept": "application/json",
        "Key": api_key
    }

    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90
    }

    try:
        response = requests.get(
            ABUSEIPDB_API_URL,
            headers=headers,
            params=params,
            timeout=15
        )

        response.raise_for_status()

        data = response.json().get("data", {})

        abuse_score = data.get("abuseConfidenceScore", 0)

        return {
            "status": "success",
            "ip": ip,
            "blacklisted": abuse_score > 0,
            "malicious": abuse_score >= 50,
            "confidence_score": abuse_score,
            "total_reports": data.get("totalReports", 0),
            "country": data.get("countryCode"),
            "isp": data.get("isp"),
            "domain": data.get("domain"),
            "last_reported": data.get("lastReportedAt")
        }

    except requests.RequestException as e:
        return {
            "status": "error",
            "ip": ip,
            "blacklisted": False,
            "malicious": False,
            "confidence_score": 0,
            "message": str(e)
        }

def check_domain_reputation(domain):
    """
    Check the reputation of a domain using VirusTotal.

    Returns structured reputation information.
    """

    api_key = os.getenv("VIRUSTOTAL_API_KEY")

    if not api_key:
        return {
            "status": "unavailable",
            "domain": domain,
            "message": "VirusTotal API key not configured."
        }

    headers = {
        "x-apikey": api_key,
        "Accept": "application/json"
    }

    url = f"{VIRUSTOTAL_API_URL}/{domain}"

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=15
        )

        response.raise_for_status()

        data = response.json().get("data", {})
        attributes = data.get("attributes", {})

        last_analysis = attributes.get("last_analysis_stats", {})

        malicious = last_analysis.get("malicious", 0)
        suspicious = last_analysis.get("suspicious", 0)
        harmless = last_analysis.get("harmless", 0)
        undetected = last_analysis.get("undetected", 0)

        total_engines = (
            malicious +
            suspicious +
            harmless +
            undetected
        )

        if malicious > 0:
            reputation = "Malicious"
        elif suspicious > 0:
            reputation = "Suspicious"
        else:
            reputation = "Clean"

        return {
            "status": "success",
            "domain": domain,
            "blacklisted": malicious > 0,
            "malicious": malicious > 0,
            "reputation": reputation,
            "malicious_engines": malicious,
            "suspicious_engines": suspicious,
            "total_engines": total_engines
        }

    except requests.RequestException as e:
        return {
            "status": "error",
            "domain": domain,
            "blacklisted": False,
            "malicious": False,
            "reputation": "Unknown",
            "message": str(e)
        }