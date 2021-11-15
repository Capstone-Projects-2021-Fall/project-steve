import os
from flask import Flask, request
from CarControl import CarControl
from client import Client
import time
from CameraControl import CameraControl

app = Flask(__name__)
carControl = None
client = None


@app.route("/")
def hello_world():
    # default route, i.e. home page
    return "<p>Hello, World!</p>"


# Parameters:
#     - Route: A string containing an identifier for the requested route
#
# Description:
#     - Begins routing the STEVE car. The RPi will communicate with the Remote Server
#      to receive information about obstacles in the way of the car, as well as to
#      provide metadata about the current status of the route
#
# Return:
#     - Returns a JSONObject containing:
#     - status: either “OK” or “FAILED”
@app.route("/startRoute", methods=['POST'])
def start_route():
    request_data = request.get_json(silent=True)
    print(request_data)
    return {"status": "success"}


# Parameters:
#     - speed: The speed we should accelerate the STEVE car to [0,1]
#     - turnVal: The angle to set the tires to [-1,1]
#
# Description:
#     - Sets the appropriate pins on the RPi to attenuate speed and angle of the STEVE car’s tires
#
# Return:
#     - Returns nothing
@app.route("/receiveCarInstructions", methods=['POST'])
def receive_car_instructions():
    request_data = request.get_json(silent=True)
    print(request_data)
    speed = request_data['speed']
    turn_val = request_data['turn_val']
    carControl.set_speed(float(speed))
    carControl.set_turn_val(float(turn_val))
    # time.sleep(.2)                              # who knows if this actually does anything
    client.send_status_update(speed, turn_val, None)
    return {"status": "success"}


if __name__ == '__main__':
    carControl = CarControl()
    camera = CameraControl()
    client = Client("http://10.226.111.152", 9999)
    # launch the app on localhost
    app.run(host='0.0.0.0', port=5000, debug=True)
