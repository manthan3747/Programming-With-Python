#define LED_PIN 13

void setup() {
    Serial.begin(9600);
    pinMode(LED_PIN, OUTPUT);
}

void loop() {
    if (Serial.available() > 0) {
        String command = Serial.readStringUntil('\n');
        command.trim();

        if (command == "ON") {
            digitalWrite(LED_PIN, HIGH);
            Serial.println("LED Turned ON");
        } else if (command == "OFF") {
            digitalWrite(LED_PIN, LOW);
            Serial.println("LED Turned OFF");
        }
    }
}
