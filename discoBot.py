from PicoAutonomousRobotics import KitronikPicoRobotBuggy
from time import sleep
from machine import Timer

buggy = KitronikPicoRobotBuggy()
run = False
buttonState = 0
DegreesPerSecond = (9/5)*360

def checkButton(p):
    global buttonState
    global run
    buttonState = buttonState <<1 | buggy.button.value() |0xE000
    buttonState &=0xFFFF
    if buttonState == 0xEFFF: #button has been pressed and passes the debouncing test
        if run == True:
            run = False
            Stop() 
        else:
            run = True

debounceTimer = Timer(-1)
debounceTimer.init(period=2, mode=Timer.PERIODIC, callback=checkButton)

def Forwards():
        buggy.motorOn("l","f",50)
        buggy.motorOn("r","f",50)
        
def Reverse():
        buggy.motorOn("l","r",50)
        buggy.motorOn("r","r",50)

        
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
        
def Spin(): 
   buggy.motorOn("l","f",80) 
   buggy.motorOn("r","r",80)
   
def rotateColours():
    # temporarily  store the first one, then overwrite it, shifting by 1 LED at a time
    first = buggy.getLED(0)
    buggy.setLED(0,buggy.getLED(1))
    buggy.setLED(1,buggy.getLED(2))
    buggy.setLED(2,buggy.getLED(3))
    buggy.setLED(3,first) # push the colour that was at 0 back in at this end.

# while True: 
#    if(run): 
#       sleep(2) 
#       Spin() 
#       sleep(5) 
#       run = False 
#    else: 
#       Stop()

# while True:
#     if(run):
sleep(1) # wait so we can get the hand clear after pressing start.
# square to the left
buggy.setLED(0, buggy.RED)
buggy.setLED(1, buggy.GREEN)
buggy.setLED(2, buggy.BLUE)
buggy.setLED(3, buggy.PURPLE)
buggy.setBrightness(10)
buggy.show()

for x in range (0,4):
#     print(str(x))
    Forwards()
#     print('sleeping')
    sleep(0.5)
    rotateColours()
    buggy.show()
#     print('left')
    TurnLeft(90)
# spin
Spin()
sleep(1)
# square to the right
buggy.setLED(0, buggy.BLACK)
buggy.setLED(1, buggy.WHITE)
buggy.setLED(2, buggy.YELLOW)
buggy.setLED(3, buggy.CYAN)
buggy.show()
for x in range (0,4):
    print(str(x))
    Reverse()
    print('sleeping')
    sleep(0.5)
    rotateColours()
    buggy.show()
    print('left')
    TurnRight(90)
