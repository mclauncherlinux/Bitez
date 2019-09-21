from flask_restful import Resource, abort
from flask import request
import re
import datetime
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
from config import DB_HOST, DB_PORT, DB_CLIENT, SECRET_KEY, ACTIVATION_EXPIRE_DAYS, TOKEN_EXPIRE_DAYS
from services.dbconfig import Database
from services.mailer import send_email
from models.user import User
from models.wallet import Wallet
from mongoengine import connect, NotUniqueError

# init mongoengine
connect(DB_CLIENT, host=DB_HOST, port=DB_PORT, retryWrites=False)

# init db
client = Database()
db = client.light()

# register a new user
class Register(Resource):
    def post(self):
        username = request.json['username']
        email = request.json['email']
        password = request.json['password']
        # email regexp validation
        if not re.match(r'^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$', email):
            abort(400, message='Email not valid.')
        # verify password weakness
        if len(password) < 6:
            abort(400, message='Password too weak.')
        else:
            try:
                user = User(username=username, email=email, password=generate_password_hash(password), active=False)
                user.save()
            # verify if email/username already exist
            except NotUniqueError:
                abort(400, message='Username or email already used by another user')
        # encode jwt    
        exp = datetime.datetime.utcnow() + datetime.timedelta(days=ACTIVATION_EXPIRE_DAYS)
        encoded = jwt.encode({'email': email, 'exp': exp},
                             SECRET_KEY, algorithm='HS256')
        activation_code = encoded.decode('utf-8')
        # Send activation email
        activation_str = "Your activation code is: "+activation_code
        send_email(email, "Activation code", activation_str)
        # create new wallet
        wallet = Wallet(username=username)
        wallet.save()
        return {'success': "Account created"}

class Login(Resource):
    def get(self):
        email = request.json['email']
        password = request.json['password']
        if db.user.find({'email': email}).count() == 0:
            abort(404, message="User not found")
        
        user = db.user.find_one({'email': email}, {'email': 1, 'password': 1})

        if not check_password_hash(user['password'], password):
            abort(400, message="Incorrect password")

        exp = datetime.datetime.utcnow() + datetime.timedelta(days=TOKEN_EXPIRE_DAYS)
        encoded = jwt.encode({'email': email, 'exp': exp}, SECRET_KEY, algorithm='HS256')
        
        return {'token': encoded.decode('utf-8')}


class Activate(Resource):
    def put(self):
        # TODO: replace by url param to be able to create activation urls
        activation_code = request.json['activation_code']
        try:
            decoded = jwt.decode(activation_code, SECRET_KEY, algorithms='HS256')
        except jwt.DecodeError:
            abort(400, message='Activation code not valid.')
        except jwt.ExpiredSignatureError:
            abort(400, message='Activation code expired.')
        email = decoded['email']
        db.user.update({'email': email}, {'$set': {'active': True}})
        return {'success': 'Account activated'}

