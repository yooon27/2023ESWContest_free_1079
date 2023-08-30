import numpy as np
import cv2
import RPi.GPIO as GPIO
from time import sleep
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model
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

# Load MobilenetV2 model
#You can load learned model by path
#model_path = '/home/pi/models/autodriving_256.h5'
#model = load_model('model_path')
model = load_model('autodriving_256.h5')



cap = cv2.VideoCapture(0)  # Video file path

carstate = "stop"

while cap.isOpened():

    ret, src = cap.read()  # Read frames from the video

    if not ret:
        break


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
    predicted_class = ['go_case1', 'go_left_case1', 'go_right_case1', 'left_case1','right_case1'][predicted_class_index]

    # Update carstate based on the predicted direction
    carstate = predicted_class

    key = cv2.waitKey(10) & 0xFF

    if key == 27:
        break

    elif key == ord('s'):
        carstate = "stop"

    else:
        if carstate == "go_case1":
            setMotor(CH1, 80, FORWARD)
            setMotor(CH2, 80, FORWARD)
        
        elif carstate == "go_left_case1":
            setMotor(CH1, 40, FORWARD)
            setMotor(CH2, 70, FORWARD)
        elif carstate == "go_right_case1":
            setMotor(CH1, 70, FORWARD)
            setMotor(CH2, 40, FORWARD)
       
        elif carstate == "left_case1":
            setMotor(CH1, 40, STOP)
            setMotor(CH2, 100, STOP)
        elif carstate == "right_case1":
            setMotor(CH1, 100, FORWARD)
            setMotor(CH2, 40, FORWARD)
        elif carstate == "stop":
            setMotor(CH1, 0, STOP)
            setMotor(CH2, 0, STOP)
            
# Cleanup GPIO
GPIO.cleanup()
cap.release()
cv2.destroyAllWindows()