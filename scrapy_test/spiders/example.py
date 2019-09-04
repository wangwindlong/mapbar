# -*- coding: utf-8 -*-
import scrapy

from scrapy_test.items import ScrapyTestItem
from scrapy.selector import Selector


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['poi.mapbar.com']
    start_urls = ['https://poi.mapbar.com/wuxi/MAPIFPCPTNFWQOHPTITOC']

    def getdict(self, item):
        result = dict()
        s = item.split("=")
        result[s[0]] = s[1]
        return result

    def getaddressdetail(self, response):
        selector = Selector(response=response)
        location = selector.xpath('//head/meta[re:test(@name, "location")]//@content').get().strip()
        print("location=", location)
        details = location.split(";")
        msg = dict()
        for detail in details:
            msg = {**msg, **self.getdict(detail)}
        print("msg =", msg)
        ulselector = selector.css('.POI_ulA')
        updatetime = ulselector.xpath("./li[1]/text()").re_first(r'时间：\s*(.*)')
        print("updatetime =", updatetime)

        ul_path = ulselector.xpath('./li[contains(., "地址")]')
        address_path = ul_path.xpath('text()').getall()
        if len(address_path) > 0:
            print("li address =", address_path[-1].strip())

        town = ''
        address = ulselector.xpath("./li[contains(., '地址')]/a")
        for item in address:
            item_str = item.xpath("text()").get().strip()
            if msg['city'] != item_str:
                town = item_str
            print("item =", item_str)

        province = msg['province']
        city = msg['city']
        print("address =", province, city, town, address_path[-1].strip())

    def getaddresses(self, cityurl):
        pass

    def getaddresstype(self, cityItem):
        pass

    def getcity(self, response):
        # Get all the <a> tags
        dd_selectors = Selector(response=response).xpath('//dl[contains(@class, "city_list")]/dd')
        # Loop on each tag
        for dd_selector in dd_selectors:
            print("dd_selector ", dd_selector)
            a_selectors = dd_selector.xpath('a[@href]')
            for selector in a_selectors:
                item = ScrapyTestItem()  # 实例化一个 DmozItem 类
                item['name'] = selector.xpath("text()").get()
                item['url'] = selector.xpath("@href").get()
                print("selector item =", item)
                # yield self.getaddresstype(item)
                yield item

    def parse(self, response):
        """ Main function that parses downloaded pages """
        print("parse url:", response)
        # self.getcity(response)
        self.getaddressdetail(response)

# json.dumps(d, ensure_ascii=False, encoding='utf-8'))
# json.loads(jd, encoding='utf-8')
