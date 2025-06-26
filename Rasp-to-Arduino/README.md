# 🛑 Emergency Stop Signal to Arduino (C++)
This lightweight C++ application is responsible for sending a stop signal ('s') to an Arduino board when road damage is detected by the AI system.

## 🔧 Features:
- Reads road damage status from ai.txt.

- If road damage is detected (ai.txt is not empty), it sends the character 's' via UART to the Arduino.

- Used to trigger an emergency stop or warning system on the car.

## ⚙️ Serial Communication:
- Uses UART port: /dev/ttyAMA4.

- Baud rate assumed to be 9600.

- Sends the character 's'.

