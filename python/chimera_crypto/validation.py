import re

_HEX40 = re.compile(r"^[0-9a-fA-F]{40}$")

def normalize_eth_address(value: str) -> str:
    if not isinstance(value, str):
        raise TypeError("address must be a string")
    value = value.strip()
    if value.startswith("0x"):
        value = value[2:]
    if not _HEX40.fullmatch(value):
        raise ValueError("invalid Ethereum address")
    return "0x" + value.lower()

def validate_eth_address(value: str) -> bool:
    try:
        normalize_eth_address(value)
        return True
    except (TypeError, ValueError):
        return False
