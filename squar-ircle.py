from PicoAutonomousRobotics import KitronikPicoRobotBuggy
from time import sleep
from machine import Timer

buggy = KitronikPicoRobotBuggy()
run = False
buttonState = 0
DegreesPerSecond = (6/5)*360

def checkButton(p):
    global buttonState
    global run
    buttonState = buttonState <<1 | buggy.button.value() |0xE000
    buttonState &=0xFFFF
    if buttonState == 0xEFFF: #button has been pressed and passes the debouncing test
        if run == True:
            run = False
        else:
            run = True

debounceTimer = Timer(-1)
debounceTimer.init(period=2, mode=Timer.PERIODIC, callback=checkButton)

def Forwards():
        buggy.motorOn("l","f",50)
        buggy.motorOn("r","f",50)
        
def TurnLeft(HowFar):
    buggy.motorOn("l","r",80)
    buggy.motorOn("r","f",80)  
    sleep(HowFar/DegreesPerSecond)
    Stop()

def TurnRight(HowFar):
    buggy.motorOn("l","f",80)
    buggy.motorOn("r","r",80)  
    sleep(HowFar/DegreesPerSecond)
    Stop()
    
def Stop():
        buggy.motorOff("r") 
        buggy.motorOff("l")

while True:
    if(run):
        sleep(1) # wait so we can get the hand clear after pressing start.
        for x in range (0,4):
            Forwards()
            sleep(0.2)
            TurnLeft(90)
        run = False
    else:
        Stop()