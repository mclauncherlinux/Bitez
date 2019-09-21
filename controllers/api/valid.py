from flask_restful import Resource, abort
from flask import request, jsonify
from resources.btc.valid import btc_addr_is_valid
from services.api_calls import use_api_key

class ValidAddr(Resource):
    def get(self, coin):
        # verify api key
        api_key = request.args['api_key']
        address = request.args['address']
        use_api_key(api_key)
        # Bitcoin
        if coin == 'btc':
            valid = btc_addr_is_valid(address)

        return jsonify(network=coin.upper(), address=address, is_valid=valid)
