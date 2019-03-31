#!/usr/bin/env python3
# /etc/init.d/power_OFF.py

### BEGIN INIT INFO
# Provides:          power_OFF.py
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start daemon at boot time
# Description:       Enable service provided by daemon.
### END INIT INFO


import RPi.GPIO as GPIO
import subprocess

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#one option
GPIO.wait_for_edge(7, GPIO.RISING)
subprocess.call(['shutdown', '-h', 'now'], shell=False)

#second option
#GPIO.add_event_detect(7, GPIO.RISING)
#try:
#    while True:
#        if GPIO.event_detected(7):
#            subprocess.call(['shutdown', '-h', 'now'], shell=False)
#            GPIO.remove_event_detect(7)
#            break
#finally:
#    GPIO.cleanup()
