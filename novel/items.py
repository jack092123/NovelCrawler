# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NovelItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    novel_type = scrapy.Field()
    name = scrapy.Field()
    image = scrapy.Field()
    time = scrapy.Field()
    url = scrapy.Field()
    
