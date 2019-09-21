import re

def bch_addr_is_valid(address):
    cashaddr = re.match('^((bitcoincash|bchreg|bchtest):)?(q|p)[a-z0-9]{41}$', address)
    legacyaddr = re.match('^([13][a-km-zA-HJ-NP-Z1-9]{25,34})', address)
    caplegacyaddr = re.match('^((BITCOINCASH:)?(Q|P)[A-Z0-9]{41})$', address)
    
    if not any([cashaddr, legacyaddr, caplegacyaddr]):
        match = False
    else:
        match = True

    return match
