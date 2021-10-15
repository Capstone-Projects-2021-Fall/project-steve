class FirebaseHelper:
    api_key = ''
    firebase_url = 'https://steve-2ecd9-default-rtdb.firebaseio.com/'

    def __init__(self, api_key, firebase_url):
        self.api_key = api_key
        self.firebase_url = firebase_url

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
        pass

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
