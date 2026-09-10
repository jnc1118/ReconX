from dataclasses import dataclass


@dataclass
class Target:
    original_input: str
    hostname: str
    ip: str
    scheme: str
    is_ip: bool