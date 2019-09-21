import functools
import jwt
from flask import request
from flask_restful import abort
from services.dbconfig import Database
from config import SECRET_KEY

client = Database()
db = client.light()

def login_required(method):
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        header = request.headers.get('Authorization')

        try:
            _, token = header.split()
            decoded = jwt.decode(token, SECRET_KEY, algorithms='HS256')
        except jwt.DecodeError:
            abort(400, message='Invalid session')
        except jwt.ExpiredSignatureError:
            abort(400, message='Session expired')
        except AttributeError:
            abort(400, message='Invalid session')
        except ValueError:
            abort(400, message='Invalid session')
        email = decoded['email']
        if db.user.find({'email': email}).count() == 0:
            abort(404, message='User not found')
        user = db.user.find_one({'email': email})
        return method(self, user, *args, **kwargs)
    return wrapper
