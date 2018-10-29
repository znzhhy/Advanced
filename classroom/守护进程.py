# import multiprocessing
# import time
#
# def func():
#     while True:
#         print('--我是子进程--')
#
# p = multiprocessing.Process(target=func,daemon=True)    # 把这个进程变成守护进程
# p.start()
# time.sleep(3)
#

 # 面向对象化的意义所在
 # 继承
 # 重写

from multiprocessing import Process

# def func(a,b):
#     print(a + b)
#
#
# p = multiprocessing.Process(target=func,args=(6,7))
# p.start()

class MyProcess(Process):
    def __init__(self,a,b):
        super().__init__()
        self.a = a
        self.b = b

    def run(self):
        print(self.a + self.b)

p = MyProcess(5,8)
p.start()
#第一步实例化是传参
#第二步直接调用start就可以完成项目的执行









