import pytest
import bit
from resources.btc.network import btc_network
from config import CRYPTO_NETWORK

def test_network():
    key = btc_network()
    if CRYPTO_NETWORK == 'testnet':
        assert type(key) == bit.wallet.PrivateKeyTestnet
    elif CRYPTO_NETWORK == 'mainnet':
        assert type(key) == bit.wallet.PrivateKey
