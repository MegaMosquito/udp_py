import socket

UDP_PORT = 5999
BROADCAST = "255.255.255.255"
UDP_IP = BROADCAST
MESSAGE = "Hello, World!"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

