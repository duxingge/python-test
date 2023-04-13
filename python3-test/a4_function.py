#!/usr/bin/python3

# def 函数名（参数列表）:
#     函数体


# def max(a, b):
#     if a > b:
#         return a
#     else:
#         return b
#
# a = 4
# b = 5
# print(max(a, b))

## 1.必需参数和关键字参数
# 必需(Positional)参数： 以正确的顺序传入函数。调用时的数量必须和声明时的一样
# 关键字参数： 使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值


# Positional argument cannot appear after keyword argumentsPylance


# def printinfo( name, age=50 ): # 默认参数设置
#     "打印任何传入的字符串"
#     print ("名字: ", name)
#     print ("年龄: ", age)
#     return
#
# #关键字参数
# printinfo( age=50, name="runoob" )
# #必需参数
# printinfo("runoob",50)

## 2. 不定长参数 *args,   args以元组形式存在
# **vardict       vardict以dict形式存在


# def printinfo( arg1, *vartuple ):
#     "打印任何传入的参数"
#     print ("输出: ")
#     print (arg1)
#     print (vartuple)
#
# printinfo( 70, 60, 50 )

# def printinfo( arg1, **vardict ):
#     "打印任何传入的参数"
#     print ("输出: ")
#     print (arg1)
#     print (vardict)

# printinfo(1, a=2,b=3)

## 3.匿名函数 Python 使用 lambda 来创建匿名函数。

# lambda [arg1 [,arg2,.....argn]]:expression

# b = lambda a:a+2
# print(b(4))
# res = lambda a,b : a * b
# print(res(2,3))

## 4.强制参数位置 Python3.8 新增了一个函数形参语法 / 用来指明函数形参必须使用指定位置参数，不能使用关键字参数的形式。

# 在以下的例子中，形参 a 和 b 必须使用指定位置参数，c 或 d 可以是位置形参或关键字形参，而 e 和 f 要求为关键字形参:
# def f(a, b, /, c, d, *, e, f):
#   f(10, 20, 30, d=40, e=50, f=60)
