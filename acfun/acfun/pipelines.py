# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem

class MyImagesPipeline(ImagesPipeline):
	def get_media_requests(self, item, info):
		all = item['image_urls']
		for num in range(len(all[1])):
			url = all[1][num]
			dir_name = all[0]
			# print(3)
			file_name = str(num) + '.jpg'
			# name = item['image_names'][num]
			# print(url, type(url))
			yield scrapy.Request(url, meta={'dir_name': dir_name, 'file_name': file_name})
			

	# def item_completed(self, results, item, info):
	# 	pass
	def file_path(self, request, response=None, info=None):
		dir_name = request.meta['dir_name']
		# print(4)
		file_name = request.meta['file_name']
		return 'full/%s/%s' % (dir_name, file_name)
