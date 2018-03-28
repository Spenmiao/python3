import requests, time, random
from bs4 import BeautifulSoup

class DownloadNovie:
	"""docstring for DownloadNovie"""
	def __init__(self):
		self.name = []
		self.urls = []
		self.num = 0
	
	def get_target(self, targeturl):
		html = requests.get(targeturl).content
		soup = BeautifulSoup(html, 'lxml')
		
		listmain = soup.find('div', class_='listmain').find_all('dd')
		for li in listmain:
			self.urls.append('http://www.biqukan.com' + li.a['href'])
			self.name.append(li.a.get_text())
			self.num = len(self.name)

	def get_content(self, url, name, path):
		try:
			response = requests.get(url).content
			soup = BeautifulSoup(response, 'lxml')
			text = soup.find('div', class_='showtxt').get_text().replace('\xa0'*8, '\n\n')
			# print(text)
			with open(path, 'a', encoding='utf-8') as dn:
				dn.write(name + '\n')
				dn.write(text + '\n\n')
		except Exception as er:
			print(er)


	
		


if __name__ == "__main__":
	dn = DownloadNovie()
	dn.get_target('http://www.biqukan.com/1_1094/')
	print(dn.urls, dn.name)
	# print(dn.get_content('http://www.biqukan.com/1_1094/5403177.html', 'yizhang','一念永恒.txt'))
	for num in range(dn.num):
		dn.get_content(dn.urls[num], dn.name[num], '一念永恒.txt', )
		print(str(num) + '完成' )
		ti = random.choice(range(10))
		time.sleep(ti / 10)
