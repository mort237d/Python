BROADCAST_TO_PORT = 11011
import time
from socket import *
from datetime import datetime
from sense_hat import SenseHat

sense = SenseHat()

g = (0, 255, 0) # Green
b = (0, 0, 0) # Black

i = 0

creeper_pixels = [
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, b, b, g, g, b, b, g,
    g, b, b, g, g, b, b, g,
    g, g, g, b, b, g, g, g,
    g, g, b, b, b, b, g, g,
    g, g, b, b, b, b, g, g,
    g, g, b, g, g, b, g, g
]

sense.clear()

s = socket(AF_INET, SOCK_DGRAM)
#s.bind(('', 14593))     # (ip, port)
# no explicit bind: will bind to default IP + random port
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
while True:
	creeper_pixels[i] = b
	sense.set_pixels(creeper_pixels)
	data = "Current time " + str(datetime.now()) + " Morten"
	s.sendto(bytes(data, "UTF-8"), ('<broadcast>', BROADCAST_TO_PORT))
	print(data)
	time.sleep(.2)
	i = i + 1
	if i == 64:
		quit()
