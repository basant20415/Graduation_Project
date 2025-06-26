# This Python script is a client that sends road damage data to a Flask server running on your computer
import requests
# You're using the requests library to make HTTP requests (like POST, GET) from Python.

# It allows you to send data to or retrieve data from web APIs.
damage_reports = [
    {
        "latitude": 30.124187,
        "longitude": 31.246448,
        "type": "Crack",
        "description": "Crack near bridge"
    },
    {
        "latitude": 30.126533,
        "longitude": 31.234144,
        "type": "Pothole",
        "description": "Large pothole on main road"
    },
    # Add more dictionaries here for more damages
]

for damage in damage_reports:
    r = requests.post("http://localhost:5000/api/add", json=damage)#Sends an HTTP POST request to this URL:
    # post request is used to sends data to server 
    # Flask will receive it on its /api/add route, if defined in your app like this:
    print(r.json())
#     r = ...
# Stores the response returned by the server in variable r.

# print(r.json())
# Prints the response from the server (e.g., a success message or inserted ID), assuming the response is JSON.


