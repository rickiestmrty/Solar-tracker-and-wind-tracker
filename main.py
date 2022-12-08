from lib.raspi_stepper import StepperMotor
from lib.sun_calc import SunCalc
from lib.magnetometer import Magnetometer

def main():
    magnetometer = Magnetometer()
    offset = magnetometer.calculate_heading_angle()

    solar_motor_x = StepperMotor(offset,27,22)
    solar_motor_y = StepperMotor(offset,23,24)
    wind_motor = StepperMotor(offset,20,21)

    suntracker = SunCalc(10.35189,123.91335)

    while True:
        curr_sun_pos = suntracker.get_angle()
        solar_motor_x.rotate_motor(curr_sun_pos[0],wind_motor)


if __name__ == "__main__":
    main()