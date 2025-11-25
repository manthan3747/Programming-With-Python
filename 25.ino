int x;
void setup()
    {Serial.begin(115200);
    Serial.setTimeout(1);
    pinMode(2,OUTPUT);
}

void loop() {
    while (!Serial.available());
    x = Serial.readString().toInt();
    Serial.print(x + 1);
}
