# Ethereum Crypto Interoperability and Upstream References

This project is intentionally limited to verification and derivation using Ethereum key material already possessed by the operator. It does not search for a private key from a public address.

## Standards

- **ERC-55 / EIP-55:** https://eips.ethereum.org/EIPS/eip-55 — mixed-case checksum address encoding using Keccak-256.
- **ERC-1191:** https://eips.ethereum.org/EIPS/eip-1191 — optional chain-ID-aware extension of EIP-55 for selected networks.
- **BIP-32:** https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki — HD derivation reference relevant to compatible wallet/key-management workflows.

## Open-source projects reviewed

- https://github.com/bitcoin-core/secp256k1 — MIT-licensed C secp256k1 implementation; reviewed as a native cryptographic reference.
- https://github.com/paulmillr/scure-bip32 — MIT-licensed, audited BIP-32 implementation; reviewed for API/test/supply-chain practices.
- https://github.com/paulmillr/scure-bip39 — MIT-licensed BIP-39 implementation; reviewed for mnemonic/test practices.
- https://github.com/bitcoinjs/bitcoinjs-lib — MIT-licensed Bitcoin library; reviewed for BIP39/BIP44 ecosystem interoperability.
- https://github.com/bitcoinjs/bip32 — MIT-licensed TypeScript BIP-32 implementation; reviewed for derivation APIs and test patterns.

## Provenance rule

Public availability does not itself grant permission to copy source. Any future adapted third-party source must preserve its copyright/license notices and record the upstream commit/version and modifications. Otherwise, Chimera II implementations should use the public specifications as behavioral references and implement independently.

## Security boundary

Allowed:

- private-key -> public-key -> Ethereum address derivation;
- verification of a supplied address against a supplied key;
- EIP-55 checksum generation/validation;
- deterministic test vectors;
- interoperability tests against independent implementations.

Not implemented:

- public-address -> private-key recovery;
- address-list targeting;
- key guessing/search/brute force;
- wallet-secret extraction from third-party wallets.

## Chimera II integration

This repository is a reference component for Chimera II C8192/R8192 cryptographic experiments. Native acceleration may expose Keccak/SHA operations, wide modular arithmetic and secp256k1 contracts, but the wallet safety boundary remains unchanged.
