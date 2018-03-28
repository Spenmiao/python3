import os , requests
img = requests.get('http://wx4.sinaimg.cn/large/006HcaCrgy1fizk7izm0nj30fx0kngn3.jpg' )

path = 'f:\meizi\\%s' %'path'
if os.path.exists(path):
	print(u'已存在')
else:
	os.makedirs(path)
os.chdir(path)
file = open('ab.jpg', 'ab')
file.write(img.content)
file.close()
pa = os.getcwd()
print(pa)