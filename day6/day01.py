# 正则表达式

import re

s= "娜扎迪丽热巴佟丽娅"
# match 只匹配开头位置
result = re.match("娜扎",s)
print(result)
print(result.span())
print(result.group())

# search 匹配所有位置
result = re.search("佟丽娅",s)
print(result)
print(result.span())
print(result.group())

# findall 匹配到一个继续匹配
msg = "masniuhd1389ur78whvyhw8f784yfy8rviwhiu73yr87y8fe"

result = re.findall("[a-z][0-9]+[a-z]",msg)
print(result)
"""
不需要引用分组的内容
    result = re.match(r"<[0-9a-zA-Z]+>(.+)<[0-9a-zA-Z]+>$")
    print(result)
    print(result.group(1))
引用分组匹配内容
    1.number
        msg = "<html><h1>abc</hi></html>"
        result = re.match(r"<([0-9a-zA-Z])><([0-9a-zA-Z])>().+</\1></\2>")
        print(result)
    2.?P<名字>
        result = re.match(r"<(?P<name1>[0-9a-zA-Z])><(?P<name2>[0-9a-zA-Z])>().+<?P=name2><?P=name1>")

"""

result = re.sub(r"\d+","100","java=2000,py=1000")
print(result)

"""
re 模块
    
    match 
    search
    findall
    group
    sub(替换)
    split(切割)
"""
