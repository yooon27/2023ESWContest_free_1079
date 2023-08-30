import cv2
import os
import numpy as np
import RPi.GPIO as GPIO
import time
import math
import carControl

stop_state = False

def get_average_position(imag, height):
    start_time = time.time()
    #print(imag.shape)

    pixel_b = imag[height:height + 200, :, 0]
    pixel_g = imag[height:height + 200, :, 1]
    pixel_r = imag[height:height + 200, :, 2]

    mask = (pixel_b != 0) | (pixel_g != 0) | (pixel_r != 0)
    rows, cols = np.where(mask)

    if len(rows) == 0:
        return 0, 0

    
    average_i = int(np.mean(cols))
    average_j = int(np.mean(rows))
    
    end_time = time.time()
    execution_time = end_time - start_time
    #print("Fast Execution time : {:.6f} seconds".format(execution_time))

    return average_i, average_j

def slope_to_angle(slope):
    arc_tangent = math.atan(slope)

    if(arc_tangent < 0):
        arc_tangent_degrees = 180 + arc_tangent * (180 / math.pi)
    
    else:
        arc_tangent_degrees = arc_tangent * (180 / math.pi)
    
    return arc_tangent_degrees

    
def decision_to_go(angle):
    
    if(angle < -4):
        carstate = 'left'
        
    elif(angle > 4):
        carstate = 'right'
    
    else:
        carstate = 'forward'


    return carstate
    

def image_processing(image):
    # Convert the cropped frame to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to the grayscale frame
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply binary thresholding to the blurred frame
    _, thresh = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY) # value should be modified 

    # Find contours in the binary frame
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create a mask with the same size as the cropped frame
    mask = np.zeros_like(image)

    # Draw filled contours on the mask
    cv2.drawContours(mask, contours, -1, (255, 255, 255), thickness=cv2.FILLED)
    
    return mask
    


def tracking():

    # Open the video file
    cap = cv2.VideoCapture(0)

    # Initialize car state to "go"
    angle = 0
    carstate = "forward"
    global stop_state
    
    while cap.isOpened():
        key = cv2.waitKey(10) # Connect frame rate

        if key == 27:  # Press 'Esc' key to exit
            break

        while stop_state == True:
            carControl.carState("stop")


        carControl.carState(carstate,angle)

    # Read continuous frames from the video
        ret, src = cap.read()
        if not ret:
            break

        print(src.shape)

        # Crop the source frame to a specific region of interest
        cropped_src = src[:, :400]


        mask = image_processing(cropped_src)
    
        upper_height = 0
        lower_height = 250
        upper_center_x, upper_center_y = get_average_position(mask, upper_height)
        lower_center_x, lower_center_y = get_average_position(mask,lower_height)

        
        
        cv2.line(mask, (upper_center_x, upper_center_y),(lower_center_x,lower_center_y+lower_height), (0, 0, 255), 5)
        
        if(upper_center_x == 0 and upper_center_y == 0):
            slope = 0
            upper_center_x = lower_center_x
        elif(upper_center_x == lower_center_x):
            slope = 1000
            
        elif(upper_center_x != lower_center_x):
            slope = -(upper_center_y-(lower_center_y+lower_height))/(upper_center_x-lower_center_x)
            angle = slope_to_angle(slope)
            angle = 72.5 -angle
        
        

        print(angle)
        carstate = decision_to_go(angle)
        
        if(angle > 20):angle = 19.5
        if(angle < -15):angle = - 14.5
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        font_color = (255, 0, 255)
        thickness = 2
        position = (50, 50)
    
        cv2.putText(mask, carstate, position, font, font_scale, font_color, thickness, cv2.LINE_AA)
        cv2.putText(mask, "{:.2f} degree".format(angle), (50,100) , font, font_scale, font_color, thickness, cv2.LINE_AA)
         

        # Display the original and masked frames
        cv2.imshow("Original", src)
        cv2.imshow("Masked", mask)
        
        
def drainStop():
    global stop_state
    stop_state = not stop_state