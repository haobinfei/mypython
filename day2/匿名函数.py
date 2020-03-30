# 简化函数定义

# 格式  lambda  参数A， 参数B ： 运算
from functools import reduce

s = lambda a, b: a + b

print(s(1, 2))

s1 = lambda a, b: a * b

t = s1(2, 5)
print(t)


def func(x, y, func):
    print(x, y)
    s = func(x, y)
    print(s)


func(2, 4, lambda x, y: x + y)

# 作用
list1 = [{"a": 10, "b": 20}, {"a": 15, "b": 24}, {"a": 1, "b": 0}]

t = max(list1, key=lambda x: x["a"])

print(t)

list2 = (2, 4, 5, 6, 7, 8, 10)

result = map(lambda x: x + 2, list2)

print(list(result))

result = map(lambda x: x if x == 2 else x + 2, list2)

print(list(result))

result = reduce(lambda x, y: x + y, list2, 20)
print(result)

result = filter(lambda i: i % 2 == 0, list2)

print(list(result))

result = sorted(list1, key=lambda x: x["a"])
print(list(result))
