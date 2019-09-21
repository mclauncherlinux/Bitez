# generate an address in a two formats (P2SH and WIT)
from resources.bch.network import bch_network

class GenerateBchKey:
    def __init__(self):
        self.network = bch_network()
    
    def generate_prkey(self):
        return self.network.to_wif()

    def generate_std_addr(self):
        return self.network.address

