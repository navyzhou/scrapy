# -*- coding: utf-8 -*-
import scrapy

'''
必须先安装selenium
	1、cmd中输入：pip install selenium
	2、检查是否安装成功：pip show selenium
	3、安装driver，我是使用的firefox，所以下载geckdriver 下载地址：https://github.com/mozilla/geckodriver/releases，
		需注意的是浏览器的版本和driver驱动的版本要匹配。
		下载对应版本的geckdriver压缩包，然后解压，解压后的名称都是一样的，driver的路径可以放在python 的script的路径下
'''
from movie_1905.items import Movie1905Item
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

'''
	Spider类定义了如何爬取某个(或某些)网站。包括了爬取的动作(例如:是否跟进链接)以及如何从网页的内容中提取结构化数据(爬取item)。
	换句话说，Spider就是您定义爬取的动作及分析某个网页(或者是有些网页)的地方。
'''
class MoviespiderSpider(scrapy.Spider):
	name = "movieSpiders" #定义spider名字的字符串(string)。spider的名字定义了Scrapy如何定位(并初始化)spider，所以其必须是唯一的。 不过您可以生成多个相同的spider实例(instance)，这没有任何限制。 name是spider最重要的属性，而且是必须的。
	
	
	allowed_domains = ["1905.com"] #可选。包含了spider允许爬取的域名(domain)列表(list)。 当 OffsiteMiddleware启用时， 域名不在列表中的URL不会被跟进。
	start_urls = ['https://www.1905.com/vod/list/n_1/o3p2.html'] #URL列表。当没有制定特定的URL时，spider将从该列表中开始进行爬取。 因此，第一个被获取到的页面的URL将是该列表之一。 后续的URL将会从获取到的数据中提取。
	
	
	# 当response没有指定回调函数时，该方法是Scrapy处理下载的response的默认方法。
	# parse 负责处理response并返回处理的数据以及(/或)跟进的URL。 Spider 对其他的Request的回调函数也有相同的要求。
	# 该方法及其他的Request回调函数必须返回一个包含 Request 及(或) Item 的可迭代的对象。
	# 可以获取到分页页面，但是获取不到分页数据，因为分页数据的是动态加载的
	
	
	def parse(self, response):
		# 将得到的页面地址传送给单个页面处理函数进行处理 -> parse_content()
		yield scrapy.Request(response.url, callback=self.parse_content)
		
		#TODO： 读取分页数据，爬取下一页
		#找到下一页的URL地址,实现翻页请求
		next_url=response.xpath("//section[@id='vod-page']/a[@class='next']/@href").extract_first() # 或extract()[0]
		# 我们在setting.py中设置了 CLOSESPIDER_PAGECOUNT = 10
		if next_url and next_url !=" javascript:;":
			# next_url="https://www.1905.com/vod/list/n_1/o3p" + next_url + ".html"
			# 通过 yield 来发起一个请求，并通过 callback 参数为这个请求添加回调函数，在请求完成之后会将响应作为参数传递给回调函数。
			# crapy框架会根据 yield 返回的实例类型来执行不同的操作，如果是 scrapy.Request 对象，
			# scrapy框架会去获得该对象指向的链接并在请求完成后调用该对象的回调函数。
			yield scrapy.Request(next_url, callback=self.parse)
	
	'''
	def __init__(self, bid = None): #示例：bid = 12339
       # 初始化起始页面
       super(MoviespiderSpider, self).__init__()
       self.bid = bid #参数bid由此传入
       self.start_urls = ['http://buluo.qq.com/p/barindex.html?bid=%s' % bid]
       self.allowed_domain = 'buluo.qq.com'
       self.driver = webdriver.Firefox()       
       self.driver.set_page_load_timeout(5) #throw a TimeoutException when thepage load time is more than 5 seconds.
	'''
	
	'''
	def __init__(self):
		# 初始化起始页面
		super(MoviespiderSpider, self).__init__()
		self.start_urls = ['https://www.1905.com/vod/list/n_1/o3p1.html']
		self.allowed_domain = '1905.com'
		self.driver = webdriver.Firefox()       
		self.driver.set_page_load_timeout(5) # throw a TimeoutException when thepage load time is more than 5 seconds.
		
	def parse(self, response):
		# 模拟浏览器实现翻页，并解析每一个页面的url_list
		
		self.driver.get(response.url)
		while True:
			
			WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)
				——driver：WebDriver 的驱动程序(Ie, Firefox, Chrome 或远程)
				——timeout：最长超时时间，默认以秒为单位
				——poll_frequency：休眠时间的间隔（步长）时间，默认为 0.5 秒
				——ignored_exceptions：超时后的异常信息，默认情况下抛 NoSuchElementException 异常
			
			wait = WebDriverWait(self.driver, 5)
			# 在设置时间（5s）内，等待后面的条件发生。如果超过设置时间未发生，则抛出异常。
			# 在等待期间，每隔一定时间（默认0.5秒)，调用until或until_not里的方法，直到它返回True或False
			wait.until(lambda driver:driver.find_element_by_xpath('//a[@class="pic-pack-outer"]')) #内容加载完成后爬取
			url = self.driver.find_elements_by_xpath("//section[@id='vod-page']/a[@class='next']/@href").extract_first()
			
			
			# url_list = [sel.get_attribute("href") for sel in sel_list]
			# url_set |= set(url_list)
			try:
				wait =WebDriverWait(self.driver, 5)
				wait.until(lambda driver:driver.find_element_by_xpath("//section[@id='vod-page']/a[@class='next']")) # 下一页地址
				next_page = self.driver.find_element_by_xpath("//section[@id='vod-page']/a[@class='next']")
				# next_page.click() # 模拟点击下一页
			except:
				print("已经到最后一页了...")
				break            
			
		yield scrapy.Request(url, callback=self.parse_content)
	'''
	
	# 单页处理器
	def parse_content(self, response):
		#将得到的单个作品的页进行分析取值
		selectors = response.xpath('//a[@class="pic-pack-outer"]')
		items = []
		names = []
		scores = []
		for selector in selectors:
			item = Movie1905Item()
			names = selector.xpath('./h3/text()').extract();  #.split()[0]  # extract()：转换为Unicode字符串  split():以空格分割取第一项
			scores = selector.xpath('./i[@class="score"]/b/text()').extract()
			
			if len(names) > 0 and  len(scores) > 0:
				item['movieName'] = names[0]
				item['moviePic'] = selector.xpath('./img/@src').extract()[0] # 获取src属性
				item['movieScore'] = scores[0]
				
				#try:cl
				#	author = response.xpath('//div[@class="son2"]/p[2]/a/text()').extract()[0]
				#except:
				#	author = '佚名'
				#item['author'] = author
				#yield item
				items.append(item)
		return items
 