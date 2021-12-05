from unittest import TestCase
from BehavioralCloningHelper import BehavioralCloningHelper

behavioralCloningHelper = BehavioralCloningHelper()


class TestBehavioralCloningHelper(TestCase):

    def test_train_model(self):
        result = behavioralCloningHelper.train_model(.12, 90, "steves_eyes.jpg")
        self.assert_(result)

    def test_get_instruction(self):
        result = behavioralCloningHelper.get_instruction(.12, 90, "steves_eyes.jpg")
        self.assert_(result)
