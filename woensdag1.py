from gpiozero import Button
from gpiozero import LED
from time import sleep
from gpiozero import LightSensor
path = '/mnt/data/Alarm'
f = open(path,'w')
f.write('on')


ldr = LightSensor(4)
groen = LED(27)
red = LED(17)
button = Button(2,hold_time=5)

def alarmafgegaan():

    while True:

        red.on()
        sleep(0.25)
        red.off()
        sleep(0.25)

        if button.is_held  == True :
            path = '/mnt/data/Alarm'
            f = open(path, 'w')
            f.write('off')
            f.close()
            print('vals alarm \nAlarm wordt uitgeschakeld')
            button.wait_for_release()
            print('druk op de knop om alarm te activeren')
            groen.off()
            aan()
            break


def alarm():

    while True:
        path = '/mnt/data/Alarm'
        f = open(path, 'w')
        f.write('off')
        f.close()
        groen.on()
        sleep(1)
        if ldr.value <=0.4:
            path = '/mnt/data/Alarm'
            f = open(path, 'w')
            f.write('on')
            f.close()
            print('intruder detected')
            alarmafgegaan()
        if button.is_held == True:

            print('alarm wordt uitgeschakeld')
            button.wait_for_release()
            print('druk op de knop om alarm te activeren')
            groen.off()
            aan()
            break



def aan():

    while True:
        path = '/mnt/data/Alarm'
        f = open(path, 'w')
        f.write('off')
        f.close()
        if button.is_pressed == True:
            print('Alarm staat aan')
            alarm()
            break



aan()