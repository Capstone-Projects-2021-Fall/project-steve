class CarControl:
    speed = 0
    turn_val = 0

    def __init__(self):
        pass

    # Parameters:
    #     - speed is double that will set the current rc car speed
    #
    # Description:
    #     - Set the current speed of the rc car to the given speed
    #
    # Return:
    #     - Returns nothing
    def set_speed(self, speed):
        pass

    # Parameters:
    #     - None
    #
    # Description:
    #     - Return current speed of the car
    #
    # Return:
    #     - Returns current speed as a double
    def get_speed(self):
        pass

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
        pass

    # Parameters:
    #     - turnVal is a double that will set the current direction of the car
    #
    # Description:
    #     - Change the direction of the car to the given angle
    #
    # Return:
    #     - Returns nothing
    def set_turn_val(self, turn_val):
        pass

    # Parameters:
    #     - None
    #
    # Description:
    #     - Return the turnVal value
    #
    # Return:
    #     - Returns turnVal, a double indicating the direction the car is facing
    def get_turn_val(self):
        pass

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
