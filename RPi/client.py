import requests
from CameraControl import CameraControl

class Client:
    target_host = ''
    target_port = ''

    def __init__(self, target_host, target_port):
        self.target_host = target_host
        self.target_port = target_port

    # Parameters:
    #     - speed: The current speed of the STEVE car [0,1]
    #     - turnVal: The turn value to set the tires to [-1,1]
    #     - image: Python Image object
    #
    # Description:
    #     - Sends the state information (speed, turnVal, current camera FOV) from the STEVE
    #     car so the remote server can process them, and decide how to attenuate these values
    #
    # Return:
    #     - Returns a JSONObject containing:
    #     - status: either “OK” or “FAILED”
    def send_status_update(self, speed, turn_val, image=None):
        request_body = {"speed": str(speed), "turn_val": str(turn_val), "image": image}
        url = str(self.target_host) + ":" + str(self.target_port) + "/receiveStatusUpdate"
        print(url)
        response = requests.post(url, json=request_body)
        print(response)


if __name__ == '__main__':
    client = Client()
    camera = CameraControl()
    client.send_status_update(0, 0, camera.get_image())

