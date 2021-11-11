import datetime
import json
import os
import pathlib

from flask import Flask, request
from flask_cors import CORS
from client import Client
from BehavioralCloningHelper import BehavioralCloningHelper
import urllib.parse
import base64

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
client = None

b = BehavioralCloningHelper()

@app.route("/")
def hello_world():
	# default route, i.e. home page
	return "<p>Hello, STEVE!</p>"


# Parameters:
# - route is a String representing the name of a given route
#
# Description:
# - Receives & processes a request from an HMI (either the mobile app
#   or Amazon Alexa enabled device) to the route with the given name
#
# Return:
# - Returns a JSONObject containing:
# 	-status: either “OK” or “FAILED”
@app.route("/beginRouteRequest", methods=['POST'])
def begin_route_request():
	request_data = request.get_json(silent=True)
	print(request_data)
	# do whatever logic needed to process request
	return {"data": "somedata"}


# Parameters:
# - speed is a double between 0 and 1, 0 being not moving, 1 being moving at max speed
# - turnVal is a double between -1 and 1, 0 being straight, -1 being all the way left, 1 being all the way right
# 	- image is an image object
#
# Description:
# - Receives the state information (all of the parameters) of the RC car
#   so it can process the information & decide on what instructions to give next
#
# Return:
# - Returns a JSONObject containing:
# 	-status: either “OK” or “FAILED”
@app.route("/receiveStatusUpdate", methods=['POST'])
def receive_status_update():
  data = request.get_data().split(b'&')
  speed_byte = data[0].split(b'=')
  speed = speed_byte[1].decode("utf-8")
  print(speed)

  turn_val_byte = data[1].split(b'=')
  turn_val = turn_val_byte[1].decode("utf-8")
  print(turn_val)

  image_byte = data[2].split(b'=')
  image = urllib.parse.unquote(str(image_byte[1]))
  # print(bytes(image[2: len(image) - 1], 'utf-8'))

  image_64_decode = base64.decodebytes(bytes(image[2: len(image) - 1], 'utf-8'))
  image_result = open('steves_eyes.jpg', 'wb')
  image_result.write(image_64_decode)

  #     datafile = open('data.txt', 'a')
  #     print("speed: " + str(speed), file=datafile)
  #     print("turn_val: " + str(turn_val), file=datafile)
  #     datafile.close()

  return {"status": "success"}


@app.route("/receiveTrainingData", methods=['POST'])
def receive_training_data():
  data = request.get_data().split(b'&')

  route_name_byte = data[0].split(b'=')
  route_name = route_name_byte[1].decode("utf-8")
  print(route_name)

  speed_byte = data[1].split(b'=')
  speed = speed_byte[1].decode("utf-8")
  print(speed)

  turn_val_byte = data[2].split(b'=')
  turn_val = turn_val_byte[1].decode("utf-8")
  print(turn_val)

  image_byte = data[3].split(b'=')
  image = urllib.parse.unquote(str(image_byte[1]))

  image_64_decode = base64.decodebytes(bytes(image[2: len(image) - 1], 'utf-8'))

  route_path = str(pathlib.Path().resolve()) + "/" + route_name
  if os.path.exists(route_path) is False:
      os.makedirs(route_path)
  if os.path.exists(route_path + "/images") is False:
      os.makedirs(route_path + "/images")
  datetime_string = str(datetime.datetime.now())
  datetime_string = datetime_string.replace(" ", "")
  full_image_path = route_path + '/images/steves_eyes_' + datetime_string + '.jpg'

  image_result = open(full_image_path, 'wb')
  image_result.write(image_64_decode)

  b.save_to_csv(speed, turn_val, full_image_path, route_name)

  return {"status": "success"}


@app.route("/controlCar", methods=['POST'])
def control_car():
	speed = request.form.get("speed")
	turn_val = request.form.get("turnVal")
	client.send_car_instructions(speed, turn_val)
	print(speed)
	print(turn_val)
	return {"status": "success"}


if __name__ == '__main__':
	client = Client("http://10.226.104.248", 5000)
	# launch the app on localhost
	app.run(host='0.0.0.0', port=9999, debug=True)
