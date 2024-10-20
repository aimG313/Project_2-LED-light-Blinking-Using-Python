import serial
import time

# Replace with your Arduino's serial port (e.g., 'COM3' for Windows or '/dev/ttyUSB0' for Linux)
arduino_port = 'COM10'
baud_rate = 9600

# Connect to Arduino
arduino = serial.Serial(arduino_port, baud_rate, timeout=1)
time.sleep(2)  # Wait for the connection to initialize

# Function to control LED
def control_led(state):
    if state == "on":
        arduino.write(b'1')  # Send '1' to turn on LED
        print("LED turned ON")
    elif state == "off":
        arduino.write(b'0')  # Send '0' to turn off LED
        print("LED turned OFF")
    else:
        print("Invalid input")

# Main loop for user input
while True:
    user_input = input("Enter 'on' to turn LED on or 'off' to turn LED off (or 'exit' to quit): ").lower()
    if user_input == "exit":
        break
    control_led(user_input)

# Close the serial connection
arduino.close()
