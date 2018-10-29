import time
import multiprocessing

def func():
    print('---子进程---start---',time.asctime(time.localtime(time.time())))
    time.sleep(5)
    print('---子进程---end---',time.asctime(time.localtime(time.time())))

print('---start---',time.asctime(time.localtime(time.time())))
p = multiprocessing.Process(target=func)    #实例化
p.start()   # 开启子进程
# p.join()    # 有我们调用的进程，阻塞等待对应子进程结束，子进程依然干自己的是
time.sleep(5)
p.join()      # 等待子进程结束  能保证子进程一定会结束，才会执行下面的代码

print('---end---',time.asctime(time.localtime(time.time())))
