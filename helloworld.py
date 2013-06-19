import RPi.GPIO as GPIO
import time

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
GPIO.setup(gpio_PWMA, GPIO.OUT)
GPIO.setup(gpio_AIN2, GPIO.OUT)
GPIO.setup(gpio_AIN1, GPIO.OUT)
GPIO.setup(gpio_STBY, GPIO.OUT)
GPIO.setup(gpio_BIN1, GPIO.OUT)
GPIO.setup(gpio_BIN2, GPIO.OUT)
GPIO.setup(gpio_PWMB, GPIO.OUT)

# Spin motor A one way
GPIO.output(gpio_AIN1, True)
GPIO.output(gpio_AIN2, False)

# Spin motor B the other way
GPIO.output(gpio_BIN1, True)
GPIO.output(gpio_BIN2, False)

# Full speed?
GPIO.output(gpio_PWMA, True)
GPIO.output(gpio_PWMB, True)

GPIO.output(gpio_STBY, True)

while 1:
    time.sleep(5)
    GPIO.output(gpio_STBY, False)
    time.sleep(5)
    GPIO.output(gpio_STBY, True)

