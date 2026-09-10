# BizX / BizXtreme Multi-Chain Verification Integration

This package is the verification layer for BizX and BizXtreme. It must remain separate from wallet signing and secret custody.

## Verification responsibilities

- validate public addresses for supported chain formats;
- normalize chain/network identifiers;
- verify signed transactions and messages where an implementation exists;
- validate transaction fields before an application treats a payment as eligible;
- expose public balance/transaction scanner adapters;
- generate explorer references.

## Supported reference families

BTC, EVM networks, Solana/SPL, Litecoin, Dogecoin, Bitcoin Cash, XRP, Cardano, Polkadot, TRON, Stellar and TON are represented by the BizXtreme registry. Additional chains should be implemented as adapters with tests rather than added as unvalidated aliases.

## Balance policy

A balance is trusted only with a source identifier, chain/network identifier and freshness metadata. Explorer pages are useful navigation aids but are not signing authorities.

## Payment verification

A game purchase is eligible only after the application verifies the expected chain, asset, recipient, amount, transaction hash and required confirmation policy. Never treat a client-provided screenshot or manually entered transaction hash as proof without independent chain verification.

## Secret boundary

This library never performs address-to-private-key recovery, seed guessing, key enumeration against target wallets, or credential attacks. Wallet providers sign transactions; BizX services consume public addresses and signed transaction data.
