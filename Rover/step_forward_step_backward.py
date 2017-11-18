import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
chan_list = [7, 11, 13, 15]
GPIO.setup(chan_list, GPIO.OUT)

chan_list_forward = [7, 13]
GPIO.setup(chan_list_forward, GPIO.OUT)

chan_list_backward = [11, 15]
GPIO.setup(chan_list_backward, GPIO.OUT)

chan_list_turn_right = [7,15]
GPIO.setup(chan_list_turn_right, GPIO.OUT)

chan_list_turn_left = [11, 13]
GPIO.setup(chan_list_turn_left, GPIO.OUT)


GPIO.output(chan_list_forward, True)
time.sleep(3)
GPIO.output(chan_list_forward, False)
time.sleep(1)

GPIO.output(chan_list_backward, True)
time.sleep(3)
GPIO.output(chan_list_backward, False)
time.sleep(1)

GPIO.cleanup()
