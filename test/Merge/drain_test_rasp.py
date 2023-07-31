import serial
import time
import RPi.GPIO as GPIO

# Motor states
STOP = 0
FORWARD = 1
BACKWARD = 2
LEFT = 3
RIGHT = 4

#LiDAR states
count = 0
distance_avg = 0
distance_tot = 0

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
ENB = 27
# GPIO PIN
IN1 = 19  # GPIO 37
IN2 = 13  # GPIO 35
IN3 = 6   # GPIO 31
IN4 = 5   # GPIO 29

# Pin configuration function
def setPinConfig(EN, INA, INB):
    GPIO.setwarnings(False)
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
        
def Motor_backward():
    setMotor(CH1, 80, BACKWARD)
    setMotor(CH2, 80, BACKWARD)
 
def Motor_go():
    setMotor(CH1, 80, FORWARD)
    setMotor(CH2, 80, FORWARD)

def Motor_stop():
    setMotor(CH1, 80, STOP)
    setMotor(CH2, 80, STOP)

def Motor_left():
    setMotor(CH1, 80, FORWARD)
    setMotor(CH2, 80, BACKWARD)

def Motor_right():
    setMotor(CH1, 80, BACKWARD)
    setMotor(CH2, 80, FORWARD)

# GPIO mode setting
GPIO.setmode(GPIO.BCM)

# Motor pin configuration
# Get PWM handles after pin configuration
pwmA = setPinConfig(ENA, IN1, IN2)
pwmB = setPinConfig(ENB, IN3, IN4)

#main
if __name__ == '__main__':
    serial = serial.Serial('/dev/ttyUSB0',115200,timeout=None)
    serial.flush()
    while True:
        Motor_go() #line tracking function
        if serial.in_waiting>0:
            line = serial.readline().decode('utf=8').rstrip()
            arr = line.split()
            
            distance_center = int(arr[3])
            distance_1 = int(arr[6])
            distance_2 = int(arr[9])
            distance_cal = int(arr[12])
            count += 1
            distance_tot += distance_cal
            if count == 50:
                distance_avg = distance_tot/50
                if distance_avg > 15 and distance_avg < 30:
                    print("Motor stop\n")
                    Motor_stop()
                    time.sleep(5)
                    print("take picture\n")
                    print("picture transmit\n")
                    print("Motor go\n")
                    Motor_go() #motor forward
                    print(distance_avg)
                    time.sleep(5) #escape drain
                distance_tot = 0
                count = 0
            
            print(count,distance_center, distance_1 ,distance_2, distance_cal, distance_avg)
    # Cleanup GPIO
    GPIO.cleanup()
            
            
