from mongoengine import connect
import json

class BookStorageMGClient:

    def __init__(self):
        self.name = "book_storage"
        self.username = "username"
        self.password = "password"
        self.host = "0.0.0.0"
        self.port = 27017

    def initialize(self):
        a = 9
