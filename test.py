from bs4 import BeautifulSoup
import requests

url = 'http://jandan.net/ooxx/page-99#comments'

contant = requests.get(url).text
print(contant)


currentpage = BeautifulSoup(contant, 'lxml').prettify()
print(currentpage)