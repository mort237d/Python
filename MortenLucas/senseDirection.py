from sense_hat import SenseHat
import time
sense = SenseHat()

orientation = sense.get_orientation()

while True:
	"""pitch = orientation["pitch"]
	roll = orientation["roll"]
	yaw = orientation["yaw"]
	print("pitch {0} roll {1} yaw {2}".format(pitch, roll, yaw))
	"""	
	print(sense.orientation)
	time.sleep(1)
