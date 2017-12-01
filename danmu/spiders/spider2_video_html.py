#coding=utf-8
import scrapy
import time
import random
import re
from bs4 import BeautifulSoup

class QuotesSpider(scrapy.Spider):
	name = "bili_spider2"

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
		av_numbers = open('av.txt','r').readlines()
		print('Load av_numbser success')
		# urls = [
		# 'http://www.bilibili.com/video/av5332013/index_1.html',
		# ]
		for av_number in av_numbers:
			url = 'http://www.bilibili.com/video/av'+av_number.strip()+'/index_1.html'
			header['User-Agent'] = userAgent[random.randint(0,len(userAgent)-1)]
			time.sleep(3+random.randint(0,10))
			yield scrapy.Request(url=url, callback=self.parse,method='GET',headers=header)

	def parse(self,response):
		av_number = response.url.split("/")[-2]

		filename = 'video_data/'+av_number + '.html'
		try:
			with open(filename,'wb') as f:
				f.write(response.body)
			f.close()
		except Exception as e:
			print(e)

		try:
			with open('av_cid.txt','a') as av_cid_file:
				soup = BeautifulSoup(response,'lxml')
				av_cid_tmp = soup.find('div',{'id':'bofqi'})
				if av_cid_tmp != None and av_cid_tmp.script != None and av_cid_tmp.script.string != None:
					jsstring = av_cid_tmp.script.string
					cid = pattern.findall(jsstring)[0][4:-1]
					av_cid_file.write(av_number.strip()+' '+cid+'\n')
			av_cid_file.close()
		except Exception as e:
			print(e)
