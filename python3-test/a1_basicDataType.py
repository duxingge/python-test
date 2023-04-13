#!/usr/bin/python3

import keyword
import operator

# test
# print(keyword.kwlist)


# switch line
total = 1 + \
    2 + \
    4
# print(total)

# set multi values
aa = bb = 111
# print(aa,bb) # 111 111

aa, bb, cc = 11, 22, 33
# print(aa,bb,cc) # 11 22 33

"""
basic type

type()查看变量的对象类型
isinstance 是否属于该类型及其子类
六个基本类型
    不可变类型: Number,String,Tuple
        number: int float complex,boolean
    可变类型: List,SET,Dictionary
        
"""

# 1. number
aa, bb, cc, dd = 11, 1.1, "1.2", True
# print(type(aa),type(bb),type(cc),type(dd)) # <class 'int'> <class 'float'> <class 'str'> <class 'bool'>


class A:
    pass


class B(A):
    pass
# print(isinstance(aa,int))   #Ture
# print(type(aa) == int)      #Ture
# print(isinstance(B(),A))    #Ture
# print(type(B())==A)         #False
# print(type(A())==A)         #Ture
#
# print(issubclass(bool,int))   #Ture


# 2. string
# '' "" ， \转义   r禁止转义
s1 = 'ss'  # s2 = "ss"

str = 'Runoob'
str.split()
# print (str)          # 输出字符串
# print (str[0:-1])    # 输出第一个到倒数第二个的所有字符
# print (str[0])       # 输出字符串第一个字符
# print (str[2:5])     # 输出从第三个开始到第五个的字符
# print (str[2:])      # 输出从第三个开始的后的所有字符
# print (str * 2)      # 输出字符串两次，也可以写成 print (2 * str)
# print (str + "TEST") # 连接字符串
# print(r'Ru\noob')    # Ru\noob

# f-string 引用变量 
# It allows you to embed expressions inside string literals by enclosing them in curly braces ({}), which are then evaluated at runtime and inserted into the string.
# print(f"testName {name}")

# 3. list

list2 = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']
list1 = [['kknoob', 7.2], [133, 'nokb']]

# print (list2)              # 输出完整列表
# print (list2[0])           # 输出列表第一个元素
# print (list2[1:3])         # 从第二个开始输出到第三个元素
# print (list2[2:])          # 输出从第三个元素开始的所有元素
# print (tinylist * 2)      # 输出两次列表
# print (list2 + tinylist)   # 连接列表
# list2[-1::-1] 有三个参数
# print(list2[-1::-1])       #list[-1::-1] 有三个参数:第一个参数 -1 表示最后一个元素;第二个参数为空，表示移动到列表末尾;第三个参数为步长，-1 表示逆向
# list2.append("element")    # 增
# list2.remove(786)          # 删1
# del list2[1]               # 删2
# list[2]="ele2"            # 改
# print(operator.eq(list1, list2)) #列表比较需要引入 operator 模块的 eq 方法


# 4.Tuple 与list类似，但是元组内的元素不能修改.

tuple1 = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')

# 元组中只包含一个元素时，需要在元素后面添加逗号 , ，否则括号会被当作运算符使用：
# print(type((23,)))  #<class 'tuple'>
# print(type((23)))   #<class 'int'>

# print (tuple1)             # 输出完整元组
# print (tuple1[0])          # 输出元组的第一个元素
# print (tuple1[1:3])        # 输出从第二个元素开始到第三个元素
# print (tuple1[2:])         # 输出从第三个元素开始的所有元素
# print (tinytuple * 2)     # 输出两次元组
# print (tuple1 + tinytuple) # 连接元组
# del tuple1                # 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
# print(tuple1)             NameError: name 'tuple1' is not defined


# 5. Set        使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
sites2 = {"marks"}
# print(sites)   # 输出集合，重复的元素被自动去掉
# # 成员测试
# if 'Runoob' in sites :
#     print('Runoob 在集合中')
# else :
#     print('Runoob 不在集合中')
#
#
# # set可以进行集合运算,list不行
# a = set('abracadabra')
# b = set('alacazam')
#
# print(a)
#
# print(a - b)     # a 和 b 的差集
#
# print(a | b)     # a 和 b 的并集
#
# print(a & b)     # a 和 b 的交集
#
# print(a ^ b)     # a 和 b 中不同时存在的元素

# sites.update(sites2)    #连接
# sites.add("marks")        #增
# sites.remove("Runoob")    #删
# sites.pop()               #随机删除
# sites.copy()              #集合copy


# 6. Dictionary 字典 类似于Map。 键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行

dict1 = {}      # 等同 dict1 = dict()
dict1['one'] = "1 - 菜鸟教程"
dict1[2] = "2 - 菜鸟工具"

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
dict2 = {('22', 3343, "dsad"): "zhangsan"}

#
# print (dict1['one'])       # 输出键为 'one' 的值
# print (dict1[2])           # 输出键为 2 的值
# print (tinydict)          # 输出完整的字典
# print (tinydict.keys())   # 输出所有键 dict_keys(['name', 'code', 'site'])
# print (tinydict.values()) # 输出所有值 dict_values(['runoob', 1, 'www.runoob.com'])
# print(dict2[('22',3343,"dsad")])


# dict1['key3'] = "value3"    #增
# del dict1['key3']           #删子项
# del dict1                   #删字典
# dict1['key3'] = "newValue3" #改
# dict1.update(dict2)         #连接


# for k in dict1:
#     print(k,end=",")          #one,2,
# for k,v in dict1.items():
#     print(k,v,end=",")                # one 1 - 菜鸟教程,2 2 - 菜鸟工具,
# for k in list(dict1.keys()):
#     print(k)

'''
数据类型转换
    隐式类型转换
    显式类型转换
'''

# 1.隐式类型转换
# num_int = 123
# num_flo = 1.23
#
# num_new = num_int + num_flo
#
# print("datatype of num_int:",type(num_int)) # <class 'int'>
# print("datatype of num_flo:",type(num_flo)) # <class 'float'>
#
# print("Value of num_new:",num_new)  # 124.23
# print("datatype of num_new:",type(num_new)) # <class 'float'>


# 2. 显式类型转换

# x = int(1)   # x 输出结果为 1
# y = int(2.8) # y 输出结果为 2
# z = int("3") # z 输出结果为 3
#
# x = str("s1") # x 输出结果为 's1'
# y = str(2)    # y 输出结果为 '2'
# z = str(3.0)  # z 输出结果为 '3.0'

'''
xx推导式：推导出一个新列表
'''
'''
1. 列表推导式：
[表达式 for 变量 in 列表] 
[out_exp_res for out_exp in input_list]

或者 

[表达式 for 变量 in 列表 if 条件]
[out_exp_res for out_exp in input_list if condition]
'''

names = ["zhangsan","lisi","wangwu"]

# longNames = [name.upper() for name in names ] # ['ZHANGSAN', 'LISI', 'WANGWU']
# longNames = [name.upper() for name in names if len(name)>5] #['ZHANGSAN', 'WANGWU']
# multiples = [i for i in range(30) if i % 3 == 0] # [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]


names = ["zhangsan", 'liSI', "lisi"]
upperNames = {n.upper() for n in names}

# print(upperNames)


'''
2.字典推导式
{ key_expr: value_expr for value in collection }
或
{ key_expr: value_expr for value in collection if condition }

'''

scores = {"zhangsan":23,"lisi":90,"wangwu":100}
print({name : scores[name] for name in scores}) # {'zhangsan': 23, 'lisi': 90, 'wangwu': 100}
# player=["zhangsan","lisi","wangwu","wangyilang"]
# print({name : len(name) for name in player if name.startswith("wang")}) # {'wangwu': 6, 'wangyilang': 10}

'''
3.集合推导式
{ expression for item in Sequence }
或
{ expression for item in Sequence if conditional }
'''

# setnew = {i**2 for i in (1,2,3)} # {1, 4, 9}

'''
4. 元组推导式(生成器表达式): 注意元组推导式返回的结果是一个生成器对象。可可用tuple()转换为元组

(expression for item in Sequence )
或
(expression for item in Sequence if conditional )
'''
# a = (x for x in range(1,10)) # <generator object <genexpr> at 0x7fa3f802c7b0>
# print(tuple(a)) # (1, 2, 3, 4, 5, 6, 7, 8, 9)
