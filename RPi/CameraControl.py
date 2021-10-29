from picamera import PiCamera
import time
import base64

class CameraControl:
    image = None
    camera = None

    def __init__(self):
        self.camera = PiCamera()


    # Parameters:
    #     - None
    #
    # Description:
    #     - Takes a real time image using the onboard camera
    #
    # Return:
    #     - an image
    def get_image(self):
        image = "steves_eyes.jpg"
        self.camera.start_preview()
        self.camera.capture(image)

        with open(image, 'rb') as f:
            im_bytes = f.read()

        im_b64 = base64.encodebytes(im_bytes)
        return im_b64
