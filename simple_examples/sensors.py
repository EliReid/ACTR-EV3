
##########################
# Title: Lego Robot Model
# By:    Elisabeth Reid
# Date:  2019
##########################

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds

ts = TouchSensor(INPUT_1)
leds = Leds()