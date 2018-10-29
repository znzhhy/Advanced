import socket
from threading import Thread #导入多线程

server = socket.socket()
server.bind(('',7878))
server.listen(1000)

def fun(conn):
    # 线程的逻辑
    recv_data = conn.recv(1024) # 接收数据
    if recv_data:   #如果存在
        print(recv_data.decode())   # 打印出来
        conn.send(recv_data)    # 返回给客户端
    else:
        conn.close()    # 关闭端口

while True:
    conn,addr = server.accept() # 生成对等连接套接字
    t = Thread(target=fun,args=(conn,)) # 开个线程去服务
    t.start()   # 启动线程