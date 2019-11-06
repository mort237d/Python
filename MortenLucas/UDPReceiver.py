from socket import *
from sense_hat import SenseHat

sense = SenseHat()

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('',11011))

while True:
	data = s.recvfrom(1024)
	print(data[0])
