from time import sleep
import RPi.GPIO as GPIO

'''
self.DIR = 20                # Direction GPIO Pin
self.STEP = 21               # Step GPIO Pin
'''

class StepperMotor:

    def __init__(self,offset,stepPin,dirPin) -> None:
        self.OFFSET = offset
        self.DIR = dirPin               # Direction GPIO Pin
        self.STEP = stepPin             # Step GPIO Pin
        self.SPR = 200                  # Steps per Revolution (360 / 1.8)
        self.curr_angle = 0             # Current position

    def initialize(self,direction):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.DIR, GPIO.OUT)
        GPIO.setup(self.STEP, GPIO.OUT)
        GPIO.output(self.DIR,direction)

        MODE = (14, 15, 18)   # Microstep Resolution GPIO Pins
        GPIO.setup(MODE, GPIO.OUT)
        RESOLUTION = {'Full': (0, 0, 0),
                    'Half': (1, 0, 0),
                    '1/4': (0, 1, 0),
                    '1/8': (1, 1, 0),
                    '1/16': (0, 0, 1),
                    '1/32': (1, 0, 1)}
        GPIO.output(MODE, RESOLUTION['Full'])

    def rotate_motor(self,angle,turbine = None ):
        curr_heading_angle = self.curr_angle + self.OFFSET
        target_heading_angle = angle + self.OFFSET

        if curr_heading_angle > 360:
            curr_heading_angle -= 360

        if target_heading_angle > 360:
            target_heading_angle -= 360

        angle_diff = target_heading_angle - curr_heading_angle
        steps = int(abs(angle_diff) * 0.55556)

        angle_diff = target_heading_angle - self.curr_angle
        direction = 0 if angle_diff < 0 else 1
        self.initialize(direction)

        delay = .0208
        for x in range(steps):
            GPIO.output(self.STEP, GPIO.HIGH)
            sleep(delay)
            GPIO.output(self.STEP, GPIO.LOW)
            sleep(delay)
            x += 1
            if turbine is not None:
                turbine_angle = angle - (x+1)
                if turbine_angle < 0:
                    turbine_angle = 0 - turbine_angle
                turbine.rotate_motor(angle-(x+1))
        self.curr_angle = angle
        GPIO.cleanup()