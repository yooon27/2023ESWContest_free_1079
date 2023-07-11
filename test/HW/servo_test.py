import RPi.GPIO as GPIO
import time

servo_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

pwm = GPIO.PWM(servo_pin, 50) # PWM waveform with a frequency of 50Hz.
pwm.start(3.0) # Start PWM control. 3.0 represents the minimum position of the motor. The maximum position is 12.5.

while True:
x = int(input("Enter a number (0 or 1): ")) # Receive a value of 0 or 1 (In actual usage, it controls whether the servo is operating or not with 0 and 1.)

if x == 0:
    pwm.ChangeDutyCycle(8.89)  # Move the motor to 115 degrees when x is 0 ((115/18.0) + 2.5 = 8.888888 = 8.9)
    time.sleep(1)
    pwm.ChangeDutyCycle(0.0)  # Stop after movement (to avoid vibration if not stopped)
    time.sleep(1)
    
elif x == 1:
    pwm.ChangeDutyCycle(2.5)  # Move to 0 degrees when x is 1 (2.5 represents 0 degrees)
    time.sleep(1)
    break  # Break the loop

pwm.stop()
GPIO.cleanup()
