# eth-key-check

Safe Ethereum key/address verification and Python cryptocurrency research utilities for Chimera II research.

## Scope

This project derives an Ethereum address from a private key already possessed by the operator and verifies a supplied address. It validates Ethereum address syntax and emits EIP-55 checksums.

It also provides a public cryptocurrency metadata catalog, SQLite research database, blockchain scanners, owner-authorized wallet transaction helpers, a Tkinter/ttk GUI, optional CNN/RNN models and an offline PPO reinforcement-learning environment.

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

For Ethereum public balance scanning and signed-transaction broadcast, set `CHIMERA_ETH_RPC_URL` to an Ethereum JSON-RPC endpoint. Ethereum sending uses `eth_sendRawTransaction`; signing is intentionally external. Bitcoin Core credentials use `CHIMERA_BTC_RPC_USER` and `CHIMERA_BTC_RPC_PASSWORD`.

Never place real wallet secrets in source control, issue reports, CI logs, command histories, or test fixtures.

## Wallet operations

- **Receive BTC:** `BitcoinCoreRPC.getnewaddress()` requests a fresh address from an authenticated Bitcoin Core wallet.
- **Send BTC:** `BitcoinCoreRPC.send_to_address()` delegates signing and authorization to the configured Bitcoin Core wallet.
- **Send ETH:** `EthereumRPC.send_raw_transaction()` broadcasts an already-signed transaction; private keys never enter this library.
- **Burn addresses:** the scanner may classify and monitor known/provably unspendable addresses, but it never attempts to recover or move funds from them.

Transaction submission should be paired with explicit user confirmation, fee/nonce validation, chain/network checks, and post-broadcast receipt monitoring.

## Components

- `crypto_catalog.py` — public coin/protocol metadata.
- `crypto_database.py` — SQLite addresses, balances, transactions and safe key fingerprints.
- `balance_scanner.py` — Ethereum and Bitcoin Core observation plus owner-authorized transaction/receiving RPC helpers.
- `crypto_ml.py` — optional PyTorch CNN and GRU/RNN models.
- `crypto_rl.py` — offline Gymnasium + Stable-Baselines3 PPO environment.
- `crypto_ai_gui.py` — unified research GUI.

## Tests

```bash
pytest -q
```

## Security boundary

Private-key recovery, seed guessing, address-targeted brute force, credential harvesting and unauthorized wallet access are deliberately excluded. Public balances and transactions are observational research data. Spending operations require a wallet or externally signed transaction that the operator controls.

Burned or provably unspendable funds are reported as `BURN`/unspendable and are never treated as recoverable wallet funds.

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
