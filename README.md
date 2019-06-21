# Donkey Car - button SHIM
I developed this idea during meetups and presentation when I had problems to connect the Donkey Car to the local WIFI. To start the main functions from the Donkey Car like the drive mode to show the car in cation it was much easier and safer to use the buttons. 

At the end I implemented the PIMORONI button SHIM to start the Donkey Car training mode or self-driving mode... or just to shutdown the Conkey Car at the end of a presentation or run. 

Da detailed description is available on my blog: https://custom-build-robots.com/raspberry-pi-roboter/autonom-fahrendes-raspberry-pi-ki-roboter-auto-manuelle-short-keys/10922

My Donkey Car with the mounted button SHIM from PIMORONI.

![Donkey Car button SHIM](https://custom-build-robots.com/wp-content/uploads/2019/03/Donkey_Car_button_SHIM.jpg)

## Function overview buttons
The picture below shows the functions I implemented in the button.py program to control my Donkey Car.

![Donkey Car button SHIM function overview](https://custom-build-robots.com/wp-content/uploads/2019/03/Donkey_Car_function_overview-1.jpg)

## Autostart
This will start the control.sh script every time the Raspberry Pi is rebooted. For a better understanding the control.sh script will start the button.py script after each reboot of the Donkey Car.

To autostart the button.py program add the following line into your crontab. 

@reboot pi /home/pi/donkey_car_button_SHIM/control.sh >> /home/pi/control.log 2>&1 &
