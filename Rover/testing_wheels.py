import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
chan_list = [7, 11, 13, 15]
GPIO.setup(chan_list, GPIO.OUT)

GPIO.output(7, True)
time.sleep(1)
GPIO.output(7, False)
GPIO.output(11, True)
time.sleep(1)
GPIO.output(11, False)
GPIO.output(13, True)
time.sleep(1)
GPIO.output(13, False)
GPIO.output(15, True)
time.sleep(1)
GPIO.output(15, False)

GPIO.cleanup()
