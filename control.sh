#!/bin/bash
source ~/env/bin/activate
python /home/pi/donkey_car_button_SHIM/button.py >> /home/pi/button.log 2>&1 &
