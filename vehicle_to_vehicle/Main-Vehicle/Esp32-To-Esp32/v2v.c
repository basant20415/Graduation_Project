#include <esp_now.h>
#include <WiFi.h>
#include <HardwareSerial.h>
#include <LiquidCrystal.h>

// LCD pin setup
LiquidCrystal lcd(19, 23, 18, 17, 16, 4);

// UART pins
#define RXD2 25
#define TXD2 26
HardwareSerial mySerial(2); // Serial2 for UART

// ESP-NOW receiver MAC address
uint8_t broadcastAddress1[] = {0xff, 0xff, 0xff, 0xff, 0xff, 0xff};

// Struct for ESP-NOW data
typedef struct struct_message {
  char object[32];
} struct_message;

struct_message outgoingMessage;

esp_now_peer_info_t peerInfo;

// ESP-NOW send callback
void DataSent(const uint8_t *mac_addr, esp_now_send_status_t status) {
  Serial.print("Send Status:\t");
  Serial.println(status == ESP_NOW_SEND_SUCCESS ? "Delivery Success" : "Delivery Fail");

  if (status == ESP_NOW_SEND_SUCCESS) {
    mySerial.println("ESP-NOW: Delivery Success");
  } else {
    mySerial.println("ESP-NOW: Delivery Failed");
  }
}

void setup() {
  Serial.begin(9600);
  mySerial.begin(9600, SERIAL_8N1, RXD2, TXD2);

  lcd.begin(16, 2);
  lcd.print("Waiting for Msg");

  WiFi.mode(WIFI_STA);

  if (esp_now_init() != ESP_OK) {
    Serial.println("Error initializing ESP-NOW");
    return;
  }
  esp_now_register_send_cb(DataSent);

  memcpy(peerInfo.peer_addr, broadcastAddress1, 6);
  peerInfo.channel = 0;
  peerInfo.encrypt = false;

  if (esp_now_add_peer(&peerInfo) != ESP_OK) {
    Serial.println("Failed to add peer");
    return;
  }

  Serial.println("ESP32 Ready");
  mySerial.println("ESP32 Ready and Listening");
}

void loop() {
  if (mySerial.available() > 0) {
    String input = mySerial.readStringUntil('\n');
    input.trim();

    Serial.println("Received from Pi: " + input);

    // Example input: "Object 1: Pothole, Avg Depth: 0.78 meters"
    int objIndex = input.indexOf(':');

    if (objIndex != -1) {
      String object = input.substring(objIndex + 1);
      object.trim();

      // Show on local LCD
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("Warnning:");
      lcd.setCursor(0, 1);
      lcd.print(object);  

      // Send via ESP-NOW
      strncpy(outgoingMessage.object, object.c_str(), sizeof(outgoingMessage.object));

      esp_now_send(broadcastAddress1, (uint8_t *)&outgoingMessage, sizeof(outgoingMessage));

      Serial.println("ESP-NOW message sent.");
      mySerial.println("ESP-NOW message sent.");
    } else {
      Serial.println("Invalid format");
      mySerial.println("Invalid format");
    }
  }

  delay(100);
}
