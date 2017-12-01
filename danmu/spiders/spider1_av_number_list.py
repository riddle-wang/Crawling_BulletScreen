#coding=utf-8
import scrapy
import re
import time
import random

class BilibiliSpider(scrapy.Spider):
	name ='bili_spider1'
	def start_requests(self):
		header = {
		'Accept-Language': 'zh-CN,zh;q=0.8',
		'Accept-Encoding': 'gzip',
		'Referer':'http://www.bilibili.com/video/boardgame-1.html',
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:45.0) Gecko/20100101 Firefox/45.0',
		}
		userAgent = [
		'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:45.0) Gecko/20100101 Firefox/45.0',
		'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
		'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
		'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
		'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0',
		'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
		'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
		'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
		'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
		'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
		'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
		'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
		'',
		]
		urls = [
		'http://api.bilibili.com/archive_rank/getarchiverankbypartion?callback=jQuery1720645756965607224_1494406451358&type=jsonp&tid=173&pn=%d&_=1494406451669',
		]

		numOfPages = 3
		start = 1

		for url in urls:
			for i in range(start,numOfPages):
				cur_url = url % i
				print(" Page No. %d",i)
				time.sleep(2+random.randint(0,5))
				header['User-Agent'] = userAgent[random.randint(0,len(userAgent)-1)]
				yield scrapy.Request(url=cur_url, callback=self.parse,method='GET',headers=header)

	def parse(self, response):
		pattern = '"aid":[0-9]+'
		r = re.compile(pattern)
		ret = re.findall(r,str(response.body))
		with open('av.txt','a') as f:
			for ele in ret:
				f.write(ele[6:]+'\n')
		f.close()



		
