from time import sleep
import RPi.GPIO as GPIO

DIR = 20                # Direction GPIO Pin
STEP = 21               # Step GPIO Pin
SPR = 200               # Steps per Revolution (360 / 1.8)
curr_angle = 0          # Current position

def initialize(direction):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DIR, GPIO.OUT)
    GPIO.setup(STEP, GPIO.OUT)
    GPIO.output(DIR,direction)

    MODE = (14, 15, 18)   # Microstep Resolution GPIO Pins
    GPIO.setup(MODE, GPIO.OUT)
    RESOLUTION = {'Full': (0, 0, 0),
                'Half': (1, 0, 0),
                '1/4': (0, 1, 0),
                '1/8': (1, 1, 0),
                '1/16': (0, 0, 1),
                '1/32': (1, 0, 1)}
    GPIO.output(MODE, RESOLUTION['Full'])

def rotate_motor(angle):
    global curr_angle
    angle_diff = angle - curr_angle
    steps = abs(angle_diff) * 1.8
    direction = 0 if angle_diff < 0 else 1
    initialize(direction)
    delay = .0208
    x = 0
    while x <= steps:
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)
        x += 0.1
    curr_angle = angle
    GPIO.cleanup()

rotate_motor(50)
rotate_motor(200)
rotate_motor(150)
