# -*- coding: utf-8 -*-
import scrapy
from kuman.items import KumanItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


# class ComicSpider(scrapy.Spider):
#     name = 'comic'
#     allowed_domains = ['kukudm.com']
#     start_urls = ['http://kukudm.com/']

#     def parse(self, response):
#     	item = KumanItem()
#     	item['image_urls'] = ['http://n.1whour.com/newkuku/2014/201412/1227a/%E6%8E%A0%E5%A4%BA%E8%80%85_%E7%AC%AC01%E8%AF%9Dv2/00017RT.jpg']
#     	yield item

        
class MycomicSpider(CrawlSpider):
    name = 'comic'
    allowed_domains = ['kukudm.com']
    start_urls = ['http://comic.kukudm.com/comiclist/2056/index.htm']
    rules = (
    	Rule(LinkExtractor(allow='2056/\d+/1.htm', deny='comic[2, 3]'), follow=True, callback='parse_item'),
    	)

    def parse_item(self, response):
        item = KumanItem()
        print(response)
        base_url = 'http://n.1whour.com/'
        part_url = response.xpath('//script/text()').re('newkuku.*?.jpg')[0]
        image_url = base_url + part_url
        item['image_urls'] = [image_url]
        yield item