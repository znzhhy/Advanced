from multiprocessing import Process,Manager
import random

m = Manager()   # 管理器实例化
q = m.Queue(5)  # 生成队列
class Producer(Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            item = random.randint(0, 99)
            self.queue.put(item)    # 队列未满，向队列中存入数据
            print('生产者生产%s' % item)

class Consumer(Process):
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