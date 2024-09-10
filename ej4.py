import RPi.GPIO as GPIO
import time

leds = [14,15,17]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(leds, GPIO.OUT)

while True:
    file = open("config.txt", 'r')
    config = file.readline()
    value = config[-2]
    print(config[:len(config)-1])
    GPIO.output(leds[::2], GPIO.HIGH)
    GPIO.output(leds[1], GPIO.LOW)
    time.sleep(int(value))
    GPIO.output(leds[::2], GPIO.LOW)
    GPIO.output(leds[1], GPIO.HIGH)
    time.sleep(int(value))
