# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685
from adafruit_servokit import ServoKit


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)
kit = ServoKit(channels=16)

kit.servo[1].angle = 90
kit.continuous_servo[0].throttle = 0.12
time.sleep(3)
kit.servo[1].angle = 180
kit.continuous_servo[0].throttle = 0.12
time.sleep(3)
kit.continuous_servo[0].throttle = 0.12
kit.servo[1].angle = 90
time.sleep(3)
kit.continuous_servo[0].throttle = 0

#kit.servo[1].angle = 180
#time.sleep(3)
#kit.servo[1].angle = 0
#time.sleep(3)
#kit.servo[1].angle = 90

#while True:

    # Move servo on channel O between extremes.
    #for i in range (10):
    #    pwm.set_pwm(i, 0, servo_min)
    #    print(i)
    #    time.sleep(1)
    #    pwm.set_pwm(i, 0, servo_max)
    #    time.sleep(1)
