# A  basic 'free roaming' robot
# uses the FRont and rear ultrasonic sensors to avoid obstacles
# if an ultrasonic is not fitted it will return -1
#uses the onboard button for a start / stop command via an IRQ.

from PicoAutonomousRobotics import KitronikPicoRobotBuggy
from time import sleep, sleep_ms

buggy = KitronikPicoRobotBuggy()
startStop = False

def ButtonIRQHandler(pin):
    global startStop
    if pin == buggy.button: 
        if startStop == True:
            startStop = False
        else:
            startStop = True

buggy.button.irq(trigger=machine.Pin.IRQ_RISING, handler =  ButtonIRQHandler)

while True:
    if startStop == True:
        frontDistance = buggy.getDistance("f")
        print(frontDistance)
        
        # E
        if(frontDistance < 10):
            buggy.motorOff("l")
            buggy.motorOff("r")
            buggy.soundFrequency(500)
            buggy.setLED(0,buggy.RED)
            buggy.setLED(1,buggy.RED)
            buggy.setLED(2,buggy.RED)
            buggy.setLED(3,buggy.RED)
            buggy.show()
        
        # G
        elif(frontDistance < 20):
            buggy.motorOn("l","f",20)
            buggy.motorOn("r","f",20)
            buggy.soundFrequency(400)
            buggy.setLED(0,buggy.YELLOW)
            buggy.setLED(1,buggy.YELLOW)
            buggy.setLED(2,buggy.YELLOW)
            buggy.setLED(3,buggy.YELLOW)
            buggy.show()
        
        # C
        elif(frontDistance < 30):
            buggy.motorOn("l","f",20)
            buggy.motorOn("r","f",20)
            buggy.soundFrequency(300)
            buggy.setLED(0,buggy.GREEN)
            buggy.setLED(1,buggy.GREEN)
            buggy.setLED(2,buggy.GREEN)
            buggy.setLED(3,buggy.GREEN)
            buggy.show()

        # D
        elif(frontDistance < 40):
            buggy.motorOn("l","f",20)
            buggy.motorOn("r","f",20)
            buggy.soundFrequency(200)
            buggy.setLED(0,buggy.WHITE)
            buggy.setLED(1,buggy.WHITE)
            buggy.setLED(2,buggy.WHITE)
            buggy.setLED(3,buggy.WHITE)
            buggy.show()
        
        # F
        elif(frontDistance < 50):
            buggy.motorOn("l","f",20)
            buggy.motorOn("r","f",20)
            buggy.soundFrequency(100)
            buggy.setLED(0,buggy.PURPLE)
            buggy.setLED(1,buggy.PURPLE)
            buggy.setLED(2,buggy.PURPLE)
            buggy.setLED(3,buggy.PURPLE)
            buggy.show()
            
        else:
            buggy.motorOff("l")
            buggy.motorOff("r")
            buggy.silence()


    else: #motors turned off
        buggy.silence()
                



