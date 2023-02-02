import socket
myp = socket.SOCK_DGRAM
afn =socket.AF_INET
ip="192.168.43.49"
port=5678
s=socket.socket(afn,myp)
s.bind((ip,port))
x=s.recvfrom(1024)
print(x)
