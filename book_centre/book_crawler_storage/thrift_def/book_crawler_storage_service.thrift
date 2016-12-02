include "book_model_shared.thrift"
include "book_crawler_storage_shared.thrift"

namespace py book_crawler_storage_service

service BookCrawlerStorageService_Read {
    book_crawler_storage_shared.LibgenLatestBookIdResult get_libgen_latest_bookid();
}

service BookCrawlerStorageService_Write extends BookCrawlerStorageService_Read {
    i64 set_libgen_latest_bookid(1:required i64 bookid);
}

service BookCrawlerStorageService extends BookCrawlerStorageService_Write {
	
}