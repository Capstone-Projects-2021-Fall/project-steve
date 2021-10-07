class Client:
    target_host = ''
    target_port = ''

    def __init__(self, target_host, target_port):
        self.target_host = target_host
        self.target_port = target_port

    # Parameters:
    #     - route is a String representing the name of a given route
    #
    # Description:
    #     - Sends a request to the RPi to start the route with the given name
    #
    # Return:
    #     - Returns nothing
    def start_route(self, route):
        pass

    # Parameters:
    #     - speed is a double between 0 and 1, 0 being not moving, 1 being moving at max speed
    #     - turnVal is a double between -1 and 1, 0 being straight, -1 being all the way left, 1 being all the way right
    #
    # Description:
    #     - Sends to the RPi the speed and turnVal that it would like the RPi to implement
    #
    # Return:
    #     - Returns nothing
    def send_car_instructions(self, speed, turn_val):
        pass
