#!/usr/bin/python3


# 1.1字符串转换
# str()： 函数返回一个用户易读的表达形式。
# repr()： 产生一个解释器易读的表达形式。

# for x in range(1, 11):
#     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
#     # 注意前一行 'end' 的使用
#     print(repr(x*x*x).rjust(4))

# 1.2 str.format()
# print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))
# 菜鸟教程网址： "www.runoob.com!"
# print('{1} 和 {0}'.format('Google', 'Runoob'))
# Runoob 和 Google


# 1.3 读取键盘输入 input("tip")

# str = input("请输入：");
# print ("你输入的内容是: ", str)


#1.4 文件
# 1.4.1 读写文件
# open(filename,mode)

# --demo
# 打开一个文件
# f = open("/tmp/foo.txt", "w")
#
# f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
#
# # 关闭打开的文件
# f.close()


# 1.4.2 文件对象的方法
# f.read(size) #这将读取一定数目的数据, 然后作为字符串或字节对象返回;size不传读取所有。
# f.readline()
# f.readlines()



# --demo1
# f = open("./support.py", "r")
# str = f.read(5)
# print(str)

# --demo2

# f = open("/tmp/foo1.txt", "w")
#
# value = ('www.runoob.com', 14)
# s = str(value)
# f.write(s)
#
# # 关闭打开的文件
# f.close()


# 1.5 对象的序列化与反序列化-pickle模块

# import pickle
#
# db = open("./db.txt", 'wb')
# books = [["math1","math2"],["music1","art2"]]
#
# pickle.dump(books,db)  #序列化并持久化到文件
# db.close()
# db = open("./db.txt", 'rb')
# books2 = pickle.load(db)# 文件中读取并反序列化
# print(books2)
# db.close()

