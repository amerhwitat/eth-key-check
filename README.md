# eth-key-check

Safe Ethereum key/address verification and Python cryptocurrency research utilities for Chimera II research.

## Scope

This project derives an Ethereum address from a private key already possessed by the operator and verifies a supplied address. It validates Ethereum address syntax and emits EIP-55 checksums.

It also provides a public cryptocurrency metadata catalog, SQLite research database, read-only blockchain balance scanners, a Tkinter/ttk GUI, optional CNN/RNN models and an offline PPO reinforcement-learning environment.

It does **not** search for, guess, infer, recover, or brute-force a private key from a public address. The database stores only non-secret key fingerprints and optional external-vault references.

## Install

```bash
python -m pip install -r requirements.txt
# Optional ML/RL stack:
python -m pip install -r requirements-ml.txt
```

## Usage

```bash
python project.py <existing-private-key> <ethereum-address>
python project.py <existing-private-key> <ethereum-address> --checksum
python crypto_gui.py
python crypto_ai_gui.py
```

For Ethereum public balance scanning, set `CHIMERA_ETH_RPC_URL` to a read-only JSON-RPC endpoint. Bitcoin Core RPC credentials use `CHIMERA_BTC_RPC_USER` and `CHIMERA_BTC_RPC_PASSWORD`.

Never place real wallet secrets in source control, issue reports, CI logs, command histories, or test fixtures.

## Components

- `crypto_catalog.py` — public coin/protocol metadata.
- `crypto_database.py` — SQLite addresses, balances, transactions and safe key fingerprints.
- `balance_scanner.py` — read-only Ethereum and Bitcoin Core adapters.
- `crypto_ml.py` — optional PyTorch CNN and GRU/RNN models.
- `crypto_rl.py` — offline Gymnasium + Stable-Baselines3 PPO environment.
- `crypto_ai_gui.py` — unified research GUI.

## Tests

```bash
pytest -q
```

## Security boundary

Private-key recovery, seed guessing, address-targeted brute force, credential harvesting and unauthorized wallet access are deliberately excluded. Public balances and transactions are observational research data.

## Standards and provenance

- ERC-55 / EIP-55 — Ethereum mixed-case checksum addresses.
- ERC-1191 — chain-ID-aware checksum extension.
- BIP-32 — hierarchical deterministic key derivation reference.
- bitcoin-core/secp256k1 — secp256k1 reference implementation.
- bitcoinjs/bip32 — BIP-32 implementation.
- scure-bip32 — BIP-32 implementation.

See `docs/CRYPTO_INTEROPERABILITY.md`, `CRYPTO_RESEARCH.md` and `docs/CRYPTO_AI_ARCHITECTURE.md`.

## Chimera II

This repository is one component of the Chimera II OS research ecosystem and can supply deterministic crypto/AI test workloads to its C8192/R8192 ISA and emulator research.
