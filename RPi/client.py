class Client:
    target_host = ''
    target_port = ''
    camera = None

    def __init__(self, target_host, target_port):
        self.target_host = target_host
        self.target_port = target_port

    # Parameters:
    # - speed: The current speed of the STEVE car [0,1]
    # -turnVal: The turn value to set the tires to [-1,1]
    # -image: Python Image object
    #
    # Description:
    # - Sends the state information (speed, turnVal, current camera FOV) from the STEVE
    #   car so the remote server can process them, and decide how to attenuate these values
    #
    # Return:
    # - Returns a JSONObject containing:
    # -status: either “OK” or “FAILED”
    def send_status_update(self, speed, turn_val, image):
        pass
