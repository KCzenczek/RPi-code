import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
#list_F = [40, 13, 16, 18]
#list_B = [11, 15, 12, 22]
GPIO.setup(18, GPIO.OUT)

GPIO.output(18, True)
time.sleep(10)
GPIO.output(18, False)

GPIO.cleanup()


