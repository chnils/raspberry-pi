import RPi.GPIO as GPIO
import time
import sys
import random

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

red_b = 14
red_LED = 7
green_b = 18
green_LED = 16
yellow_b = 24
yellow_LED = 26

GPIO.setup(red_b,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(red_LED,GPIO.OUT)
GPIO.setup(green_b,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(green_LED,GPIO.OUT)
GPIO.setup(yellow_b,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(yellow_LED,GPIO.OUT)

setuplist = [red_b, red_LED, green_b, green_LED, yellow_b, yellow_LED]
#A list where the first slot represents the number of the GPIO linked to the button controlling the first LED (chosen arbitrarily).
#The next slot is the number to the GPIO controlling said button.
#The pattern then repeats for following combinations of button and LEDs. The list is filled manually.


#methods in the game-------------------------------------------------------------------------------------------------------

def LEDblink(LEDnummer, seconds):

    # The method that makes an LED glow for a specified time.

    GPIO.output(LEDnummer, GPIO.HIGH)
    time.sleep(seconds)
    GPIO.output(LEDnummer, GPIO.LOW)
    time.sleep(0.1)




def LEDpress():

    # The method that makes an LED glow when the corresponding button is pressed and returns the correct GPIOnumber for that LED.
    # Currently only made for three LEDs

    bool = True
    x = 0
    while bool:
        if GPIO.input(setuplist[0])==False:
            GPIO.output(setuplist[1], GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(setuplist[1], GPIO.LOW)
            bool = False
            x = 1

        if GPIO.input(setuplist[2])==False:
            GPIO.output(setuplist[3], GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(setuplist[3], GPIO.LOW)
            bool = False
            x = 3

        if GPIO.input(setuplist[4])==False:
            GPIO.output(setuplist[5], GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(setuplist[5], GPIO.LOW)
            bool = False
            x = 5

    return setuplist[x]



def spelet():
    ingame2 = True
    while(ingame2):

        for k in range (0, sekvenslangd, 1):
            rand = random.randint(1,3)
            if rand == 1:
                rand = setuplist[1] #GPIO number for LED nr 1
            elif rand == 2:
                rand = setuplist[3] #GPIO number for LED nr 2
            elif rand == 3:
                rand = setuplist[5] #GPIO number for LED nr 3

            answerlist[k] = rand

            LEDblink(answerlist[k], seconds)

        repeat = input('Do you want to see the sequence again? Yes = Y, No = N')
        if repeat == 'Y':
            for k in range (0, sekvenslangd, 1):
                LEDblink(answerlist[k], seconds)


        print('Repeat the sequence')

        b = 0
        while (b<sekvenslangd):

            testlist[b] = LEDpress()

            if testlist[b] == answerlist[b]:
                print ('OK')

            else:
                svar = int(input('wrong, play again under the same circumstances: Type 1'
                                    'Play again with new conditions: Type 2'
                                    'Abort game: Type 3'))

                if svar ==1:
                    b = sekvenslangd

                if svar == 2:
                    ingame2 = False

                elif svar == 3:
                    ingame1 = False
                    ingame2 = False

            b = b + 1





#Start of the game--------------------------------------------------------------------------------------------------------

ingame1 = True
while ingame1:

    sekvenslangd = int (input('Specify length of sequence'))

    answerlist = [0]*sekvenslangd
    # A list that will be filled with the randomized sequence. In the beginning just an empty list with the
    # the legnth of sekvenslangd

    testlist = [0]*sekvenslangd
    # A list that will be filled with the sequence the player creates. In the beginning just an empty list
    # with the lenght of sekvenslangd


    svarighetsgrad = int (input('Specify difficulty setting, 1 to 3 (1=easy, 2=medium, 3=hard)'))
    seconds = 0
    if svarighetsgrad == 1:
        seconds = 1.2
    elif svarighetsgrad == 2:
        seconds = 0.75
    elif svarighetsgrad == 3:
        seconds = 0.4

    start = int(input('Type "1" to start'))
    time.sleep(1.5)

    spelet()

print('Congratulations, you made it! Faboo')
print('Thanks for playing!')