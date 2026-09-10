# Chimera Crypto AI Architecture

## Scope

This repository now combines public cryptocurrency research, read-only balance observation, deterministic cryptographic verification, deep-learning experiments and offline reinforcement learning.

## Data layer

`crypto_database.py` provides SQLite storage for public addresses, balance snapshots, transactions and key fingerprints. A key fingerprint is a SHA-256 identifier for a private key already possessed by the operator; the private key itself is not stored by the database.

## Blockchain observation

`balance_scanner.py` provides a read-only Ethereum JSON-RPC adapter and a Bitcoin Core RPC adapter. Ethereum uses `eth_getBalance`; Bitcoin Core exposes wallet balance methods such as `getbalances`. Provider credentials are supplied through environment variables.

## Deep learning

`crypto_ml.py` provides optional PyTorch CNN and GRU/RNN classifiers over numerical research sequences. Models are intended for market, transaction and protocol-feature experiments, not key recovery.

## Reinforcement learning

`crypto_rl.py` provides an offline Gymnasium environment and an optional Stable-Baselines3 PPO trainer. The environment consumes historical features and returns and does not connect to an exchange or submit transactions.

## GUI

`crypto_ai_gui.py` combines the database with public Ethereum balance scanning and displays recorded observations.

## Security boundary

The system deliberately does not implement address-to-private-key recovery, seed-phrase guessing, arbitrary wallet brute force, credential harvesting, or unauthorized wallet access. This is both a security boundary and a reproducibility requirement.

## Reproducibility

ML dependencies are isolated in `requirements-ml.txt`. Keep model datasets, random seeds, provider endpoints and training configurations recorded with each experiment.
