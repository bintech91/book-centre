namespace py book_model_shared

struct TBookIdentifier {
    1:optional string identifier,
    2:optional string issn,
    3:optional string asin,
    4:optional string udc,
    5:optional string lbc,
    6:optional string ddc,
    7:optional string lcc,
    8:optional string doi,
    9:optional string google_book_id,
    10:optional string open_library_id,
}

struct TBookChecksum {
    1:optional string md5,
    2:optional string crc32,
    3:optional string edonkey,
    4:optional string aich,
    5:optional string sha1,
    6:optional string tth,
}

struct TBookMeta {
    1:required i64 bookid,
    2:required string title,
    3:optional string volume_info,
    4:optional string series,
    5:optional string periodical,
    6:optional string author,
    7:optional string year,
    8:optional string edition,
    9:optional string publisher,
    10:optional string city,
    11:optional i64 pages,
    12:optional string language,
    13:optional string topic,
    14:optional string library,
    15:optional string issue,
    16:optional TBookIdentifier book_identifiers,
    17:optional string commentary,
    18:optional i32 dpi,
    19:optional bool color,
    20:optional bool cleaned,
    21:optional bool orientation,
    22:optional bool paginated,
    23:optional bool scanned,
    24:optional bool bookmarked,
    25:optional bool searchable,
    26:optional i64 filesize,
    27:optional string extension,
    28:optional TBookChecksum file_checksums,
    29:optional string generic,
    30:optional string filename,
    31:optional string visible,
    32:optional string locator,
    33:optional i32 local,
    34:optional i64 added_timestamp,
    35:optional i64 lastmodified_timestamp,
    36:optional string cover_url,
}


struct TBookStorage {

}


struct TBookMetaResult {
	1:required i32 error,
	2:required TBookMeta book_meta,
}

struct TMapBookMetaResult {
	1:required i32 error,
	2:required map<i64, TBookMeta> map_book_meta,
}


