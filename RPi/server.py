import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    # default route, i.e. home page
    return "<p>Hello, World!</p>"


@app.route("/sampleGetRequest", methods=['GET'])
def sample_get_request():
    # do whatever logic needed to retrieve data
    return {"data": "somedata"}


@app.route("/samplePostRequest", methods=['POST'])
def sample_post_request():
    request_data = request.get_json(silent=True)
    print(request_data)
    # do whatever logic needed to process request
    return {"data": "somedata"}


if __name__ == '__main__':

    # launch the app on localhost
    app.run(host='127.0.0.1', port=5000, debug=True)
