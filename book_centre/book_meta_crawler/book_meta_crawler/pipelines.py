# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

from spiders import book_storage
import items

class MongoDBPipleline(object):
    def __init__(self):
        self.name_pipelines = "MongoDBPipeline"

    def process_item(self, item, spider):
        spider.logger.debug("process_item")
        if isinstance(item, items.BookMetaCrawlerItem):
            try:
                spider.connect_storage()
                storage_book_meta = book_storage.MBookMeta()
                if item["bookid"]:
                    storage_book_meta.bookid = item["bookid"]
                if item["title"]:
                    storage_book_meta.title = item["title"]
                else:
                    storage_book_meta.title = "MISS"
                if item["volume_info"]:
                    storage_book_meta.volume_info = item["volume_info"]
                if item["series"]:
                    storage_book_meta.series = item["series"]
                if item["periodical"]:
                    storage_book_meta.periodical = item["periodical"]
                if item["author"]:
                    storage_book_meta.author = item["author"]
                if item["year"]: storage_book_meta.year = item["year"]
                if item["edition"]:
                    storage_book_meta.edition = item["edition"]
                if item["publisher"]:
                    storage_book_meta.publisher = item["publisher"]
                if item["city"]:
                    storage_book_meta.city = item["city"]
                if item["pages"]:
                    storage_book_meta.pages = item["pages"]
                if item["language"]:
                    storage_book_meta.language = item["language"]
                if item["topic"]:
                    storage_book_meta.topic = item["topic"]
                if item["library"]:
                    storage_book_meta.library = item["library"]
                if item["issue"]:
                    storage_book_meta.issue = item["issue"]

                # book identifiers
                storage_book_meta.book_identifiers = book_storage.MBookIdentifier()
                if item["book_identifiers"]["identifier"]:
                    storage_book_meta.book_identifiers.identifier = item["book_identifiers"]["identifier"]
                if item["book_identifiers"]["issn"]:
                    storage_book_meta.book_identifiers.issn = item["book_identifiers"]["issn"]
                if item["book_identifiers"]["asin"]:
                    storage_book_meta.book_identifiers.asin = item["book_identifiers"]["asin"]
                if item["book_identifiers"]["udc"]:
                    storage_book_meta.book_identifiers.udc = item["book_identifiers"]["udc"]
                if item["book_identifiers"]["lbc"]:
                    storage_book_meta.book_identifiers.lbc = item["book_identifiers"]["lbc"]
                if item["book_identifiers"]["ddc"]:
                    storage_book_meta.book_identifiers.ddc = item["book_identifiers"]["ddc"]
                if item["book_identifiers"]["lcc"]:
                    storage_book_meta.book_identifiers.lcc = item["book_identifiers"]["lcc"]
                if item["book_identifiers"]["doi"]:
                    storage_book_meta.book_identifiers.doi = item["book_identifiers"]["doi"]
                if item["book_identifiers"]["googlebookid"]:
                    storage_book_meta.book_identifiers.googlebookid = item["book_identifiers"]["googlebookid"]
                if item["book_identifiers"]["openlibraryid"]:
                    storage_book_meta.book_identifiers.openlibraryid = item["book_identifiers"]["openlibraryid"]

                if item["commentary"]:
                    storage_book_meta.commentary = item["commentary"]
                if item["dpi"]:
                    storage_book_meta.dpi = item["dpi"]
                if item["color"]:
                    storage_book_meta.color = item["color"]
                if item["cleaned"]:
                    storage_book_meta.cleaned = item["cleaned"]
                if item["orientation"]:
                    storage_book_meta.orientation = item["orientation"]
                if item["paginated"]:
                    storage_book_meta.paginated = item["paginated"]
                if item["scanned"]:
                    storage_book_meta.scanned = item["scanned"]
                if item["bookmarked"]:
                    storage_book_meta.bookmarked = item["bookmarked"]
                if item["searchable"]:
                    storage_book_meta.searchable = item["searchable"]
                if item["filesize"]:
                    storage_book_meta.filesize = item["filesize"]
                if item["extension"]:
                    storage_book_meta.extension = item["extension"]

                # book file checksums
                storage_book_meta.file_checksums = book_storage.MBookChecksum()
                if item["file_checksums"]["md5"]:
                    storage_book_meta.file_checksums.md5 = item["file_checksums"]["md5"]
                if item["file_checksums"]["crc32"]:
                    storage_book_meta.file_checksums.crc32 = item["file_checksums"]["crc32"]
                if item["file_checksums"]["aich"]:
                    storage_book_meta.file_checksums.aich = item["file_checksums"]["aich"]
                if item["file_checksums"]["sha1"]:
                    storage_book_meta.file_checksums.sha1 = item["file_checksums"]["sha1"]
                if item["file_checksums"]["tth"]:
                    storage_book_meta.file_checksums.tth = item["file_checksums"]["tth"]

                if item["generic"]:
                    storage_book_meta.generic = item["generic"]
                if item["visible"]:
                    storage_book_meta.visible = item["visible"]
                if item["locator"]:
                    storage_book_meta.locator = item["locator"]
                if item["local"]:
                    storage_book_meta.local = item["local"]
                if item["added_timestamp"]:
                    storage_book_meta.added_timestamp = item["added_timestamp"]
                if item["lastmodified_timestamp"]:
                    storage_book_meta.lastmodified_timestamp = item[
                        "lastmodified_timestamp"]
                if item["cover_url"]:
                    storage_book_meta.cover_url = item["cover_url"]

                storage_book_meta.downloaded = 0
                storage_book_meta.save()
            except Exception, ex:
                spider.logger.error("process_item " + str(item["bookid"]) + ex.message)
        return item