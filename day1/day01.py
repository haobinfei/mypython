a = 11


def func():
    b = 2

    def inmer_func():
        nonlocal b
        global a
        c = 88
        a += 1
        print(globals())
        print(locals())
        print(a, b, c)

    inmer_func()


func()
