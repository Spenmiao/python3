from bs4 import BeautifulSoup
import urllib.request, re

def getpage(url):
	request = urllib.request.Request(url)
	response = urllib.request.urlopen(request).read().decode()

	soup = BeautifulSoup(response, 'lxml')
	return soup

def parsepage_geturl(url):
	soup = getpage(url)
	acfunlist = []
	file = open('acfun.txt', 'a')
	for item in soup('a', title=re.compile('.*?评论.*?')):
		href = item['href']
		url = 'http://www.acfun.cn' + href 
		acfunlist.append(url)
	return acfunlist
	
def wenzhangpage(url):
	soup = getpage(url)
	for item in soup('div', id='area-player'):
		for it in item('p'):
			print(it.get_text())

def main():
	start_url = 'http://www.acfun.cn/v/list74/index.htm'
	urllsit = parsepage_geturl(start_url)
	for url in urllsit:
		wenzhangpage(url)
main()