安装scrapy(脚手架形式)：
	1、将python中的D:\Python\Python37\Scripts目录添加到python环境变量中
	2、在cmd中输入：pip install scrapy

创建scrapy工程： 
	参考网站：https://baijiahao.baidu.com/s?id=1647203767646744476&wfr=spider&for=pc
			  https://baijiahao.baidu.com/s?id=1605850951730946687&wfr=spider&for=pc
	打开CMD -> 切换到工程保存路径 -> scrapy startproject <工程名>
	然后切换到 movie_1905\movie_1905\spiders目录，输入指令 scrapy genspider <爬虫名称> <网页域名> 
	
	创建好以后下面有一下文件和目录：
		scrapy.cfg：项目的配置文件
		Spider/spiders/：存储爬虫代码目录在spiders 里面
		__init__.py ：
		items.py : 项目的目标文件。定义爬虫需要爬取的项目，比如：电影名称、评分、图片地址
		pipelines.py : 项目的管道文件。定义爬取的网页内容如何处理
		Spider/settings.py：项目的设置文件
		middlewares.py 中间健编写，就是一些反扒措施，比如浏览器模拟，ip代理反扒这些，都在中间件里编写
		
	Scrapy架构
		Scrapy Engine(引擎)：负责Spider、ItemPipeline、Downloader、Scheduler中间的通讯，信号、数据传递等。
		Scheduler(调度器)：它负责接受引擎发送过来的Request请求，并按照一定的方式进行整理排列，入队，当引擎需要时，交还给引擎。
		Downloader（下载器）：负责下载Scrapy Engine(引擎)发送的所有Requests请求，并将其获取到的Responses交还给Scrapy Engine(引擎)，
			由引擎交给Spider来处理。
		Spider（爬虫）：它负责处理所有Responses,从中分析提取数据，获取Item字段需要的数据，
			并将需要跟进的URL提交给引擎，再次进入Scheduler(调度器)。
		Item Pipeline(管道)：它负责处理Spider中获取到的Item，并进行进行后期处理（详细分析、过滤、存储等）的地方。
		Downloader Middlewares（下载中间件）：一个可以自定义扩展下载功能的组件。
		Spider Middlewares（Spider中间件）：一个可以自定扩展和操作引擎和Spider中间通信的功能组件。

启动scrapy项目：
	打开 CMD 切换到 scrapy.cfg 所在目录，然后运行：Scrapy crawl movieSpider  # Scrapy crawl <爬虫名>
	