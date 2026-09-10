# Safe Crypto Scope

This repository is limited to legitimate cryptocurrency key/address verification and derivation.

## Supported

- Derive an Ethereum address from a private key that the operator already possesses.
- Validate Ethereum address syntax/checksum where supported by the selected library.
- Derive addresses from BIP-39/BIP-32/BIP-44 material that the operator legitimately possesses.
- Use published cryptographic test vectors.

## Not supported

This project does not search for, recover, infer, brute-force, or map a private key from a public Bitcoin/Ethereum address. A public address is not a reversible representation of its private key.

Existing key-search datasets and wallet-search loops should not be used for unauthorized access.

## Security

Never commit private keys, seed phrases, wallet files, API credentials, or test secrets to Git. Prefer offline operation and sanitized test vectors.
