import socket
from multiprocessing import Pool,cpu_count
from multiprocessing.pool import ThreadPool

server = socket.socket()
server.bind(('',5678))
server.listen(1000)
## 线程池
def work_thread(conn):
    while True:
        recv_data = conn.recv(1000)
        if recv_data:
            print(recv_data)
            conn.send(recv_data)

        else:
            conn.close()
            break

def work_process(server):
    t_pool = ThreadPool((2*cpu_count()))    # 开启线程池
    while True:
        conn,addr = server.accept()
        t_pool.apply_async(work_thread,args=(conn,))

n = cpu_count() # 获取cpu核心
p = Pool(n)    # 开启进程池
for i in range(n):
    p.apply_async(work_process,args=(server,))
p.close()
p.join()