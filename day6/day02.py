# 进程的创建

from multiprocessing import Process
from time import sleep

time = 0

def task(s,name):
    global time
    print("这个进程的名字是{}".format(name))
    while True:
        sleep(s)
        time +=1
        print("这是第{}次打印".format(time))

def task1(s,name):
    global time
    print("这个进程的名字是{}".format(name))
    while True:
        sleep(s)
        time +=1
        print("这是第{}次打印".format(time))

if __name__ == "__main__":
    pid1 = Process(target=task,name="任务1",args=[2,"任务1"])
    pid1.start()

    pid2 = Process(target=task1,name="任务2",args=[1,"任务2"])
    pid2.start()