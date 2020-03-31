# 类表推导式

# 1.列表推导式 ： 格式  ：[表达式 for 变量 in 旧列表]

names = ["tom", "lili", "daming", "qiangge"]

result = [name for name in names if len(name)>3]

print(result)
result = [name.capitalize() for name in names if len(name)>3]
print(result)

new_num = [i for i in range(0,101) if i % 3 ==0 ]

print(new_num)

new_num = [(x,y) for x in range(0,6) if x%2==0 for y in range(0,11) if y%2 != 0 ]

print(new_num)

list1 = {"name": "tom", "salary": 3000}
list2 = {"name": "lili", "salary": 13000}
list3 = {"name": "jier", "salary": 23000}
list4 = {"name": "aj", "salary": 33000}

list_lod = [list1,list2,list3,list4]
list_new = [emp["salary"] + 2000 if emp["salary"] < 15000 else emp["salary"] -2000 for emp in list_lod ]


print(list_new)

# 集合推导式

list10 = [1,2,3,4,5,4,3,2,1]

set1 = {x+1 for x in list10 if x > 2}
print(set1)

# 字典推导式

dict10 = {"a": 10 , "b": 20, "c" : 30,"d":40}

dict_new = {value:key  for key,value in dict10.items()}
print(dict_new)
