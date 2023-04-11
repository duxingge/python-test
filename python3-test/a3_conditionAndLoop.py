#!/usr/bin/python3
import sys

### 1. if

"""
if condition_1:
    statement_block_1
elif condition_2:
    statement_block_2
else:
    statement_block_3
"""

#demo1

#
# age = int(input("请输入你家狗狗的年龄: "))
# print("")
# if age <= 0:
#     print("你是在逗我吧!")
# elif age == 1:
#     print("相当于 14 岁的人。")
# elif age == 2:
#     print("相当于 22 岁的人。")
# elif age > 2:
#     human = 22 + (age -2)*5
#     print("对应人类年龄: ", human)


### 2. while循环

# while <expr>:
#     <statement(s)>
# else:
#     <additional_statement(s)>     #只执行一次

# count = 0
# while count < 5:
#     print (count, " 小于 5")
#     count = count + 1
# else:
#     print (count, " 大于或等于 5")

### 3. for循环

# for <variable> in <sequence>:
#     <statements>
# else:
#     <statements>

# languages = ["C", "C++", "Perl", "Python"]
# for l in languages :
#     print(l)
# else:
#     print("end")

# range(5)      #生成数字数列
# print(list(range(5)))           # [0, 1, 2, 3, 4]
# print(list(range(0, 10, 3)))    # [0, 3, 6, 9]

### 循环中 break & continue & pass
    # pass是空语句，是为了保持程序结构的完整性。

## 4. 迭代器

# 4.1 迭代器的基本方法： iter()和next()

# list=[1,2,3,4]
# it = iter(list)
# while True :
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()

#4.2 实现迭代器
# 把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 。
class MyNumber:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a = x+1
        if x>10 :
            raise StopIteration
        else:
            return x

# nums = MyNumber()
# numIters = iter(nums)
# while True:
#     try:
#         print(next(numIters))
#     except StopIteration:
#         break

# 4.3 StopIteration 该异常标识迭代完成,在 __next__() 方法中我们可以设置触发 StopIteration 异常来结束迭代。

## 5.生成器
# 在 Python 中，使用了 yield 的函数被称为生成器（generator）。
# 跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
# 在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。
# 调用一个生成器函数，返回的是一个迭代器对象。

def fibonacci(n):
    a,b = 0,1
    while b<n :
        yield b
        a,b=b,a+b;

f = fibonacci(10)

while True :
    try:
        print(next(f))
    except StopIteration:
        break


