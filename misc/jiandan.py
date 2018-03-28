import urllib.request, re
from bs4 import BeautifulSoup
#py抓取页面图片并保存到本地

#获取页面信息
def getHtml(url):
	request = urllib.request.Request(url)
	html = urllib.request.urlopen(request).read().decode()
	return BeautifulSoup(html, 'lxml')


def getImg(html):
	imglist = html('li', id=re.compile(r'comment.*?')) 
	return imglist

def saveImg(pagenum):
	url = 'http://jandan.net/ooxx/page-%s#comments/' %pagenum
	html = getHtml(url)
	list=getImg(html)
	x = 0
	for imgurl in list:
		print(x)
		for img in imgurl('a', href=re.compile(r'.*?jpg')):
			imgurl = 'http:' + img['href']
			name = str(pagenum) + '-' +str(x)
			urllib.request.urlretrieve(imgurl, r'C:\Users\Administrator\Desktop\df\\%s.jpg' %name)
			x += 1
	print(str(pagenum) +' done')

def main(pagestart, pageend):
	for num in range(pagestart, pageend):
		saveImg(num)
	
page1 = int(input(u'输入开始页: '))
page2 = int(input(u'输入结束页: '))
pagestart = min(page1, page2)
pageend = max(page1, page2)

main(pagestart, pageend)


