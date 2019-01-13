import RPi.GPIO as GPIO
import subprocess

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.IN)
button_pressed = GPIO.input(16)

try:
    while True:
        if button_pressed:
            subprocess.call('./photo.sh')
finally:
    GPIO.cleanup()
