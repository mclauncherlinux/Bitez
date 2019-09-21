from dotenv import load_dotenv
from os.path import join, dirname
import os

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# config variables

# database
DB_HOST = os.getenv('DB_HOST')
DB_PORT = 51004
DB_CLIENT = 'bitez'

# jwt auth
SECRET_KEY = os.getenv('SECRET_KEY')
ACTIVATION_EXPIRE_DAYS = 5
TOKEN_EXPIRE_DAYS = 30

# email
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USERNAME = os.getenv('MAIL_USERNAME')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
MAIL_DEFAULT_SENDER = os.getenv('MAIL_USERNAME')

# crypto network
CRYPTO_NETWORK = 'testnet'

# encryption secrect
ENCRYPTION_SECRET = os.getenv('ENCRYPTION_SECRET')
