from collections import OrderedDict

import pytest
from unittest import mock
from unittest.mock import Mock
from FirebaseHelper import FirebaseHelper


@mock.patch("FirebaseHelper.pyrebase")
def test_register_location(firebase):
    location = "Serc"
    expected_data = {"location": location}

    firebase.return_value = Mock()
    firebase_helper = FirebaseHelper()
    returned_data = firebase_helper.register_location(location)
    assert expected_data == returned_data


@mock.patch("FirebaseHelper.pyrebase")
def test_register_route(firebase):
    location = "Tech-Center"
    route = "root 3"
    duration = 45
    expected_data = {"location": location, "name": route, "duration": duration}

    firebase.return_value = Mock()
    firebase_helper = FirebaseHelper()
    returned_data = firebase_helper.register_route(location, route, duration)
    assert expected_data == returned_data


@mock.patch("FirebaseHelper.pyrebase")
def test_get_routes(firebase):
    firebase.return_value = Mock()
    firebase.database.child.get.val.return_value = OrderedDict([('-MoH-4uBXfOh5RzVaE87', {'duration': 356,
                                           'location': 'test location',
                                           'name': 'test route'})])
    firebase_helper = FirebaseHelper()
    expected_data = OrderedDict([('-MoH-4uBXfOh5RzVaE87', {'duration': 356,
                                           'location': 'test location',
                                           'name': 'test route'})])
    returned_data = firebase_helper.get_routes()
    assert expected_data == returned_data




