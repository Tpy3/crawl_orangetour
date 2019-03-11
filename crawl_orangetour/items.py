# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlOrangetourItem(scrapy.Item):
    pageid = scrapy.Field()
    titleid = scrapy.Field()
    titleurl = scrapy.Field()
    title = scrapy.Field()
    days = scrapy.Field()
    departure_date = scrapy.Field()
    price = scrapy.Field()
    total = scrapy.Field()
    now = scrapy.Field()