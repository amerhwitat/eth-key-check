"""Read-only blockchain balance scanner for public addresses.

The scanner never asks for private keys and never attempts address->key recovery.
Providers are explicit and credentials, when needed, come from environment
variables rather than source control.
"""
from __future__ import annotations

import json
import os
import urllib.request
from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class BalanceResult:
    coin: str
    network: str
    address: str
    atomic_balance: str
    unit: str
    block_ref: Optional[str]
    source: str

class EthereumRPC:
    def __init__(self, endpoint: str, timeout: float = 15.0) -> None:
        self.endpoint, self.timeout = endpoint, timeout

    def balance(self, address: str, block: str = "latest") -> BalanceResult:
        payload = json.dumps({"jsonrpc":"2.0","method":"eth_getBalance",
                              "params":[address, block],"id":1}).encode()
        request = urllib.request.Request(self.endpoint, payload,
                                         headers={"Content-Type":"application/json"})
        with urllib.request.urlopen(request, timeout=self.timeout) as response:
            data = json.load(response)
        if "error" in data:
            raise RuntimeError(str(data["error"]))
        return BalanceResult("ETH", "ethereum", address, str(int(data["result"], 16)),
                             "wei", block, self.endpoint)

def ethereum_from_env() -> Optional[EthereumRPC]:
    endpoint = os.getenv("CHIMERA_ETH_RPC_URL")
    return EthereumRPC(endpoint) if endpoint else None

class BitcoinCoreRPC:
    """Read-only Bitcoin Core adapter. Credentials are environment supplied."""
    def __init__(self, endpoint: str = "http://127.0.0.1:8332", timeout: float = 15.0) -> None:
        self.endpoint, self.timeout = endpoint, timeout

    def getbalances(self) -> dict:
        user = os.getenv("CHIMERA_BTC_RPC_USER", "")
        password = os.getenv("CHIMERA_BTC_RPC_PASSWORD", "")
        import base64
        auth = base64.b64encode(f"{user}:{password}".encode()).decode()
        payload = json.dumps({"jsonrpc":"2.0","id":"chimera","method":"getbalances","params":[]}).encode()
        request = urllib.request.Request(self.endpoint, payload, headers={
            "Content-Type":"application/json", "Authorization":f"Basic {auth}"})
        with urllib.request.urlopen(request, timeout=self.timeout) as response:
            data = json.load(response)
        if "error" in data:
            raise RuntimeError(str(data["error"]))
        return data["result"]
