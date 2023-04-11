#!/usr/bin/python3
import random
import math

'''
与Java类似的：
    算术表达式:+ - * / %
    比较运算符： == != > < >= <=
    赋值运算符： 算术运算符= (如+= -=)
    位运算符：   | ^ & ~ << >>
与Java不同:
    算术表达式: ** 幂等 //向下取整除
    逻辑运算符: and or not
    成员运算符: in ; not in
    身份运算符： is(类似id(x)==id(y)) ; is not
'''

# a = 2
# b = 3
# c = a**b # 8

# 9//2 #4
# -9//2 # -5

# a = 10
# b = 20
#
# if  a and b :
#     print ("1 - 变量 a 和 b 都为 True")
#
# if  a or b :
#     print( "4 - 变量 a 和 b 都为 True，或其中一个变量为 True")
#
# if not( a and b ):
#     print( "5 - 变量 a 和 b 都为 False，或其中一个变量为 False")

# a = 10
# b = 20
# list = [1, 2, 3, 4, 5 ];
#
# if ( a in list ):
#     print( "1 - 变量 a 在给定的列表中 list 中")
#
#
# if ( b not in list ):
#     print( "2 - 变量 b 不在给定的列表中 list 中")

# a = 20
# b = 20
#
# if ( a is b ):
#     print( "1 - a 和 b 有相同的标识")
# b = 30
# if ( a is not b ):
#     print ("4 - a 和 b 没有相同的标识")

print(math.modf(-20.3))
print(random.randrange(10.2, 20.3))
