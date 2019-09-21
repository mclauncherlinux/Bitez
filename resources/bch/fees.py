from bitcash.network import get_fee

def bch_tx_fees(fast=False):
    return get_fee(fast)
