import socket
import selectors

epoll_selector = selectors.EpollSelector()  # 如果是windows Def...

server = socket.socket()
server.bind(('',8888))
server.listen(1000)

def read(conn):
    recv_data = conn.recv(1024)
    if recv_data:
        print(recv_data)
        conn.send(recv_data)

    else:
        epoll_selector.unregister(conn)     # 取消注册
        conn.close()

def accept(server):
    conn,addr = server.accept()
    epoll_selector.register(conn,selectors.EVENT_READ,read)


epoll_selector.register(server,selectors.EVENT_READ,accept)

## 事件循环
while True:
    events = epoll_selector.select()    # 查询准备好的事件，返回列表
    for key,mask in events:
        callback = key.data # 吧 accept 取出来
        sock = key.fileobj  # 把准备好的客户端套接字取出来
        callback(sock)