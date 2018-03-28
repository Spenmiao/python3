# -*- coding: utf-8 -*-
import scrapy, json
from acfun.items import AcfunItem


class AfunSpiderSpider(scrapy.Spider):
    name = 'afun_spider'
    allowed_domains = ['acfun.cn']
    start_urls = ['http://webapi.aixifan.com/query/article/list?pageNo=1&size=10&realmIds=15&originalOnly=false&orderType=1&periodType=-1&filterTitleImage=true']
    base_url = 'http://www.acfun.cn/a/ac'

    def parse(self, response):
        item = AcfunItem()
        # item['image_urls'] = response.xpath('//div[@class="article-content"]/p/img/@src').extract()
        # item['image_names'] = [(str(x) + '.png') for x in range(len(item['image_urls']))]
        # print(item['image_names'])
        articleList = json.loads(response.text)['data']['articleList']
        for x in range(len(articleList)):
            id = articleList[x].get('id')
            title = articleList[x].get('title').strip()
            # print(1)
            print(title)
            next_url = self.base_url + str(id)
            yield scrapy.Request(next_url, meta={'title': title}, callback= self.parse1)


    def parse1(self, response):
    	item = AcfunItem()
    	dir_name = response.meta['title']
    	img_urls = response.xpath('//div[@class="article-content"]/p/img/@src').extract()
    	item['image_urls'] = [dir_name, img_urls]
    	# print(2)
    	# print(dir_name)
    	yield item

        
        
