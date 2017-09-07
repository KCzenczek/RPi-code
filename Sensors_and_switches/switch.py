import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.IN)

try:
    while True:
        if GPIO.input(16) == 0:
            print('go on, press the button')
        else:
            print('thank you for your cooperation')

finally:
    GPIO.cleanup()