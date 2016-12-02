# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy import Request
import json
import mongoengine
import book_storage
import book_storage
import urllib2
from book_content_crawler import items
from mongoengine.context_managers import switch_db


class LibgenSpider(scrapy.Spider):
    name = "libgen"

    allowed_domains = ["libgen.io"]

    save_path = "/data/book/libgen/"

    url_get_download_template = "http://libgen.io/ads.php?md5=%s"

    url_download_template = "http://libgen.io%s"

    def connect_crawl_storage(self):
        mongoengine.connect("libgen_crawl_storage")
        mongoengine.register_connection("book_storage", "book_storage")

    def connect_book_storage(self):
        mongoengine.connect("book_storage")

    def get_book_crawl_meta(self):
        self.connect_crawl_storage()

        # get latest crawl bookid , and not downloaded
        crawl_book_meta = book_storage.MBookMeta.objects(downloaded=0).order_by("-bookid").limit(-1).first()

        return crawl_book_meta

    def build_book_name(self, title, md5, extension):
        name = title.replace(" ", "_")
        name = name + "_.-._" + md5 + "." + extension
        return name

    def start_requests(self):
        # get crawl_book_meta to download
        crawl_book_meta = self.get_book_crawl_meta()

        self.logger.info("Download BookId " + str(crawl_book_meta.bookid))

        # build first request
        crawl_downloaded_url = self.url_get_download_template % crawl_book_meta.file_checksums.md5

        request = scrapy.Request(url=crawl_downloaded_url, callback=self.parse_download, priority=0)

        request.meta["crawl_book_meta"] = crawl_book_meta

        yield request

    def parse_download(self, response):
        self.logger.info("start parse_download")
        selector = Selector(response)
        download_uri = selector.css("a").xpath("@href").extract()

        book_download_url = self.url_download_template % download_uri[1]

        crawl_book_meta = response.meta["crawl_book_meta"]
        book_name = self.build_book_name(crawl_book_meta.title, crawl_book_meta.file_checksums.md5,
                                         crawl_book_meta.extension)

        try:
            # Download book from HTTP URL
            self.logger.debug("Download URL " + book_download_url)
            download_response = urllib2.urlopen(book_download_url)
            book_content = download_response.read()

            file = open(self.save_path + book_name, 'w+')
            file.write(book_content)
            file.close()

            book_storage.MBookMeta.objects(bookid=crawl_book_meta.bookid).update_one(set__downloaded=1)
            crawl_book_meta.reload()

            latest_bookid = 0
            book_meta = book_storage.MBookMeta()
            with switch_db(book_storage.MBookMeta, "book_storage") as book_storage.MBookMeta:
                latest_book_item = book_storage.MBookMeta.objects.only("bookid").order_by("-bookid").limit(-1).first()
                if latest_book_item is None:
                    latest_bookid = 0
                else:
                    latest_bookid = latest_book_item.bookid

                book_meta.bookid = latest_bookid + 1
                book_meta.title = crawl_book_meta.title
                book_meta.volume_info = crawl_book_meta.volume_info
                book_meta.series = crawl_book_meta.series
                book_meta.periodical = crawl_book_meta.periodical
                book_meta.author = crawl_book_meta.author
                book_meta.edition = crawl_book_meta.edition
                book_meta.publisher = crawl_book_meta.publisher
                book_meta.city = crawl_book_meta.city
                book_meta.pages = crawl_book_meta.pages
                book_meta.language = crawl_book_meta.language
                book_meta.topic = crawl_book_meta.topic
                book_meta.library = crawl_book_meta.library
                book_meta.issue = crawl_book_meta.issue

                # book identifiers
                book_meta.book_identifiers = book_storage.MBookIdentifier()
                book_meta.book_identifiers.identifier = crawl_book_meta.book_identifiers.identifier
                book_meta.book_identifiers.issn = crawl_book_meta.book_identifiers.issn
                book_meta.book_identifiers.asin = crawl_book_meta.book_identifiers.asin
                book_meta.book_identifiers.udc = crawl_book_meta.book_identifiers.udc
                book_meta.book_identifiers.lbc = crawl_book_meta.book_identifiers.lbc
                book_meta.book_identifiers.ddc = crawl_book_meta.book_identifiers.ddc
                book_meta.book_identifiers.lcc = crawl_book_meta.book_identifiers.lcc
                book_meta.book_identifiers.doi = crawl_book_meta.book_identifiers.doi
                book_meta.book_identifiers.googlebookid = crawl_book_meta.book_identifiers.googlebookid
                book_meta.book_identifiers.openlibraryid = crawl_book_meta.book_identifiers.openlibraryid

                book_meta.commentary = crawl_book_meta.commentary
                book_meta.dpi = crawl_book_meta.dpi
                book_meta.color = crawl_book_meta.color
                book_meta.cleaned = crawl_book_meta.cleaned
                book_meta.orientation = crawl_book_meta.orientation
                book_meta.paginated = crawl_book_meta.paginated
                book_meta.scanned = crawl_book_meta.scanned
                book_meta.bookmarked = crawl_book_meta.bookmarked
                book_meta.searchable = crawl_book_meta.searchable
                book_meta.filesize = crawl_book_meta.filesize
                book_meta.extension = crawl_book_meta.extension

                # book file checksums
                book_meta.file_checksums = book_storage.MBookChecksum()
                book_meta.file_checksums.md5 = crawl_book_meta.file_checksums.md5
                book_meta.file_checksums.crc32 = crawl_book_meta.file_checksums.crc32
                book_meta.file_checksums.aich = crawl_book_meta.file_checksums.aich
                book_meta.file_checksums.sha1 = crawl_book_meta.file_checksums.sha1
                book_meta.file_checksums.tth = crawl_book_meta.file_checksums.tth

                book_meta.generic = crawl_book_meta.generic
                book_meta.visible = crawl_book_meta.visible
                book_meta.locator = crawl_book_meta.locator
                book_meta.local = crawl_book_meta.local
                book_meta.added_timestamp = crawl_book_meta.added_timestamp
                book_meta.lastmodified_timestamp = crawl_book_meta.lastmodified_timestamp
                book_meta.cover_url = crawl_book_meta.cover_url

                book_meta.downloaded = 1
                book_meta.save()

            print "BookMeta book_meta " + str(book_meta.bookid)

            with switch_db(book_storage.MBookStorage, db_alias="book_storage") as book_storage.MBookStorage:
                book_storage_item = book_storage.MBookStorage()
                book_storage_item.storage_bookid = book_meta.bookid
                book_storage_item.local_storage = self.save_path + book_name
                book_storage_item.save()
        except Exception, ex:
            self.logger.error("book_content_crawler exception " + str(ex.message))

        # get crawl_book_meta to download
        next_crawl_book_meta = self.get_book_crawl_meta()

        self.logger.info("Download BookId " + str(next_crawl_book_meta.bookid))

        # build first request
        crawl_downloaded_url = self.url_get_download_template % next_crawl_book_meta.file_checksums.md5

        next_request = scrapy.Request(url=crawl_downloaded_url, callback=self.parse_download, priority=0,
                                      dont_filter=True)

        next_request.meta["crawl_book_meta"] = next_crawl_book_meta

        yield next_request
