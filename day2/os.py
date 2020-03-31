# os.path

"""
os.path:
    os.path.dirname
    os.path.join
    os.path.isabs
    os.path.abspath  获取其他文件绝对路径
    os.path.abspath(__file__) 获取当前文件绝对路径
    os.path.split  切割文件与目录
    os.path.splitext 获取文件扩展名
    os.path.getsize 获取文件大小，返回字节

    os.getcwd  == os.path.dirname
"""
import os

print(os.path)
print(os.path.dirname(__file__))

dirname = os.path.dirname(__file__)

print(os.path.join(dirname, 'bbb.txt'))

"""
os 模块的方法
    os.getcwd 获取当前目录
    os.listdir 浏览文件夹
    os.mkdir 创建文件夹
    os.remove 删除文件
    os.rmdir 删除文件夹
    os.chdir 切换文件夹
    
"""
# path = os.path.dirname('day2')
# print(path)
# mudi_file = os.path.join(path,'day1')

# os.remove(r'../day1/aaa.txt')
