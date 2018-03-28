from lxml import etree
import requests, re
from bs4 import BeautifulSoup
for num in range(1, 8):
	html = requests.get('http://webapi.aixifan.com/query/article/list?pageNo=%s&size=10&realmIds=5&originalOnly=false&orderType=1&periodType=-1&filterTitleImage=true' %num).json()
	# etree = etree.HTML(html.content)
	# contant = etree.xpath('//div[@class="article-list"]//div[contains(@class, "article-item")]//div[2]//@href')
	# # text = contant.xpath('//div[2]//text()')
	# print(contant)
	# soup = BeautifulSoup(html.content, 'lxml')
	# alltext = soup.find_all('div', atts={'data-id' : 4276090})
	# for text in alltext:
	# 	# te = text.find('div', class_='act-cont-top clearfix').a
	# 	# num = text.find('div', class_=re.compile('atc-left'))
	# 	# print(num)
	# 	print(text)
	allinfo = html['data']['articleList']
	for info in allinfo:
			description = info['description']
			title = info['title']
			print(title, '\n', description, '\n\n')