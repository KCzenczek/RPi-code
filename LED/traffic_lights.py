import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
chan_list = [7, 11, 13]
GPIO.setup(chan_list, GPIO.OUT)

for x in range(0, 3):
    GPIO.output(7, True)
    GPIO.output(11, False)
    GPIO.output(13, False)
    time.sleep(5)
    GPIO.output(7, False)
    GPIO.output(11, True)
    GPIO.output(13, False)
    time.sleep(2)
    GPIO.output(7, False)
    GPIO.output(11, False)
    GPIO.output(13, True)
    time.sleep(5)

GPIO.cleanup()