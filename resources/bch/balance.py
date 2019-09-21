from resources.bch.network import bch_network

def bch_balance(currency, prkey):
    key = bch_network(prkey=prkey)
    return key.get_balance(currency)
