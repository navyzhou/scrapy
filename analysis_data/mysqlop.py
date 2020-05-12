# -*- coding: utf-8 -*-

# 先在mysql中创建好库：create database movies default character set utf8 collate utf8_bin; 
import pymysql as mysql
from contextlib import contextmanager


# 上下文管理器工具模块contextlib，它是通过生成器实现的，我们不需要再创建类以及__enter__和__exit__这两个特俗的方法
@contextmanager
def openMysqlContext():
  # 打开是连接数据库   
  conn = mysql.connect("127.0.0.1", "root", "a", "movies", charset='utf8'); # 打开数据库连接(url, username, password, dbName, encoding)
  try:
    yield conn # 返回conn连接对象那
  finally:
    conn.close() # 退出时关闭这个连接

class OpMysql:
 
    
  # 创建表  
  def createTable(self):
    sql = '''create table if not exists movieinfo(
      mid int primary key auto_increment,
      mname varchar(100) not null,
      mpic varchar(200),
      mscore decimal(3)
    )'''
    with openMysqlContext() as conn:
      try:
        cursor = conn.cursor(); # 使用cursor()方法获取操作游标
        cursor.execute(sql) # 执行创建
        print("电影信息表创建成功...")
      except:
        print("电影信息表创建失败...")
  
  # 单数据添加
  def addData(self, name, pic, score):
    with openMysqlContext() as conn:
      cursor = conn.cursor(); # 使用cursor()方法获取操作游标
      sql = "insert into movieinfo values(0, '%s', '%s', %d)" %(name, pic, score)
      
      try:
        cursor.execute(sql)
        # 提交到数据库执行
        conn.commit()
        
        if (cursor.rowcount > 0) :
          print('电影数据：', name, ' 添加成功...');
        else:
          print('电影数据：', name, ' 添加失败...');       
      except:
        conn.rollback() # 如果添加失败，则回滚数据
      
  # 批量添加电影数据库到数据库表中  
  def addDatas(self, items):
    with openMysqlContext() as conn:
      cursor = conn.cursor(); # 使用cursor()方法获取操作游标
      sql = "insert into movieinfo values(0, %s, %s, %s)"
      
      try:
        datas = [tuple(item.values()) for item in items] # 获取每个字典里面的所有值构成一个集合，然后把这个集合转成一个元组
        cursor.executemany(sql, datas) #items = [('战狼','1.jpg',9.0),('战狼','1.jpg',9.0)]
        # 提交到数据库执行
        conn.commit()
        if (cursor.rowcount > 0) :
          print('电影数据批量添加成功...');
        else:
          print('电影数据批量添加失败...');       
      except Exception as e:
        conn.rollback() # 如果添加失败，则回滚数据
        print("执行mysql:%s时出错：%s" %(sql, e))
      
  # 查询所有电影数据          
  def findAll(self):
    with openMysqlContext() as conn:
      cursor = conn.cursor(); # 使用cursor()方法获取操作游标
      sql = "select mid, mname, mpic, mscore from movieinfo order by mid"
      cursor.execute(sql)
      data = cursor.fetchall()
      datas = [item for item in data]
      return datas
    
  # 根据电影名称查询  
  def findByName(self, name) :
    with openMysqlContext() as conn:
      datas = []
      try:
        cursor = conn.cursor(); # 使用cursor()方法获取操作游标
        name = '%' + name + '%'
        sql = "select mid, mname, mpic, mscore from movieinfo where mname like '%s'" % name
        cursor.execute(sql)
        data = cursor.fetchall()
        datas = [item for item in data]
      except Exception as e:
        conn.rollback() # 如果添加失败，则回滚数据
        print("执行mysql:%s时出错：%s" %(sql, e))
      return datas
  
  # 根据评分范围查询
  def findByScore(self, startScore, endScore=-1):
    with openMysqlContext() as conn:
      datas = []
      try:
        cursor = conn.cursor(); # 使用cursor()方法获取操作游标
        sql = "select mid, mname, mpic, mscore from movieinfo where mscore >= %d" % int(startScore)
        if endScore != -1:  
          sql += " and mscore <= %d" % int(endScore)
        #tuple(map(int, params))
        sql += " order by mscore desc"
        print(sql)
        cursor.execute(sql)
        data = cursor.fetchall()
        datas = [item for item in data]
      except Exception as e:
        conn.rollback() # 如果添加失败，则回滚数据
        print("执行mysql:%s时出错：%s" %(sql, e))
      return datas