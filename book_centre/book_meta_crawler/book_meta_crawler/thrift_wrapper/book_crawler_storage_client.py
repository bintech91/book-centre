from thrift import Thrift

import sys
sys.path.append("/bintech/projects/book-centre/book_centre/book_meta_crawler/thrift_gen")
from book_meta_crawler.thrift_wrapper.book_crawler_storage_client import BookCrawlerStorageClient
from thrift_gen.book_crawler_storage_shared.ttypes import *
from thrift_gen.book_crawler_storage_service.BookCrawlerStorageService import Client
from book_meta_crawler.common.thrift_client import ThriftClient

class BookCrawlerStorageClient:
    def __init__(self):
        self.__client_factory = ThriftClient('0.0.0.0', 12345, Client, 3)

    def get_libgen_latest_bookid(self):
        for index in range(0, self.__client_factory.get_num_retries()):
            try:
                client = self.__client_factory.get_client()
                if client is None:
                    continue
                last_bookid_result = client.get_libgen_latest_bookid()
                return last_bookid_result
            except Thrift.TException, tx:
                continue
        return None

    def set_libgen_latest_bookid(self, bookid):
        for index in range(0, self.__client_factory.get_num_retries()):
            try:
                client = self.__client_factory.get_client()
                client.set_libgen_latest_bookid(1)
                return
            except Thrift.TException, tx:
                continue
        return 0

