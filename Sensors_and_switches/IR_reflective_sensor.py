import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)
GPIO.setup(11, GPIO.OUT)

try:
    while True:
        if GPIO.input(7) == 1:
            GPIO.output(11, True)
        else:
            GPIO.output(11, False)
finally:
    GPIO.cleanup()
