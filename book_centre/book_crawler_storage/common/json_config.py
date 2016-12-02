import json
import logging
import sys

try:
    from demjson import jsonlint
except ImportError:
    # Run `pip install -r requirements.txt` to fix this
    jsonlint = None


class JSONConfig:
    def __init__(self, file_path):
        print file_path
        self.logger = logging.getLogger('json_config')
        self.file_path = file_path
        self.load = {}

    def __load_file_json(self):
        # load config from json filename
        try:
            with open(self.file_path, 'rb') as data:
                self.load.update(json.load(data))
        except ValueError:
            if jsonlint:
                with open(self.file_path, 'rb') as data:
                    lint = jsonlint()
                    rc = lint.main(['-v', self.file_path])
            self.logger.critical('Error with configuration file')
            sys.exit(-1)

    def load_config(self):
        self.__load_file_json()

    def get_json_property(self, property_name):
        return self.load[property_name]
