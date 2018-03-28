# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import log

class JiandansimagePipeline(object):
    def process_item(self, item, spider):
        return item

class JiandanPipeline(ImagesPipeline):
	def get_media_requests(self, item, info):
		for imgae_url in item['imgurl']:
			yield scrapy.Request(imgae_url)
	
