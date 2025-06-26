# (Other Vehicle - ESP32 Receiver)
This ESP32 sketch is responsible for receiving V2V alerts from another ESP32 device via ESP-NOW and taking action:

## 🔧 Key Features:
- Receives road damage alerts (e.g., "Pothole", "Crack") over ESP-NOW.

- Displays the warning on an LCD screen connected to the ESP32.

- Sends a stop signal ('S') to an Arduino via UART to trigger a braking or control mechanism.

## 📟 LCD Display:
Shows Warning: followed by the type of detected object (e.g., pothole).

## 📤 UART Communication:
Sends 'S' to the Arduino immediately upon receiving a message, allowing the Arduino to act (e.g., stop the car).

## ⚙️ Technologies Used:
ESP-NOW for peer-to-peer communication.

UART (Serial2) for Arduino connection.