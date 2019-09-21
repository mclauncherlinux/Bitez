# generate a mainnet api key
import uuid

def gen_api_key():
    key = uuid.uuid4().hex
    return key
