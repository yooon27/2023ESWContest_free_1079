#carControl
import RPi.GPIO as GPIO
from time import sleep
import time


STOP = 0
FORWARD = 1
BACKWARD = 2
LEFT = 3
RIGHT = 4
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


CH1 = 0
CH2 = 1

OUTPUT = 1
INPUT = 0

HIGH = 1
LOW = 0

ENA = 26  # 37 pin
ENB = 0   # 27 pin

# GPIO PIN
IN1 = 19  # 37 pin
IN2 = 13  # 35 pin
IN3 = 6   # 31 pin
IN4 = 5   # 29 pin

def setPinConfig(EN, INA, INB):
    GPIO.setup(EN, GPIO.OUT)
    GPIO.setup(INA, GPIO.OUT)
    GPIO.setup(INB, GPIO.OUT)
    pwm = GPIO.PWM(EN, 100)
    pwm.start(0)
    return pwm


def setMotorControl(pwm, INA, INB, speed, stat):
    pwm.ChangeDutyCycle(speed)

    if stat == FORWARD:
        GPIO.output(INA, HIGH)
        GPIO.output(INB, LOW)

    elif stat == BACKWARD:
        GPIO.output(INA, LOW)
        GPIO.output(INB, HIGH)

    elif stat == STOP:
        GPIO.output(INA, LOW)
        GPIO.output(INB, LOW)


def setMotor(ch, speed, stat):
    if ch == CH1:
        setMotorControl(pwmA, IN1, IN2, speed, stat)
    elif ch == CH2:
        setMotorControl(pwmB, IN3, IN4, speed, stat)


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


pwmA = setPinConfig(ENA, IN1, IN2)
pwmB = setPinConfig(ENB, IN3, IN4)


def carState(carstate):

    if carstate == "stop":
        print("stop")
        setMotor(CH1, 0, STOP)
        setMotor(CH2, 0, STOP)
                    
       
    elif carstate == "go":
        print("go")
        carstate = "go"
        setMotor(CH1, 50, FORWARD)
        setMotor(CH2, 50, FORWARD)
                
                
    elif carstate == "left":
        print("left")
        setMotor(CH1, 0, FORWARD)
        setMotor(CH2, 80, FORWARD)
                    
                    
    elif carstate == "right":
        print("right")
        carstate = "right"
        setMotor(CH1, 80, FORWARD)
        setMotor(CH2, 0, FORWARD)
        
