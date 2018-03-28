import requests
from urllib.request import urlretrieve

l = [i for i in range(10)]
for x in range(len(l)):
	print(l[-(x+1)])