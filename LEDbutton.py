import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(18,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24,GPIO.OUT)
#GPIO.setup(25,GPIO.OUT)

#GPIO.output(25,GPIO.IN, Pull_Up_)
while True:
	
	if  GPIO.input(18) == False:
		GPIO.output(24,GPIO.HIGH)
		#print "A"
		time.sleep(0.02)
	else: 
		GPIO.output(24,GPIO.LOW)
		#print "B"
		time.sleep(0.02)

