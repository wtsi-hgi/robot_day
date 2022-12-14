import time
from machine import Pin
from PicoAutonomousRobotics import KitronikPicoRobotBuggy
from time import sleep

buggy = KitronikPicoRobotBuggy()
led = Pin(25, Pin.OUT)

buggy.setLED(0, buggy.WHITE)
buggy.setLED(1, buggy.WHITE)
buggy.setLED(2, buggy.RED)
buggy.setLED(3, buggy.RED)
buggy.setBrightness(30)
buggy.show()

while True:
    buggy.motorOn('r', 'f', 10)
    buggy.motorOn('l', 'f', 100)
    distance = buggy.getDistance("f")
    if(distance < 1):
        red_channel = 0
        green_channel = 0
        blue_channel = 0
    elif(distance < 51): #0-50
        red_channel = 255
        green_channel = 5*distance
        blue_channel = 0
    elif(distance < 101): #51-100
        red_channel = 255-(5*(distance-51))
        green_channel = 255
        blue_channel = 0
    elif(distance < 150): #101 - 150
        red_channel = 0
        green_channel = 255
        blue_channel = (5*(distance-101))
    elif(distance < 201): #151-200
        red_channel = 0
        green_channel = 255-(5*(distance-151))
        blue_channel = 255
    else: #over 200
        red_channel = 0
        green_channel = 0
        blue_channel =255

    buggy.setLED(0,(int(red_channel),int(green_channel),int(blue_channel)))
    buggy.setLED(1,(int(red_channel),int(green_channel),int(blue_channel)))
    buggy.show()
    sleep(0.01)

