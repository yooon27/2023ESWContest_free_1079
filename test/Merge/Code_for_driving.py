import random
import numpy as np
import cv2
import RPi.GPIO as GPIO
from time import sleep
import tensorflow as tf
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
import serial
import time



# Motor states
STOP = 0
FORWARD = 1
BACKWARD = 2

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
ENA = 26  # 37 pin
ENB = 0   # 27 pin

# GPIO PIN
IN1 = 19  # 37 pin
IN2 = 13  # 35 pin
IN3 = 6   # 31 pin
IN4 = 5   # 29 pin


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

# Load RESNET 50 model(Should be modified)

model = load_model('address')


i = 0
j = 0
k = 0

cap = cv2.VideoCapture(0)  # Video file path

carstate = "stop"

while cap.isOpened():
    key = cv2.waitKey(10) & 0xFF  # Frame rate and key detection

    ret, src = cap.read()  # Read frames from the video

    if not ret:
        break

    ######################################
    # Receive using Serial Communication #
    ######################################

    
    distance = random

    if distance < 15 :
        carstate = "stop"
        
    
    else :
        src = cv2.flip(src,-1)
    
        gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # Convert to grayscale

        blurred = cv2.GaussianBlur(gray, (5, 5), 0)  # Apply Gaussian blur

        _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)  # Apply thresholding

        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # Find contours

        mask = np.zeros_like(src)  # Create a blank mask

        cv2.drawContours(mask, contours, -1, (255, 255, 255), thickness=cv2.FILLED)  # Draw contours on the mask


        cv2.imshow("Result", mask)

        input_image = cv2.resize(mask, (224, 224))  # Resize the image to match the model input size
        input_image = np.expand_dims(input_image, axis=0)
        input_image = input_image / 255.0  # Normalize the image (assuming the model was trained with normalized inputs)

        # Predict using the loaded model
        predictions = model.predict(input_image)
        predicted_class_index = np.argmax(predictions[0])
        predicted_class = ['stop', 'go', 'left', 'right'][predicted_class_index]

        # Update carstate based on the predicted direction
        carstate = predicted_class

    if key == 27:
        break
    elif carstate == "go":
        setMotor(CH1, 80, FORWARD)
        setMotor(CH2, 80, FORWARD)
        
    elif carstate == "left":
        setMotor(CH1, 80, FORWARD)
        setMotor(CH2, 80, BACKWARD)
    elif carstate == "right":
        setMotor(CH1, 80, BACKWARD)
        setMotor(CH2, 80, FORWARD)
       
    elif carstate == "stop":
        setMotor(CH1, 0, STOP)
        setMotor(CH2, 0, STOP)


# Cleanup GPIO
GPIO.cleanup()
cap.release()
cv2.destroyAllWindows()