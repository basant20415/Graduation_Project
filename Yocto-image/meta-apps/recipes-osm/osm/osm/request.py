import requests

# Paths to the notification files
AI_FILE = "/home/root/main_app/ai.txt"
GPS_FILE = "/home/root/main_app/gps.txt"

# Extracts the damage type from the AI file (e.g., "Pothole")
def extract_damage_type(ai_file_path):
    try:
        with open(ai_file_path, 'r') as file:
            line = file.readline()
            if ',' in line:
                # "Object 1: Pothole, Avg Depth: 0.78 meters" -> "Object 1: Pothole"
                part = line.split(',')[0]
                # "Object 1: Pothole" -> "Pothole"
                if ':' in part:
                    return part.split(':')[1].strip()
                else:
                    return part.strip()
            else:
                return line.strip()
    except FileNotFoundError:
        print("❌ AI file not found.")
        return None

# Extract latitude and longitude from GPS file
def extract_gps_coordinates(gps_file_path):
    try:
        with open(gps_file_path, 'r') as file:
            line = file.readline().strip()
            if ',' in line:
                lat, lon = line.split(',', 1)
                return float(lat.strip()), float(lon.strip())
    except FileNotFoundError:
        print("❌ GPS file not found.")
    return None, None

# Main logic
damage_type = extract_damage_type(AI_FILE)
latitude, longitude = extract_gps_coordinates(GPS_FILE)

if damage_type and latitude and longitude:
    damage_report = {
        "latitude": latitude,
        "longitude": longitude,
        "type": damage_type,
        "description": f"{damage_type} detected on road"
    }

    try:
        response = requests.post("http://localhost:5000/api/add", json=damage_report)
        print("✅ Server response:", response.json())
    except Exception as e:
        print("⚠️ Error posting data:", e)
else:
    print("⚠️ Incomplete data. Skipping POST.")