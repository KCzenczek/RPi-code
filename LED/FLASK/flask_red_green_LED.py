from flask import Flask, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)
pin_list = [12, 16]

for pin in pin_list:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

pin_dict = {
    12: {
        'led_colour': 'Green LED',
        'led_state': GPIO.LOW
        },
    16: {
        'led_colour': 'Red LED',
        'led_state': GPIO.LOW
        }
    }
        
@app.route('/')
def main():
    for pin in pin_dict:
        pin_dict[pin]['led_state'] = GPIO.input(pin)
        
    template_data = {
        'title': 'LEDs current state',
        'pin_dict': pin_dict,
        }

    return render_template('main.html', **template_data)

    
if __name__ == '__main__':
    app.run(host='192.168.0.20', port=80, debug=True)
    
GPIO.cleanup()
