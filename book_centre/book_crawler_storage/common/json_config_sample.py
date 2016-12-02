from json_config import JSONConfig

config = JSONConfig("json_config_sample.json")
config.load_config()

storage = config.get_json_property("mongodb_book_storage")

host = storage['host']
print(host)