import os
from flask import Flask, request

app = Flask(__name__,template_folder=os.getcwd())

@app.route('/',methods = ['POST', 'GET'])
def handle_request():
	if request.method == 'POST':
		print("Received post request")
	else:
		print("Received get request")
	print("Request headers: \n=========\n",request.headers,"\r========")
	print("Request data: ",request.get_data())
	
	#send greeting to client
	return "Welcome"
	
app.run("localhost",80,debug=False)
	