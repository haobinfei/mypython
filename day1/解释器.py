# 定义 函数作为参数
"""特点1 函数作为参数 被函数B接收
   特点2 有闭包的特点
"""

# 地址引用

import time


def outer(a):
    def decorate(func):
        def warrper(*gars, **kwagrs):
            func(*gars, **kwagrs)
            time.sleep(5)
            meany = a * 5
            print("一共花了{}万元".format(meany))

        return warrper

    return decorate


@outer(a=100)
def func(a=100):
    print("zheshiyige {}平米的毛坯房".format(a))


func()
