# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyTestItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    url = scrapy.Field()


class AddressTypeItem(scrapy.Item):
    # define the fields for your item here like:
    cityname = scrapy.Field()
    cityurl = scrapy.Field()

    typename = scrapy.Field()
    typetitle = scrapy.Field()
    typeurl = scrapy.Field()


class AddressItem(scrapy.Item):
    # define the fields for your item here like:
    cityname = scrapy.Field()

    typename = scrapy.Field()
    typetitle = scrapy.Field()
    typeurl = scrapy.Field()


class AddressDetailItem(AddressItem):
    # define the fields for your item here like:
    cityname = scrapy.Field()

    typename = scrapy.Field()
    typetitle = scrapy.Field()
    typeurl = scrapy.Field()
