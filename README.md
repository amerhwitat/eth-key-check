# eth-key-check

Safe Ethereum key/address verification utilities for Chimera II research.

## Scope

This project derives an Ethereum address from a private key already possessed by the operator and verifies a supplied address. It also validates Ethereum address syntax and emits EIP-55 checksums.

It does **not** search for, guess, infer, recover, or brute-force a private key from a public address.

## Install

```bash
python -m pip install -r requirements.txt
```

## Usage

```bash
python project.py <existing-private-key> <ethereum-address>
python project.py <existing-private-key> <ethereum-address> --checksum
```

Never place real wallet secrets in source control, issue reports, CI logs, command histories, or test fixtures.

## Tests

```bash
pytest -q
```

## Standards and provenance

- [ERC-55 / EIP-55](https://eips.ethereum.org/EIPS/eip-55) — Ethereum mixed-case checksum addresses.
- [ERC-1191](https://eips.ethereum.org/EIPS/eip-1191) — chain-ID-aware checksum extension.
- [BIP-32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki) — HD key derivation reference.
- [bitcoin-core/secp256k1](https://github.com/bitcoin-core/secp256k1) — MIT-licensed secp256k1 reference implementation.
- [bitcoinjs/bip32](https://github.com/bitcoinjs/bip32) — MIT-licensed BIP-32 reference implementation.
- [paulmillr/scure-bip32](https://github.com/paulmillr/scure-bip32) — MIT-licensed audited BIP-32 implementation.

See [`docs/CRYPTO_INTEROPERABILITY.md`](docs/CRYPTO_INTEROPERABILITY.md) for the provenance and interoperability catalogue.

## Chimera II

This repository is one component of the [Chimera II OS](https://github.com/amerhwitat/ChimeraIIOS) research ecosystem and can supply deterministic crypto test workloads to its C8192/R8192 ISA and emulator research.
