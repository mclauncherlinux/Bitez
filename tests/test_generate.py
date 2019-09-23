import pytest
import re
from config import CRYPTO_NETWORK
from resources.btc.generate import GenerateBtcKey
from resources.bch.generate import GenerateBchKey

def test_btc_key():
    btc_key = GenerateBtcKey()
    addr = btc_key.generate_std_addr()
    if CRYPTO_NETWORK == 'mainnet':
        assert re.match('^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$', addr)
    elif CRYPTO_NETWORK == 'testnet':
        assert re.match('^[2mn][1-9A-HJ-NP-Za-km-z]{26,35}', addr)

def test_bch_key():
    bch_key = GenerateBchKey()
    addr = bch_key.generate_std_addr()
    assert re.match('^((bitcoincash|bchreg|bchtest):)?(q|p)[a-z0-9]{41}$', addr)
