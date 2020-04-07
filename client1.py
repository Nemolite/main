import socket

host = 'localhost'
port = 9090
addr = (host,port)


sock = socket.socket()
sock.connect(addr)

sock.sendall(b'Hello, world')

data = sock.recv(1024)
sock.close()