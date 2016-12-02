from common.thrift_server import ThriftServer
from storage_thrift_handler import StorageThriftHandler
from thrift_gen.book_crawler_storage_service import BookCrawlerStorageService


class StorageThriftServer:
    def __init__(self):
        storage = 'CrawlerStorage'

    def setup_and_start(self):
        thrift_server = ThriftServer('0.0.0.0', 12345, 8)
        handler = StorageThriftHandler()
        processor = BookCrawlerStorageService.Processor(handler)
        thrift_server.setup(processor)
        return thrift_server.start()
