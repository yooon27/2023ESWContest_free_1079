#tracking
import robotState
import carControl
from time import sleep
import time
import cv2
import numpy as np

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

    
def decision_to_go(slope):
    if(slope<0 or slope >1000):
        carstate = 'left'
    elif(slope<13):
        carstate = 'right'
    else:
        carstate = 'forward'


    return carstate
    


def tracking():
    i = 0
    j = 0
    k = 0
    l = 0
    m = 0

    cap = cv2.VideoCapture(1)

    carstate = "forward"

    while cap.isOpened():
        key = robotState.robotState()
        if key != "tracking":  # Press 'Esc' key to exit
            break

        carControl.carState(carstate)
                
                
        # Read continuous frames from the video
        ret, src = cap.read()
        if not ret:
            break

            #print(src.shape)

            # Crop the source frame to a specific region of interest
        cropped_src = src[:, :400]


            # Convert the cropped frame to grayscale
        gray = cv2.cvtColor(cropped_src, cv2.COLOR_BGR2GRAY)

            # Apply Gaussian blur to the grayscale frame
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

            # Apply binary thresholding to the blurred frame
        _, thresh = cv2.threshold(blurred, 190, 255, cv2.THRESH_BINARY_INV) # value should be modified 

            # Find contours in the binary frame
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # Create a mask with the same size as the cropped frame
        mask = np.zeros_like(cropped_src)

            # Draw filled contours on the mask
        cv2.drawContours(mask, contours, -1, (255, 255, 255), thickness=cv2.FILLED)
        
        upper_height = 0
            #middle_height = 350
        lower_height = 350
        upper_center_x, upper_center_y = get_average_position(mask, upper_height)
            #middle_center_x, middle_center_y = get_average_position(mask, middle_height)
        lower_center_x, lower_center_y = get_average_position(mask,lower_height)

            
            #get_average(mask,upper_height)
            #get_average(mask,lower_height)

        if(upper_center_x == 0 and upper_center_y == 0):
            upper_center_x, upper_center_y = lower_center_x, lower_center_y


        cv2.line(mask, (upper_center_x, upper_center_y),(lower_center_x,lower_center_y+lower_height), (0, 0, 255), 5)
            #cv2.line(mask, (middle_center_x,middle_center_y+middle_height),(lower_center_x,lower_center_y+lower_height),(0,0,255),5)
            #cv2.line(mask, (upper_center_x, upper_center_y),(middle_center_x,middle_center_y+middle_height), (0, 0, 255), 5)


        if(upper_center_x == lower_center_x):
            slope = 1000
        elif(upper_center_x != lower_center_x):
            slope = -(upper_center_y-(lower_center_y+lower_height))/(upper_center_x-lower_center_x)
                
            

        
        carstate = decision_to_go(slope)
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        font_color = (255, 0, 0)  
        thickness = 2
        position = (50, 50)  
            
        cv2.putText(mask, carstate, position, font, font_scale, font_color, thickness, cv2.LINE_AA)
        #cv2.putText(mask, slope, 100,50, font, font_scale, font_color, thickness, cv2.LINE_AA)
            
            

        # Display the original and masked frames
        cv2.imshow("Original", src)
        cv2.imshow("Masked", mask)

        # Release the video and close all windows
    cap.release()
    cv2.destroyAllWindows()

