#!/usr/bin/python3

# python两种错误：语法错误和异常

# 1.语法错误

# >>> while True print('Hello world')
# File "<stdin>", line 1, in ?
# while True print('Hello world')
# ^
# SyntaxError: invalid syntax
#正确的应该是: while True : print('Hello world')

# 2.异常-语法是正确的，在运行它的时候，也有可能发生错误。运行期检测到的错误被称为异常

# >>> 10 * (1/0)             # 0 不能作为除数，触发异常
# Traceback (most recent call last):
# File "<stdin>", line 1, in ?
# ZeroDivisionError: division by zero

# 3.异常处理
# try/except/else/finally

# try:
#     runoob()
# except AssertionError as error:
#     print(error)
# else:
#     try:
#         with open('file.log') as file:
#             read_data = file.read()
#     except FileNotFoundError as fnf_error:
#         print(fnf_error)
# finally:
#     print('这句话，无论异常是否发生都会执行。')

# 4.抛出异常

# raise Exception("exception describe")

# 5.用户自定义异常-继承Exception

class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
#
# try:
#     raise MyError(2*2)
# except MyError as e:
#     print('My exception occurred, value:', e.value)
