import socket
import ipaddress
from urllib.parse import urlparse

from core.target import Target


def validate_target(user_input: str):

    user_input = user_input.strip()

    if not user_input:
        raise ValueError("Target cannot be empty.")
    
    parsed = urlparse(user_input)

    if parsed.scheme:
        hostname = parsed.hostname
        scheme = parsed.scheme
    
    else:
        hostname = user_input
        scheme = "https"

    try:
        ipaddress.ip_address(hostname)
        ip = hostname
    
    except ValueError:
        try:
            ip = socket.gethostbyname(hostname)
        except socket.gaierror:
            raise ValueError(f"Unable to resolve '{hostname}'.")
        
    return Target(
        original_input=user_input,
        hostname=hostname,
        ip=ip,
        scheme=scheme
    )