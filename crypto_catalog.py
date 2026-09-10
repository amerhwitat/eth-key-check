"""Python crypto/coin reference catalog and safe local analysis helpers.

This module is intentionally non-custodial: it stores public metadata about
cryptocurrencies and cryptographic primitives, validates addresses, and
computes hashes. It does not recover or search for private keys.
"""
from __future__ import annotations

import hashlib
import json
import sqlite3
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class Coin:
    symbol: str
    name: str
    network: str
    address_family: str
    signature_family: str
    hash_family: str
    notes: str = ""


DEFAULT_COINS = (
    Coin("BTC", "Bitcoin", "Bitcoin", "Base58Check/Bech32", "ECDSA-secp256k1", "SHA-256", "Proof-of-work UTXO network"),
    Coin("ETH", "Ethereum", "Ethereum", "hex/Keccak-256", "ECDSA-secp256k1", "Keccak-256", "Account-based smart-contract network"),
    Coin("LTC", "Litecoin", "Litecoin", "Base58Check/Bech32", "ECDSA-secp256k1", "SHA-256", "Bitcoin-derived UTXO network"),
    Coin("DOGE", "Dogecoin", "Dogecoin", "Base58Check", "ECDSA-secp256k1", "Scrypt/SHA-256 family", "Proof-of-work UTXO network"),
    Coin("XMR", "Monero", "Monero", "Monero address formats", "EdDSA/Curve25519 family", "Keccak-256 family", "Privacy-oriented protocol; address formats differ from Bitcoin/Ethereum"),
    Coin("SOL", "Solana", "Solana", "Base58", "Ed25519", "SHA-256/Keccak families", "High-throughput account/program network"),
)


class CryptoCatalog:
    """Small SQLite catalog for public coin/crypto metadata."""

    def __init__(self, path: str | Path = "crypto_catalog.sqlite") -> None:
        self.path = str(path)
        self.db = sqlite3.connect(self.path)
        self.db.row_factory = sqlite3.Row
        self.db.execute("PRAGMA foreign_keys=ON")
        self.db.execute("""
            CREATE TABLE IF NOT EXISTS coins (
                symbol TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                network TEXT NOT NULL,
                address_family TEXT NOT NULL,
                signature_family TEXT NOT NULL,
                hash_family TEXT NOT NULL,
                notes TEXT NOT NULL DEFAULT ''
            )
        """)
        self.db.execute("""
            CREATE TABLE IF NOT EXISTS hash_records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                algorithm TEXT NOT NULL,
                input_text TEXT NOT NULL,
                digest_hex TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.db.commit()
        self.seed()

    def seed(self, coins: Iterable[Coin] = DEFAULT_COINS) -> None:
        self.db.executemany(
            """INSERT OR IGNORE INTO coins
            (symbol,name,network,address_family,signature_family,hash_family,notes)
            VALUES (:symbol,:name,:network,:address_family,:signature_family,:hash_family,:notes)""",
            [asdict(c) for c in coins],
        )
        self.db.commit()

    def list_coins(self) -> list[dict]:
        return [dict(row) for row in self.db.execute("SELECT * FROM coins ORDER BY symbol")]

    def search(self, text: str) -> list[dict]:
        q = f"%{text.strip()}%"
        return [dict(row) for row in self.db.execute(
            "SELECT * FROM coins WHERE symbol LIKE ? OR name LIKE ? OR network LIKE ? OR signature_family LIKE ? ORDER BY symbol",
            (q, q, q, q),
        )]

    def hash_text(self, algorithm: str, text: str) -> str:
        normalized = algorithm.lower().replace("-", "")
        if normalized not in {"sha256", "sha512", "sha3_256", "sha3_512"}:
            raise ValueError("Supported local algorithms: sha256, sha512, sha3_256, sha3_512")
        digest = hashlib.new(normalized, text.encode("utf-8")).hexdigest()
        self.db.execute(
            "INSERT INTO hash_records(algorithm,input_text,digest_hex) VALUES(?,?,?)",
            (algorithm, text, digest),
        )
        self.db.commit()
        return digest

    def export_json(self, path: str | Path) -> None:
        payload = {"coins": self.list_coins()}
        Path(path).write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")

    def close(self) -> None:
        self.db.close()
