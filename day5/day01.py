# 模块
"""
1. 自定义模块
2. 使用系统模块

导入模块
    1. import
    2. from 模块名 import 部分方法
    3. from 模块名 import *  所有方法     __all__ = []  在模块中定义可以导入的内容


"""


# 系统模块
import time

t = time.time()
print(t)

time.sleep(3)
t1 = time.time()
print(t1)

T1 = time.ctime(t1)
print(T1)

t2 = time.localtime(t1)
print(t2)

t3 = time.mktime(t2)
print(t3)

t4 = time.strftime("%Y-%m-%d")
print(t4)