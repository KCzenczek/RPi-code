import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.IN)      # PIR sensor
GPIO.setup(10, GPIO.OUT)    # green LED
GPIO.setup(11, GPIO.OUT)    # red LED

GPIO.setup(32, GPIO.IN)     # reflective IR sensor
GPIO.setup(36, GPIO.OUT)    # green LED
GPIO.setup(38, GPIO.OUT)    # red LED

try:
    while True:
        if GPIO.input(32) == 1:     # means nighttime
            GPIO.output(36, True)   # green ON; may procced
            GPIO.output(38, False)  
              
            if GPIO.input(7) == 1:      # movement detected; wait for green
                GPIO.output(10,False)
                GPIO.output(11,True)    # red ON
            else:
                GPIO.output(10,True)    # green ON; armed and ready
                GPIO.output(11,False)
                
        elif GPIO.input(32) == 0:    # means daytime
            GPIO.output(36, False)
            GPIO.output(38, True)    # red ON; wait for dark :)
finally:
    GPIO.cleanup()


