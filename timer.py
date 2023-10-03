"""
This program is used as an example for MGTC28.
timer.py is a simple Python script that will allow user to set timer duration.
Upon timer expiry, user will see the time up meme and sound notification.
timer.py uses the time library to help keep track of time
"""


# This program is timer that counts down

import random
import time # The time library has a sleep function that will pause the script for a specifized amount of time

#Game Start display begin signal
print ("Player stand")

#Randomly generate a sleep time
set_time = random.randint(5,25)

#Stall the program by the randomly generated number 
time.sleep(set_time)

#Game End display end signal
print ("Time Up. Last to Sit down wins")


