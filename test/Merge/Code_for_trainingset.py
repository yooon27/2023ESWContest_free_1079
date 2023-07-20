import numpy as np
import cv2
import os
import RPi.GPIO as GPIO
from time import sleep

# Define motor control states
STOP = 0
FORWARD = 1
BACKWARD = 2

# Define motor channels
CH1 = 0
CH2 = 1

# Define GPIO pin modes
OUTPUT = 1
INPUT = 0

# Define GPIO pin levels
HIGH = 1
LOW = 0

# Define GPIO pin assignments for motor control
ENA = 26  # GPIO pin 37
ENB = 0   # GPIO pin 27

IN1 = 19  # GPIO pin 37
IN2 = 13  # GPIO pin 35
IN3 = 6   # GPIO pin 31
IN4 = 5   # GPIO pin 29

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
    else:
        setMotorControl(pwmB, IN3, IN4, speed, stat)

# Set GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Initialize PWM configurations for motor control
pwmA = setPinConfig(ENA, IN1, IN2)
pwmB = setPinConfig(ENB, IN3, IN4)

# Initialize variables for car state
i = 0
j = 0
k = 0

# Open video capture from camera
cap = cv2.VideoCapture(0)

# Initialize carstate as "stop"
carstate = "stop"

while cap.isOpened():
    k = cv2.waitKey(10) & 0xFF  # Capture keyboard input
    if k == 27:  # Press 'Esc' key to exit
        break
    elif k == 82:  # Press 'R' key to go forward
        print("go")
        carstate = "go"
        setMotor(CH1, 80, FORWARD)
        setMotor(CH2, 80, FORWARD)
        
    elif k == 81:  # Press 'Q' key to go left
        print("left")
        carstate = "left"
        setMotor(CH1, 80, FORWARD)
        setMotor(CH2, 80, BACKWARD)

    elif k == 83:  # Press 'S' key to go right
        print("right")
        carstate = "right"
        setMotor(CH1, 80, BACKWARD)
        setMotor(CH2, 80, FORWARD)
       
    elif k == 84:  # Press 'T' key to stop
        print("stop")
        carstate = "stop"
        setMotor(CH1, 0, STOP)
        setMotor(CH2, 0, STOP)

    ret, src = cap.read()  # Capture continuous frames from the camera
    if not ret:
        break

    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # Convert frame to grayscale

    blurred = cv2.GaussianBlur(gray, (5, 5), 0)  # Apply Gaussian blur

    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)  # Apply thresholding

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # Find contours

    mask = np.zeros_like(src)  # Create a mask with the same size as the frame

    cv2.drawContours(mask, contours, -1, (255, 255, 255), thickness=cv2.FILLED)  # Draw filled contours on the mask
    
    cv2.imshow("Result", mask)  # Display the masked frame

GPIO.cleanup()  # Clean up GPIO pins
cap.release()  # Release video capture
cv2.destroyAllWindows()  # Close all windows
