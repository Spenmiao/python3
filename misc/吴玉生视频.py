from bs4 import BeautifulSoup

import requests
from lxml import etree
urls = []
base_urs = 'http://www.scwj.net/media/video/changxiao/xingkaiyibentong/index%s.htm'
for i in range(1, 51):
	url = base_urs %i
	html = requests.get(url).content
	content = etree.HTML(html)
	rurl = content.xpath('//a[@href]')
	if not len(rurl) == 0:
		
		# info = {num : all_url}
		for x in range(len(rurl)):
			num = str(i) + '-' + str(x + 1)

			epname = ''.join(rurl[x].xpath('.//span/text()'))
			url = rurl[x].xpath('./@href')[0]
			print(epname, url)
			# url = all_url[x]
			with open('shufa.txt', 'a', encoding='utf-8') as f:
				f.write(' '.join([num, epname, url, '\n']))
		# urls.append(info)
	print(i)


# print(urls)
