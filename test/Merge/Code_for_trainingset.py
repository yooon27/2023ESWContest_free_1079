import numpy as np
import cv2
import os
import RPi.GPIO as GPIO
from time import sleep

# Motor states
STOP = 0
FORWARD = 1
BACKWARD = 2
LEFT = 3
RIGHT = 4

# Motor channels
CH1 = 0
CH2 = 1

# Pin I/O settings
OUTPUT = 1
INPUT = 0

# Pin settings
HIGH = 1
LOW = 0

# Physical pin definitions
# PWM PIN
ENA = 26  # GPIO 37

# GPIO PIN
IN1 = 19  # GPIO 37
IN2 = 13  # GPIO 35
IN3 = 6   # GPIO 31
IN4 = 5   # GPIO 29

# Pin configuration function
def setPinConfig(EN, INA, INB):
    GPIO.setup(EN, GPIO.OUT)
    GPIO.setup(INA, GPIO.OUT)
    GPIO.setup(INB, GPIO.OUT)

    # Set PWM frequency to 100kHz
    pwm = GPIO.PWM(EN, 100)

    # Initially stop PWM
    pwm.start(0)
    return pwm

# Motor control function
def setMotorControl(pwm, INA, INB, speed, stat):
    # Set motor speed with PWM
    pwm.ChangeDutyCycle(speed)

    if stat == FORWARD:
        GPIO.output(INA, HIGH)
        GPIO.output(INB, LOW)

    # Backward
    elif stat == BACKWARD:
        GPIO.output(INA, LOW)
        GPIO.output(INB, HIGH)

    # Stop
    elif stat == STOP:
        GPIO.output(INA, LOW)
        GPIO.output(INB, LOW)

    # Left
    elif stat == LEFT:
        GPIO.output(INA, LOW)
        GPIO.output(INB, HIGH)

    # Right
    elif stat == RIGHT:
        GPIO.output(INA, HIGH)
        GPIO.output(INB, LOW)


# Simplified motor control function
def setMotor(ch, speed, stat):
    if ch == CH1:
        # pwmA is the PWM handle returned after pin configuration
        setMotorControl(pwmA, IN1, IN2, speed, stat)
    else:
        # pwmB is the PWM handle returned after pin configuration
        setMotorControl(pwmB, IN3, IN4, speed, stat)


# GPIO mode setting
GPIO.setmode(GPIO.BCM)

# Motor pin configuration
# Get PWM handles after pin configuration
pwmA = setPinConfig(ENA, IN1, IN2)
pwmB = setPinConfig(ENB, IN3, IN4) #ENB??

# Dataset saving paths
dataset_path = "/home/raspberrypi/dataset"
os.makedirs(dataset_path, exist_ok=True)

dataset_path_right = os.path.join(dataset_path, "right")
os.makedirs(dataset_path_right, exist_ok=True)

dataset_path_left = os.path.join(dataset_path, "left")
os.makedirs(dataset_path_left, exist_ok=True)

dataset_path_forward = os.path.join(dataset_path, "forward")
os.makedirs(dataset_path_forward, exist_ok=True)

i = 0
j = 0
k = 0

cap = cv2.VideoCapture(0)  # Video file path

carstate = "stop"

while cap.isOpened():
    k = cv2.waitKey(10) & 0xFF  # Frame rate and key detection
    if k == 27:
        break
    elif k == 82:
        print("go")
        carstate = "go"
        setMotor(CH1, 80, FORWARD)
        setMotor(CH2, 80, FORWARD)
        
    elif k == 81:
        print("left")
        carstate = "left"
        setMotor(CH1, 80, FORWARD)
        setMotor(CH2, 80, BACKWARD)
    elif k == 83:
        print("right")
        carstate = "right"
        setMotor(CH1, 80, BACKWARD)
        setMotor(CH2, 80, FORWARD)
       
    elif k == 84:
        print("stop")
        carstate = "stop"
        setMotor(CH1, 0, STOP)
        setMotor(CH2, 0, STOP)

    ret, src = cap.read()  # Read frames from the video
    if not ret:
        break

    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # Convert to grayscale

    blurred = cv2.GaussianBlur(gray, (5, 5), 0)  # Apply Gaussian blur

    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)  # Apply thresholding

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # Find contours

    mask = np.zeros_like(src)  # Create a blank mask

    cv2.drawContours(mask, contours, -1, (255, 255, 255), thickness=cv2.FILLED)  # Draw contours on the mask

    # Save label information
    
    cv2.imshow("Result", mask)

    if carstate == "right":
        cv2.imwrite(os.path.join(dataset_path_right, "right_%05d.jpg" % i), mask)
        i += 1
    elif carstate == "left":
        cv2.imwrite(os.path.join(dataset_path_left, "left_%05d.jpg" % j), mask)
        j += 1
    elif carstate == "go":
        cv2.imwrite(os.path.join(dataset_path_forward, "forward_%05d.jpg" % k), mask)
        k += 1

# Cleanup GPIO
GPIO.cleanup()
cap.release()
cv2.destroyAllWindows()