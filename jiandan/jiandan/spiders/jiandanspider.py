import scrapy, os, requests, re
from bs4 import BeautifulSoup
from scrapy.http import Request 
from jiandan.items import JiandanItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class JiandanSpider(scrapy.Spider):
    name = 'jiandanmeizi'
    allowed_domains = ['jandan.net']
    start_urls = ['http://jandan.net/ooxx']
    urllist = []
    def parse(self, response):      
        soup = BeautifulSoup(response.text, 'lxml')
        currentpage = soup.find('span', class_='current-comment-page').get_text()[1:-1]
        x = 1
        imgs = soup.find_all('img', src=re.compile('.*?jpg'))
        for img in imgs:
            imgurl = img['src']
            if re.search(r'http:', imgurl):
                imgurl = re.sub(r'http:', '', imgurl)
            imgurl = 'http:' + imgurl
            self.urllist.append(imgurl)                 
            #name = currentpage + '-' + str(x)
            #print(name)
            #path = 'D:\jiandanmeizitu'
            ########if not os.path.exists(path):
               ####### os.makedirs(path)
            ######os.chdir(path)
            #####content = requests.get(imgurl).content.strip()
            ####file = open(name + '.jpg', 'ab')
            ###file.write(content)
            ##file.close
            #x+=1
        
        #print(u'第' + currentpage + u'页下载完')
        if not  currentpage == str(1):
            nextpage = soup.find('a', title='Older Comments').find_previous('a').get_text().strip()
        
            nexturl = 'http://jandan.net/ooxx/page-%s#comments' %int(nextpage)     
        
            yield Request(nexturl, callback=self.parse)
        else:
            item = JiandanItem()
            item['imgurl'] = self.urllist 
            yield item 



       