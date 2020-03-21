import socket
a=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
a.bind(('127.0.0.1',9999))
print('绑定9999端口')
while True:
    data,addr=a.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    a.sendto(b'Hello, %s!' % data, addr)