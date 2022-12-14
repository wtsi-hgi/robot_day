from PicoAutonomousRobotics import KitronikPicoRobotBuggy
from time import sleep
from machine import Timer

buggy = KitronikPicoRobotBuggy()

#TODO add other letters
morse = {'s':[0, 0, 0],
         'o':[1, 1, 1]}


def makeNoise(frequency):
    buggy.soundFrequency(frequency)
    sleep(0.15)
    
def morseDash():
    makeNoise(330)
    makeNoise(330)
    makeNoise(10)
    
def morseDot():
    makeNoise(330)
    makeNoise(10)

 
def playMorse(code):
    for note in code:
#         print(note)
        if note == 0:
            morseDot()
        elif note == 1:
            morseDash()
    

message = ['s', 'o', 's']

for letter in message:
    playMorse(morse[letter])





