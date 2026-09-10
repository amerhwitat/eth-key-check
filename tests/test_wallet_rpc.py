import pytest

from balance_scanner import EthereumRPC, BitcoinCoreRPC


class DummyEthereum(EthereumRPC):
    def __init__(self):
        pass

    def _call(self, method, params):
        assert method == "eth_sendRawTransaction"
        assert params == ["0xdeadbeef"]
        return "0x" + "ab" * 32


class DummyBitcoin(BitcoinCoreRPC):
    def __init__(self):
        pass

    def _call(self, method, params):
        assert method == "sendtoaddress"
        assert params == ["bc1qexample", "0.001"]
        return "txid-example"


def test_ethereum_broadcast_requires_signed_hex():
    rpc = DummyEthereum()
    assert rpc.send_raw_transaction("0xdeadbeef").startswith("0x")
    with pytest.raises(ValueError):
        rpc.send_raw_transaction("not-signed-data")


def test_bitcoin_send_delegates_to_authenticated_wallet():
    assert DummyBitcoin().send_to_address("bc1qexample", "0.001") == "txid-example"
