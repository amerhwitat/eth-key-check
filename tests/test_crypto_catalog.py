from crypto_catalog import CryptoCatalog


def test_catalog_and_hash(tmp_path):
    db = CryptoCatalog(tmp_path / "crypto.sqlite")
    rows = db.list_coins()
    assert any(row["symbol"] == "BTC" for row in rows)
    assert db.hash_text("sha256", "abc") == "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
    db.close()
