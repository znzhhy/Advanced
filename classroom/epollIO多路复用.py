# IO多路复用epoll来显示我们的并发服务器
import socket
import selectors # IO多路复用选择器的模块

epoll_selector = selectors.EpollSelector()  # 实例化一个和epoll通信的选择器
# epoll_selector = selectors.DefaultSelector()  #根据系统自动选择通信器
# windows 上面写并发并不强大，做并发都在linux系统上写

server = socket.socket()    # 生成监听套接字
server.bind(('',7788))
server.listen(1000) # 开始监听

def read(conn):
    recv_data = conn.recv(1024)
    if recv_data:
        print(recv_data)
        conn.send(recv_data)
    else:
        epoll_selector.unregister(conn) # 处理完数据不要再监控，则关闭监控
        conn.close()    # 关闭监听

def accept(server):
    conn,addr = server.accept() # 当有连接过来时生成对等连接套接字
    # 接收数据
    epoll_selector.register(conn,selectors.EVENT_READ,read) # 接收数据会阻塞，这里再注册事件

epoll_selector.register(server,selectors.EVENT_READ,accept) # 注册可读事件，当有连接过来则触发
# 这个事件当有链接过来的时候会被触发
# 注册事件的目的是不阻塞
# 上面写的代码不会主动执行，需要我们自己去查询，查出来后自行执行
# 有连接过来的时候，我们才可查询

while True: # epoll是惰性的，所以我们要自行查询，查出来自行执行回调函数
    events = epoll_selector.select()    # 查询所有已经准备好的事件
    for key,mask in events:  # 返回二元组的列表 取出拆包。、
        callback = key.data # 取出回调函数    不同的回调函数有不同的地址，执行不同的时间
        sock = key.fileobj  # 取出套接字
        callback(sock)
# epoll是惰性的，他自己不会主动调用，需要我们自行调用
# epoll写代码方式，与我们平时写代码习惯不一样，因为有回调函数
