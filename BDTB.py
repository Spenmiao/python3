# -*- coding:utf-8 -*- 
import urllib.request, re
from bs4 import BeautifulSoup
url = 'https://tieba.baidu.com/p/3138733512?see_lz=1&pn=1'
class BDTB:
	def __init__(self, baseurl, see_lz):
		self.baseurl = baseurl
		self.see_lz = '?see_lz='+str(see_lz)
	def getPage(self, pageNum):
		url = self.baseurl + self.see_lz + '&pn=' +str(pageNum)
		request = urllib.request.Request(url)
		respones = urllib.request.urlopen(request).read().decode()
		print(respones)
		return respones
	def getContent(self, page):
		pattern = re.compile(r'<div id="post_content.*?" class="d_post_content j_d_post_content">(.*?)</div>',re.S)
		items = re.findall(pattern, page)
		
		print('\n\n\n'.join(items))
	
baseurl = 'http://tieba.baidu.com/p/3138733512'
bdtb = BDTB(baseurl, 1)
page = bdtb.getPage(1)
soup = BeautifulSoup(page, 'html.parser')
print(soup.get_text())



