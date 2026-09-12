# eth-key-check

Safe Ethereum key/address verification and cross-language cryptocurrency research utilities for Chimera II research.

## Start / build all

Use the repository-wide automation:

```bat
build-tools\build.bat
```

or:

```powershell
.\build-tools\build.ps1
```

The orchestrator detects and builds Python, Node.js, Java and C++/Qt targets, reporting dependencies, compilation, linking, tests and artifacts.

## Cross-language solution

| Track | Location | Role |
|---|---|---|
| Python | `python/chimera_crypto/` | Reference research package and compatibility layer |
| Node.js | `node/` | ESM CLI/integration implementation |
| Java | `java/` | JavaFX desktop implementation |
| C++ | `cpp/` | C++20/Qt 6 native implementation |

## Scope

This project verifies cryptographic material already possessed by the operator and derives public addresses. The supported recovery model is **restore-and-verify**, not cracking. The project does not search for, guess, infer, enumerate, or brute-force private keys or seed phrases from public addresses, balances, or transaction history.

## Node.js

```bash
cd node && npm test && npm run verify -- 0x0000000000000000000000000000000000000000
```

## Python

```bash
python -m pip install -r requirements.txt
pytest -q
```

## Java

```bash
cd java && mvn test
```

## C++ / Qt

```bash
cd cpp
cmake -S . -B build
cmake --build build --parallel
ctest --test-dir build --output-on-failure
```

## Wallet operations

Spending remains operator-controlled through configured wallets or already-signed transactions. Never place real wallet secrets in source control, issue reports, CI logs, command histories, or test fixtures.

## Chimera II

This repository supplies deterministic crypto/AI workloads to Chimera II OS C8192/R8192 ISA and emulator research. Cross-language interoperability is documented in `docs/CRYPTO_INTEROPERABILITY.md`.
