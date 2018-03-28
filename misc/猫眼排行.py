import re, requests
from bs4 import BeautifulSoup
import pymongo

def get_one_page(url):
	headers = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '}
	html = requests.get(url, headers = headers)
	if html.status_code == 200:
		soup = BeautifulSoup(html.text, 'lxml')
		return soup
	return 'status_error'

#content = {}
result =[]
client = pymongo.MongoClient('localhost')
maoyan = client.pachong.maoyan
for page in range(0, 10):
	url = 'http://maoyan.com/board/4?offset=%s' %(page*10)
	soup = get_one_page(url)
	lists = soup.find('div', class_='container', id='app').find_all('dd')
	for l in lists:
		


		index = l.i.get_text()
		info = l.find('div', class_='movie-item-info')
		name = info.a.get_text()
		if info.find('p', class_='star'):
			star = info.find('p', class_='star').get_text().strip()
		else:
			star = ''
		releasetime = info.find('p', class_='releasetime').get_text().strip()
		content = {
		'index' : index,
		'name' : name,
		'star' : star,
		'releasetime' : releasetime,
		}
		
		#print(content)
		maoyan.insert_one(content)
		result.append(content)
		print('完成%s' %index)


		


		
		with open('maoyan.txt', 'a', encoding='utf-8') as file:
			file.write(index + ' '+ name + 'jk ' + star + ' ' + releasetime + '\n')
#print(result)

