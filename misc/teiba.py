# _*_ coding:utf-8 _*_
import requests, re
from bs4 import BeautifulSoup

def get_tieba(url):
	html = requests.get(url).text
	soup = BeautifulSoup(html, 'lxml')
	return html
url = 'https://tieba.baidu.com/p/3498761702?pn=3'
soup = get_tieba(url)
pattern = re.compile('<li class="d_name".*?target="_blank">(\w*)</a>.*?(\d*@qq.com)', re.S)
# pattern = re.compile('target="_blank">(\w*72122)')
result = re.findall(pattern, soup)



print(dict(result))