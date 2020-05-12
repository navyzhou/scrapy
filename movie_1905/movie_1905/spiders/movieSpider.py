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
  name = "movieSpider" 
  
  # 可选。包含了spider允许爬取的域名(domain)列表(list)。 当 OffsiteMiddleware启用时， 域名不在列表中的URL不会被跟进。
  allowed_domains = ["1905.com"] 
  
  # URL列表。当没有制定特定的URL时，spider将从该列表中开始进行爬取。 因此，第一个被获取到的页面的URL将是该列表之一。 
  # 后续的URL将会从获取到的数据中提取。
  start_urls = ['https://www.1905.com/vod/list/n_1/o3p1.html'] 
	
	
  # 当response没有指定回调函数时，该方法是Scrapy处理下载的response的默认方法。
  # parse 负责处理response并返回处理的数据以及(/或)跟进的URL。 Spider 对其他的Request的回调函数也有相同的要求。
  # 该方法及其他的Request回调函数必须返回一个包含 Request 及(或) Item 的可迭代的对象。
  # 可以获取到分页页面，但是获取不到分页数据，因为分页数据的是动态加载的
  def parse(self, response):
    # 将得到的页面地址传送给单个页面处理函数进行处理 -> parse_content()
    yield scrapy.Request(response.url, callback=self.parse_content)
    
    
    #TODO： 读取分页数据，爬取下一页。找到下一页的URL地址,实现翻页请求
    next_url=response.xpath("//section[@id='vod-page']/a[@class='next']/@href").extract_first() # 或extract()[0]
    if next_url and next_url !=" javascript:;":
      # 通过 yield 来发起一个请求，并通过 callback 参数为这个请求添加回调函数，在请求完成之后会将响应作为参数传递给回调函数。
      # crapy框架会根据 yield 返回的实例类型来执行不同的操作，如果是 scrapy.Request 对象，
      # scrapy框架会去获得该对象指向的链接并在请求完成后调用该对象的回调函数。
      # dont_filter默认是false。在爬虫出现了重复的链接或重复的请求会过滤，我们需要关闭不然拿不到分页中的数据
      yield scrapy.Request(next_url, callback=self.parse, method='GET', dont_filter=True)
      # yield response.follow(next_url, callback=self.parse)
      
  # 单页处理器
  def parse_content(self, response):
    #将得到的单个作品的页进行分析取值
    selectors = response.xpath('//a[@class="pic-pack-outer"]')
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
        yield item 
 