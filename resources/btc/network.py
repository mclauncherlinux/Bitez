# init mainnet or testnet
from bit import Key, PrivateKeyTestnet
from config import CRYPTO_NETWORK

def btc_network(net=CRYPTO_NETWORK, prkey=None):
    if net == 'mainnet':
        key = Key(prkey)
    elif net == 'testnet':
        key = PrivateKeyTestnet(prkey)
    return key
