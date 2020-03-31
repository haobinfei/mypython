# 语法错误可以避免
#异常需要做处理
"""
try :
    可能出现异常的代码
except：
    如果有异常执行的代码
finally：(让代码结束)
    无论是否有异常，都会执行


格式：
try:

except 错误类型  as  err:
    print（err）
"""
    # try:
    #     a = int(input())
    #     b=int(input())
    #     def chu():
    #         return a/b
    #     chu()
    # except:
    #     print("请输入整数")

def refister():
    username = input("请输入用户名")
    if len(username) < 6:
        raise Exception("用户长度必须大于6")
    else:
        print(username)

try:
    refister()
except Exception as err:
    print(err)
    print("注册失败")
else:
    print("注册成功")