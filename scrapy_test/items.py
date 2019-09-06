# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyTestItem(scrapy.Item):
    name = scrapy.Field()  # 城市的名字
    url = scrapy.Field()  # 城市的链接地址


class AddressTypeItem(ScrapyTestItem):
    # def __init__(self, length, breadth, unit_cost=0, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.length = length
    #     self.breadth = breadth
    #     self.unit_cost = unit_cost

    typename = scrapy.Field()  # 地址的类别名称
    typetitle = scrapy.Field()  # 地址的类别名称
    typeurl = scrapy.Field()  # 地址的类别url


class AddressItem(AddressTypeItem):
    province = scrapy.Field()  # 省
    city = scrapy.Field()  # 市
    county = scrapy.Field()  # 县
    town = scrapy.Field()  # 镇
    address = scrapy.Field()  # 详细地址

    addressname = scrapy.Field()  # 小区的名字
    addressurl = scrapy.Field()  # 小区的详细地址url

    location = scrapy.Field()  # WGS84经纬度 需要转bd09坐标
    updatetime = scrapy.Field()  # 地址更新日期
