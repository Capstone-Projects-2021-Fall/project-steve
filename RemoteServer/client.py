import csv
import sys

import requests,os,time
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

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
		pygame.init()
		key_input = pygame.key.get_pressed()
		
		sur_obj=pygame.display.set_mode((400,300))
		pygame.display.set_caption("Manual car control")
		
		fps = 10
		
		#initial values
		speed = 0.0
		turnVal = 90
		
		#increments
		turn_inc = 90/fps
		speed_int = .1/fps
		
		#limits
		speed_limit = .15
		speed_min = 0
		
		turncapL = 180
		turncapR = 0
		
		pressed = False
		
		#press q to exit
		#if an arrow key was pressed
		while not key_input[pygame.K_q]:
			pressed = False
			key_input = pygame.key.get_pressed()
			for eve in pygame.event.get():
				if eve.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
			#up arrowkey
			if key_input[pygame.K_UP]:
				pressed = True
				if(speed == 0):
					speed = .11
				else:
					speed += speed_int
			
			#down arrowkey
			if key_input[pygame.K_DOWN]:
				pressed = True
				if(speed == .11):
					speed = 0
				else:
					speed -= speed_int
			
			#left arrowkey
			if key_input[pygame.K_LEFT]:
				pressed = True
				turnVal += turn_inc
				
			#right arrowkey
			if key_input[pygame.K_RIGHT]:
				pressed = True
				turnVal -= turn_inc
			
			if pressed:
				speed = round(speed,4)
					
				speed = max(min([speed,speed_limit]),speed_min)
				turnVal = max(min(turnVal, turncapL),turncapR)
					
				print("Setting car values to ",speed, ",",turnVal)
				self.send_car_instructions(speed,turnVal)
				
			time.sleep(1/fps)
		
		#stop car upon exiting
		self.send_car_instructions(0,turnVal)
		
		print("Exiting manual control")
		pygame.quit()

	def execute_recorded_route(self, route_name):
		lines = []
		try:

			with open(str(route_name) + "/training_data.csv") as f:
				content = csv.reader(f)
				for line in content:
					lines.append(line)

			for i in range(len(lines)):
				speed = lines[i][0]
				turn_val = lines[i][1]
				self.send_car_instructions(speed, turn_val)
				time.sleep(.5)

		except:
			print("Route does not exist on Remote Server")


if __name__ == '__main__':
	client = Client("http://10.226.106.23", 5000)
	# client.start_manual_control()
	print('testing')
	# client.start_route("test")
	# client.start_manual_control()
	# client.execute_recorded_route()
	client.execute_recorded_route("blakes_room")
