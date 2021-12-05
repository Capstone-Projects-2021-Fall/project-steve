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
		result = client.send_status_update(.12, 90, "000000000")
		self.assertEqual(result["status"], "success")
