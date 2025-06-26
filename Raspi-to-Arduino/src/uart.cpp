#include <iostream>
#include <fstream>
#include <fcntl.h>
#include <termios.h>
#include <unistd.h>
#include <string>

#define SERIAL_PORT "/dev/ttyAMA4"
#define AI_FILE     "/home/root/main_app/ai.txt"

// Send a character 's' to Arduino via UART
void sendMessageToArduino() {
    int serialPort = open(SERIAL_PORT, O_WRONLY | O_NOCTTY);
    if (serialPort == -1) {
        std::cerr << "❌ Error: Cannot open UART2!" << std::endl;
        return;
    }

    struct termios options;
    tcgetattr(serialPort, &options);
    options.c_cflag = CS8 | CLOCAL | CREAD;
    tcsetattr(serialPort, TCSANOW, &options);
    
    // Send the character 's'
    write(serialPort, "s", 1);
    write(serialPort, "\n", 1);  // Optional: add newline if needed

    std::cout << "📡 Sent to Arduino: s" << std::endl;
    close(serialPort);
}

// Read the entire file content (single-line or multi-line)
std::string readFile(const std::string &filePath) {
    std::ifstream file(filePath);
    std::string content;

    if (file.is_open()) {
        std::getline(file, content);  // Only first line
        file.close();
    } else {
        std::cerr << "⚠️ Error: Cannot open file " << filePath << std::endl;
    }

    return content;
}

int main() {
    std::cout << "✅ AI Notification Monitor Started..." << std::endl;

    std::string aiMessage = readFile(AI_FILE);

    if (!aiMessage.empty()) {
        sendMessageToArduino();
    }
    
    if (aiMessage.empty()) {
        std::cout << "🔍 No alerts detected. Waiting..." << std::endl;
    }

    return 0;
}
