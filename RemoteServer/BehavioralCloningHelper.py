class BehavioralCloningHelper:
    model = None
    target_port = None

    def __init__(self):
        self.model = None
        self.target_port = None

    # Parameters:
    #     - speed is a double between 0 and 1, 0 being not moving, 1 being moving at max speed
    #     - turnVal is a double between -1 and 1, 0 being straight, -1 being all the way left, 1 being all the way right
    #     - image is an image object
    #
    # Description:
    #     - Observing all parameters to train the model in order to replicate the state later
    #
    # Return:
    #     - Returns nothing
    def train_model(self, speed, turn_val, image):
        pass

    # Parameters:
    #     - speed is a double between 0 and 1, 0 being not moving, 1 being moving at max speed
    #     - turnVal is a double between -1 and 1, 0 being straight, -1 being all the way left, 1 being all the way right
    #     - image is an image object
    #
    # Description:
    #     - Takes in the current state and uses the trained model to determine what its next state should be
    #
    # Return:
    #     - Returns a JSON Object that contains:
    #         - speed which is a double
    #         - turnVal which is a double
    def get_instruction(self, speed, turn_val, image):
        pass
