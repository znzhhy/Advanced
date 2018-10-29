import time
import multiprocessing


def func():
    print('---子进程---start---',time.asctime())
    time.sleep(5)   # 打印当前进程
    print('---子进程---end---',time.asctime())

print('---start---',time.asctime())
p = multiprocessing.Process(target=func)    #实例化
p.start()   # 开启子进程
time.sleep(2)
p.terminate()   # 终止子进程

print('---end---',time.asctime())
