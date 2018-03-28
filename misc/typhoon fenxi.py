# _*_ encoding:utf_8 _*_
import requests, json
from bs4 import BeautifulSoup

def get_typhoonlist(year):
	url = 'http://typhoon.zjwater.gov.cn/Api/Typhoonlist/' + str(year)
	html = requests.get(url).text
	tylist = json.loads(html)
	return tylist
def get_typhooninfo(tfid):
	url = 'http://typhoon.zjwater.gov.cn/Api/Typhooninfo/' + str(tfid)
	html = requests.get(url).text 
	tyinfo = json.loads(html)
	return tyinfo


# print(get_typhoonlist(2017))
# print(get_typhooninfo(201702))
tylist = get_typhoonlist(2017)
tfids = [id['tfid'] for id in tylist]

pointlists = {}
for id in tfids:
	pointlist = []
	print(id)
	tyinfo = get_typhooninfo(id)[0]
	points = tyinfo['points']
	for point in points:
		lat = point['lat']
		lng = point['lng']
		result = {
		'lat' : lat,
		'lng' : lng,
		}
		pointlist.append(result)
	print(str(id) + '完成')
	pointlists[str(id)] = pointlist
print(pointlists)



