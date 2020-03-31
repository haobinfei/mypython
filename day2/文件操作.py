#

stream = open(r'./aaa.txt')

container = stream.read()

print(container)

# open操作
"""
    read    读所有 
    readline 读一行
    readlines  将每一行转成列表
    readable  判断是否可读
"""

"""
写文件

mode = w
方法 ：
    write 先清空，再写
    
"""

with open(r'./aaa.txt', mode='rb') as stream:
    inner = stream.read()
with open(r'../day1/aaa.txt', mode='wb') as file:
    file.write(inner)
