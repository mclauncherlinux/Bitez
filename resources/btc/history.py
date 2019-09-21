from resources.btc.network import btc_network

def btc_tx_history(prkey):
    key = btc_network(prkey=prkey)
    return key.get_transactions()

def btc_tx_count(prkey):
    key = btc_network(prkey=prkey)
    txs = key.get_transactions()
    return len(txs)
