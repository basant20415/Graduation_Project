import requests

# Function to read coordinates from file (latitude and longitude separated by space)
def read_coordinates(file_path):
    coordinates = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:  # Skip empty lines
                lat, lon = line.split(' ', 1)  # Split on first space only
                coordinates.append((float(lat), float(lon)))
    return coordinates

# Modified function to read damage types from file (read only up to first space)
def read_damage_types(file_path):
    damage_types = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:  # Skip empty lines
                # Split on first space and take only the first part
                damage_type = line.split(' ', 1)[0]
                damage_types.append(damage_type)
    return damage_types

# Paths to your input files
coordinates_file = 'coordinates.txt'  # Format: "lat lon" on each line
damage_types_file = 'damage_types.txt'  # Format: "type description" on each line

# Read data from files
coordinates = read_coordinates(coordinates_file)
damage_types = read_damage_types(damage_types_file)

# Check if we have matching number of coordinates and damage types
if len(coordinates) != len(damage_types):
    print(f"Warning: Mismatch in data counts - {len(coordinates)} coordinates vs {len(damage_types)} damage types")

# Create damage reports
damage_reports = []
for (lat, lon), damage_type in zip(coordinates, damage_types):
    damage_reports.append({
        "latitude": lat,
        "longitude": lon,
        "type": damage_type,
        "description": f"{damage_type} detected at this location"
    })

# Send data to server
for damage in damage_reports:
    try:
        r = requests.post("http://localhost:5000/api/add", json=damage)
        print(r.json())
    except requests.exceptions.RequestException as e:
        print(f"Failed to send data for {damage}: {e}")