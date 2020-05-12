# -*- coding: utf-8 -*-
# with上下文管理器
'''
import pymysql as mysql


class OpenMysqlContext(object):
  # 初始化是建立连接
  def __init__(self):
    self.conn = mysql.connect("127.0.0.1", "root", "a", "movies", charset='utf8');
  
  # 每次操作时返回这个连接
  def __enter__(self):
    return self.conn
  
  # 退出时关闭连接
  def __exit__(self):
    self.conn.close()
    
# 使用就可以用  with OpenMysqlContext as fp:
    # fp.execute(sql)
'''