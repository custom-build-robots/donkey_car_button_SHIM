#!/usr/bin/env python
# Autor:   Ingmar Stapel
# Datum:   20190125
# Version:   1.0
# Homepage:   http://custom-build-robots.com

# This python script will help you to control the Donkey Car.
# To use this program a Pimoroni Button Shim needs to be installed
# on your Donkey Car.
# Button A: Shutdown the Raspberry Pi
# Button B: Start training mode
# Button C: Start auto pilot mode
# Button D: Generate videos from the tub folders pictures
# Button E: Copy the data folder plus videos to an usb stick

import signal
import buttonshim
import subprocess
import time
from subprocess import Popen
global process
process = None

from sys import version_info

import os

def mountusb():
   process_usb = subprocess.Popen(["sudo", "mount", "-t", "exfat", "-o", "utf8,uid=pi,gid=pi,noatime", "/dev/sda1", "/media/usbstick"]) 
   while True:
      poll = process_usb.poll()
      if poll == None:
         buttonshim.set_pixel(0x00, 0xff, 0x00)
         time.sleep(0.1)
         buttonshim.set_pixel(0x00, 0x00, 0x00)       
      else:
         process_usb = None
         buttonshim.set_pixel(0x00, 0x00, 0xff)
         break

def unmountusb():
   process_usb = subprocess.Popen(["sudo", "umount", "/media/usbstick"]) 
   while True:
         poll = process_usb.poll()
         if poll == None:
            buttonshim.set_pixel(0x00, 0xff, 0x00)
            time.sleep(0.1)
            buttonshim.set_pixel(0x00, 0x00, 0x00)       
         else:
            process_usb = None
            buttonshim.set_pixel(0x00, 0x00, 0xff)
            break

@buttonshim.on_press(buttonshim.BUTTON_A)
def button_a(button, pressed):
   for x in range(3):
       buttonshim.set_pixel(0xff, 0x00, 0x00)
       time.sleep(0.1)
       buttonshim.set_pixel(0x00, 0x00, 0x00)
   time.sleep(0.1)
   os.system("sudo halt")

# Start the Donkey Car drive mode to record training data
@buttonshim.on_press(buttonshim.BUTTON_B)
def button_b(button, pressed):
   global process
   if process == None:
      process = subprocess.Popen(["python", "/home/pi/mycar/manage.py", "drive"]) 
      #print("Starting PID: ", process.pid)
      for x in range(9):
         buttonshim.set_pixel(0x00, 0xff, 0x00)
         time.sleep(0.05)
         buttonshim.set_pixel(0x00, 0x00, 0x00)
      buttonshim.set_pixel(0x00, 0xff, 0x00)   
   else:
      #print("Killing PID: ", process.pid)
      process.terminate()
      for x in range(9):
         buttonshim.set_pixel(0xff, 0x00, 0x00)
         time.sleep(0.05)
         buttonshim.set_pixel(0x00, 0x00, 0x00)
      process = None
      buttonshim.set_pixel(0x00, 0x00, 0xff)

   time.sleep(0.1)

# Start the Donkey Car auto mode to autonomously drive around
@buttonshim.on_press(buttonshim.BUTTON_C)
def button_c(button, pressed):
   global process

   mountusb()

   if process == None:
      process = subprocess.Popen(["python", "/home/pi/mycar/manage.py", "--model", "/home/pi/mycar/mypilot"]) 
      
      #print("Starting PID: ", process.pid)
      for x in range(9):
         buttonshim.set_pixel(0x00, 0xff, 0x00)
         time.sleep(0.05)
         buttonshim.set_pixel(0x00, 0x00, 0x00)
      buttonshim.set_pixel(0x00, 0xff, 0x00)   
   else:
      #print("Killing PID: ", process.pid)
      process.terminate()
      unmountusb()

      for x in range(9):
         buttonshim.set_pixel(0xff, 0x00, 0x00)
         time.sleep(0.05)
         buttonshim.set_pixel(0x00, 0x00, 0x00)
      process = None
      buttonshim.set_pixel(0x00, 0x00, 0xff)

   time.sleep(0.1)

@buttonshim.on_press(buttonshim.BUTTON_D)
def button_d(button, pressed):
   global process
   
   if process == None:
      process = subprocess.Popen(["sh", "/home/pi/tub2movie.sh"]) 
      for x in range(9):
         buttonshim.set_pixel(0x00, 0xff, 0x00)
         time.sleep(0.05)
         buttonshim.set_pixel(0x00, 0x00, 0x00)
      buttonshim.set_pixel(0x00, 0xff, 0x00)   
   while True:
         poll = process.poll()
         if poll == None:
            buttonshim.set_pixel(0x00, 0xff, 0x00)
            time.sleep(0.1)
            buttonshim.set_pixel(0x00, 0x00, 0x00)       
         else:
            process = None
            buttonshim.set_pixel(0x00, 0x00, 0xff)
            break

@buttonshim.on_press(buttonshim.BUTTON_E)
def button_e(button, pressed):
   global process
   
   if process == None:
      # tar example
      process = subprocess.Popen(["tar", "-cf" "team_00.tar", "/home/pi/mycar/data/"])
      for x in range(9):
         buttonshim.set_pixel(0x00, 0xff, 0x00)
         time.sleep(0.05)
         buttonshim.set_pixel(0x00, 0x00, 0x00)
      buttonshim.set_pixel(0x00, 0xff, 0x00)   
   while True:
         poll = process.poll()
         if poll == None:
            buttonshim.set_pixel(0x00, 0xff, 0x00)
            time.sleep(0.1)
            buttonshim.set_pixel(0x00, 0x00, 0x00)       
         else:
            process = None
            buttonshim.set_pixel(0x00, 0x00, 0xff)
            break
   time.sleep(1)

   mountusb()     

   time.sleep(1) 
   if process == None:
      process = subprocess.Popen(["cp", "/home/pi/team_00.tar", "/media/usbstick"]) 
   while True:
         poll = process.poll()
         if poll == None:
            buttonshim.set_pixel(0x00, 0xff, 0x00)
            time.sleep(0.1)
            buttonshim.set_pixel(0x00, 0x00, 0x00)       
         else:
            process = None
            buttonshim.set_pixel(0x00, 0x00, 0xff)
            break
   time.sleep(1) 

   unmountusb()


buttonshim.set_pixel(0x00, 0x00, 0xff)

signal.pause()
