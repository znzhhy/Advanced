import time
import multiprocessing


def func():
    print('---子进程---start---',time.asctime())
    print(multiprocessing.current_process())    # 打印当前进程
    print('---子进程---end---',time.asctime())

print('---start---',time.asctime())
p = multiprocessing.Process(target=func)    #实例化
p.start()   # 开启子进程
# p.join()    # 有我们调用的进程，阻塞等待对应子进程结束，子进程依然干自己的事
p.join()      # 等待子进程结束  能保证子进程一定会结束，才会执行下面的代码

print('---end---',time.asctime())
