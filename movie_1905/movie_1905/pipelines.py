# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# 定义爬取的网页内容如何处理
import time
import codecs
import json

class Movie1905Pipeline:
	def process_item(self, items, spider):  # spider : 蜘蛛
		# now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime());
		now = time.strftime('%Y-%m-%d', time.localtime())
		fileName = now + '.json'  #以当前日期为文件名
    
		# codecs.open(filepath,method,encoding)
		# codecs专门用作编码转换，当然，其实通过它的接口是可以扩展到其他关于代码方面 的转换的，这个东西这里不涉及。
		with codecs.open(fileName, 'a', 'utf8') as fp:
		# dumps(obj) => obj是一个dict-like类型的数据
		
		
		#json.dumps 用于将 Python 对象编码成 JSON 字符串
		#python 原始类型向 json 类型的转化对照表：
		#Python            JSON
		#dict              object
		#list、tuple       array
		#str、unicode      string
		#int、long、float   number
		#True              true
		#False             false
		#None              null
		# fp.write(item['movieName'] + ' ' + item['movieScore'] + ' ' + item['moviePic'])
			line = json.dumps(dict(items), ensure_ascii=False) + '\r\n'
			fp.write(line) # 将数据写到指定的文件中
		return item # 会在控制台显示
