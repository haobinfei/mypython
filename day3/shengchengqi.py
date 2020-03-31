# 生成器
"""
得到生成器的方式
    1.通过列表推导式
        用（） 产生generator格式

    2.通过借助函数完成

"""

#1.通过列表推导式
# g = (x * 2 for x in range(0,2))
# print(g)
#
# # print(g.__next__())
# try:
#     print(next(g))
#     print(next(g))
#     print(next(g))
#     print(next(g))
# except StopIteration as err:
#     print(err)

# 2.借助函数完成
#只要函数出现了yield关键字，说明函数就不是函数了

"""
步骤：
    1.定义一个函数
    2.调用函数，接受调用的结果
    3.得到的结果就是生成器
"""
# def func():
#     n =0
#     while True:
#         n+=1
#         yield n
# g = func()
#
# print(g)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

#菲波那切数列
def fib(length):
    a,b = 0,1
    n =0

    while n < length:
        print(b)
        yield b
        a, b = b,a+b
        n+=1
g = fib(10)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
