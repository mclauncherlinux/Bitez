from flask_restful import abort
from services.dbconfig import Database

# init db
client = Database()
db = client.light()

def use_api_key(key):
    api_keys = []
    for api_key in db.user.find({'api_keys.key': key}):
        for k in api_key['api_keys']:
            api_keys.append(k['key'])
    if any(e == key for e in api_keys):
        pass
    else:
        abort(404, message="API Key not valid")
