from PicoAutonomousRobotics import KitronikPicoRobotBuggy
from time import sleep

import machine
import math
import time

buggy = KitronikPicoRobotBuggy()

brightness = 50

#set the LEDs initial pattern
buggy.setLED(0, buggy.RED)
buggy.setLED(1, buggy.GREEN)
buggy.setLED(2, buggy.BLUE)
buggy.setLED(3, buggy.PURPLE)
buggy.setBrightness(brightness)
buggy.show()

ntf0 = 10

ntf1 = 261
ntf2 = 293
ntf3 = 329
ntf4 = 349
ntf5 = 392
ntf6 = 440
ntf7 = 493

ntfh1 = 1046
ntfh2 = 1175
ntfh3 = 1319
ntfh4 = 1397
ntfh5 = 1568
ntfh6 = 1760
ntfh7 = 1976

ntfl1 = 130
ntfl2 = 146
ntfl3 = 164
ntfl4 = 174
ntfl5 = 196
ntfl6 = 220
ntfl7 = 246

tune = [ ntf3,ntf3,ntf3,ntf3,ntf3,ntf3,
         ntf3,ntf5,ntf1,ntf2,ntf3,ntf0,
         ntf4,ntf4,ntf4,ntf4,ntf4,ntf3,ntf3,ntf3,ntf3,
         ntf5,ntf5,ntf4,ntf2,ntf1,ntf0,
         
         ntf5,ntf3,ntf2,ntf1,ntfl5,ntf0,ntfl5,ntfl5,
         ntfl5,ntf3,ntf2,ntf1,ntfl6,ntf0,
         ntfl6,ntf4,ntf3,ntf2,ntfl7,ntf0,
         ntf5,ntf5,ntf4,ntf2,ntf3,ntf1,ntf0,
         
         ntfl5,ntf3,ntf2,ntf1,ntfl5,ntf0,
         ntfl5,ntf3,ntf2,ntf1,ntfl6,ntf0,ntfl6,
         ntfl6,ntf4,ntf3,ntf2,ntf5,ntf5,ntf5,ntf5,
         ntf6,ntf5,ntf4,ntf2,ntf1,ntf0]

durt = [ 0.5,0.5,1,0.5,0.5,1,
         0.5,0.5,0.75,0.25,1.5,0.5,
         0.5,0.5,1,0.5,0.5,0.5,0.5,0.25,0.25,
         0.5,0.5,0.5,0.5,1.5,0.5,
         
         0.5,0.5,0.5,0.5,1,0.5,0.25,0.25,
         0.5,0.5,0.5,0.5,1,1,
         0.5,0.5,0.5,0.5,1,1,
         0.5,0.5,0.5,0.5,1,0.75,0.25,
         
         0.5,0.5,0.5,0.5,1,1,
         0.5,0.5,0.5,0.5,1,0.5,0.5,
         0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
         0.5,0.5,0.5,0.5,0.75,0.25]

durt_new = [i * 4 for i in durt]

def makesong(tune):
    newtune = []
    for idx, t in enumerate(tune):
        s = durt_new[idx]
        while s > 0:
            newtune.append(t)
            s = s - 1 
        newtune.append(ntf0)
    return newtune

def makeled(tune):
    if tune == 10:
        buggy.clear(0)
        buggy.clear(1)
        buggy.clear(2)
        buggy.clear(3)
        buggy.show()
    else:
        buggy.setLED(0, buggy.GREEN)
        buggy.setLED(1, buggy.GREEN)
        buggy.setLED(2, buggy.GREEN)
        buggy.setLED(3, buggy.GREEN)
        buggy.show()
        
def dance(t1,t2):
    if t1 == t2:
        if t1 == 10:
            buggy.motorOn("l","f",90)
            buggy.motorOn("r","r",90)
        else:
            buggy.motorOn("l","f",20)
            buggy.motorOn("r","f",20)
    else:
        buggy.motorOn("l","r",20)
        buggy.motorOn("r","r",20)
    
while True:
    buggy.show()
    sleep(0.5)
    
    song = makesong(tune)
    if(buggy.button.value() == True):
        for idx, x in enumerate(song):
            buggy.soundFrequency(x)
            makeled(x)
            sleep(0.1)
            if idx != 0:
                dance(song[idx-1], x)
        sleep(10)
        buggy.motorOff("r")
        buggy.motorOff("l") 
            
