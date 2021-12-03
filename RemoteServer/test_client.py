# -*- coding: utf-8 -*-
import json
import requests
from unittest import TestCase
from client import *

client = Client("http://10.226.106.23", 5000)


class TestClient(TestCase):

    def test_start_route(self):
        result = client.start_route("blakes_room")
        self.assertEqual(result.status, "success")

    def test_send_car_instructions(self):
        result = client.send_car_instructions(.12, 90)
        self.assertEqual(result.status, "success")
