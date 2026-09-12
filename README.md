# eth-key-check

Safe Ethereum key/address verification and cross-language cryptocurrency research utilities for Chimera II research.

## Cross-language solution

The repository now has four aligned implementation tracks:

| Track | Location | Role |
|---|---|---|
| Python | `python/chimera_crypto/` | Reference research package and compatibility layer |
| Node.js | `node/` | ESM CLI/integration implementation |
| Java | `java/` | JavaFX desktop implementation |
| C++ | `cpp/` | C++20/Qt 6 native implementation |
| Apple | `apple/` | SwiftUI/Xcode iOS/iPadOS and macOS application boundary |

The implementations share the `chimera.crypto.interop` envelope and deterministic public/synthetic conformance data. Existing Python scripts remain available for compatibility.

## Apple build

`apple/project.yml` is an XcodeGen specification. On macOS install Xcode/XcodeGen, run `xcodegen generate --spec apple/project.yml`, then build/archive/export through Xcode. The Apple shell preserves the same safe owner-authorized verification boundary; it does not perform private-key cracking, seed guessing or unauthorized credential recovery.

## Scope

This project verifies cryptographic material already possessed by the operator, derives public addresses, scans public blockchain state, and supports owner-authorized wallet operations through configured wallet software or already-signed transactions.

It provides a public cryptocurrency metadata catalog, SQLite research database, blockchain scanners, owner-authorized wallet transaction helpers, desktop GUIs, optional CNN/RNN models, and offline PPO reinforcement-learning research.

### Owner-authorized recovery

The supported recovery model is **restore-and-verify**, not cracking. If the operator already has legitimate wallet recovery material or a wallet backup, the software may validate it locally, derive deterministic public addresses, compare those addresses with an owner-supplied address inventory, and hand subsequent signing to a secure wallet or external signer.

The project does **not** search for, guess, infer, enumerate, or brute-force private keys or seed phrases from public addresses, balances, or transaction history.

## Node.js

```bash
cd node
npm test
npm run verify -- 0x0000000000000000000000000000000000000000
```

Node uses ECMAScript modules and an explicit package export surface. The Node layer is intentionally aligned with the Python/Java/C++ validation and audit contracts.

## Python

```bash
python -m pip install -r requirements.txt
python -m pip install -r requirements-ml.txt
pytest -q
```

The canonical package facade is `python/chimera_crypto/`; legacy entry points remain supported.

## Java

Requirements: JDK 21 and Maven.

```bash
cd java
mvn test
mvn javafx:run
```

The JavaFX application provides Dashboard, Verification, Blockchain, AI/RL, C8192/R8192 and Audit views.

## C++ / Qt

Requirements: C++20, CMake 3.21+ and Qt 6.

```bash
cd cpp
cmake -S . -B build
cmake --build build
ctest --test-dir build --output-on-failure
```

The Qt application and `chimera_crypto_core` library share the same deterministic validation contract.

## Wallet operations

- Receive BTC through an authenticated Bitcoin Core wallet.
- Send BTC through an operator-controlled Bitcoin Core wallet.
- Broadcast an already-signed Ethereum transaction.
- Monitor/classify burn or provably unspendable addresses without attempting to move their funds.

Never place real wallet secrets in source control, issue reports, CI logs, command histories, or test fixtures.

## Security boundary

Private-key cracking, seed guessing, address-targeted brute force, credential harvesting and unauthorized wallet access are deliberately excluded. Public balances and transactions are observational research data. Spending operations require a wallet or externally signed transaction that the operator controls.

## Chimera II

This repository supplies deterministic crypto/AI workloads to Chimera II OS C8192/R8192 ISA and emulator research. Cross-language interoperability is documented in `docs/CRYPTO_INTEROPERABILITY.md` and the consolidation plan in `docs/superpowers/plans/2026-09-10-cross-language-consolidation.md`.
