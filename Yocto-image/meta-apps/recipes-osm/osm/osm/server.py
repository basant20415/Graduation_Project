import sys
sys.path.append('/home/root/python-packages')
sys.path.insert(0, '/home/root/python_packages')

from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)
DB_NAME = 'damages.db'

# Add damage to DB
def add_road_damage(latitude, longitude, damage_type, description):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO road_damage (latitude, longitude, type, description)
            VALUES (?, ?, ?, ?)
        ''', (latitude, longitude, damage_type, description))
        conn.commit()
    except sqlite3.IntegrityError:
        print("⚠️ Duplicate entry ignored.")
    finally:
        conn.close()

# Get all damage data
def get_all_damages():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT latitude, longitude, type, description FROM road_damage')
    rows = cursor.fetchall()
    conn.close()
    return rows

# Endpoint to receive GPS + damage info
@app.route('/api/add', methods=['POST'])
def api_add():
    data = request.get_json()
    add_road_damage(data['latitude'], data['longitude'], data['type'], data['description'])
    return jsonify({'status': 'success', 'message': 'Damage recorded'})

# Serve the map
@app.route('/')
def map_view():
    damages = get_all_damages()
    return render_template('map.html', damages=damages)

if __name__ == '__main__':
    app.run(host='0.0.0.0' , port=5000 ,debug=True)
