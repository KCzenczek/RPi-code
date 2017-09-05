import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
chan_list = [7, 11]
GPIO.setup(chan_list, GPIO.OUT)

for x in range(0, 10):
    GPIO.output(chan_list, (GPIO.HIGH, GPIO.LOW))
    time.sleep(.5)
    GPIO.output(chan_list, (GPIO.LOW, GPIO.HIGH))
    time.sleep(.5)

GPIO.cleanup()
