# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy import Request
import json
import mongoengine
import book_storage
import urllib2
from book_meta_crawler import items


class LibgenSpider(scrapy.Spider):
    name = "libgen"

    allowed_domains = ["libgen.io"]

    url_meta_template = "http://libgen.io/json.php?ids=%s&fields=id,title,volumeinfo,series,periodical,author,year,edition,publisher,city,pages,language,topic,library,issue,identifier,issn,asin,udc,lbc,ddc,lcc,doi,googlebookid,openlibraryid,commentary,dpi,color,cleaned,orientation,paginated,scanned,bookmarked,searchable,filesize,extension,md5,crc32,aich,sha1,tth,generic,visible,locator,local,timeadded,timelastmodified,coverurl"

    url_get_download_template = "http://libgen.io/ads.php?md5=%s"

    url_download_template = "http://libgen.io%s"

    url_first_request = "http://libgen.io/search.php?mode=last"

    def connect_storage(self):
        mongoengine.connect("libgen_crawl_storage")

    def start_requests(self):
        self.connect_storage()
        yield scrapy.Request(url=self.url_first_request, callback=self.parse_latest_bookid, priority=0)

    def parse_latest_bookid(self, response):
        # get latest libgen bookid
        selector = Selector(response)
        libgen_latest_bookid = int(selector.xpath("/html/body/table[3]/tr[2]/td[1]/text()").extract_first())

        # get latest storage bookid
        storage_latest_book_meta_item = \
            book_storage.MBookMeta.objects.only("bookid").order_by("-bookid").limit(-1).first()

        storage_latest_bookid = 0
        if storage_latest_book_meta_item is None:
            storage_latest_bookid = 1
        else:
            storage_latest_bookid = storage_latest_book_meta_item.bookid

        # calculate the range of ids to crawl for metadata
        crawl_range = 0
        if libgen_latest_bookid - storage_latest_bookid > 100:
            crawl_range = 100
        else:
            crawl_range = libgen_latest_bookid - storage_latest_bookid

        crawl_meta_ids = ""
        for crawl_bookid in range(storage_latest_bookid, storage_latest_bookid + crawl_range):
            if crawl_bookid == (storage_latest_bookid):
                crawl_meta_ids = str(crawl_bookid) + ","
            elif crawl_bookid == (storage_latest_bookid + crawl_range - 1):
                crawl_meta_ids = crawl_meta_ids + str(crawl_bookid)
            else:
                crawl_meta_ids = crawl_meta_ids + str(crawl_bookid) + ","

        crawl_meta_url = self.url_meta_template % crawl_meta_ids
        request = Request(url=crawl_meta_url, callback=self.parse_meta, priority=1)
        yield request

    def parse_meta(self, response):
        self.log("start parse_meta")
        json_content = json.loads(response.body)
        for book_meta in json_content:
            book_meta_item = items.BookMetaCrawlerItem()
            book_meta_item["bookid"] = book_meta["id"]
            book_meta_item["title"] = book_meta["title"]
            book_meta_item["volume_info"] = book_meta["volumeinfo"]
            book_meta_item["series"] = book_meta["series"]
            book_meta_item["periodical"] = book_meta["periodical"]
            book_meta_item["author"] = book_meta["author"]
            book_meta_item["year"] = book_meta["year"]
            book_meta_item["edition"] = book_meta["edition"]
            book_meta_item["publisher"] = book_meta["publisher"]
            book_meta_item["city"] = book_meta["city"]
            book_meta_item["pages"] = book_meta["pages"]
            book_meta_item["language"] = book_meta["language"]
            book_meta_item["topic"] = book_meta["topic"]
            book_meta_item["library"] = book_meta["library"]
            book_meta_item["issue"] = book_meta["issue"]
            book_meta_item["book_identifiers"] = {}
            book_meta_item["book_identifiers"]["identifier"] = book_meta["identifier"]
            book_meta_item["book_identifiers"]["issn"] = book_meta["issn"]
            book_meta_item["book_identifiers"]["asin"] = book_meta["asin"]
            book_meta_item["book_identifiers"]["udc"] = book_meta["udc"]
            book_meta_item["book_identifiers"]["lbc"] = book_meta["lbc"]
            book_meta_item["book_identifiers"]["ddc"] = book_meta["ddc"]
            book_meta_item["book_identifiers"]["lcc"] = book_meta["lcc"]
            book_meta_item["book_identifiers"]["doi"] = book_meta["doi"]
            book_meta_item["book_identifiers"]["googlebookid"] = book_meta["googlebookid"]
            book_meta_item["book_identifiers"]["openlibraryid"] = book_meta["openlibraryid"]
            book_meta_item["commentary"] = book_meta["commentary"]
            book_meta_item["dpi"] = book_meta["dpi"]
            book_meta_item["color"] = book_meta["color"]
            book_meta_item["cleaned"] = book_meta["cleaned"]
            book_meta_item["orientation"] = book_meta["orientation"]
            book_meta_item["paginated"] = book_meta["paginated"]
            book_meta_item["scanned"] = book_meta["scanned"]
            book_meta_item["bookmarked"] = book_meta["bookmarked"]
            book_meta_item["searchable"] = book_meta["searchable"]
            book_meta_item["filesize"] = book_meta["filesize"]
            book_meta_item["extension"] = book_meta["extension"]
            book_meta_item["file_checksums"] = {}
            book_meta_item["file_checksums"]["md5"] = book_meta["md5"]
            book_meta_item["file_checksums"]["crc32"] = book_meta["crc32"]
            book_meta_item["file_checksums"]["aich"] = book_meta["aich"]
            book_meta_item["file_checksums"]["sha1"] = book_meta["sha1"]
            book_meta_item["file_checksums"]["tth"] = book_meta["tth"]
            book_meta_item["generic"] = book_meta["generic"]
            book_meta_item["visible"] = book_meta["visible"]
            book_meta_item["locator"] = book_meta["locator"]
            book_meta_item["local"] = book_meta["local"]
            book_meta_item["added_timestamp"] = book_meta["timeadded"]
            book_meta_item["lastmodified_timestamp"] = book_meta["timelastmodified"]
            book_meta_item["cover_url"] = book_meta["coverurl"]
            self.logger.info(book_meta["title"])
            yield book_meta_item

        # after parse and update all meta, check again for latestbookid
        yield scrapy.Request(url=self.url_first_request, callback=self.parse_latest_bookid, priority=0,
                             dont_filter=True)

    def parse_download(self, response):
        self.log("start parse_download")
        selector = Selector(response)
        download_uri = selector.css("a").xpath("@href").extract()

        book_download_url = self.url_download_template % download_uri

        response = urllib2.urlopen(book_download_url)
        book = response.read()
