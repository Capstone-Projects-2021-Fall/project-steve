import pyrebase
from SpeakerControl import SpeakerControl


class AlexaConnect():
    firebase = None
    db = None
    speaker = None

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
        self.speaker = SpeakerControl()


    def stream_handler(self, message):
        print("Stream Handler Started")
        print(message["data"])
        if (message["data"] == "test"):
            print("Message Received from Alexa")
            self.db.child("dummy").child("test").set("!!!!!")

            locations = self.db.child("route").get()
            routes = locations.val()

            s = ""
            for key, value in routes.items():
                s = s + value["name"] + ", "
            print("Now Speaking", s)
            self.speaker.play_message(s)

    def register(self):
        my_stream = self.db.child("dummy").child("test").stream(self.stream_handler)



if __name__ == '__main__':
    ac = AlexaConnect()
    ac.register()



