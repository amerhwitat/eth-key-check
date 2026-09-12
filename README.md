# eth-key-check

Safe Ethereum key/address verification and cross-language cryptocurrency research utilities for Chimera II research.

## Complete source-code citation index

| Area | Source |
|---|---|
| Python implementation | [python/](python/) |
| Node.js implementation | [node/](node/) |
| Java implementation | [java/](java/) |
| C++ implementation | [cpp/](cpp/) |
| Apple implementation | [apple/](apple/) |
| Documentation/contracts | [docs/](docs/) |
| Complete tracked repository | [source tree](.) |

These links are the README-level citations for all maintained implementation areas; component directories remain the detailed source record.

## Centralized Apple Objective-C + Flutter

The Apple companion is maintained in [`general/Apple-Implementations/eth-key-check`](https://github.com/amerhwitat/general/tree/master/Apple-Implementations/eth-key-check). It combines an Objective-C/Xcode native boundary with Flutter iOS/macOS UI while preserving the repository's owner-authorized crypto security model.

## Cross-language solution

The repository has aligned Python, Node.js, Java, C++ and Apple implementation tracks sharing deterministic public/synthetic conformance data.

## Apple build

On macOS install Xcode and XcodeGen, generate the native project, then build/archive/export through Xcode. IPA signing is external and operator-controlled. The Apple application does not perform private-key cracking, seed guessing or unauthorized credential recovery.

## Scope

This project verifies cryptographic material already possessed by the operator, derives public addresses, scans public blockchain state, and supports owner-authorized wallet operations through configured wallet software or already-signed transactions.

## Security boundary

Private-key cracking, seed guessing, address-targeted brute force, credential harvesting and unauthorized wallet access are deliberately excluded. Public balances and transactions are observational research data.

## Chimera II

This repository supplies deterministic crypto/AI workloads to Chimera II OS C8192/R8192 ISA and emulator research.
