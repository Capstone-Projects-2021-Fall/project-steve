from unittest import TestCase
import server


class TestServer(TestCase):

    def test_start_route(self):
        result = server.start_route()
        self.assertEqual(result.status, "success")

    def test_receive_car_instructions(self):
        result = server.receive_car_instructions()
        self.assertEqual(result.status, "success")
