import subprocess
import re


def run_nmap_scan(target):
    """
    Run an Nmap service version scan and return structured results.
    """

    try:
        result = subprocess.run(
            ["nmap", "-T4", "-F","--max-retries", "3", "-sV", target],
            capture_output=True,
            text=True,
            check=True
        )

        scan_results = {}

        lines = result.stdout.splitlines()

        parsing = False

        for line in lines:

            # Start parsing after the PORT header
            if line.startswith("PORT"):
                parsing = True
                continue

            if not parsing:
                continue

            # Stop parsing when Service Info or Nmap done appears
            if line.startswith("Service Info") or line.startswith("Nmap done"):
                break

            if not line.strip():
                continue

            parts = line.split()

            # Skip lines that are not actual port entries
            if len(parts) < 3:
                continue

            if not re.match(r"^\d+/(tcp|udp)$", parts[0]):
                continue

            port = parts[0]
            state = parts[1]
            service = parts[2]
            version = " ".join(parts[3:]) if len(parts) > 3 else ""

            scan_results[port] = {
                "state": state,
                "service": service,
                "version": version
            }

        return scan_results

    except subprocess.CalledProcessError as e:
        return {}