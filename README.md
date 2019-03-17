# Donkey Car - button SHIM
I developed this idea during meetups and presentation when I had problems to connect the Donkey Car to the local WIFI. To start the main functions from the Donkey Car like the drive mode to show the car in cation it was much easier and safer to use the buttons. 

At the end I implemented the PIMORONI button SHIM to start the Donkey Car training mode or self-driving mode... or just to shutdown the Conkey Car at the end of a presentation or run. 

Da detailed description is available on my blog: https://custom-build-robots.com/raspberry-pi-roboter/autonom-fahrendes-raspberry-pi-ki-roboter-auto-short-keys/10922

My Donkey Car with the mounted button SHIM from PIMORONI.
![Donkey Car button SHIM](https://custom-build-robots.com/wp-content/uploads/2019/03/Donkey_Car_button_SHIM.jpg)

## Function overview buttons
![Donkey Car button SHIM function overview](https://custom-build-robots.com/wp-content/uploads/2019/03/Donkey_Car_function_overview-1.jpg)

## Autostart
To autostart the button.py program add the following line into your crontab. This will start the control.sh script every time the Raspberry Pi is rebooted.
@reboot pi /home/pi/control.sh >> /home/pi/control.log 2>&1 &
