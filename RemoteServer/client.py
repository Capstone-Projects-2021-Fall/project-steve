import requests
import steve_util

class Client:
	target_host = ''
	target_port = ''

	def __init__(self, target_host, target_port):
		self.target_host = target_host
		self.target_port = target_port

	# Parameters:
	#	 - route is a String representing the name of a given route
	#
	# Description:
	#	 - Sends a request to the RPi to start the route with the given name
	#
	# Return:
	#	 - Returns nothing
	def start_route(self, route):
		request_body = {"route": route}
		url = str(self.target_host) + ":" + str(self.target_port) + "/startRoute"
		print(url)
		response = requests.post(url, json=request_body)
		print(response)

	# Parameters:
	#	 - speed is a double between 0 and 1, 0 being not moving, 1 being moving at max speed
	#	 - turnVal is a double between -1 and 1, 0 being straight, -1 being all the way left, 1 being all the way right
	#
	# Description:
	#	 - Sends to the RPi the speed and turnVal that it would like the RPi to implement
	#
	# Return:
	#	 - Returns nothing
	def send_car_instructions(self, speed, turn_val):
		request_body = {"speed": speed, "turn_val": turn_val}
		url = str(self.target_host) + ":" + str(self.target_port) + "/receiveCarInstructions"
		print(url)
		response = requests.post(url, json=request_body)
		print(response)
		
		
	def start_manual_control(self):
		print("Starting manual control. Press q to exit.")
		getch = steve_util.Getch()
		key = ''
		
		#initial values
		speed = 0.0
		turnVal = 90
		
		#increments
		turn_inc = 45
		speed_int = .01
		
		#limits
		speed_limit = .15
		speed_min = 0
		
		turncapL = 180
		turncapR = 0
		
		keymap = {b'P':"back",b'H':"forward",b'K':"left",b'M':"right"}
		
		#press q to exit
		while key != b'q':
			key = getch()
			#if an arrow key was pressed
			if key == b'\xe0':
				direction = keymap[getch()]
				
				#up arrowkey
				if(direction == "forward"):
					if(speed == 0):
						speed = .11
					else:
						speed += speed_int
				
				#down arrowkey
				if(direction == "back"):
					if(speed == .11):
						speed = 0
					else:
						speed -= speed_int
				
				#left arrowkey
				if(direction == "left"):
					turnVal += turn_inc
					
				#right arrowkey
				if(direction == "right"):
					turnVal -= turn_inc
					
				speed = round(speed,4)
					
				speed = max(min([speed,speed_limit]),0)
				turnVal = max(min(turnVal, 180),0)
					
				print("Setting car values to ",speed, ",",turnVal)
				self.send_car_instructions(speed,turnVal)
				
			else:
				print("Received unhandled key input: ",chr(key[0])) if key != b'q' else None
			
		#stop car upon exiting
		self.send_car_instructions(0,turnVal)
		
		print("Exiting manual control")


if __name__ == '__main__':
	client = Client("http://10.226.109.23", 5000)
	# client.start_manual_control()
	print('testing')
	client.start_route("test")
