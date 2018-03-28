import re, urllib.request
from bs4 import BeautifulSoup

class QiuShi:
	def getHtml(self, url):
		self.url = url
		user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
		headers = {'User-Agent':user_agent}
		request = urllib.request.Request(url, headers = headers)
		response = urllib.request.urlopen(request).read().decode()
		return BeautifulSoup(response, 'lxml')

	def getContent(self, html):
		self.html = html
		contents = self.html('div', class_=re.compile(r'article block.*?'))
		contlist = [] 
		for content in contents:
			hasImg = content('div', class_='thumb')
			if not hasImg:
				cont = content('a', class_='contentHerf')[0].get_text(strip=True)
				print(cont)
				contlist.append(cont)
		return ' ' 

		

		return content

qiushi = QiuShi()

url = 'https://www.qiushibaike.com/'
html = qiushi.getHtml(url)
content = qiushi.getContent(html)
print(content)