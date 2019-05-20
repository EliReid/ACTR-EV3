#!/usr/bin/env python3

"""
File desc.
##########################
# Title: Lego Robot Model
# By:    Elisabeth Reid
# Date:  2019
##########################
"""

import ccm
#log=ccm.log(html=True)
from ccm.lib.actr import *
from sensors import *


class Env(ccm.Model):
	touch_sensor = ccm.Model(isa = 'sensor', value = 'none') # A sensor is part of the enviornment

class MotorModule(ccm.Model): # create a motor module to controll the robots actuators
	def do_green_light(self):

		# Here is where we turn on the physical LED sensor of the robot
		print("Light up the LED display")

		leds.set_color("LEFT", "GREEN")
		leds.set_color("RIGHT", "GREEN")

	def do_red_light(self):
		leds.set_color("LEFT","RED")
		leds.set_color("RIGHT","RED")


class SensorModule(ccm.Model):
	def feel(self):
		# Here is where we update the touch sensors value
		# from the lego sensor in real-time, set at 'true' for testing
		if ts.is_pressed:
			self.parent.parent.touch_sensor.value = 'true'
		#else:
		#	self.parent.parent.touch_sensor.value = 'none'
		#self.parent.parent.touch_sensor.value = 'true'

	def clear(self):
		if not ts.is_pressed:
			self.parent.parent.touch_sensor.value = 'none'

class MySensorModule(ccm.ProductionSystem):  # create a production system to update touch_sensor value
	production_time = 0.0001

	def wait(focus = 'wait'):
		#print ("waiting for touch...")
		senses.feel()
		focus.set('check')

	def reset(focus = 'reset'):
		senses.clear()
		focus.set('wait')

class LegoAgent(ACTR):

	focus = Buffer()
	motor = MotorModule()
	sensor = MySensorModule()
	senses = SensorModule()

	def init():
		focus.set('wait')

	def touched(touch_sensor = 'value:true'):
		print ("Oh I noticed something! Emiting green light...")
		motor.do_green_light()
		focus.set('reset')

	def not_touched(touch_sensor = 'value:none'):
		print ("Nothing...")
		motor.do_red_light()
		focus.set('wait')

robot = LegoAgent()
env   = Env()

# adding agent to enviornment
env.agent = robot

ccm.log_everything(env)

env.run()
ccm.finished()
