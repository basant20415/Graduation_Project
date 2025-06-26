#include <esp_now.h>
#include <WiFi.h>
#include <LiquidCrystal.h>

// LCD pins (D7, D6, D5, D4, Enable, RS)
LiquidCrystal lcd(19, 23, 18, 17, 16, 15);

// Define UART pins for communication with Arduino
#define UART_TX_PIN 25  // TX
#define UART_RX_PIN 26  // RX 

// Define the struct used by the sender
typedef struct struct_message {
  char object[32];
} struct_message;

struct_message incomingData;

// Callback function for receiving ESP-NOW messages
void DataRecv(const esp_now_recv_info_t *recv_info, const uint8_t *data, int len)
{
  memcpy(&incomingData, data, sizeof(incomingData));

  Serial.println("Data received via ESP-NOW:");
  Serial.print("Object: ");
  Serial.println(incomingData.object);

  // Send 's' to Arduino over UART
  Serial2.write('S');

  // Display on LCD
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Warnning:");
  lcd.setCursor(0, 1);
  lcd.print(incomingData.object);
}

void setup() {
  Serial.begin(9600);

  // Initialize UART2 for Arduino communication
  Serial2.begin(9600, SERIAL_8N1, UART_RX_PIN, UART_TX_PIN);

  // Initialize LCD
  lcd.begin(16, 2);
  lcd.print("Waiting for Msg");

  // Initialize WiFi and ESP-NOW
  WiFi.mode(WIFI_STA);
  
  if (esp_now_init() != ESP_OK) {
    Serial.println("Error initializing ESP-NOW");
    lcd.clear();
    lcd.print("ESP-NOW Init Fail");
    return;
  }

  // Register the receive callback
  esp_now_register_recv_cb(DataRecv);
}

void loop() {
  // Nothing needed in loop
}
