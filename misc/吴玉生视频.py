from bs4 import BeautifulSoup

import requests
from lxml import etree
urls = []

base_urs = 'http://www.scwj.net/media/video/changxiao/xingkaiyibentong/index%s.htm'
for i in range(1, 51):
	url = base_urs %i
	html = requests.get(url).content
	content = etree.HTML(html)
	rurl = content.xpath('//a/@href')
	num = str(i) + '-' + str(len(rurl))
	info = {num : rurl}
	urls.append(info)


print(urls)
