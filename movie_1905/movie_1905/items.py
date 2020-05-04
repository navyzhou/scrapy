# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
'''
Item 定义结构化数据字段，用来保存爬取到的数据，这里和 dict 类似，但是提供了一些额外的保护减少错误
可以通过创建一个 scrapy.Item 类， 并且定义类型为 scrapy.Field 的类属性来定义一个 Item（可以理解成类似于 ORM 的映射关系）
'''
# scrapy.Item中存储的这些数据
class Movie1905Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 定义所需的字段
	movieName = scrapy.Field()
	movieScore = scrapy.Field()
	moviePic = scrapy.Field()