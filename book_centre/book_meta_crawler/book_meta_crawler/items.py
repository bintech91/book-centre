# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookMetaCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    bookid = scrapy.Field()
    title = scrapy.Field()
    volume_info = scrapy.Field()
    series = scrapy.Field()
    periodical = scrapy.Field()
    author = scrapy.Field()
    year = scrapy.Field()
    edition = scrapy.Field()
    publisher = scrapy.Field()
    city = scrapy.Field()
    pages = scrapy.Field()
    language = scrapy.Field()
    topic = scrapy.Field()
    library = scrapy.Field()
    issue = scrapy.Field()
    book_identifiers = scrapy.Field()
    commentary = scrapy.Field()
    dpi = scrapy.Field()
    color = scrapy.Field()
    cleaned = scrapy.Field()
    orientation = scrapy.Field()
    paginated = scrapy.Field()
    scanned = scrapy.Field()
    bookmarked = scrapy.Field()
    searchable = scrapy.Field()
    filesize = scrapy.Field()
    extension = scrapy.Field()
    file_checksums = scrapy.Field()
    generic = scrapy.Field()
    filename = scrapy.Field()
    visible = scrapy.Field()
    locator = scrapy.Field()
    local = scrapy.Field()
    added_timestamp = scrapy.Field()
    lastmodified_timestamp = scrapy.Field()
    cover_url = scrapy.Field()
