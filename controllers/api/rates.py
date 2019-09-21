# get rates for 1 unit in a given currency to another given currency
from flask_restful import Resource, abort
from flask import request, jsonify
from resources.btc.rates import btc_to_fiat, fiat_to_btc
from services.api_calls import use_api_key

class RatesToFiat(Resource):
    def get(self, coin):
        # verify api key
        api_key = request.args['api_key']
        currency = request.args['currency']
        use_api_key(api_key)
        # Bitcoin
        if coin == 'btc':
            rate = btc_to_fiat(1, currency)

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
            rate = fiat_to_btc(int(amount), currency)

        return jsonify(network=coin.upper(), rate=rate, currency=currency.upper())
