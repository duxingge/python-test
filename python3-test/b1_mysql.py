#!/usr/bin/python3


import pymysql

hostname = "localhost"
port = 3306
user = "root"
password = "123123"


db = pymysql.connect(host=hostname, port=port, user=user, password=password,database="wjxdb")

# 1.建表
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
#
# # 使用 execute() 方法执行 SQL，如果表存在则删除
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
#
# # 使用预处理语句创建表
# sql = """CREATE TABLE EMPLOYEE (
#          FIRST_NAME  CHAR(20) NOT NULL,
#          LAST_NAME  CHAR(20),
#          AGE INT,
#          SEX CHAR(1),
#          INCOME FLOAT )"""
#
# cursor.execute(sql)
#
# # 关闭数据库连接
# db.close()

# 2.增
# 对于支持事务的数据库， 在Python数据库编程中，当游标建立之时，就自动开始了一个隐形的数据库事务。
#
# commit()方法游标的所有更新操作，rollback（）方法回滚当前游标的所有操作。每一个方法都开始了一个新的事务。


# # 使用cursor()方法获取操作游标
# cursor = db.cursor()
#
# # SQL 插入语句
# sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
#          LAST_NAME, AGE, SEX, INCOME)
#          VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
# try:
#     # 执行sql语句
#     cursor.execute(sql)
#     # 提交到数据库执行
#     db.commit()
# except:
#     # 如果发生错误则回滚
#     db.rollback()
#
# # 关闭数据库连接
# db.close()

# 3.查
# fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
# fetchall(): 接收全部的返回结果行.
# rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。

# # 使用cursor()方法获取操作游标
# cursor = db.cursor()
#
# # SQL 查询语句
# sql = "SELECT * FROM account \
#        WHERE id < 3"
# try:
#     # 执行SQL语句
#     cursor.execute(sql)
#     # 获取所有记录列表
#     results = cursor.fetchall()
#     for row in results:
#         name = row[1]
#         account = row[2]
#         # 打印结果
#         print ("name=%s,account=%s" % \
#                (name, account))
# except:
#     print ("Error: unable to fetch data")
#
# # 关闭数据库连接
# db.close()


