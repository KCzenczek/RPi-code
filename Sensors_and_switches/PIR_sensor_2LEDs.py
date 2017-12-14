import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.OUT) # red
GPIO.setup(11,GPIO.OUT) # green 
    
GPIO.setup(7,GPIO.IN) # pir

try:
    while True:
        if GPIO.input(7) == 1:
            GPIO.output(11,False)
            GPIO.output(10,True)
        else:
            GPIO.output(11,True)
            GPIO.output(10,False)

finally:
    GPIO.cleanup()
