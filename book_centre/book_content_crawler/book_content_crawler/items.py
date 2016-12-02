# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookContentCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    book_name = scrapy.Field()
    book_content = scrapy.Field()
    book_meta = scrapy.Field()
    book_path = scrapy.Field()