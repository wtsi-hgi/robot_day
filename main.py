from PicoAutonomousRobotics import KitronikPicoRobotBuggy
from time import sleep
from machine import Timer

buggy = KitronikPicoRobotBuggy()


run = False
buttonState = 0 

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



def SetLEDs(colour):
    buggy.setLED(0,colour)
    buggy.setLED(1,colour)
    buggy.setLED(2,colour)
    buggy.setLED(3,colour)
    buggy.show()
    
def ClearLEDs():
    buggy.clear(0)
    buggy.clear(1)
    buggy.clear(2)
    buggy.clear(3)
    buggy.show()
    
def Forward():
    buggy.motorOn('r', 'f', 10)
    buggy.motorOn('l', 'f', 10)
    
def Reverse():
    buggy.motorOn('r', 'r', 0.2)
    buggy.motorOn('l', 'r', 0.2)
    
def Stop():
    buggy.motorOff('r')
    buggy.motorOff('l')
    
def TurnLeft():
    buggy.motorOn("l","r",0.2)
    buggy.motorOn("r","f",0.2)
    
def TurnRight():
    buggy.motorOn("l","f",0.2)
    buggy.motorOn("r","r",0.2)

def StopAndTurn(direction):
    for i in range(7):
        print('Going back')
        Reverse()
    sleep(0.2)
    Stop()
    if (direction == 'l'):
        for i in range(4):
            print('Turning left')
            #buggy.motorOn(direction, 'f', 1)
            TurnLeft()
    elif (direction == 'r'):
        for i in range(4):
            print('Turning right')
            #buggy.motorOn(direction, 'f', 1)
            TurnRight()


delay = 0
colour = buggy.GREEN
while True:
    centreVal = buggy.getRawLFValue("c")
    leftVal = buggy.getRawLFValue("l")
    rightVal = buggy.getRawLFValue("r")
    if delay > 50:
        print("Centre:", centreVal, " Left:",leftVal," Right:",rightVal)
        delay = 0
    delay += 1
    if run:
        SetLEDs(buggy.GREEN)
        Forward()
        #black line means centre should be high value, so if its not we are off the line.
        if(centreVal > 11000):
            SetLEDs(buggy.RED)
            #figure out which side we went
            if (leftVal > rightVal):
                sleep(1)
                StopAndTurn('l')
            elif (rightVal > leftVal):
                sleep(1)
                StopAndTurn('r')
        else:
            colour = buggy.GREEN
    else:
        ClearLEDs()
        Stop()




