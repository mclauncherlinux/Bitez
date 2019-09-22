from flask import Flask
from flask_restful import Api
import sys

# user methods
from controllers.user.account import Register, Login, Activate
from controllers.user.key import GenerateApiKey, GetApiKeys
# api methods
from controllers.api.address import GenerateAddr, GetAllAddr
from controllers.api.balance import GetBalance
from controllers.api.fees import GetTxFees
from controllers.api.rates import RatesToFiat, RatesToCrypto
from controllers.api.history import GetHistory
from controllers.api.valid import ValidAddr
from controllers.api.transaction import Transaction

app = Flask(__name__)
api = Api(app)

# user routes
api.add_resource(Register, '/api/auth/register')
api.add_resource(Login, '/api/auth/login')
api.add_resource(Activate, '/api/auth/activate')
api.add_resource(GenerateApiKey, '/api/generate_key')
api.add_resource(GetApiKeys, '/api/keys')

# api routes
api.add_resource(GenerateAddr, '/api/<string:coin>/generate')
api.add_resource(GetAllAddr, '/api/<string:coin>/addresses')
api.add_resource(GetBalance, '/api/<string:coin>/balance')
api.add_resource(GetTxFees, '/api/<string:coin>/fees')
api.add_resource(RatesToFiat, '/api/<string:coin>/rates')
api.add_resource(RatesToCrypto, '/api/<string:coin>/fiat_rates')
api.add_resource(GetHistory, '/api/<string:coin>/history')
api.add_resource(ValidAddr, '/api/<string:coin>/validate')
api.add_resource(Transaction, '/api/<string:coin>/tx')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        DEBUG = True
    else:
        DEBUG = False
    app.run(debug=DEBUG)
