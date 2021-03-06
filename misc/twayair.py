import requests, json, re, time
from bs4 import BeautifulSoup

#获得航线信息
# url = 'https://www.twayair.com/main.do?_langCode=ZH'
# html = requests.get(url, verify=False)
# soup = BeautifulSoup(html.content, 'lxml')
# # print(soup.dd('a'))
# ls = []
# for x in soup('dd'):
# 	if x.span:
# 		# print(x)
# 		print(x('span')[0].string, x('span')[1].string )
# 		print(x('input')[0]['value'], x('input')[1]['value'])
# 		ls.append((x('input')[0]['value'], x('span')[0].string))
# 		ls.append((x('input')[1]['value'], x('span')[1].string))
# print(dict(ls))
#测试session
# import time
# from selenium import webdriver

# browser = webdriver.Chrome()
# browser.get('https://www.twayair.com/main.do?_langCode=ZH')
# sess = browser.find_element_by_css_selector('input[name="clientSessionId"]')
# print(sess.get_attribute('value'))
# print(browser.get_cookies())
# browser.close()


airlineinfo = {
	'dpturCntryCode': '出发国家',
	'arrivCntryCode': ' 到达国家',
	'GMP': '金浦', 'CJU': '济州', 'TAE': '大邱', 'KWJ': '光州', 'MWX': '务安', 'NGO': '名古屋', 'ICN': '仁川', 'NRT': '东京（成田）', 'KMJ': '熊本', 'HSG': '佐贺', 'CTS': '札幌', 'KIX': '大阪', 'OIT': '大分', 'OKA': '冲绳', 'FUK': '福冈', 'PUS': '釜山', 'MFM': '澳门', 'SYX': '三亚', 'WNZ': '温州', 'TNA': '济南', 'TAO': '青岛', 'HAK': '海口', 'HKG': '香港', 'NNG': '南寧', 'TPE': '台北(桃园)', 'KHH': '高雄', 'RMQ': '台中', 'DAD': '岘港', 'BKK': '曼谷', 'VTE': '万象', 'SGN': '胡志明', 'TSA': '台北(松山)', 'CEB': '宿務', 'VVO': '符拉迪沃斯托克', 'SPN': '塞班', 'GUM': '关岛',
	'flightNumber': '航班',
	'flightDate': '日期',
	'scheduledDepartureDateTime': '出发时间',
	'scheduledArrivalTime': '到达时间'
}


headers = {
	'Host': 'www.twayair.com',
	'Connection': 'keep-alive',
	'Accept': 'txt/htm',
	'X-Requested-With': 'XMLHttpRequest',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64)',
	'Referer': 'https://www.twayair.com/booking/availabilityList.do',
	'Accept-Encoding': 'gzip',
	'Accept-Language': 'zh-CN',
	'Cookie': 'TWAYLANG=ZH;JSESSIONID=s6~4072681BA2CBC00EE1029D444F1937AE.Homepage_137_Node02;'
	}
url = 'https://www.twayair.com/booking/ajax/searchAvailability.do?origin=TAE&destination=CJU&origin1=&destination1=&origin2=&destination2=&onwardDateStr=20180527&returnDateStr=&pointOfPurchase=KR&paxTypeCountStr=1%2C0%2C0&today=20180417&travelType=OW&orderByOW=&orderByRT=&fareBasisCodeOW=&fareBasisCodeRT=&searchType=byDate&arrivCntryCode=&currencyCode=KRW&domesticYn=Y&promotionCode=&searchAvailId=fdf26f7bd5c992667baf7e9949732776dceab71714f07211b4055c222811d67d&segmentId=&fareTypeOW=&fareTypeRT=&onwardFareSum=&returnFareSum=&segmentIdOW=&segmentIdRT=&bundleIndexOW=&bundleIndexRT=&bundleAmountOW=0&bundleAmountRT=0&selectedAvailValueOW=&selectedAvailValueRT='
pre_url = 'https://www.twayair.com/booking/ajax/setBookingParam.do?origin=TAE&destination=CJU&origin1=&destination1=&origin2=&destination2=&onwardDateStr=20180527&returnDateStr=&pointOfPurchase=KR&paxTypeCountStr=1%2C0%2C0&today=20180417&travelType=OW&orderByOW=&orderByRT=&fareBasisCodeOW=&fareBasisCodeRT=&searchType=byDate&arrivCntryCode=&currencyCode=KRW&domesticYn=Y&promotionCode=&searchAvailId=fdf26f7bd5c992667baf7e9949732776dceab71714f07211b4055c222811d67d&segmentId=&fareTypeOW=&fareTypeRT=&onwardFareSum=&returnFareSum=&segmentIdOW=&segmentIdRT=&bundleIndexOW=&bundleIndexRT=&bundleAmountOW=0&bundleAmountRT=0&selectedAvailValueOW=&selectedAvailValueRT=&_={0}'


time_stampt = time.time() * 1000
se = requests.session()
se.get(pre_url.format(time_stampt), headers=headers, verify=False)
# url = 'https://www.twayair.com/booking/ajax/searchAvailability.do?origin=TAE&destination=CJU&origin1=TAE&destination1=CJU&origin2=&destination2=&onwardDateStr=20180414&returnDateStr=&pointOfPurchase=KR&paxTypeCountStr=1%2C0%2C0&today=20180413&travelType=OW&orderByOW=&orderByRT=&fareBasisCodeOW=&fareBasisCodeRT=&searchType=byDate&arrivCntryCode=&currencyCode=KRW&domesticYn=Y&promotionCode=&searchAvailId=027f5a11e3283bdead25c9feef2f9e4ef87a2313a110008f463cd881cd13998b&segmentId=&fareTypeOW=&fareTypeRT=&onwardFareSum=&returnFareSum=&segmentIdOW=&segmentIdRT=&bundleIndexOW=&bundleIndexRT=&bundleAmountOW=0&bundleAmountRT=0&selectedAvailValueOW=&selectedAvailValueRT='

html = se.get(url, headers=headers, verify=False)
# print(html.url)
soup = BeautifulSoup(html.content, 'lxml')
x = soup.select('.px')

for j, i in enumerate(x):
	print(j)
	print(i.select_one('input[name="flightNumber"]')['value'])
	print(i.select_one('input[name="flightDate"]')['value'])
	print(i.select_one('input[name="origin"]')['value'])
	print(i.select_one('input[name="destination"]')['value'])
	print(i.select_one('input[name="scheduledDepartureDateTime"]')['value'])
	print(i.select_one('input[name="flightNumber"]')['value'])
	print(i.select_one('input[name="scheduledArrivalTime"]')['value'])

	print(i)
	
