from PicoAutonomousRobotics import KitronikPicoRobotBuggy
from time import sleep

buggy = KitronikPicoRobotBuggy()
run = False

DegreesPerSecond = (6/5)*360

def ButtonIRQHandler(pin):
    global run
    if(run):
        run = False
    else:
        run = True

buggy.button.irq(trigger=machine.Pin.IRQ_RISING, handler =  ButtonIRQHandler)   

def Forwards():
    buggy.motorOn("l","f",22)
    buggy.motorOn("r","f",20)
        
def Reverse():
    buggy.motorOn("l","r",22)
    buggy.motorOn("r","r",20)

def Stop():
    buggy.motorOff("r") 
    buggy.motorOff("l")

def Spin():
    buggy.motorOn("l","f",80)
    buggy.motorOn("r","r",80)

def TurnRight(HowFar):
    buggy.motorOn("l","f",20)
    buggy.motorOn("r","r",20)  
    sleep(HowFar/DegreesPerSecond)
    Stop()

def TurnLeft(HowFar):
    buggy.motorOn("l","r",20)
    buggy.motorOn("r","f",20)  
    sleep(HowFar/DegreesPerSecond)
    Stop()

def PenUp():
    buggy.goToPosition(2,1)

def PenDown():
    buggy.goToPosition(2,125)


while True:
   if(run):
        sleep(2) # wait so we can get the hand clear after pressing start.
        PenUp()
        sleep(1)
        PenDown()
        for x in range (0,1):
            Forwards()
            sleep(1)
            Reverse()
            sleep(0.5)
            TurnRight(90)
            Forwards()
            sleep(0.5)
            TurnLeft(90)
            Forwards()
            sleep(0.5)
            Reverse()
            sleep(1)
            PenUp()
            TurnRight(90)
            Forwards()
            sleep(0.5)
            TurnLeft(90)
            PenDown()
            Forwards()
            sleep(0.2)
            Reverse()
            sleep(0.2)
            TurnLeft(90)
            Forwards()
            sleep(0.5)
            TurnRight(90)
            Forwards()
            sleep(0.5)
            TurnRight(90)
            Forwards()
            sleep(0.5)
        run = False
   else:
        Stop()