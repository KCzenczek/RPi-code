#!/bin/bash
DATE=`date '+%Y-%m-%d_%H:%M'`;
raspistill -vf -hf - /home/pi/Desktop/projects/button_camera_project/$DATE.jpg
