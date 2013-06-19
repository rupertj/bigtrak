#!/usr/bin/python
import RPi.GPIO as GPIO
import time

# Globals for the GPIO pin setup.
gpio_PWMA = 14
gpio_AIN2 = 15
gpio_AIN1 = 18
gpio_STBY = 23
gpio_BIN1 = 24
gpio_BIN2 = 25
gpio_PWMB = 22

# Set the mode of numbering the pins.
GPIO.setmode(GPIO.BCM)

# All these are outs.
GPIO.setup(gpio_AIN1, GPIO.OUT)
GPIO.setup(gpio_AIN2, GPIO.OUT)
GPIO.setup(gpio_PWMA, GPIO.OUT)

GPIO.setup(gpio_BIN1, GPIO.OUT)
GPIO.setup(gpio_BIN2, GPIO.OUT)
GPIO.setup(gpio_PWMB, GPIO.OUT)

GPIO.setup(gpio_STBY, GPIO.OUT)

# Enable the H-Bridge. This should probably be on the start/stop of an individual motion.
GPIO.output(gpio_STBY, True)

class Motor(object):

	def __init__(self, in1, in2, pwm):
		self.in1 = in1
		self.in2 = in2
		self.pwm = pwm
	
	def setDirection(self, direction):
		if direction:
			GPIO.output(self.in1, True)
			GPIO.output(self.in2, False)
		else:
			GPIO.output(self.in1, False)
			GPIO.output(self.in2, True)

	def setSpeed(self, speed):
		if speed == 0:
			GPIO.output(self.in1, False)
			GPIO.output(self.in2, False)
			GPIO.output(self.pwm, False)
		else:
			GPIO.output(self.pwm, True)
			

class Bigtrak(object):

	def __init__(self):
		self.motorA = Motor(gpio_AIN1, gpio_AIN2, gpio_PWMA)
		self.motorB = Motor(gpio_BIN1, gpio_BIN2, gpio_PWMB)
	
	def turn(self, direction):

		self.motorA.setDirection(direction)
		self.motorB.setDirection(not direction)		

		self.motorA.setSpeed(1)
		self.motorB.setSpeed(1)

	def stop(self):
		self.motorA.setSpeed(0)
		self.motorB.setSpeed(0)

		
bt = Bigtrak()

#while 1:
#	bt.turn(1)
#	time.sleep(2)
#	GPIO.output(gpio_STBY, False)
#	time.sleep(2)
#	GPIO.output(gpio_STBY, True)

bt.turn(0)
time.sleep(2)
bt.stop()

bt.turn(1)
time.sleep(2)
bt.stop()
