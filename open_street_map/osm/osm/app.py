from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB Atlas connection
MONGO_URI = "mongodb+srv://bassantehab60:o7kM0Wls0L1IFCgl@cluster0.acffgrk.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)
db = client["road_damage_db"]
collection = db["damages"]

# Add damage to MongoDB
def add_road_damage(latitude, longitude, damage_type):
    collection.insert_one({
        "latitude": latitude,
        "longitude": longitude,
        "type": damage_type
    })

# Get all damage data from MongoDB
def get_all_damages():
    return [(d["latitude"], d["longitude"], d["type"]) for d in collection.find()]

# Endpoint to receive GPS + damage info
@app.route('/api/add', methods=['POST'])
def api_add():
    data = request.get_json()
    add_road_damage(data['latitude'], data['longitude'], data['type'])
    return jsonify({'status': 'success', 'message': 'Damage recorded'})

# Serve the map
@app.route('/')
def map_view():
    damages = get_all_damages()
    return render_template('map.html', damages=damages)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
