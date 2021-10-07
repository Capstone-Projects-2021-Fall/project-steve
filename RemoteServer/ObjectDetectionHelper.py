class ObjectDetectionHelper:
    detector = None

    def __init__(self):
        self.detector = None

    # Parameters:
    #     - image is an image object
    #
    # Description:
    #     - Takes an image and processes it to determine two things. First it determines whether there is an obstacle
    #     in STEVE’s immediate vicinity. If it determines there is an obstacle,
    #     then it determines which direction STEVE should start turning to avoid it
    #
    # Return:
    #     - Returns an object that contains:
    #         - a Boolean value representing whether there is or isn’t an object present
    #         - a Boolean value representing which direction to turn in to avoid it (false for left, true for right)
    def detect_obstacle(self, image):
        pass
