from resources.btc.network import btc_network

def btc_balance(currency, prkey):
    key = btc_network(prkey=prkey)
    return key.get_balance(currency)
