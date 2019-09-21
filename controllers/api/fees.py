# get transactions fees for a given crypto
from flask_restful import Resource, abort
from flask import request, jsonify
from resources.btc.fees import btc_tx_fees
from services.api_calls import use_api_key

class GetTxFees(Resource):
    def get(self, coin):
        # verify api key
        api_key = request.args['api_key']
        use_api_key(api_key)
        # Bitcoin
        if coin == 'btc':
            unit = 'satoshis/byte'
            tx_fees = btc_tx_fees()
            tx_fees_fast = btc_tx_fees(fast=True)

        return jsonify(network=coin.upper(), unit=unit, tx_fees=tx_fees, tx_fees_fast=tx_fees_fast)
