# -*- coding: utf-8 -*-

from OpFile import MovieFileOp

if __name__ == '__main__':
  # ReadMovieFile.read('../movie_1905/2020-05-05.json')
  items = MovieFileOp.readList('../movie_1905/2020-05-05.json')
  
  # 写入文件
  # MovieFileOp.writeOrder(items)
  #print( MovieFileOp.totalMovieScore(items) )
  
  print(MovieFileOp.getMovieByScore(items, '3'))