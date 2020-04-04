"""
面向对象：
程序  现实中
对象  具体的事务

# 所有的类名要求首字母大写，多个单词使用驼峰式命名
    class 类名【父类（可以不写）】
        属性： 特征

        方法： 动作
"""

class Phone:
    brand = "xiaomi"
    price = "2000"
    type = "80"

    def call(self):
        print(self)
        print("正在打电话")
phone1 =Phone()
print(phone1.brand)
phone1.call()
phone2 = Phone()
phone2.call()



"""

类的方法
种类： 普通方法 类方法 静态方法  魔术方法
def 方法名（self【参数，参数】）：
    pass

"""