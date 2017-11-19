from flask import Flask, render_template, request
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


@app.route('/<led_colour>', methods=['GET', 'POST'])
def led_change(led_colour):
# soon will be DRY :)
    if request.method == 'GET':
        if led_colour == 'red':
            state_read = GPIO.input(16)
            if state_read == True:
                msg = 'Red LED is currently ON.'
            else:
                msg = 'Red LED is currently OFF.'
            template_data = {
                'title': 'Red LED',
                'message': msg,
                }
            return render_template('change_red.html', **template_data)

        if led_colour == 'green':
            state_read = GPIO.input(12)
            if state_read == True:
                msg = 'Green LED is currently ON.'
            else:
                msg = 'Green LED is currently OFF.'
            template_data = {
                'title': 'Green LED',
                'message': msg,
                }
            return render_template('change_green.html', **template_data)

    elif request.method =='POST':
        if led_colour == 'red':
            if request.form['red_led_change'] == 'red_led':
                GPIO.output(16, not GPIO.input(16))
                state_read = GPIO.input(16)
                if state_read == True:
                    msg = 'Red LED is currently ON.'
                else:
                    msg = 'Red LED is currently OFF.'
                template_data = {
                    'title': 'Red LED',
                    'message': msg,
                    }
                return render_template('change_red.html', **template_data)

        if led_colour == 'green':
            if request.form['green_led_change'] == 'green_led':
                GPIO.output(12, not GPIO.input(12))
                state_read = GPIO.input(12)
                if state_read == True:
                    msg = 'Green LED is currently ON.'
                else:
                    msg = 'Green LED is currently OFF.'
                template_data = {
                    'title': 'Green LED',
                    'message': msg,
                    }
                return render_template('change_green.html', **template_data)
        
        
if __name__ == '__main__':
    app.run(host='192.168.0.20', port=80, debug=True)
    
GPIO.cleanup()
