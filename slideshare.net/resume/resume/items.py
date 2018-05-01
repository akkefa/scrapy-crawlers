# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ResumeItem(scrapy.Item):
    """
    Parse Item
    """
    url = scrapy.Field()
    user_name = scrapy.Field()
    text = scrapy.Field()
