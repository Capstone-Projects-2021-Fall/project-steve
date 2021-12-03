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
        db = self.firebase.database()
        data = {"location": location}
        db.child("location").push(data)

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

        existing_routes = self.get_routes(location)
        flag = False

        for val in existing_routes:
            if existing_routes[val]['name'] == route:
                flag = True
                break

        if flag is False:
            data = {"location": location, "name": route, "duration": duration}
            db.child("route").push(data)
        else:
            print('Route already exists')

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
        db = self.firebase.database()
        locations = db.child("route").get()
        return locations.val()


if __name__ == '__main__':
    firebase_helper = FirebaseHelper()
    # firebase_helper.register_location("apartment")
    # firebase_helper.register_route("test", "route 3", 2)
    # firebase_helper.register_route("test", "route 4", 37)
    routes = firebase_helper.get_routes("location")

    print(routes)

    s = ""
    for key, value in routes.items():
        s = s + value["name"] + ", "

    print(s)

    # new_route = input("enter a route name: ")
    # firebase_helper.register_route("test location", new_route, 356)
