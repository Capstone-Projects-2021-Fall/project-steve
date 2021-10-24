from picamera import PiCamera
import time

class CameraControl:
    image = None
    camera = None

    def __init__(self):
        camera = PiCamera()


    # Parameters:
    #     - None
    #
    # Description:
    #     - Takes a real time image using the onboard camera
    #
    # Return:
    #     - an image
    def get_image(self):
        self.camera.start_preview()
        image = self.camera.capture("steves_eyes.jpg")

        with open(image, "rb") as image:
            f = image.read()
            b = bytearray(f)

        return b
