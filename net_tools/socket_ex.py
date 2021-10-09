#  Address families
#  Socket.AF_INET      Internet protocol (IPv4)
#  socket.AF_INET6     Internet protocol (IPv6)
#  
#  Socket types
#  socket.SOCK_STREAM  Connection based stream (TCP)
#  socket.SOCK_DGRAM   Datagrams (UDP)

from socket import *
s = socket(AF_INET,SOCK_STREAM) 
s.connect(("127.0.0.1",8888))            # Connect
s.send("GET /index.html HTTP/1.0\n\n")   # Send request
data = s.recv(10000)                     # Get response
print (data)
