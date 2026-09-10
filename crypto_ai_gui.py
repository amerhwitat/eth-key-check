"""Tkinter console for the public crypto database, balance scanner and ML lab."""
import tkinter as tk
from tkinter import ttk, messagebox

from crypto_database import CryptoDatabase, AddressRecord
from balance_scanner import ethereum_from_env

class CryptoAIGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chimera Crypto AI Research Console")
        self.geometry("1100x700")
        self.db = CryptoDatabase()
        self._build(); self.refresh()

    def _build(self):
        toolbar = ttk.Frame(self, padding=8); toolbar.pack(fill="x")
        ttk.Button(toolbar, text="Refresh", command=self.refresh).pack(side="left")
        ttk.Label(toolbar, text="ETH address:").pack(side="left", padx=(12, 4))
        self.address = ttk.Entry(toolbar, width=46); self.address.pack(side="left")
        ttk.Button(toolbar, text="Scan ETH", command=self.scan_eth).pack(side="left", padx=5)
        self.status = ttk.Label(toolbar, text="Public-data research mode"); self.status.pack(side="right")
        columns = ("coin", "network", "address", "balance", "unit", "source")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col.title()); self.tree.column(col, width=155 if col != "address" else 330)
        self.tree.pack(fill="both", expand=True, padx=8, pady=8)
        ttk.Label(self, text="CNN/RNN: crypto_ml.py | PPO: crypto_rl.py | No private-key recovery or seed guessing").pack(fill="x", padx=8, pady=8)

    def refresh(self):
        for item in self.tree.get_children(): self.tree.delete(item)
        for row in self.db.latest_balances():
            self.tree.insert("", "end", values=(row["coin"], row["network"], row["address"], row["balance_atomic"], row["unit"], row["source"]))

    def scan_eth(self):
        address = self.address.get().strip()
        if not address:
            messagebox.showwarning("Address required", "Enter a public Ethereum address."); return
        provider = ethereum_from_env()
        if provider is None:
            messagebox.showwarning("RPC not configured", "Set CHIMERA_ETH_RPC_URL to a read-only Ethereum JSON-RPC endpoint."); return
        try:
            result = provider.balance(address)
            self.db.add_balance(AddressRecord("ETH", "ethereum", address), result.atomic_balance, result.unit, result.source, result.block_ref)
            self.status.config(text=f"ETH balance recorded: {result.atomic_balance} wei")
            self.refresh()
        except Exception as exc:
            messagebox.showerror("Scanner error", str(exc))

if __name__ == "__main__":
    CryptoAIGUI().mainloop()
