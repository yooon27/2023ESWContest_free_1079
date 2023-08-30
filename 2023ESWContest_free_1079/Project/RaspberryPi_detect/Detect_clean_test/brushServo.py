import RPi.GPIO as GPIO
from time import sleep
import time

servo_pin = 12
brush = 2 #pin = 3
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT) 

pwm = GPIO.PWM(servo_pin, 50)
pwm.start(3.0)
GPIO.setup(brush, GPIO.OUT)



def servoMotor(boxState):
    if boxState == True:
        pwm.ChangeDutyCycle(6.5)
        time.sleep(0.1)
    elif boxState == False:
        pwm.ChangeDutyCycle(2.5)
        time.sleep(0.1)

def brushMotor(brushState):
    GPIO.output(brush, brushState)
