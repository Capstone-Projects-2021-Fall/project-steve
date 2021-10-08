import requests


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
        request_body = {"route": route}
        url = str(self.target_host) + ":" + str(self.target_port) + "/startRoute"
        print(url)
        response = requests.post(url, json=request_body)
        print(response)

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
        request_body = {"speed": speed, "turn_val": turn_val}
        url = str(self.target_host) + ":" + str(self.target_port) + "/receiveCarInstructions"
        print(url)
        response = requests.post(url, json=request_body)
        print(response)


if __name__ == '__main__':
    client = Client("http://127.0.0.1", 5000)
    client.send_car_instructions(10, 20)
