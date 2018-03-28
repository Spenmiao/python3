import requests, time
from bs4 import BeautifulSoup

headers = {
	'Host' : 'bbs.ngacn.cc',
	'Connection' : 'keep-alive',
	'Upgrade-Insecure-Requests' : '1',
	'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
	'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Encoding' : 'gzip, deflate, sdch',
	'Accept-Language' : 'zh-CN,zh;q=0.8',
	# 'Referer' : 'http://bbs.ngacn.cc/misc/adpage_insert_2.html?http://bbs.ngacn.cc/thread.php?fid=-7&rand=539',
	'Cookie' : 'UM_distinctid=162389a3bbe3e-0908d788f7617a-3e3d5f01-100200-162389a3bbf2d0; Hm_lvt_5adc78329e14807f050ce131992ae69b=1521368055; taihe=7c54478fffccf49319cfeaafb891c0ff; taihe_session=dd33db26509ca7bd8fe49c8d1ef653b2; CNZZDATA30043604=cnzz_eid%3D974595344-1521363358-null%26ntime%3D1521368758; CNZZDATA30039253=cnzz_eid%3D1162687469-1521363306-null%26ntime%3D1521368706; CNZZDATA1256638820=1599498494-1521364508-http%253A%252F%252Fbbs.ngacn.cc%252F%7C1521369908; guestJs=1521370161; ngacn0comUserInfo=%25CB%25AE%25B7%25E2%25C1%25F7%25D4%25B5%09%25E6%25B0%25B4%25E5%25B0%2581%25E6%25B5%2581%25E7%25BC%2598%0939%0939%09%0910%09400%094%090%090%0961_4; ngacn0comUserInfoCheck=884d6a784416e5822fc320e7c67320e6; ngacn0comInfoCheckTime=1521370365; ngaPassportUid=39744331; ngaPassportUrlencodedUname=%25CB%25AE%25B7%25E2%25C1%25F7%25D4%25B5; ngaPassportCid=Z8bqlnqrrn1fvp45pjqbeecr5v181lr7tk1g5rvg; lastvisit=1521370377; lastpath=/read.php?tid=13675384&_ff=-7; bbsmisccookies=%7B%22insad_refreshid%22%3A%7B0%3A%22/799c3399b842d2d5e22b77e4%22%2C1%3A1521972853%7D%2C%22pv_count_for_insad%22%3A%7B0%3A-31%2C1%3A1521392426%7D%2C%22insad_views%22%3A%7B0%3A1%2C1%3A1521392426%7D%7D; Hm_lpvt_5adc78329e14807f050ce131992ae69b=1521370377',
}
url = 'http://bbs.ngacn.cc/'
url2 = 'http://bbs.ngacn.cc/thread.php?fid=-7'
r = requests.Session()
re = r.get(url)
resp = r.get(url2)
# time.sleep(20)
response = r.get(url2, headers=headers)

response.encoding = 'gbk'
soup = BeautifulSoup(response.text, 'lxml')
contents = soup.find_all('td', class_='c2')
for content in contents:
	href = content.a['href']
	text = content.a.get_text().strip()
	# print(content)
	href = 'http://bbs.ngacn.cc' + href

	print(href, text)
# print(soup)
