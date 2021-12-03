from unittest import TestCase
import server


class TestServer(TestCase):

    def test_begin_route_request(self):
        result = server.begin_route_request()
        self.assertEqual(result.status, "success")

    def test_receive_status_update(self):
        result = server.receive_status_update()
        self.assertEqual(result.status, "success")
