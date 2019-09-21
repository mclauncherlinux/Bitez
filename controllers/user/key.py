# generate, get, verify and revoke api keys 
from flask_restful import Resource, abort
from flask import request, jsonify
from mongoengine import connect
from services.auth import login_required
from config import DB_HOST, DB_PORT, DB_CLIENT
from services.dbconfig import Database
from models.user import User, ApiKeys
from resources.network.key import gen_api_key

# init db
client = Database()
db = client.light()

# init mongoengine
connect(DB_CLIENT, host=DB_HOST, port=DB_PORT, retryWrites=False)

class GenerateApiKey(Resource):
    @login_required
    def get(self, user):
        api_key = gen_api_key()
        # store to db
        apikeys = ApiKeys(key=api_key)
        user = User.objects.get(username=user['username'])
        user.api_keys.append(apikeys)
        user.save()
        # return api key
        return jsonify(api_key=api_key)

class GetApiKeys(Resource):
    @login_required
    def get(self, user):
        api_keys = []
        for keys in user['api_keys']:
            api_keys.append(keys['key'])
        # return api keys
        return jsonify(api_keys=api_keys)

