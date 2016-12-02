from common.thrift_server import ThriftServer

class StorageThriftServer():
    def __init__(self, config):
        host = config.get_json_property("StorageThriftServer")


