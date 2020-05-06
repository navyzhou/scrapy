# -*- coding: utf-8 -*-
from collections import Counter


class MovieFileOp:
  # 显示爬取到的电影信息
  def showMovie(path):
    with open(path, 'r', encoding='utf-8') as fp:
      for line in fp:
        print(line)
        
  # 将电影信息读取到一个列表中  
  def readList(path):
    items = []
    with open(path, 'r', encoding='utf-8') as fp:
      for line in fp:
       items.append(eval(line)) # 将字符串转成字典对象，放到列表对象中。不能使用dict()函数
    return items
  
  # 按评分降序写入
  def writeOrder(items):
    items.sort(key=lambda item:item['movieScore'], reverse=True) # reverse=True说明降序排，为False说明根据评分升序排列
    # items =  sorted(items, key=lambda item:item['movieScore'], reverse=True) # 降序排列
  
    # sorted和sort的区别在于sorted不对原列表进行改变，它需要一个变量来接受排序后的列表，不改变列表本身的顺序，至于用哪个排序方法，应该跟实际情况来调整。
    # item in items:
    #  print(item)
    with open('./movie_list.json', 'w', encoding='utf-8') as fp:
      for item in items:
        fp.write(str(item) + "\n")
      print('写入完成')
    
  # 根据电影评分统计电影数量
  def totalMovieScore(items) :
    aList = [x['movieScore'] for x in items] # 根据分数生成一个列表
    return Counter(aList) # 统计列表中每个元素出现的次数，并以字典方式返回
    
  # 返回指定评分的电影
  def getMovieByScore(items, score):
    result = set()
    result = [x for x in items if x['movieScore'] == score]
    return result
  
  