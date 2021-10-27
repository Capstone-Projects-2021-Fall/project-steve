import pyrebase


class FirebaseHelper:
    firebase = None

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

    # Parameters:
    #     - location is a string representing the name of building
    #
    # Description:
    #     - Posts the location name to Firebase
    #
    # Return:
    #     - Returns nothing
    def register_location(self, location):
        pass

    # Parameters:
    #     - location is a string representing the name of the building
    #     - route is a string that represents the name of the user’s destination
    #     - duration is an integer value that contains the time it takes to reach the destination
    #
    # Description:
    #     - Posts the route name to Firebase
    #
    # Return:
    #     - Returns nothing
    def register_route(self, location, route, duration):
        db = self.firebase.database()
        data = {"location": location, "route": route, "duration": duration}
        db.child("user").push(data)

    # Parameters:
    #     - location is a string representing the name of building
    #
    # Description:
    #     - Fetches a list of all routes at a given location on Firebase
    #
    # Return:
    #     - Returns an array of JSON Objects, which include:
    #         - Unique route ID
    #         - Route name
    #         - Active boolean
    #         - Duration integer
    def get_routes(self, location):
        pass

