# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Article(scrapy.Item):
     url = scrapy.Field()
     source = scrapy.Field()
     title = scrapy.Field()
     description = scrapy.Field()
     date = scrapy.Field()
     author = scrapy.Field()
