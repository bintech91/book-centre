include "book_model_shared.thrift"

namespace py book_storage_service

service book_storage_service_read {
	book_model_shared.TBookMetaResult findBook(1:required i64 bookid);
	book_model_shared.TMapBookMetaResult findListBook(1:required list<i64> list_bookid);
	
}

service book_storage_service_write extends book_storage_service_read {

}

service book_storage_service extends book_storage_service_write {
	
}