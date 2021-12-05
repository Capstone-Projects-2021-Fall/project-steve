from unittest import TestCase
from ObjectDetectionHelper import ObjectDetectionHelper

objectDetectionHelper = ObjectDetectionHelper()


class TestObjectDetectionHelper(TestCase):

    def test_detect_obstacle(self):
        result = objectDetectionHelper.detect_obstacle("object_detection_test.jpg")
        self.assertTrue(result)
