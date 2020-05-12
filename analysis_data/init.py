# -*- coding: utf-8 -*-

from OpFile import MovieFileOp
from mysqlop import OpMysql

if __name__ == '__main__':
  # ReadMovieFile.read('../movie_1905/2020-05-05.json')
  items = MovieFileOp.readList('../movie_1905/2020-05-05.json')
  
  # 写入文件
  # MovieFileOp.writeOrder(items)
  #print( MovieFileOp.totalMovieScore(items) )
  #print(MovieFileOp.getMovieByScore(items, '3'))
  op = OpMysql()
  '''
  # op.createTable(); # 创建表
  # op.addDatas(items)
  datas = op.findAll()
  for data in datas:
    print(data)
  '''
  datas = op.findByName('叶问')
  for data in datas:
    print(data)
   
  '''
  datas = op.findByScore(7,8)
  for data in datas:
    print(data)
  '''