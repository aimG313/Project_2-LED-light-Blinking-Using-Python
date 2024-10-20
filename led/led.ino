int ledPin = 7; // Built-in LED pin

void setup()
{
  pinMode(ledPin, OUTPUT); // Set pin mode
  Serial.begin(9600);      // Start serial communication at 9600 baud rate
}

void loop()
{
  if (Serial.available() > 0)
  {
    char input = Serial.read(); // Read the input from the serial port
    if (input == '1')
    { // If input is '1', turn on the LED
      digitalWrite(ledPin, HIGH);
    }
    else if (input == '0')
    { // If input is '0', turn off the LED
      digitalWrite(ledPin, LOW);
    }
  }
}
