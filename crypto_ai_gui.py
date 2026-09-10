"""Tkinter console for the public crypto database, balance scanner and ML lab."""
import tkinter as tk
from tkinter import ttk, messagebox

from crypto_database import CryptoDatabase, AddressRecord
from balance_scanner import ethereum_from_env

class CryptoAIGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chimera Crypto AI Research Console")
        self.geometry("1000x650")
        self.db = CryptoDatabase()
        self._build()
        self.refresh()

    def _build(self):
        toolbar = ttk.Frame(self, padding=8); toolbar.pack(fill="x")
        ttk.Button(toolbar, text="Refresh", command=self.refresh).pack(side="left")
        ttk.Button(toolbar, text="Scan ETH", command=self.scan_eth).pack(side="left", padx=5)
        self.status = ttk.Label(toolbar, text="Public-data research mode")
        self.status.pack(side="right")
        columns = ("coin", "network", "address", "balance", "unit", "source")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col.title())
            self.tree.column(col, width=150 if col != "address" else 320)
        self.tree.pack(fill="both", expand=True, padx=8, pady=8)
        ttk.Label(self, text="ML modules: crypto_ml.py (CNN/RNN) and crypto_rl.py (offline PPO). Private-key recovery is intentionally unavailable.").pack(fill="x", padx=8, pady=8)

    def refresh(self):
        for item in self.tree.get_children(): self.tree.delete(item)
        for row in self.db.latest_balances():
            self.tree.insert("", "end", values=(row["coin"], row["network"], row["address"], row["balance_atomic"], row["unit"], row["source"]))

    def scan_eth(self):
        provider = ethereum_from_env()
        if provider is None:
            messagebox.showinfo("RPC not configured", "Set CHIMERA_ETH_RPC_URL and enter a public Ethereum address in the source/API integration.")
            return
        messagebox.showinfo("ETH scanner", "RPC configured. Use balance_scanner.EthereumRPC.balance(address) from the research API.")

if __name__ == "__main__":
    CryptoAIGUI().mainloop()
