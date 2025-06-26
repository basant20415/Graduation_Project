# ADVANCED ROAD SAFETY SYSTEM BASED ON V2V AND V2C
## 🔁 1. Requirements Analysis
Goal: Detect road damages and send alerts to nearby cars, the cloud (government), and visualize on a map.

Stakeholders: Smart car users,Non smart car users ,government agencies.

###Functional Requirements:

Detect potholes/cracks/fainted paintings/any object using YOLOv12.

Send alerts to:

Other vehicles (V2V via ESP-NOW).

AWS Cloud (V2C via MQTT over AWS IoT Core Broker).

Visualization interface (OpenStreetMap + Flask).

###Non-functional Requirements:

Real-time performance.

Secure transmission (TLS, certificates).

Low latency for alerts.

##🧠 2. System Design
Architecture:

Modular design with subsystems:

AI Subsystem (YOLO).

V2V Communication (ESP32 via ESP-NOW).

V2C Communication (AWS IoT Core).

Flask Server (Map + MongoDB).

Technology Stack:

Raspberry Pi (Python/C++).

ESP32 (Arduino/C++).

AWS IoT Core (MQTT).

MongoDB Atlas (Cloud DB).

Flask + Leaflet.js for map UI.

Data Flow:

Camera detects damage → AI confirms → GPS adds location.

Alert sent to:

Other vehicles (via UART).

AWS (MQTT).

Database (MongoDB).

Map updated via Flask API.

##💻 3. Implementation
Programming Languages:

C++ (main app + MQTT).

Python (Flask, AI inference).

JavaScript (Leaflet.js map).

Hardware Integration:

YOLO runs on Pi + webcam.

ESP32 UART code for V2V.

Secure communication (TLS + AWS certs).

Key Files:

main.cpp: Reads AI + GPS + sends MQTT.

flask_server.py: Receives data + renders map.

ESP32_rx.ino: Receives via UART.

Security:

TLS encryption.

IoT policies and certificates.

##🧪 4. Testing
Unit Testing:

AI detection accuracy.

GPS string parsing.

UART transmission.

Integration Testing:

AI + GPS + MQTT pipeline.

Flask + MongoDB + map markers.

System Testing:

Full end-to-end flow: detect → send → visualize.

Edge Case Testing:

No GPS signal.

No internet → local backup.

ESP32 not responding.

##🚀 5. Deployment
On Raspberry Pi:

Auto-run app on boot using systemd.

Custom image using Yocto.

Database:

MongoDB Atlas with static IP whitelisting.

Web Map:

Flask server accessible via public static IP or EC2.

Security:

Certificates uploaded to Pi.

Private key permissions restricted.

##📈 6. Maintenance & Future Work
Maintenance:

Fix AI false positives.

Monitor MQTT message delivery.

Future Enhancements:

Add SMS/email alerts.

Support for RSU (V2I).

Add data analytics dashboard.

Real-time speed control based on alerts.


