from bit.network import get_fee

def btc_tx_fees(fast=False):
    return get_fee(fast)
