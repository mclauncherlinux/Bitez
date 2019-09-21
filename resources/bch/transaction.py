from resources.bch.network import bch_network
from bitcash.exceptions import InsufficientFunds

def bch_tx(recipient, amount, currency, prkey):
    key = bch_network(prkey=prkey)
    try:
        tx = key.send([(recipient, amount, currency)])
        error = False
    except InsufficientFunds:
    	tx = False
    except ValueError:
    	tx = False
    return tx
