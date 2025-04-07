# Water Sensor/Detector Demo with LED
from machine import Pin, PWM  
import machine
import time

# Define GPIO pins
Water = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)  # Input for water sensor
LED = machine.Pin(21, machine.Pin.OUT)                         # Output for LED

while True:                        # Endless main loop
    if Water.value() == 1:         # Test if sensor detects water
        print("WET")               # If wet
        LED.value(1)               # Turn LED ON
    else:                          # If sensor does not detect water
        print("DRY")               # If dry
        LED.value(0)               # Turn LED OFF
    time.sleep(1)                  # Delay for 1 second
