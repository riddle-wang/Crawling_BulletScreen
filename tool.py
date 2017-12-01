#coding=utf-8
import re
from bs4 import BeautifulSoup

av_numbers = open('av.txt','r').readlines()
av_cid = open('av_cid.txt','a')


pattern = re.compile(r'cid=\d+&')

for av_number in av_numbers:
	filename = 'video_data/av'+av_number.strip()+'.html' 
	try:
		with open(filename,'r') as f :
			soup = BeautifulSoup(f.read(),'lxml')
			danmu_tmp = soup.find('div',{'id':'bofqi'})
			if danmu_tmp != None and danmu_tmp.script != None and danmu_tmp.script.string != None:
				jsstring = danmu_tmp.script.string
				cid = pattern.findall(jsstring)[0][4:-1]
				av_cid.write(av_number.strip()+' '+cid+'\n')
		f.close()
	except Exception as e:
		print(e)

