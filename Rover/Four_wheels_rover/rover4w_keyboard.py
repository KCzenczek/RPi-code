import RPi.GPIO as GPIO
import curses


GPIO.setmode(GPIO.BOARD)
list_F = [11, 15, 12, 18]
list_B = [40, 13, 16, 38]
list_L = [11, 15, 16, 38]
list_R = [40, 13, 12, 18]

GPIO.setup(list_F, GPIO.OUT)
GPIO.setup(list_B, GPIO.OUT)
GPIO.setup(list_L, GPIO.OUT)
GPIO.setup(list_R, GPIO.OUT)

stdscr = curses.initscr()	# curses initialization
curses.noecho()				# to turn-off echoing of keybord to screen
curses.cbreak()				# no waiting key response
stdscr.keypad(True)			# spciecial values for cursor keys - keypad mode

try:
    while True:
        c = stdscr.getch()

        if c == ord('q'):
            break

        elif c == ord('s'):
            GPIO.output(list_F, GPIO.LOW)
            GPIO.output(list_B, GPIO.LOW)
            GPIO.output(list_L, GPIO.LOW)
            GPIO.output(list_R, GPIO.LOW)

        elif c == curses.KEY_UP:
            GPIO.output(list_F, GPIO.HIGH)

        elif c == curses.KEY_DOWN:
            GPIO.output(list_B, GPIO.HIGH)

        elif c == curses.KEY_LEFT:
            GPIO.output(list_L, GPIO.HIGH)

        elif c == curses.KEY_RIGHT:
            GPIO.output(list_R, GPIO.HIGH)

finally: #ending curses; 
    curses.nocbreak()		# to leave half-delay mode
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()
    GPIO.cleanup()
