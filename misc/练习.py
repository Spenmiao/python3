import requests
from lxml import etree
from bs4 import BeautifulSoup
#小说去br空格
rq = requests.get('https://www.biquge5200.com/52_52542/153188126.html').content
# cont= etree.HTML(html).xpath('//div[@id="content"]/text()')
# print([x for x in cont] )
soup = BeautifulSoup(rq, 'lxml')
# print(soup.prettify())
print(soup.find('div', id='content').get_text('\n', strip=True))
