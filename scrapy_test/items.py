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
    province = scrapy.Field()  # 省
    city = scrapy.Field()  # 市
    county = scrapy.Field()  # 县
    town = scrapy.Field()  # 镇
    address = scrapy.Field()  # 详细地址

    cityurl = scrapy.Field()  # 城市的链接地址
    cityname = scrapy.Field()  # 城市的名字
    typetitle = scrapy.Field()  # 地址的类别名称
    typeurl = scrapy.Field()  # 地址的类别url
    addressname = scrapy.Field()  # 小区的名字
    addressurl = scrapy.Field()  # 小区的详细地址url

    location = scrapy.Field()  # WGS84经纬度 需要转bd09坐标
    updatetime = scrapy.Field()  # 地址更新日期



