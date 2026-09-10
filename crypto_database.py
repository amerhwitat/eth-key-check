"""SQLite storage for public crypto research data and operator-owned key references.

Private keys are never stored in plaintext by this module.  The key table stores
only a SHA-256 fingerprint and optional encrypted reference metadata supplied by
an external vault.  This intentionally does not implement address->private-key
recovery, seed guessing, or brute-force search.
"""
from __future__ import annotations

import hashlib
import sqlite3
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional

SCHEMA = """
CREATE TABLE IF NOT EXISTS addresses (
    id INTEGER PRIMARY KEY,
    coin TEXT NOT NULL,
    network TEXT NOT NULL,
    address TEXT NOT NULL,
    label TEXT,
    first_seen TEXT,
    UNIQUE(coin, network, address)
);
CREATE TABLE IF NOT EXISTS balances (
    id INTEGER PRIMARY KEY,
    address_id INTEGER NOT NULL REFERENCES addresses(id),
    balance_atomic TEXT NOT NULL,
    unit TEXT NOT NULL,
    block_ref TEXT,
    source TEXT NOT NULL,
    observed_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS transactions (
    txid TEXT NOT NULL,
    coin TEXT NOT NULL,
    network TEXT NOT NULL,
    address TEXT,
    block_ref TEXT,
    direction TEXT,
    amount_atomic TEXT,
    observed_at TEXT NOT NULL,
    PRIMARY KEY(txid, coin, network, address)
);
CREATE TABLE IF NOT EXISTS key_fingerprints (
    id INTEGER PRIMARY KEY,
    coin TEXT NOT NULL,
    network TEXT NOT NULL,
    address TEXT,
    key_fingerprint TEXT NOT NULL,
    vault_ref TEXT,
    created_at TEXT NOT NULL,
    UNIQUE(coin, network, key_fingerprint)
);
"""

@dataclass(frozen=True)
class AddressRecord:
    coin: str
    network: str
    address: str
    label: Optional[str] = None

class CryptoDatabase:
    def __init__(self, path: str = "crypto_research.sqlite3") -> None:
        self.connection = sqlite3.connect(path)
        self.connection.row_factory = sqlite3.Row
        self.connection.executescript(SCHEMA)
        self.connection.commit()

    def add_address(self, record: AddressRecord) -> int:
        now = datetime.now(timezone.utc).isoformat()
        cur = self.connection.execute(
            "INSERT OR IGNORE INTO addresses(coin,network,address,label,first_seen) VALUES(?,?,?,?,?)",
            (record.coin, record.network, record.address, record.label, now),
        )
        self.connection.commit()
        row = self.connection.execute(
            "SELECT id FROM addresses WHERE coin=? AND network=? AND address=?",
            (record.coin, record.network, record.address),
        ).fetchone()
        return int(row[0]) if row else int(cur.lastrowid)

    def add_balance(self, record: AddressRecord, balance_atomic: str, unit: str,
                    source: str, block_ref: Optional[str] = None) -> None:
        address_id = self.add_address(record)
        self.connection.execute(
            "INSERT INTO balances(address_id,balance_atomic,unit,block_ref,source,observed_at) VALUES(?,?,?,?,?,?)",
            (address_id, str(balance_atomic), unit, block_ref, source,
             datetime.now(timezone.utc).isoformat()),
        )
        self.connection.commit()

    def add_owned_key_fingerprint(self, coin: str, network: str, address: str,
                                  private_key_hex: str, vault_ref: Optional[str] = None) -> str:
        """Record only a fingerprint for a key already possessed by the operator."""
        fp = hashlib.sha256(private_key_hex.lower().removeprefix("0x").encode()).hexdigest()
        self.connection.execute(
            "INSERT OR REPLACE INTO key_fingerprints(coin,network,address,key_fingerprint,vault_ref,created_at) VALUES(?,?,?,?,?,?)",
            (coin, network, address, fp, vault_ref, datetime.now(timezone.utc).isoformat()),
        )
        self.connection.commit()
        return fp

    def latest_balances(self):
        return self.connection.execute("""
            SELECT a.coin,a.network,a.address,a.label,b.balance_atomic,b.unit,b.block_ref,b.source,b.observed_at
            FROM addresses a JOIN balances b ON b.address_id=a.id
            WHERE b.id IN (SELECT MAX(id) FROM balances GROUP BY address_id)
            ORDER BY a.coin,a.address
        """).fetchall()

    def close(self) -> None:
        self.connection.close()
