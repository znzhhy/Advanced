import time
import multiprocessing

def fun():
    print('start',time.asctime())
    time.sleep(5)
    print('end',time.asctime())

p = multiprocessing.Process(target=fun) # 实例化进程对象
p.start()   # 真正调用fun函数的是进程里的run方法
time.sleep(5)
print('外层end',time.asctime())
