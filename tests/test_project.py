import pytest

from project import checksum_address, normalize_private_key, validate_address


def test_eip55_vectors():
    vectors = {
        "0x5aAeb6053F3E94C9b9A09f33669435E7Ef1BeAed": "0x5aAeb6053F3E94C9b9A09f33669435E7Ef1BeAed",
        "0xfB6916095ca1df60bB79Ce92cE3Ea74c37c5d359": "0xfB6916095ca1df60bB79Ce92cE3Ea74c37c5d359",
        "0xdbF03B407c01E7cD3CBea99509d93f8DDDC8C6FB": "0xdbF03B407c01E7cD3CBea99509d93f8DDDC8C6FB",
        "0xD1220A0cf47c7B9Be7A2E6BA89F429762e7b9aDb": "0xD1220A0cf47c7B9Be7A2E6BA89F429762e7b9aDb",
    }
    for address, expected in vectors.items():
        assert checksum_address(address.lower()) == expected


def test_address_validation():
    assert validate_address("0x" + "00" * 20) == "0x" + "00" * 20
    with pytest.raises(ValueError):
        validate_address("0x1234")
    with pytest.raises(ValueError):
        validate_address("not-an-address")


def test_private_key_validation():
    assert normalize_private_key("0x" + "01" * 32) == "01" * 32
    with pytest.raises(ValueError):
        normalize_private_key("00")
    with pytest.raises(ValueError):
        normalize_private_key("0x" + "00" * 32)
