# eth-key-check

Safe Ethereum key/address verification and Python cryptocurrency research utilities for Chimera II research.

## Scope

This project derives an Ethereum address from a private key already possessed by the operator and verifies a supplied address. It validates Ethereum address syntax and emits EIP-55 checksums.

It also provides a public cryptocurrency metadata catalog and a professional Tkinter/ttk research GUI in `crypto_catalog.py` and `crypto_gui.py`.

It does **not** search for, guess, infer, recover, or brute-force a private key from a public address.

## Install

```bash
python -m pip install -r requirements.txt
```

## Usage

```bash
python project.py <existing-private-key> <ethereum-address>
python project.py <existing-private-key> <ethereum-address> --checksum
python crypto_gui.py
```

Never place real wallet secrets in source control, issue reports, CI logs, command histories, or test fixtures.

## Tests

```bash
pytest -q
```

## Crypto catalog

The SQLite catalog currently indexes BTC, ETH, LTC, DOGE, XMR and SOL with their network, address, signature and hash families. It is a technical reference and not a price feed or investment recommendation.

## Standards and provenance

- ERC-55 / EIP-55 — Ethereum mixed-case checksum addresses.
- ERC-1191 — chain-ID-aware checksum extension.
- BIP-32 — hierarchical deterministic key derivation reference.
- bitcoin-core/secp256k1 — secp256k1 reference implementation.
- bitcoinjs/bip32 — BIP-32 implementation.
- scure-bip32 — BIP-32 implementation.

See `docs/CRYPTO_INTEROPERABILITY.md` and `CRYPTO_RESEARCH.md` for the provenance and interoperability catalogue.

## Chimera II

This repository is one component of the Chimera II OS research ecosystem and can supply deterministic crypto test workloads to its C8192/R8192 ISA and emulator research.
