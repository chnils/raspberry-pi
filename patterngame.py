import RPi.GPIO as GPIO
import time
import sys
import random

GPIO.setmode(GPIO.BCM)
#Skriv in alla GPIO.setup() konfiguartioner.

setuplist = []
#En lista där första platsen är nummret till GPIOn kopplad till knappen som styr den första LEDn (väljs arbiträrt).
#Nästa plats är nummret till GPIOn som går till motsvarande LED. Sen för nästkommande platser så upprepas mönstret för
#knappar och motsvarande LEDs. Listan fylls i manuellt.


#metoder i spelet-------------------------------------------------------------------------------------------------------

def LEDblink(LEDnummer, seconds): #LEDnummer får motsvara den GPIO som den LEDn är kopplad till.

    # metoden som får raspberrien att kunna lysa upp en LED under en viss tid.
    # komplettera med rätt GPIO nummer när breadbord layouten är klar.

    GPIO.output(LEDnummer, HIGH)
    time.sleep(seconds)
    GPIO.output(LEDnummer, LOW)
    time.sleep(0.1)




def LEDpress(x):
    # metoden som gör att LED lyser upp när motsvarande knapp trycks samt returnerar ett korrekt värde för just den LEDn
    # komplettera med rätt GPIO nummer när breadbord layouten är klar
    # Just nu bara anpassat för 3 LEDer

    bool = True
    x = 0
    while bool:
        if GPIO.input(setuplist[0])==False:
            GPIO.output(setuplist[1]), HIGH)
            time.sleep(0.5)
            GPIO.output(setuplist[1]), LOW)
            bool = False
            x = 1

        if GPIO.input(setuplist[2])==False:
            GPIO.output(setuplist[3], HIGH)
            time.sleep(0.5)
            GPIO.output(setuplist[3], LOW)
            bool = False
            x = 3

        if GPIO.input(setuplist[4])==False:
            GPIO.output(setuplist[5], HIGH)
            time.sleep(0.5)
            GPIO.output(setuplist[5], LOW)
            bool = False
            x = 5

    return setuplist[x]



def spelet():
    ingame2 = True
    while(ingame2):

        for k in range (0, sekvenslangd, 1):
            rand = random.randint(1,3)
            if rand == 1:
                rand = setuplist[1] #GPIO numret till LED nr 1
            elif rand == 2:
                rand = setuplist[3] #GPIO numret till LED nr 2
            elif rand == 3:
                rand = setuplist[5] #GPIO numret till LED nr 3

            answerlist[k] = rand

            LEDblink(answerlist[k], seconds)

        repeat = input('Vill du se sekvensen igen? Ja = Y, Nej = N')
        if repeat == 'Y':
            for k in range (0, sekvenslangd, 1):
                LEDblink(answerlist[k], seconds)


        print('Repetera sekvensen')


        for b in range (0, sekvenslangd, 1):

            testlist[b] = LEDpress()

            if testlist[b] == answerlist[b]:
                print ('OK')

            else:
                svar = int(input('Fel, spela igen med samma forutsattningar: Skriv 1'
                                    'spela igen med nya forutsattningar: Skriv 2'
                                    'Avbryta spel: Skriv 3'))


                if svar == 2:
                    ingame2 = False

                elif svar == 3:
                    ingame1 = False
                    ingame2 = False

            print('Grattis! Du klarade det!')




#spelets start--------------------------------------------------------------------------------------------------------

ingame1 = True
while ingame1:

    sekvenslangd = int (input('Ange sekvenslängd'))

    answerlist = [0]*sekvenslangd
    # En lista som kommer fyllas med den sekvens som slumpas fram. Till en början bara en tom lista med längden
    # sekvenslängd

    testlist = [0]*sekvenslangd
    # En lista som fylls med den sekvens som spelaren skapar. Till en början bara en tom lista med längden
    # sekvenslängd

    svarighetsgrad = int (input('Ange svårighetsgrad 1 till 3 (1=lätt, 2=medium, 3=svårt)'))
    seconds = 0
    if svarighetsgrad == 1:
        seconds = 1.2
    elif svarighetsgrad == 2:
        seconds = 0.75
    elif svarighetsgrad == 3:
        seconds = 0.4

    spelet()

print('Tack för att du spelade')