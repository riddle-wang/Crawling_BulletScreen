# Crawling_BulletScreen 弹幕爬虫

使用工具：

1.	VirtualEnv
2.	Scrapy
3.	Python3.5

爬取目标：B站电影数据；

欧美电影：http://www.bilibili.com/video/movie_west_1.html

国产电影：http://www.bilibili.com/video/movie_chinese_1.html

日本电影：http://www.bilibili.com/video/movie_japan_1.html


#### 爬虫设计思路：

Spider1-视频爬虫
根据电影的大类，如欧美电影。进入电影列表后，爬取每页的视频数据（每页含有20部电影）。按页数爬至末尾。同时根据每个视频的av_number 获得视频页面的html源码，并保存为 av<number>.html


Spider2-弹幕爬虫
根据视频html源码，获得cid（请求弹幕资源的id），请求对应的弹幕资源xml文件，并保存。


爬虫设计的防封策略：
1_	控制访问速度3-8秒中随机发起一次请求；
2_	伪装浏览器，每次请求随机更换浏览器信息；


浏览器伪装参数：

```
header = {
		'Accept-Language': 'zh-CN,zh;q=0.8',
		'Accept-Encoding': 'gzip',
		'Referer':'http://www.bilibili.com/video/movie_west_1.html',
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

```
