# -*- coding: utf-8 -*-
import json
import requests
from unittest import TestCase
from client import *

client = Client("http://10.226.107.151", 9999)


class TestClient(TestCase):
	def test_connection(self):
		# test that the server response is in the 200 range
		url = str(client.target_host) + ":" + str(client.target_port)
		response = requests.post(url)
		self.assert_(response)

	def test_send_status_update(self):
		# test that status updates are processed by the server
		request_body = {"speed": str(5), "turn_val": str(5), "image": None}
		url = str(client.target_host) + ":" + str(client.target_port) + "/receiveStatusUpdate"
		response = requests.post(url, data=request_body, headers={'Content-Type': 'application/octet-stream'})
		self.assertEqual(json.loads(response.content)["status"], "success")
