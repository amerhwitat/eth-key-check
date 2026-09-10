from crypto_database import AddressRecord, CryptoDatabase


def test_public_balance_and_key_fingerprint(tmp_path):
    db = CryptoDatabase(str(tmp_path / "crypto.sqlite3"))
    record = AddressRecord("ETH", "ethereum", "0x0000000000000000000000000000000000000001")
    db.add_balance(record, "100", "wei", "test")
    fp = db.add_owned_key_fingerprint("ETH", "ethereum", record.address, "11" * 32, "vault:test")
    assert len(fp) == 64
    rows = db.latest_balances()
    assert rows[0]["balance_atomic"] == "100"
    db.close()
