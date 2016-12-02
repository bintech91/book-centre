import sys
sys.path.append('../thrift_gen')

from thrift_wrapper.book_crawler_storage_client import BookCrawlerStorageClient

client = BookCrawlerStorageClient()
client.set_libgen_latest_bookid(1)
