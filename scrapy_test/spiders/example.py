# -*- coding: utf-8 -*-
import scrapy

from scrapy_test.items import ScrapyTestItem, AddressTypeItem, AddressItem
from scrapy.selector import Selector


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['poi.mapbar.com']
    start_urls = ['https://poi.mapbar.com/']

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
        addr = address_path[-1].strip()
        if len(address_path) > 0:
            print("li address =", addr)

        town = ''
        addresses = ulselector.xpath("./li[contains(., '地址')]/a")
        for address in addresses:
            item_str = address.xpath("text()").get().strip()
            if msg['city'] != item_str:
                town = item_str
            print("item =", item_str)

        province = msg['province']
        city = msg['city']
        item = response.meta['item']
        print("address =", province, city, town, addr)
        addressItem = AddressItem(province=province, city=city, county=town, address=addr,
                                  addressurl=item.get('addressurl'), addressname=item.get('addressname'),
                                  typeurl=item.get('typeurl'), typename=item.get('typename'),
                                  name=item.get('name'), url=item.get('url'))
        yield addressItem

    def getaddresses(self, response):
        dl_selectors = Selector(response=response).xpath('//div[@class="sortC"]/dl')
        print("dl_selectors ", dl_selectors)
        item = response.meta['item']
        for dl_selector in dl_selectors:
            print("dl_selector ", dl_selector)
            a_selectors = dl_selector.xpath('./dd/a[@href]')
            for selector in a_selectors:
                addressname = selector.xpath("text()").get()
                addressurl = selector.xpath("@href").get()
                addressItem = AddressItem(addressurl=addressurl, addressname=addressname,
                                          typeurl=item.get('typeurl'), typename=item.get('typename'),
                                          name=item.get('name'), url=item.get('url'))
                print("getaddresses addressItem =", addressItem)
                request = response.follow(addressurl, callback=self.getaddressdetail)
                request.meta['from'] = response.url
                request.meta['item'] = addressItem
                yield request
                # yield self.getaddresstype(item)
                # yield item

    # def gettypes(self, selectors, response):

    def getaddresstype(self, response):
        row_selectors = Selector(response=response).xpath('//div[@class="isortRow"]')
        # for row_selector in row_selectors:
        if len(row_selectors) > 1:
            row_selector = row_selectors[-1].xpath('./h3')
            print("row_selector ", row_selector)
            for row in row_selector:
                if "小区" not in row.get() and "商务" not in row.get():
                    continue
                # yield self.gettypes(, response)
                selectors = row.xpath('following-sibling::div[1]')
                item = response.meta['item']
                print("selectors ", selectors)
                a_selectors = selectors.xpath('./a[@href]')
                print("a_selectors ", a_selectors)
                for selector in a_selectors:
                    typeurl = selector.xpath('@href').get()
                    type = selector.xpath('text()').get()
                    typeItem = AddressTypeItem(typeurl=typeurl, typename=type, name=item.get('name'),
                                               url=item.get('url'))
                    print("gettypes typeItem=", typeItem)
                    request = response.follow(typeurl, callback=self.getaddresses)
                    request.meta['from'] = response.url
                    request.meta['item'] = typeItem
                    yield request

            # # 只获取小区数据
            # house_selectors = row_selector.xpath('./h3[contains(., "小区")]/following-sibling::div[1]')
            # business_selectors = row_selector.xpath('./h3[contains(., "商务")]/following-sibling::div[1]')
            # self.gettypes(house_selectors)
            # self.gettypes(business_selectors)

    # def getcity(self, response):

    def parse(self, response):
        print("parse url:", response)
        dd_selectors = Selector(response=response).xpath('//dl[contains(@class, "city_list")]/dd')
        for dd_selector in dd_selectors:
            print("dd_selector ", dd_selector)
            a_selectors = dd_selector.xpath('a[@href]')
            for selector in a_selectors:
                item = ScrapyTestItem()  # 实例化一个 DmozItem 类
                item['name'] = selector.xpath("text()").get()
                item['url'] = selector.xpath("@href").get()
                print("selector item =", item)
                request = response.follow(item['url'], callback=self.getaddresstype)
                request.meta['from'] = response.url
                request.meta['item'] = item
                yield request

# json.dumps(d, ensure_ascii=False, encoding='utf-8'))
