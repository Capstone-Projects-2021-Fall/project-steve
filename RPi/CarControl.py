import Adafruit_PCA9685
from adafruit_servokit import ServoKit
import time


class CarControl:
    speed = 0
    turn_val = 0
    kit = None

    def __init__(self):
        self.speed = 0
        self.turn_val = 0
        self.kit = ServoKit(channels=16)

    # Parameters:
    #     - speed is double that will set the current rc car speed
    #
    # Description:
    #     - Set the current speed of the rc car to the given speed
    #
    # Return:
    #     - Returns nothing
    def set_speed(self, speed):
        if speed != 0 or speed < .11 or speed > .2:
            print('Invalid speed input, must be between .11 and .2')
        else:
            self.kit.continuous_servo[0].throttle = speed

    # Parameters:
    #     - None
    #
    # Description:
    #     - Return current speed of the car
    #
    # Return:
    #     - Returns current speed as a double
    def get_speed(self):
        return self.kit.continuous_servo[0].throttle

    # Parameters:
    #     - speed is a double that will set the current rc car speed
    #     - time is a double that indicates how long to take the turn
    #
    # Description:
    #     - Set the current speed of the RC car to the given speed, over the course of the given time
    #
    # Return:
    #     - Returns nothing
    def gradual_speed_up(self, speed, time):
        interval = 200  # ms
        step = (speed - self.get_speed()) / float((time / interval))
        while (self.get_speed() < speed):
            # placeholder servo object
            self.kit.continuous_servo[0].throttle += step
            if (self.kit.continuous_servo[0].throttle >= speed):
                self.kit.continuous_servo[0].throttle = speed
                return
            print("Set car speed to", self.kit.continuous_servo[0].throttle, "(+{0})".format(step))
            time.sleep(interval / 1000)

    # Parameters:
    #     - turnVal is a double that will set the current speed of the car
    #
    # Description:
    #     - Change the speed of the car to the given value
    #
    # Return:
    #     - Returns nothing

    def set_turn_val(self, turn_val):
        if turn_val > 180 or turn_val < 0:
            print('Invalid turning input, must be between 0 and 180')
        else:
            self.kit.servo[1].angle = turn_val

    # Parameters:
    #     - None
    #
    # Description:
    #     - Return the turnVal value
    #
    # Return:
    #     - Returns turnVal, a double indicating the direction the car is facing
    def get_turn_val(self):
        return self.kit.servo[1].angle

    # Parameters:
    #     - speed is a double that will set the current rc car speed
    #     - time is a double that indicates how long to take the turn
    #
    # Description:
    #     - Change the direction of the RC car over the given amount of time
    #
    # Return:
    #     - Returns nothing
    def gradual_turn(self, turn_val, time):
        pass
