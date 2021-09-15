import os, requests

headers = requests.utils.default_headers()
data = {"xyz":123}

req = requests.post("http://localhost/",headers=headers,data=data)

if(req):
	print(req.content)
else:
	print("Connection failed")
