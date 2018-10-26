from gpiozero import Button
from gpiozero import LED
from time import sleep
from gpiozero import LightSensor
import pygame




ldr = LightSensor(4)
groen = LED(27)
red = LED(17)
button = Button(2,hold_time=5)

def alarmafgegaan():
    path = '/mnt/csn/Alarm'
    x = open(path, 'r')
    pygame.mixer.init()
    pygame.mixer.music.load("/home/pi/Downloads/badabingbadaboem.mp3")
    pygame.mixer.music.play(loops=-1)



    while True:

        red.on()
        sleep(0.25)
        red.off()
        sleep(0.25)


        if button.is_held  == True :
            pygame.mixer.music.stop()

            path = '/mnt/csn/Alarm'
            f = open(path, 'w')
            f.write('off')
            f.close()
            print('vals alarm \nHet alarm is uitgeschakeld')
            button.wait_for_release()
            print('Druk op de knop om alarm te activeren')
            groen.off()
            aan()

            break


def alarm():

    while True:

        path = '/mnt/csn/Alarm'
        f = open(path, 'w')
        f.write('off')
        f.close()
        groen.on()
        sleep(1)

        if ldr.value <=0.5:
            path = '/mnt/csn/Alarm'
            f = open(path, 'w')
            f.write('on')
            f.close()
            print('Intruder detected')
            alarmafgegaan()
            break
        if button.is_held == True:

            print('Alarm wordt uitgeschakeld')
            button.wait_for_release()
            print('Druk op de knop om alarm te activeren')
            groen.off()
            aan()

            break



def aan():

    while True:

        path = '/mnt/csn/Alarm'
        f = open(path, 'w')
        f.write('down')
        f.close()


        if button.is_pressed == True:
            path = '/mnt/csn/Alarm'
            f = open(path, 'w')
            f.write('off')
            f.close()
            print('Het alarm staat aan')
            alarm()

            break
aan()
