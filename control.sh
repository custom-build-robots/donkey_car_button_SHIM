#!/bin/bash
source ~/env/bin/activate
python /home/pi/button.py >> /home/pi/button.log 2>&1 &
