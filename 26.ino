void setup() {
  pinMode(13, OUTPUT);  // Set LED pin as output
  Serial.begin(9600);   // Start Serial communication
}

void loop() {
  if (Serial.available()) { // Check if data is received
    char command = Serial.read(); // Read the received command
    if (command == '1') {
      digitalWrite(13, HIGH); // Turn ON LED
    } else if (command == '0') {
      digitalWrite(13, LOW);  // Turn OFF LED
    }
  }
}
