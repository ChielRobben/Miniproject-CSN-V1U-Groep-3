from gpiozero import Button
from gpiozero import LED
from time import sleep
from gpiozero import LightSensor
ldr = LightSensor(4)
groen = LED(27)
red = LED(17)
button = Button(2)


def alarmafgegaan():

    #Zenden naar de server
    while True:
        groen.on()
        red.on()
        sleep(0.25)
        red.off()
        sleep(0.25)

        if button.is_held  == True:
            print('vals alarm')
            break

def alarm():
    while True:
        groen.on()
        sleep(1)
        groen.off()
        sleep(1)

        if ldr.value <=0.1:
            print('intruder detected')
            alarmafgegaan()
            break
alarm()



