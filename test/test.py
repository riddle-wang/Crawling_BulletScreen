#coding=utf-8
import urllib.request
import urllib.response
from io import BytesIO
import zlib
import re
import gzip
import random

def gzip2data(url):
        header = {
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Referer': 'http://www.bilibili.com/',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
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

        header['User-Agent'] = userAgent[random.randint(0,len(userAgent)-1)]
        request = urllib.request.Request(url,headers=header)
        response = urllib.request.urlopen(request)

        data = None
        try:
            # gzio uncompress
            if response.info().get('Content-Encoding') == 'gzip':
                compresseddata = response.read()
                buf = BytesIO(compresseddata)
                f = gzip.GzipFile(fileobj=buf)
                data = f.read()
                # return data
            # return None
            # deflate uncompress
            else:
                data = zlib.decompress(response.read(),-zlib.MAX_WBITS)
        except Exception as  e:
            print("Exception occur at gzip2data , url = ",url)
            print(e)
        return data
url_tmp = 'http://api.bilibili.com/archive_rank/getarchiverankbypartion?callback=jQuery17206361782311011706_1487812181149&type=jsonp&tid=147&pn=%d&_=1487812181419'
url = url_tmp % 1
print(gzip2data(url))