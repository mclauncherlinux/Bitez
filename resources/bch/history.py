from resources.bch.network import bch_network

def bch_tx_history(prkey):
    key = bch_network(prkey=prkey)
    return key.get_transactions()

def bch_tx_count(prkey):
    key = bch_network(prkey=prkey)
    txs = key.get_transactions()
    return len(txs)
