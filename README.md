# robot_day

BUILT-IN FUNCTIONS

Import package:
    from PicoAutonomousRobotics import KitronikPicoRobotBuggy

Creating instance of buggy:
    buggy = KitronikPicoRobotBuggy()

Button:
    buggy.button.value()

Buzzer:
    buggy.beepHorn()
    
Lights:
(LEDs are numbered 0 to 3, colours can be changed)
    buggy.setLED(LED_number, buggy.LED_colour)


Frequencies lifted from wikipedia

C3	130.81
C#3/Db3 138.59
D3	146.83	
D#3/Eb3 155.56
E3	164.81
F3	174.61
F#3/Gb3 185.00
G3	196.00
G#3/Ab3 207.65
A3	220.00
A#3/Bb3 233.08
B3	246.94
C4	261.63
C#4/Db4 277.18
D4	293.66
D#4/Eb4 311.13
E4	329.63
F4	349.23
F#4/Gb4 369.99
G4	392.00
G#4/Ab4 415.30
A4	440.00
A#4/Bb4 466.16
B4	493.88
