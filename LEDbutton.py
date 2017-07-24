import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(18,GPIO.IN)
GPIO.setup(24,GPIO.OUT)
#GPIO.setup(25,GPIO.OUT)

#GPIO.output(25,GPIO.HIGH)
while True:
	
	if  GPIO.input(18):
		GPIO.output(24,GPIO.HIGH)
		print("hej")
	else: 
		GPIO.output(24,GPIO.LOW)


