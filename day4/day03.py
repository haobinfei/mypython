# 多态

class Person:
    def __init__(self,name):
        self.name = name

    def feed_pet(self,pet):
        print("{}喜欢养宠物{}".format(self.name,set))