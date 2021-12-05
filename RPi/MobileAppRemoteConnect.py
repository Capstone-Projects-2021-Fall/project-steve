import pyrebase
from CarControl import CarControl


class MobileAppRemoteConnect:
    firebase = None
    db = None
    carControl = None

    def __init__(self):
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

        self.firebase = pyrebase.initialize_app(firebaseConfig)
        self.db = self.firebase.database()
        self.carControl = CarControl()

    def stream_handler(self, message):
        print("Stream Handler Started")
        data = message["data"]
        print(data)
        speed = data['speed']
        turn_val = data['turnVal']
        self.carControl.set_speed(speed)
        self.carControl.set_turn_val(turn_val)

    def register(self):
        self.db.child("car_data").stream(self.stream_handler)

if __name__ == '__main__':
    ac = MobileAppRemoteConnect()
    ac.register()



