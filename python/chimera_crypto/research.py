"""Unified facade over the existing Python research components.

Legacy root modules remain compatibility entry points; this facade is the
single import surface for new Python integrations.
"""
from .validation import normalize_eth_address, validate_eth_address
from .audit import AuditEvent
from .contracts import InteropEnvelope

try:
    from balance_scanner import EthereumRPC, BitcoinCoreRPC
except ImportError:
    EthereumRPC = None
    BitcoinCoreRPC = None

try:
    from crypto_database import CryptoDatabase
except ImportError:
    CryptoDatabase = None

try:
    from crypto_ml import CryptoCNN, CryptoGRU
except ImportError:
    CryptoCNN = None
    CryptoGRU = None

try:
    from crypto_rl import CryptoResearchEnv
except ImportError:
    CryptoResearchEnv = None

__all__ = [
    "normalize_eth_address", "validate_eth_address", "AuditEvent", "InteropEnvelope",
    "EthereumRPC", "BitcoinCoreRPC", "CryptoDatabase", "CryptoCNN", "CryptoGRU",
    "CryptoResearchEnv",
]
