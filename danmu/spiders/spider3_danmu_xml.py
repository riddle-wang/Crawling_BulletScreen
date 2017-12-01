#coding=utf-8
import scrapy
import time
import random

class DanmuSpider(scrapy.Spider):
	name = "bili_spider3"

	def start_requests(self):
		header = {
		'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
		'Accept-Encoding': 'gzip, deflate, sdch',
		'Connection':'keep-alive',
		'Host':'comment.bilibili.com',
		'Referer':'http://www.bilibili.com/video/av5332021/',
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
		av_cid_file = open('av_cid.txt','r').readlines()
		tmp_str = 'http://www.bilibili.com/video/av'
		for ele in av_cid_file:
			segment = ele.strip().split(' ')
			filename = 'danmu_data/'+segment[0]+'.xml'
			cid = segment[1]
			danmu_url = 'http://comment.bilibili.com/'+cid+'.xml'
			header['User-Agent'] = userAgent[random.randint(0,len(userAgent)-1)]
			header['Referer'] = tmp_str + segment[0]+'/'
			time.sleep(3+random.randint(0,10))
			yield scrapy.Request(url=danmu_url, callback=self.parse,method='GET',headers=header)

	def parse(self,response):
		filename = 'danmu_data/'+response.url.split("/")[-1]
		try:
			with open(filename,'wb') as f:
				f.write(response.body)
			f.close()
		except Exception as e:
			print(e) 
