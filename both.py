import socket
import sys
import threading
import time

UDP_PORT = 5999
BIND_ALL = "0.0.0.0"
BROADCAST = "255.255.255.255"
BUFFER_SIZE = 1024

DATA = "Hello, World!"

class UdpListenThread(threading.Thread):
  def run(self):
    print("LISTENER started!")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Binding to address {}, port {}.".format(BIND_ALL, UDP_PORT))
    sock.bind((BIND_ALL, UDP_PORT))
    print("Listening...")
    while True:
      data, address = sock.recvfrom(BUFFER_SIZE)
      print("Received from {}: \"{}\".".format(address, data.decode('UTF-8')))
      # To Do ...  convert address and data ino JSOn and insert into array

class UdpPublishThread(threading.Thread):
  def run(self):
    print("PUBLISHER started!  data: \"{}\"".format(self.getName()))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.settimeout(5)
    data = self.getName()
    while True:
      print("Sending to {}, port {}: \"{}\".".format(BROADCAST, UDP_PORT, self.getName()))
      sock.sendto(data.encode(), (BROADCAST, UDP_PORT))
      time.sleep(10)

if __name__ == '__main__':
  udp_listener = UdpListenThread()
  udp_publisher = UdpPublishThread(name = DATA)
  udp_listener.start()
  udp_publisher.start()
  udp_listener.join()
  udp_publisher.join()





