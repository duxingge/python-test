#!/usr/bin/python3

# 1.类定义，继承，多重继承(方法名同，默认调用的是在括号中参数位置排前父类的方法),方法重写
# 私有属性，私有方法：以__开头，不能在类外调用
# 类的方法：类方法必须包含参数 self，且为第一个参数，self 代表的是类的实例


# 2.类的专有方法

# 类的专有方法：
# __init__ : 构造函数，在生成对象时调用
# __del__ : 析构函数，释放对象时使用
# __repr__ : 打印，转换
# __setitem__ : 按照索引赋值
# __getitem__: 按照索引获取值
# __len__: 获得长度
# __cmp__: 比较运算
# __call__: 函数调用
# __add__: 加运算
# __sub__: 减运算
# __mul__: 乘运算
# __truediv__: 除运算
# __mod__: 求余运算
# __pow__: 乘方


# class people:
#     #定义基本属性
#     name = ''
#     age = 0
#     # 定义私有属性，在类外无法访问
#     __weight = 0
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def speak(self):
#         print(f"{self.name} say: i am {self.age}")
#     #定义私有方法
#     def __who(self):
#         print('name  : ', self.name)
#
#
# class speaker:
#     name = ''
#     age = 0
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def speak(self):
#         print(f"i am a speaker, name {self.name},age {self.age}")
#
#
# #方法名同，默认调用的是在括号中参数位置排前父类的方法
# class student(people,speaker):
#     grade=0
#
#     def __init__(self,name,age,grade):
#         people.__init__(self,name,age)
#         speaker.__init__(self,name,age)
#         self.grade = grade
#     # def speak(self):
#     #     print(f"{self.name} say: i am {self.age} in grade {self.grade}")
#
#
# if __name__ == '__main__' :
#     stu = student('zhangsan',15,6)
#     stu.speak()


# 3.运算符重载

# class Vector:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __str__(self):
#         return 'Vector (%d, %d)' % (self.a, self.b)
#
#     def __add__(self,other):
#         return Vector(self.a + other.a, self.b + other.b)
#
# v1 = Vector(2,10)
# v2 = Vector(5,-2)
# print (v1 + v2) #Vector(7,8)


# 4.作用域(搜索顺序L->E->G->B)

# L (Local作用域)
# E (Enclosing作用域)(non-local作用域/non-global作用域) 比如两个嵌套函数，一个函数（或类） A 里面又包含了一个函数 B ，那么对于 B 中的名称来说 A 中的作用域就为 nonlocal。
# G (Global作用域)
# B (Built-in）包含内建的关键字和变量

# 5. global 和 nonlocal关键字
# 当内部作用域想修改外部作用域的变量时，就要用到 global 和 nonlocal 关键字了。

# num = 1
# def fun1():
#     global num  # 需要使用 global 关键字声明
#     print(num)
#     num = 123
#     print(num)
# fun1()
# print(num)
#
# def outer():
#     num = 10
#     def inner():
#         nonlocal num   # nonlocal关键字声明
#         num = 100
#         print(num)
#     inner()
#     print(num)
# outer()