import socket

# 完成非阻塞套接字实现并发服务器（同时服务多个客户端）
# 整体思路：吃满cpu，不要出闲置
# 实现cpu百分比的使用，我们空闲的时候再去干点别的
# 写一下如何在一个线程跟一个进程里面去做出我们的并发效果

server = socket.socket()    # 实例化，生成一个套接字
server.setblocking(False)   # 设置成非阻塞套接字
server.bind(('',6789))
server.listen(5)    # 开始监听

conn_list = []
while True:
    # 处理连接，生成对等连接套接字
    try:
        conn,addr = server.accept() # 非阻塞生成对等连接套接字
        conn.setblocking(False) # 设置非阻塞
        conn_list.append(conn)
    except BlockingIOError as error:
        pass

    del_list = [conn for conn in conn_list]
    for conn in del_list:
        try:
            recv_data = conn.recv(1024)
            if recv_data:
                print(recv_data)
                conn.send(recv_data)

            else:
                conn.close()
                conn_list.remove(conn)
        except BlockingIOError as error:
            pass
