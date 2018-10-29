import socket

client = socket.socket()
number = int(input('请输入要连接的端口号：'))
client.connect(('127.0.0.1',number))

while True:
    mgs = input('请输入：')
    client.send(mgs.encode())
    data = client.recv(1024)
    print('客户端返回的数据：%s' % data.decode())