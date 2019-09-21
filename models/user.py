from mongoengine import *
import datetime

class ApiKeys(EmbeddedDocument):
    key = StringField(unique=True)
    valid = BooleanField(default=True)
    created_at = DateTimeField(default=datetime.datetime.utcnow)

class User(Document):
    username = StringField(max_length=25, required=True, unique=True)
    email = StringField(max_length=64, required=True, unique=True)
    password = StringField(required=True)
    active = BooleanField(default=False)
    api_keys = EmbeddedDocumentListField(ApiKeys)
    joined_at = DateTimeField(default=datetime.datetime.utcnow)
