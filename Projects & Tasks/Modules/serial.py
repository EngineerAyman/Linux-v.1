'''
PySerial Module:
The PySerial module is used for serial communication between a microcontroller and a computer.
Here's an example code for reading data from a serial port:
'''
import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

while True:
    data = ser.readline()
    print(data)