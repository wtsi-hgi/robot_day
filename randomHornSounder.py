# A  basic 'free roaming' robot
# uses the FRont and rear ultrasonic sensors to avoid obstacles
# if an ultrasonic is not fitted it will return -1
#uses the onboard button for a start / stop command via an IRQ.

from PicoAutonomousRobotics import KitronikPicoRobotBuggy
from time import sleep_ms

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

buggy.setLED(0,buggy.PURPLE)
buggy.setLED(1,buggy.PURPLE)
buggy.setLED(2,buggy.PURPLE)
buggy.setLED(3,buggy.PURPLE)
buggy.show()

while True:
    if startStop == True:
        buggy.beepHorn()
        frontDistance = buggy.getDistance("f")
        print(frontDistance)
        
        if(frontDistance > 15):
            buggy.setLED(0,buggy.GREEN)
            buggy.setLED(1,buggy.GREEN)
            buggy.setLED(2,buggy.GREEN)
            buggy.setLED(3,buggy.GREEN)
            
        else:
            buggy.soundFrequency(440)
            buggy.setLED(0,buggy.RED)
            buggy.setLED(1,buggy.RED)
            buggy.setLED(2,buggy.RED)
            buggy.setLED(3,buggy.RED)
        
        buggy.show()
        
    else: #motors turned off
        buggy.setLED(0,buggy.PURPLE)
        buggy.setLED(1,buggy.PURPLE)
        buggy.setLED(2,buggy.PURPLE)
        buggy.setLED(3,buggy.PURPLE)
        buggy.show()


