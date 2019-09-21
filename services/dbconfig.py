import pymongo
from config import DB_HOST, DB_PORT, DB_CLIENT

class Database:
    def __init__(self):
        self.host = DB_HOST
        self.port = DB_PORT
        self.client = DB_CLIENT

    def light(self):
        client = pymongo.MongoClient(host=self.host, port=self.port, retryWrites=False)
        db = client[self.client]
        return db
