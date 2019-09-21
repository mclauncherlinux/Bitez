import re
from config import CRYPTO_NETWORK

def btc_addr_is_valid(address):
    if CRYPTO_NETWORK == 'mainnet':
        if not re.match('^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$', address):
            match = False
        else:
            match = True
    elif CRYPTO_NETWORK == 'testnet':
        if not re.match('^[2mn][1-9A-HJ-NP-Za-km-z]{26,35}', address):
            match = False
        else:
            match = True

    return match
