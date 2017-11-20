from flask import Flask, render_template
import RPi.GPIO as GPIO
import time
from datetime import datetime

app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.IN)     # PIR PIN as input
GPIO.setup(16, GPIO.OUT)    # LED PIN as output

history = [None]

@app.route('/')
def main():
    while True:
        
        if GPIO.input(12) == 1:
            GPIO.output(16, True)
            msg = 'Last movement was detected on '
            time.sleep(10)
            GPIO.output(16, False)
            date_time = str(datetime.now().strftime('%d-%m-%Y %H:%M'))
            history.append(date_time)

        else:
            GPIO.output(16, False)
            msg = 'No movement detected. The last one detected during this conection was:'
        
        template_data = {
            'title': 'motion detector',
            'message': msg,
            'history': history
            }

        return render_template('main.html', **template_data)

if __name__ == '__main__':
    app.run('192.168.0.20', port=8000, debug=True)
    
    GPIO.cleanup()

# [work in progress]
