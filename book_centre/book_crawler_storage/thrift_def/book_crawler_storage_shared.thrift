include "book_model_shared.thrift"

namespace py book_crawler_storage_shared

struct LibgenLatestBookIdResult {
    1:required i16 error,
    2:required i64 bookid,
}

