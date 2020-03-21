import socket
a=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for data in [b'qiufeihong', b'how', b'are', b'you']:
    a.sendto(data, ('127.0.0.1', 9999))
    print(a.recv(1024).decode('utf-8'))
a.close()