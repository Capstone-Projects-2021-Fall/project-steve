from unittest import TestCase
from SpeakerControl import SpeakerControl

speakerControl = SpeakerControl()


class TestSpeakerControl(TestCase):

    def test_set_volume(self):
        volume = 50
        speakerControl.set_volume(volume)
        self.assertEqual(speakerControl.get_volume(), volume)

    def test_get_volume(self):
        volume = speakerControl.get_volume()
        flag = False
        if 0 <= volume <= 100:
            flag = True
        self.assert_(flag)

    def test_play_message(self):
        result = speakerControl.play_message("this is a test")
        self.assert_(result)
