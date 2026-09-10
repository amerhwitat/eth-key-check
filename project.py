"""Safe Ethereum key/address verification utilities.

This module intentionally supports only private-key -> address derivation for
keys already possessed by the operator. It does not search for or recover a
private key from a public address.
"""

import argparse
from hdwallet import HDWallet
from hdwallet.symbols import ETH as SYMBOL


def ethereum_address_from_private_key(private_key: str) -> str:
    """Derive an Ethereum P2PKH-style address from an existing private key."""
    key = private_key.strip().removeprefix("0x")
    if len(key) != 64:
        raise ValueError("Ethereum private keys must contain 64 hexadecimal characters")
    int(key, 16)  # validate hexadecimal input
    wallet = HDWallet(symbol=SYMBOL)
    wallet.from_private_key(private_key=key)
    return wallet.p2pkh_address()


def verify_address(private_key: str, expected_address: str) -> bool:
    """Verify that an existing private key derives the supplied address."""
    derived = ethereum_address_from_private_key(private_key)
    return derived.lower() == expected_address.strip().lower()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verify an Ethereum address against a private key you already own."
    )
    parser.add_argument("private_key", help="Existing private key; do not use a wallet secret you do not own")
    parser.add_argument("address", help="Ethereum address to verify")
    args = parser.parse_args()

    derived = ethereum_address_from_private_key(args.private_key)
    print("Derived address:", derived)
    print("Match:", derived.lower() == args.address.strip().lower())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
