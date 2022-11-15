from operator import truediv
from time import sleep
#import RPi.GPIO as GPIO

DIR = 20                # Direction GPIO Pin
STEP = 21               # Step GPIO Pin
ROTATION: bool = 1      # Direction of rotation (1 - CW, 0 - CCW)
SPR = 48                # Steps per Revolution (360 / 7.5)
CURR_STEP_SOLAR = 0     # Tracks the position of the x-axis stepper motor for solar
CURR_STEP_WIND = 0      # Tracks the position of the x-axis stepper motor for wind

'''
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)   # direction pin is out
GPIO.setup(STEP, GPIO.OUT)  # step pin is out
GPIO.output(DIR, ROTATION)        # clockwise direction
'''

step_cnt = SPR
delay = 0.0208

''' 360 rotation and back

# Clockwise
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)

sleep(.5)

# Counter Clockwise
ROTATION = 0
GPIO.output(DIR, ROTATION)
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)

'''

#GPIO.cleanup()

def solar_x(steps):

    for x in range(steps):
        if CURR_STEP_SOLAR == SPR:
            ROTATION = not ROTATION
            #GPIO.output(DIR,ROTATION)
            CURR_STEP_SOLAR = 0
        #GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        #GPIO.output(STEP, GPIO.LOW)
        sleep(delay)
        wind(1,True)
        CURR_STEP_SOLAR += 1

def wind(steps,solar=False):

    for x in range(steps):
        if solar:
            wind_rotation = not ROTATION
        else:
            wind_rotation = ROTATION
        if CURR_STEP_WIND == SPR:
            wind_rotation = not wind_rotation
            #GPIO.output(DIR,ROTATION)
            CURR_STEP_WIND = 0
        #GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        #GPIO.output(STEP, GPIO.LOW)
        sleep(delay)
        CURR_STEP_WIND += 1

