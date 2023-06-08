'''
GPIO (General Purpose Input/Output) Module:
The GPIO module is used to control the input and output pins of a microcontroller.
 Here's an example code for controlling a GPIO pin:
'''

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

while True:
    GPIO.output(18, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(18, GPIO.LOW)
    time.sleep(1)