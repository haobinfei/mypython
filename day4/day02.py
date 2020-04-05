"""
继承
将相同的代码提取——————》 Person类
class Student（Person）：
    pass

特点：
    1. 如果类中不定义__init__, 调用suoer class的__init__
    2.如果类继承父类也需要自己定义__init__。就需要在当前类的__init__中调用父类的__init__
    3.如何调用父类的__init__
    4.如果父类与子类有相同的方法，默认找子类的方法
    5.子类的方法中也可以引用父类的方法
"""
# 定义相同信息的父类
class Person:
    # 定义基本信息
    def __init__(self,num,name,wage):
        self.__num = num
        self.__name = name
        self.wage = wage
    # 定义信息
    def __str__(self):
        return "工号：{} 名字：{} 工资：{}".format(self.__num,self.__name,self.wage)
    # 修改名字
    # def set_name(self,name):
    #     self.__name = name


    # 获取姓名
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.name = name

    # 获取员工号
    def get_num(self):
        return self.__num
# 定义 工人子类
class Worker(Person):

    def __init__(self,num,name,wage):
        super().__init__(num,name,wage)

    # 工人薪资方法
    def Wage(self,time,H_wage):
        self.wage = time*H_wage

# 定义销售员子类
class Salesman(Person):

    def __init__(self,num,name,wage):
        super().__init__(num,name,wage)

    # 销售员薪资
    def Wage(self,sales,commission):
        self.wage = sales*commission





    # def __init__(self, num, name, wage):
    #     super().__init__(num, name, wage)

    # def __str__(self):
    #     return "个人信息：姓名：{}  工号：{}  工资：{}".format(self.name,
    #                                              self.num,self.wage)

# 定义经理类
class Manager(Person):

    def __init__(self,num,name,wage):
        super().__init__(num,name,wage)

    # 经理薪资
    def Wage(self,wage):
        self.wage = wage

# 定义销售经理
class Salemanager(Person):

    def __init__(self,num,name,wage):
        super().__init__(num,name,wage)

    # 销售经理薪资
    def Wage(self,sales,commission,Fixed_wage):
        self.wage = sales*commission + Fixed_wage




