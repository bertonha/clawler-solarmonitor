# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SolarmonitorItem(scrapy.Item):
    date = scrapy.Field()
    type = scrapy.Field()

    image_urls = scrapy.Field()
    images = scrapy.Field()

    number = scrapy.Field()
    location = scrapy.Field()
    hale_class = scrapy.Field()
    mcintosh_class = scrapy.Field()
    area = scrapy.Field()
    number_of_spots = scrapy.Field()
    flares = scrapy.Field()
