import redis
class RedisBookIdStorage:
    def __init__(self,config):
        storage_config = config.get_json_property('RedisBookIdStorage')
        self.host = storage_config['host']
        self.port = storage_config['port']
        self.password = storage_config['password']