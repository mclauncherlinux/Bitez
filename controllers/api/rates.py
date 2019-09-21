# get rates for 1 unit in a given currency to another given currency
from flask_restful import Resource, abort
from flask import request, jsonify
from services.api_calls import use_api_key
# btc
from resources.btc.rates import btc_to_fiat, fiat_to_btc
# bch
from resources.bch.rates import bch_to_fiat, fiat_to_bch

class RatesToFiat(Resource):
    def get(self, coin):
        # verify api key
        api_key = request.args['api_key']
        currency = request.args['currency']
        use_api_key(api_key)
        # Bitcoin
        if coin == 'btc':
            rate = btc_to_fiat(1, currency)
        # Bitcoin cash
        elif coin == 'bch':
            rate = bch_to_fiat(1, currency)

        return jsonify(network=coin.upper(), rate=rate, currency=currency.upper())

class RatesToCrypto(Resource):
    def get(self, coin):
        # verify api key
        api_key = request.args['api_key']
        amount = request.args['amount']
        currency = request.args['currency']
        use_api_key(api_key)
        # Bitcoin
        if coin == 'btc':
            rate = fiat_to_btc(float(amount), currency)
        # Bitcoin cash
        elif coin == 'bch':
            rate = fiat_to_bch(float(amount), currency)

        return jsonify(network=coin.upper(), rate=rate, currency=currency.upper())
