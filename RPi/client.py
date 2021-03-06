# -*- coding: utf-8 -*-
import requests
import pygame
from CameraControl import CameraControl
from CarControl import CarControl

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
        response = requests.post(url, data=request_body, headers={'Content-Type': 'application/octet-stream'})
        print(response)
        return response

    def send_training_data(self, route_name, speed, turn_val, image=None):
        request_body = {"route_name": str(route_name), "speed": str(speed), "turn_val": str(turn_val), "image": image}
        url = str(self.target_host) + ":" + str(self.target_port) + "/receiveTrainingData"
        print(url)
        response = requests.post(url, data=request_body, headers={'Content-Type': 'application/octet-stream'})
        print(response)
        return response

    def start_xbox_manual_control(self):
        carControl = CarControl()
        camera = CameraControl()

        finished_flag = False

        state_data = []

        pygame.init()

        pygame.joystick.init()
        clock = pygame.time.Clock()

        print
        pygame.joystick.get_count()
        _joystick = pygame.joystick.Joystick(0)
        _joystick.init()

        while 1:
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.JOYBUTTONDOWN:
                    print("Joystick button pressed.")
                    print(event)
                    if event.button == 7:
                        finished_flag = True
                if event.type == pygame.JOYAXISMOTION:
                    # print _joystick.get_axis(0)
                    # print event
                    if event.axis == 0:  # this is the x axis
                        print(event.value)
                    if event.axis == 5:  # right trigger
                        print(event.value)
            xdir = _joystick.get_axis(0)

            rtrigger = _joystick.get_axis(5)
            # deadzone
            if abs(xdir) < 0.2:
                xdir = 0.0
            if rtrigger < -0.9:
                rtrigger = -1.0

            # print([xdir, rtrigger])

            throttle = ((rtrigger + 1) / 2) * .15
            turn = ((xdir - 1) / -2) * 180

            print([turn, throttle])

            carControl.set_speed(float(throttle))
            carControl.set_turn_val(float(turn))

            state = [carControl.get_speed(), carControl.get_turn_val(), camera.get_image()]
            state_data.append(state)

            # self.send_status_update(carControl.get_speed(), carControl.get_turn_val(), camera.get_image())

            if finished_flag:
                break

            clock.tick(30)

        print("exited manual control")

        route_name = input("Enter the name of the route: ")

        for i in range(0, len(state_data)):
            print(state_data[i])
            self.send_training_data(route_name, state_data[i][0], state_data[i][1], state_data[i][2])

        pygame.quit()


if __name__ == '__main__':
    # camera = CameraControl()
    client = Client("http://10.226.107.151", 9999)
    # image = camera.get_image()
    # print(image)
    # client.send_status_update(5,6,image)
    client.start_xbox_manual_control()
