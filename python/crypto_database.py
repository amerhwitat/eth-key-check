"""SQLite storage for public crypto research data and operator-owned key references."""
from __future__ import annotations
import hashlib, sqlite3
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional
SCHEMA='''CREATE TABLE IF NOT EXISTS addresses(id INTEGER PRIMARY KEY,coin TEXT NOT NULL,network TEXT NOT NULL,address TEXT NOT NULL,label TEXT,first_seen TEXT,UNIQUE(coin,network,address)); CREATE TABLE IF NOT EXISTS balances(id INTEGER PRIMARY KEY,address_id INTEGER NOT NULL REFERENCES addresses(id),balance_atomic TEXT NOT NULL,unit TEXT NOT NULL,block_ref TEXT,source TEXT NOT NULL,observed_at TEXT NOT NULL); CREATE TABLE IF NOT EXISTS transactions(txid TEXT NOT NULL,coin TEXT NOT NULL,network TEXT NOT NULL,address TEXT,block_ref TEXT,direction TEXT,amount_atomic TEXT,observed_at TEXT NOT NULL,PRIMARY KEY(txid,coin,network,address)); CREATE TABLE IF NOT EXISTS key_fingerprints(id INTEGER PRIMARY KEY,coin TEXT NOT NULL,network TEXT NOT NULL,address TEXT,key_fingerprint TEXT NOT NULL,vault_ref TEXT,created_at TEXT NOT NULL,UNIQUE(coin,network,key_fingerprint));'''
@dataclass(frozen=True)
class AddressRecord: coin:str; network:str; address:str; label:Optional[str]=None
class CryptoDatabase:
 def __init__(self,path='crypto_research.sqlite3'): self.connection=sqlite3.connect(path); self.connection.row_factory=sqlite3.Row; self.connection.executescript(SCHEMA); self.connection.commit()
 def add_address(self,r):
  now=datetime.now(timezone.utc).isoformat(); self.connection.execute('INSERT OR IGNORE INTO addresses(coin,network,address,label,first_seen) VALUES(?,?,?,?,?)',(r.coin,r.network,r.address,r.label,now)); self.connection.commit(); row=self.connection.execute('SELECT id FROM addresses WHERE coin=? AND network=? AND address=?',(r.coin,r.network,r.address)).fetchone(); return int(row[0])
 def add_balance(self,r,balance_atomic,unit,source,block_ref=None):
  i=self.add_address(r); self.connection.execute('INSERT INTO balances(address_id,balance_atomic,unit,block_ref,source,observed_at) VALUES(?,?,?,?,?,?)',(i,str(balance_atomic),unit,block_ref,source,datetime.now(timezone.utc).isoformat())); self.connection.commit()
 def add_owned_key_fingerprint(self,coin,network,address,private_key_hex,vault_ref=None):
  fp=hashlib.sha256(private_key_hex.lower().removeprefix('0x').encode()).hexdigest(); self.connection.execute('INSERT OR REPLACE INTO key_fingerprints(coin,network,address,key_fingerprint,vault_ref,created_at) VALUES(?,?,?,?,?,?)',(coin,network,address,fp,vault_ref,datetime.now(timezone.utc).isoformat())); self.connection.commit(); return fp
 def latest_balances(self): return self.connection.execute('SELECT a.coin,a.network,a.address,a.label,b.balance_atomic,b.unit,b.block_ref,b.source,b.observed_at FROM addresses a JOIN balances b ON b.address_id=a.id WHERE b.id IN (SELECT MAX(id) FROM balances GROUP BY address_id) ORDER BY a.coin,a.address').fetchall()
 def close(self): self.connection.close()
