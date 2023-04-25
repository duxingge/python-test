#!/usr/bin/python3
import sys
## 1. module

"""
sys.path 包含了一个 Python 解释器自动查找所需模块的路径的列表
['/Users/wangjiaxing/IdeaProjects/python-test/python3-test', 
'/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python38.zip',
 '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8', 
 '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8/lib-dynload', 
 '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8/site-packages', 
 '/Library/Python/3.8/site-packages']
"""



# 1.1 导入模块(引用需要加模块名前缀) 一个模块被另一个程序第一次引入时，其主程序将运行。
import support

# 现在可以调用模块里包含的函数了
support.print_func("Runoob")

# 1.2 导入部分
# from 模块 import 指定部分(省去了模块名前缀)
# from 模块 import *  导入模块所有内容，那些由单一下划线（_）开头的名字不在此例(省去了模块名前缀)

# from support import print_func

# print_func("Runbbb")

# 1.3 __name__属性:  一个模块被另一个程序第一次引入时，其主程序将运行。如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。
if __name__ == '__main__':
    print("sss")


# 注：每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，
#                              否则是被引入，值为模块名。

import support

# 1.4 包
# 比如一个模块的名称是 A.B， 那么他表示一个包 A中的子模块 B 。
# 目录只有包含一个叫做 __init__.py 的文件才会被认作是一个包
# 导入语句遵循如下规则：如果包定义文件 __init__.py 存在一个叫做 __all__ 的列表变量，那么在使用 from package import * 的时候就把这个列表中的所有名字作为包内容导入。

# sound/                          顶层包 
#     __init__.py               初始化 sound 包
#     formats/                  文件格式转换子包
#         __init__.py
#         wavread.py
#         wavwrite.py
#         aiffread.py
#         aiffwrite.py
#         auread.py
#         auwrite.py
#         ...
#     effects/                  声音效果子包
#         __init__.py
#         echo.py
#         surround.py
#         reverse.py
#         ...
#     filters/                  filters 子包
#         __init__.py
#         equalizer.py
#         vocoder.py
#         karaoke.py
#         ...