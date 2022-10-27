"""This is a Raspberry Pi script to blink a led connected to pin 8 and stay constantly on when the button pressed"""

# import the necesary library to access the gpio pins
from RPi import GPIO
from time import sleep

LED = 8 # where the  led will be connecte to
BUTTON = 10 # whre the push button will be connected

GPIO.setmode(GPIO.BOARD)

GPIO.setup(LED, GPIO.OUT)
GPIO.setup(BUTTON, GPIO.IN)

while True:
	if GPIO.input(BUTTON):
		"""If the button is pressed,an high value will be read"""
		GPIO.output(LED, GPIO.HIGH)
		sleep(1)
	else:
		GPIO.output(LED, GPIO.LOW)
		sleep(.5)
		GPIO.output(LED, GPIO.HIGH)
		sleep(.5)
