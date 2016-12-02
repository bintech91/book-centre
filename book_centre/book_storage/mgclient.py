from mongoengine import connect
from common.thrift_server import  ThriftServer

class MongodbClient:
    def __init__(self):
        self.name = "book_storage"
        self.username = "username"
        self.password = "password"
        self.host = "0.0.0.0"
        self.port = 27017

    def initialize(self, config):
        a = 0
