#!/usr/bin/python3


# 1.标准库
# 操作系统接口 os
# 文件与目录管理 shutil
# 正则处理 re
# 数学模块math
# 日期处理 datetime 为日期和时间处理同时提供了简单和复杂的方法。

import os
import shutil
import sys
import re
from datetime import date
import datetime

# print(os.getcwd())
# print(os.getuid())
#
# shutil.copy("./db.txt","./db2.txt")
# shutil.move("./db2.txt","./resource/db2.txt")

# print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')) # ['foot', 'fell', 'fastest']

# now = date.today()
# oldDay = datetime.date(2003,12,2)
# age = now - oldDay
# print(age.days)



# 2.命令行参数 sys.argv
# print(sys.argv) #   python3 a9_standardlib.py a1 a2 a3  #输出结果 ['a9_standardlib.py', 'a1', 'a2', 'a3']

# 3. sys 还有 stdin，stdout 和 stderr 属性,大多脚本的定向终止都使用 "sys.exit()"。
