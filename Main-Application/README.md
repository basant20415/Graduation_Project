# 📍 GPS Location & Triggered Alert Pipeline (C++)
This main application is the central controller of the system. It listens to GPS data and triggers all other subsystems (V2V, V2C, and OSM) when road damage is detected.

## 🔧 Features:
- Reads live GPS data over UART from a GPS module (parsing NMEA $GPGGA sentences).

- Converts NMEA to decimal coordinates (latitude and longitude).

- Checks if ai.txt is not empty (indicating road damage).

- If road damage is detected, the app:

  - Saves GPS coordinates to gps.txt

  - Launches the following subsystems in parallel:

  - uart: Sends alert to ESP32 (V2V).

  - mqtt: Sends alert to AWS IoT Core (V2C).

  - uart2: Sends emergency stop signal to Arduino.

  - request.py: Sends alert to Flask API for OpenStreetMap visualization.

- Clears ai.txt and gps.txt after processing to prevent duplicate alerts.

## 📁 Input Files:
- ai.txt: AI detection flag.

- GPS via /dev/ttyAMA3.

## 📤 Output Files:
- gps.txt: Stores current GPS coordinates when damage is detected.

