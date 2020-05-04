# -*- coding: utf-8 -*-
import scrapy

from movie_1905.items import Movie1905Item

'''
	Spider类定义了如何爬取某个(或某些)网站。包括了爬取的动作(例如:是否跟进链接)以及如何从网页的内容中提取结构化数据(爬取item)。
	换句话说，Spider就是您定义爬取的动作及分析某个网页(或者是有些网页)的地方。
'''
class MoviespiderSpider(scrapy.Spider):
	# 定义spider名字的字符串(string)。spider的名字定义了Scrapy如何定位(并初始化)spider，所以其必须是唯一的。 
	# 不过您可以生成多个相同的spider实例(instance)，这没有任何限制。 name是spider最重要的属性，而且是必须的。
	name = "movieSpider2" 
	
	def __init__(self, bid = None): #示例：bid = 12339
		# 初始化起始页面
		super(MoviespiderSpider, self).__init__()
		
		# 可选。包含了spider允许爬取的域名(domain)列表(list)。 当 OffsiteMiddleware启用时， 域名不在列表中的URL不会被跟进。 
		self.allowed_domain = "1905.com"
		
		#URL列表。当没有制定特定的URL时，spider将从该列表中开始进行爬取。 因此，第一个被获取到的页面的URL将是该列表之一。 
		# 后续的URL将会从获取到的数据中提取。
		for i in range(1,10) :
			self.start_urls.append('https://www.1905.com/vod/list/n_1/o3p' + str(i) + '.html')
	   
	def parse(self, response):
		# 将得到的页面地址传送给单个页面处理函数进行处理 -> parse_content()
		yield scrapy.Request(response.url, callback=self.parse_content)
	
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
 