from unittest import TestCase
from CameraControl import CameraControl

cameraControl = CameraControl()


class TestCameraControl(TestCase):

    def test_get_image(self):
        image = cameraControl.get_image()
        self.assert_(bool(image))
