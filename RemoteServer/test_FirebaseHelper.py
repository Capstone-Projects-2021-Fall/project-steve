from unittest import TestCase
from FirebaseHelper import FirebaseHelper

firebaseHelper = FirebaseHelper()

class TestFirebaseHelper(TestCase):
    def test_register_location(self):
        self.fail()

    def test_register_route(self):
        route = "TESTROUTE"
        firebaseHelper.register_route("testlocation", route, "20")
        flag = False

        routes = firebaseHelper.get_routes("location")
        s = ""
        for key, value in routes.items():
            s = s + value["name"] + ", "
            if value["name"] == route:
                flag = True

        print(s)
        self.assertTrue(flag)

    def test_get_routes(self):
        self.fail()
