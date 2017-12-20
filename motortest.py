import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5,GPIO.OUT)   #Left motor input A
GPIO.setup(7,GPIO.OUT)   #Left motor input B
GPIO.setup(11,GPIO.OUT)  #Right motor input A
GPIO.setup(13,GPIO.OUT)  #Right motor input B
GPIO.setup(12,GPIO.IN, pull_up_down=GPIO.PUD_UP) #button
GPIO.setwarnings(False)

a = False

while True:

    if GPIO.input(12) == False:
        a = True
        time.sleep(0.1)
    else:
        GPIO.output(5, 0)
        GPIO.output(7, 0)
        GPIO.output(11, 0)
        GPIO.output(13, 0)
        time.sleep(0.1)

    while(a):
            print "Rotating right motor forwards"
            GPIO.output(5,0)
            GPIO.output(7,0)
            GPIO.output(11,1)
            GPIO.output(13,0)
            time.sleep(4)     #One second delay

            print "Rotating right motor backwards"
            GPIO.output(5,0)
            GPIO.output(7,0)
            GPIO.output(11,0)
            GPIO.output(13,1)
            time.sleep(4)

            print "Rotating left motor forwards"
            GPIO.output(5, 1)
            GPIO.output(7, 0)
            GPIO.output(11, 0)
            GPIO.output(13, 0)
            time.sleep(4)

            print "Rotating left motor backwards"
            GPIO.output(5, 0)
            GPIO.output(7, 1)
            GPIO.output(11, 0)
            GPIO.output(13, 0)
            time.sleep(4)