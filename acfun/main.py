from scrapy import cmdline
import scrapy
from scrapy.pipelines.images import ImagesPipeline
# from scrapy.contrib.pipeline.images import ImagesPipeline
# cmdline.execute('scrapy crawl afun_spider'.split(' '))

cmdline.execute('scrapy crawl afun_spider --nolog'.split(' '))

# help(ImagesPipeline.__class__)
# print(dir(ImagesPipeline))
# print(scrapy.__file__)
# help(ImagesPipeline)
