# Crypto / Cryptography Research Layer

This repository now includes a Python-first public cryptocurrency and cryptography research layer.

## Covered public concepts

- Bitcoin (BTC): UTXO model, SHA-256 proof-of-work, secp256k1 signatures, Base58Check/Bech32 address families.
- Ethereum (ETH): account model, Keccak-256, secp256k1 signatures, hexadecimal address representation and EIP-55 checksums.
- Litecoin (LTC): Bitcoin-derived UTXO design and address families.
- Dogecoin (DOGE): proof-of-work UTXO design and Scrypt-derived mining family.
- Monero (XMR): privacy-oriented protocol with distinct address and signature constructions.
- Solana (SOL): account/program architecture and Ed25519 signatures.

The catalog is a research index, not a market-price feed or investment recommendation.

## Python implementation

`crypto_catalog.py` provides a small SQLite catalog for public metadata and safe local hash experiments. `crypto_gui.py` provides a Tkinter/ttk interface.

The existing `project.py` remains deliberately limited to deriving an Ethereum address from a private key already possessed by the operator and validating an expected address. It does not implement address-to-private-key recovery.

## Security boundary

Do not add wallet-key recovery, address-targeted private-key search, credential harvesting, seed-phrase guessing, or unauthorized wallet access. Cryptographic experiments should use synthetic or published test vectors.

Bitcoin's public-key model and blockchain structure are documented in the Bitcoin developer reference material; Bitcoin uses elliptic-curve operations for signatures and SHA-256 in its block-header hashing. See the project's upstream references before adapting external code.

## Run

```bash
python crypto_gui.py
```

Tests:

```bash
python -m pytest -q
```
