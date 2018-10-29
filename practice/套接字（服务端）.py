import socket

server = socket.socket()
server.bind(('',5522))
server.listen(5)

while True:
    conn, addr = server.accept()                #生成对等连接套接字
    while True:
        recv_data = conn.recv(1024)
        if recv_data:                           #只要有数据，recv_date 就为true
            print(recv_data)
            conn.send(recv_data)                #把接收到的数据发给客户端
        else:
            conn.close()
            break









