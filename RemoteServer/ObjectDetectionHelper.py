import cv2
from matplotlib import pyplot as plt
import pathlib

import Adafruit_PCA9685
from adafruit_servokit import ServoKit
import time

from picamera import PiCamera
import time

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
        detected = False
        img = cv2.imread(image)
  
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  
        basePath = str(pathlib.Path().resolve()) + "/HaarCascade/"

        stop_data = cv2.CascadeClassifier('stop_data.xml')
        face_data = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        cat_data = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalcatface.xml')
        full_body_data = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')
        #lower_body_data = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_lowerbody.xml')
  
        found_stop = stop_data.detectMultiScale(img_gray, minSize =(20, 20))

        found_face = face_data.detectMultiScale(img_gray, minSize =(20, 20))

        found_cat = cat_data.detectMultiScale(img_gray, minSize =(20, 20))

        found_body = full_body_data.detectMultiScale(img_gray, minSize =(20, 20))

        #found_lower_body = lower_body_data.detectMultiScale(img_gray, minSize =(20, 20))
  
        amount_found = len(found_stop)
        amount_found += len(found_face)
        amount_found += len(found_cat)
        amount_found += len(found_body)
        #amount_found += len(found_lower_body)
 
        #found = [face_data, found_cat, lower_body_data]
        if amount_found != 0:
            detected = True
            #for i in range(found):
                #for (x, y, width, height) in found[i]:
          
                    #cv2.rectangle(img_rgb, (x, y), 
                                #(x + height, y + width), 
                                #(0, 255, 0), 5)
          
       # plt.subplot(1, 1, 1)
       # plt.imshow(img_rgb)
       # plt.show()
        return detected


if __name__ == '__main__':
    kit = ServoKit(channels=16)
    kit.continuous_servo[0].throttle = 0.15
    time.sleep(0.1)
    kit.continuous_servo[0].throttle = 0.12
    camera = PiCamera()

    object_detection_instructions = [
        {"speed": .12, "turn_val": 0},
        {"speed": .12, "turn_val": 180},
        {"speed": .12, "turn_val": 180},
        {"speed": .12, "turn_val": 90},
        {"speed": .12, "turn_val": 90},
        {"speed": .12, "turn_val": 90}
    ]

    while(True):
        image = "demo.jpg"
        camera.start_preview()
        camera.capture(image)

        detector = ObjectDetectionHelper()
        if detector.detect_obstacle("demo.jpg"):
            print("Detected")

            for i in range(len(object_detection_instructions)):
                speed, turn_val = object_detection_instructions[i]['speed'], object_detection_instructions[i]['turn_val']
                kit.continuous_servo[0].throttle = speed
                kit.servo[1].angle = turn_val
                time.sleep(.5)
            
            kit.continuous_servo[0].throttle = 0
            break

        else:
           kit.continuous_servo[0].throttle = 0.12
           print("Nothing Detected")
