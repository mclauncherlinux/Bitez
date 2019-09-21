from resources.btc.network import btc_network
from bit.exceptions import InsufficientFunds

def btc_tx(recipient, amount, currency, prkey):
    key = btc_network(prkey=prkey)
    try:
        tx = key.send([(recipient, amount, currency)])
        error = False
    except InsufficientFunds:
    	tx = False
    except ValueError:
    	tx = False
    return tx
