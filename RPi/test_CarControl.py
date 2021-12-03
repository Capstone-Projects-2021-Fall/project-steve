from unittest import TestCase
from CarControl import CarControl

carControl = CarControl()


class TestCarControl(TestCase):
    def test_set_speed(self):
        speed = .15
        carControl.set_speed(speed)
        self.assertEqual(carControl.get_speed(), speed)

    def test_get_speed(self):
        speed = carControl.get_speed()
        flag = False
        if 0 <= int(speed) <= .15:
            flag = True
        self.assert_(flag)

    def test_gradual_speed_up(self):
        init_speed = .10
        speed = .15
        carControl.set_speed(init_speed)
        carControl.gradual_speed_up(speed, .5)
        flag = False
        if init_speed <= carControl.get_speed() <= speed:
            flag = True
        self.assert_(flag)

    def test_set_turn_val(self):
        turn_val = 180
        carControl.set_turn_val(turn_val)
        self.assertEqual(carControl.get_turn_val(), turn_val)

    def test_get_turn_val(self):
        turn_val = carControl.get_turn_val()
        flag = False
        if 0 <= int(turn_val) <= 180:
            flag = True
        self.assert_(flag)

    def test_gradual_turn(self):
        init_turn_val = 0
        turn_val = 180
        carControl.set_turn_val(init_turn_val)
        carControl.gradual_turn(turn_val, .5)
        flag = False
        if init_turn_val <= carControl.get_turn_val() <= turn_val:
            flag = True
        self.assert_(flag)
