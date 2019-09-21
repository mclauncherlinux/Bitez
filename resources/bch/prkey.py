# encrypt prkey and return encrypted string to store somewhere
from resources.utils.encrypt import genkey, encrypt_prkey, decrypt_prkey
from config import ENCRYPTION_SECRET

def encrypt(prkey):
    enc_key = genkey(ENCRYPTION_SECRET)
    encrypted = encrypt_prkey(prkey, enc_key)
    return encrypted

def decrypt(encrypted):
    enc_key = genkey(ENCRYPTION_SECRET)
    decrypted = decrypt_prkey(encrypted, enc_key)
    return decrypted.decode("utf-8")
