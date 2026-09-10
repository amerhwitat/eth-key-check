"""Professional Tkinter GUI for the safe crypto catalog."""
from __future__ import annotations

import tkinter as tk
from tkinter import messagebox, ttk

from crypto_catalog import CryptoCatalog


class CryptoApp(tk.Tk):
    def __init__(self, db_path: str = "crypto_catalog.sqlite") -> None:
        super().__init__()
        self.title("Chimera Crypto Research Console")
        self.geometry("1100x700")
        self.minsize(900, 600)
        self.catalog = CryptoCatalog(db_path)
        self._build()
        self.refresh()

    def _build(self) -> None:
        root = ttk.Frame(self, padding=12)
        root.pack(fill="both", expand=True)
        ttk.Label(root, text="Cryptocurrency & Cryptography Research", font=("TkDefaultFont", 18, "bold")).pack(anchor="w")
        ttk.Label(root, text="Public metadata, address-safe verification, and local hash experiments; no private-key recovery.").pack(anchor="w", pady=(0, 12))
        controls = ttk.Frame(root)
        controls.pack(fill="x", pady=(0, 8))
        ttk.Label(controls, text="Search").pack(side="left")
        self.query = ttk.Entry(controls)
        self.query.pack(side="left", fill="x", expand=True, padx=8)
        ttk.Button(controls, text="Search", command=self.refresh).pack(side="left")
        ttk.Button(controls, text="All Coins", command=lambda: self._set_all()).pack(side="left", padx=(8, 0))

        columns = ("symbol", "name", "network", "address", "signature", "hash")
        self.table = ttk.Treeview(root, columns=columns, show="headings", height=16)
        headings = {"symbol":"Symbol", "name":"Name", "network":"Network", "address":"Address Family", "signature":"Signature", "hash":"Hash"}
        widths = {"symbol":80,"name":150,"network":150,"address":190,"signature":190,"hash":170}
        for col in columns:
            self.table.heading(col, text=headings[col])
            self.table.column(col, width=widths[col], anchor="w")
        self.table.pack(fill="both", expand=True)

        hash_box = ttk.LabelFrame(root, text="Local Hash Lab", padding=8)
        hash_box.pack(fill="x", pady=(12, 0))
        self.algorithm = ttk.Combobox(hash_box, values=("sha256", "sha512", "sha3_256", "sha3_512"), state="readonly")
        self.algorithm.set("sha256")
        self.algorithm.pack(side="left")
        self.hash_input = ttk.Entry(hash_box)
        self.hash_input.pack(side="left", fill="x", expand=True, padx=8)
        ttk.Button(hash_box, text="Hash", command=self.make_hash).pack(side="left")
        self.result = ttk.Entry(hash_box)
        self.result.pack(side="left", fill="x", expand=True, padx=8)

    def _set_all(self) -> None:
        self.query.delete(0, "end")
        self.refresh()

    def refresh(self) -> None:
        rows = self.catalog.search(self.query.get()) if self.query.get().strip() else self.catalog.list_coins()
        for item in self.table.get_children():
            self.table.delete(item)
        for row in rows:
            self.table.insert("", "end", values=(row["symbol"], row["name"], row["network"], row["address_family"], row["signature_family"], row["hash_family"]))

    def make_hash(self) -> None:
        try:
            digest = self.catalog.hash_text(self.algorithm.get(), self.hash_input.get())
            self.result.delete(0, "end")
            self.result.insert(0, digest)
        except ValueError as exc:
            messagebox.showerror("Crypto error", str(exc))


if __name__ == "__main__":
    CryptoApp().mainloop()
