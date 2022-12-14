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