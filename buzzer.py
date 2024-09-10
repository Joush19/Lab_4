import RPi.GPIO as GPIO
import time

buzz = 14
button = [3,4]
count = 0

def increase(channel):
    global count
    count = 1

def decrease(channel):
    global count
    count = 0

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(buzz,GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.add_event_detect(button[0], GPIO.FALLING, callback=increase, bouncetime=300)
#GPIO.add_event_detect(button[1], GPIO.FALLING, callback=decrease, bouncetime=300)

while True:

    if (GPIO.input(button[0]) == GPIO.LOW):
        GPIO.output(buzz, GPIO.HIGH)
    else:
        GPIO.output(buzz, GPIO.LOW)
    #GPIO.output(buzz, count)

