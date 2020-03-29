import io


#  闭包函数

def func(c, d):
    a = 100

    def inner_func():
        b = 99
        i = a + b + c + d
        print(i)

    return inner_func


x = func(2, 3)

x()

# 闭包的作用
# 1保存函数的状态

x1 = func(5, 6)
x1()


# 2 闭包函数-计数器

def generate_count():
    container = [0]

    def add_one():
        container[0] += 1
        print("这是第{}次调用".format(container[0]))
        return container
    def test():
        t = add_one()
        print(t)
    return test




counter = generate_count()

counter()

print(counter)
