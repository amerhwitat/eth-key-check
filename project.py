"""Safe Ethereum key/address verification utilities.

This module intentionally supports only private-key -> address derivation for
keys already possessed by the operator. It does not search for or recover a
private key from a public address.
"""

import argparse
import re

from eth_utils import is_address, to_checksum_address
from hdwallet import HDWallet
from hdwallet.symbols import ETH as SYMBOL

ADDRESS_RE = re.compile(r"^0x[0-9a-fA-F]{40}$")


def normalize_private_key(private_key: str) -> str:
    """Validate and normalize an existing 32-byte Ethereum private key."""
    key = private_key.strip()
    if key.lower().startswith("0x"):
        key = key[2:]
    if len(key) != 64 or not re.fullmatch(r"[0-9a-fA-F]{64}", key):
        raise ValueError("Ethereum private keys must contain 64 hexadecimal characters")
    if int(key, 16) == 0:
        raise ValueError("Ethereum private key must not be zero")
    return key.lower()


def validate_address(address: str) -> str:
    """Validate basic Ethereum address syntax and return its 0x-prefixed form."""
    candidate = address.strip()
    if not ADDRESS_RE.fullmatch(candidate) or not is_address(candidate):
        raise ValueError("Ethereum address must be 0x followed by 40 hexadecimal characters")
    return candidate


def checksum_address(address: str) -> str:
    """Return the EIP-55 checksummed representation of an Ethereum address."""
    return to_checksum_address(validate_address(address))


def ethereum_address_from_private_key(private_key: str) -> str:
    """Derive an Ethereum address from an existing private key."""
    key = normalize_private_key(private_key)
    wallet = HDWallet(symbol=SYMBOL)
    wallet.from_private_key(private_key=key)
    return checksum_address(wallet.p2pkh_address())


def verify_address(private_key: str, expected_address: str) -> bool:
    """Verify that an existing private key derives the supplied address."""
    expected = checksum_address(expected_address)
    derived = ethereum_address_from_private_key(private_key)
    return derived == expected


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verify an Ethereum address against a private key you already own."
    )
    parser.add_argument(
        "private_key",
        help="Existing private key; do not use a wallet secret you do not own",
    )
    parser.add_argument("address", help="Ethereum address to verify")
    parser.add_argument(
        "--checksum",
        action="store_true",
        help="Print the EIP-55 checksummed form of the supplied address",
    )
    args = parser.parse_args()

    supplied = validate_address(args.address)
    if args.checksum:
        print("Checksummed address:", checksum_address(supplied))

    derived = ethereum_address_from_private_key(args.private_key)
    print("Derived address:", derived)
    print("Match:", derived == checksum_address(supplied))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
