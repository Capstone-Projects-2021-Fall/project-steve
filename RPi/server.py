import os
from flask import Flask, request

app = Flask(__name__)


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
    # do whatever logic needed to process request
    return {"data": "somedata"}


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
    # do whatever logic needed to process request
    return {"data": "somedata"}



if __name__ == '__main__':

    # launch the app on localhost
    app.run(host='127.0.0.1', port=5000, debug=True)
