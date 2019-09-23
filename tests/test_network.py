import pytest
import bit
import bitcash
from resources.btc.network import btc_network
from resources.bch.network import bch_network
from config import CRYPTO_NETWORK

def test_btc_network():
    key = btc_network()
    if CRYPTO_NETWORK == 'testnet':
        assert type(key) == bit.wallet.PrivateKeyTestnet
    elif CRYPTO_NETWORK == 'mainnet':
        assert type(key) == bit.wallet.PrivateKey

def test_bch_network():
    key = bch_network()
    if CRYPTO_NETWORK == 'testnet':
        assert type(key) == bitcash.wallet.PrivateKeyTestnet
    elif CRYPTO_NETWORK == 'mainnet':
        assert type(key) == bitcash.wallet.PrivateKey
