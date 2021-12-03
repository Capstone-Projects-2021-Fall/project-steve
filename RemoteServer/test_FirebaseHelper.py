from unittest import TestCase
from FirebaseHelper import FirebaseHelper
import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyCiBPkwDTFuiOrRtKc3ZKUAh_xwvSb8WSI",
    "authDomain": "steve-2efa6.firebaseapp.com",
    "databaseURL": "https://steve-2efa6-default-rtdb.firebaseio.com",
    "projectId": "steve-2efa6",
    "storageBucket": "steve-2efa6.appspot.com",
    "messagingSenderId": "650370236834",
    "appId": "1:650370236834:web:0bca880b2938e86c04f2fb",
    "measurementId": "G-LJ8TNR05TL"
    }

firebase = pyrebase.initialize_app(firebaseConfig)

firebaseHelper = FirebaseHelper()

class TestFirebaseHelper(TestCase):
    def test_register_location(self):
        location = "TESTREGISTERLOCATION"
        firebaseHelper.register_location(location)
        flag = False

        db = firebase.database()
        locations = db.child("location").get()

        s = ""
        for key, value in locations.val().items():
            s = s + value["location"] + ", "
            if value["location"] == location:
                flag = True

        print(s)
        self.assertTrue(flag)

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
        result = bool(firebaseHelper.get_routes("location"))
        print(firebaseHelper.get_routes("location"))
        self.assertTrue(result)

