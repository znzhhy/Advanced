from threading import Thread
from queue import Queue
import random

q = Queue(5)
class Producer(Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            item = random.randint(0, 99)
            self.queue.put(item)    # 队列未满，向队列中存入数据
            print('生产者生产%s' % item)

class Consumer(Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
            while True:
                item = self.queue.get() # 只要列表不为空，就从列表中取出数据
                print('消费者消费%s' % item)
                # self.queue.task_done()  # 告诉队列，这个任务执行完成了

p = Producer(q)
c = Consumer(q)
p.start()
c.start()
p.join()
c.join()































# import time
# from threading import Thread
#
# a = 0
#
# def incr(n):
#    global a
#    for i in range(n):
#        a += 1
#
# def decr(n):
#     global a
#     for i in range(n):
#         a -= 1
#
# t1 = Thread(target=incr,args=(1000000,))
# t1.start()
# t2 = Thread(target=decr,args=(1000000,))
# t2.start()
# t1.join()
# t2.join()
# print(t1)

# 隔着进程用线程通讯同样用manager




# mgr = Manager() # 先开启一个子进程，并且返回一个用来与其通信的管理器
# shared_list = mgr.list()    # 在公共空间里开启一个list空间，就调用mgr的list方法
# # proxy 代理
#
# print(type(shared_list))
#
# def func(list_1):
#     list_1.append('aaa')
#
# p = Process(target=func,args=(shared_list,))
# p.start()
# p.join()
# print(shared_list)



# a = 1
#
# def fun():
#     global a    # 声明全局变量
#     a = 2   # 修改全局变量
#     print(a)
#
# p = Process(target=fun)
# p.start()
# p.join()    # 保证子进程执行完毕再执行以下代码
# print(a)    # 主进程
#


# 进程内存空间是独立得，互补影响
# 表面上只是变量不会被修改，深层考虑，这两个进程完全失去了联系。





























