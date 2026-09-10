"""Blockchain observation and owner-authorized transaction broadcast helpers.

The module never accepts a private key or seed phrase. Ethereum transactions must
be signed externally and are submitted as raw signed transactions. Bitcoin
spending is delegated to an authenticated Bitcoin Core wallet RPC.
"""
from __future__ import annotations

import base64
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

    def _call(self, method: str, params: list) -> object:
        payload = json.dumps({"jsonrpc": "2.0", "method": method,
                              "params": params, "id": 1}).encode()
        request = urllib.request.Request(
            self.endpoint, payload, headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(request, timeout=self.timeout) as response:
            data = json.load(response)
        if "error" in data:
            raise RuntimeError(str(data["error"]))
        return data["result"]

    def balance(self, address: str, block: str = "latest") -> BalanceResult:
        result = self._call("eth_getBalance", [address, block])
        return BalanceResult("ETH", "ethereum", address, str(int(result, 16)),
                             "wei", block, self.endpoint)

    def send_raw_transaction(self, signed_transaction: str) -> str:
        """Broadcast an already-signed Ethereum transaction.

        Signing is intentionally external: this method never receives a private
        key or seed phrase.
        """
        if not isinstance(signed_transaction, str) or not signed_transaction.startswith("0x"):
            raise ValueError("signed_transaction must be 0x-prefixed hex")
        return str(self._call("eth_sendRawTransaction", [signed_transaction]))


def ethereum_from_env() -> Optional[EthereumRPC]:
    endpoint = os.getenv("CHIMERA_ETH_RPC_URL")
    return EthereumRPC(endpoint) if endpoint else None


class BitcoinCoreRPC:
    """Bitcoin Core adapter using authenticated wallet RPCs."""

    def __init__(self, endpoint: str = "http://127.0.0.1:8332", timeout: float = 15.0) -> None:
        self.endpoint, self.timeout = endpoint, timeout

    def _call(self, method: str, params: list) -> object:
        user = os.getenv("CHIMERA_BTC_RPC_USER", "")
        password = os.getenv("CHIMERA_BTC_RPC_PASSWORD", "")
        auth = base64.b64encode(f"{user}:{password}".encode()).decode()
        payload = json.dumps({"jsonrpc": "1.0", "id": "chimera",
                              "method": method, "params": params}).encode()
        request = urllib.request.Request(
            self.endpoint, payload,
            headers={"Content-Type": "application/json", "Authorization": f"Basic {auth}"},
        )
        with urllib.request.urlopen(request, timeout=self.timeout) as response:
            data = json.load(response)
        if data.get("error"):
            raise RuntimeError(str(data["error"]))
        return data["result"]

    def getbalances(self) -> dict:
        return self._call("getbalances", [])

    def getnewaddress(self, label: str = "", address_type: str = "") -> str:
        """Request a fresh receiving address from the authenticated wallet."""
        params = [label]
        if address_type:
            params.append(address_type)
        return str(self._call("getnewaddress", params))

    def send_to_address(self, address: str, amount_btc: str | float) -> str:
        """Send BTC through the authenticated Bitcoin Core wallet.

        The wallet/node performs signing; this adapter never handles raw private
        keys. The caller must have configured and authorized the wallet.
        """
        return str(self._call("sendtoaddress", [address, amount_btc]))
