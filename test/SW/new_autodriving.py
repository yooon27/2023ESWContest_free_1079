import cv2
import os
import numpy as np
import time


def get_average_position(imag, height):
    start_time = time.time()

    pixel_b = imag[height:height + 200, :, 0]
    pixel_g = imag[height:height + 200, :, 1]
    pixel_r = imag[height:height + 200, :, 2]

    mask = (pixel_b != 0) & (pixel_g != 0) & (pixel_r != 0)
    rows, cols = np.where(mask)

    if len(rows) == 0:
        return None, None

    average_i = int(np.mean(cols))
    average_j = int(np.mean(rows))

    end_time = time.time()
    execution_time = end_time - start_time
    print("Fast Execution time : {:.6f} seconds".format(execution_time))

    return average_i, average_j

def get_average(imag, height):

    start_time = time.time()

    print(imag.shape)
    
    count = 0
    w = imag.shape[1]
    total_i = 0
    total_j = 0


    for i in range(0,w):
        for j in range(height,height+200):
            pixel_b,pixel_g,pixel_r = imag[j][i]
           
            if(pixel_b!=0 and pixel_g!=0 and pixel_r!=0):
                total_i += i
                total_j += j
                count += 1
                #print("error", total_i,total_j,count)

    average_i = total_i // count
    average_j = total_j // count

    print(average_i, average_j)

    end_time = time.time()
    execution_time = end_time - start_time
    print("Slow Execution time : {:.6f} seconds".format(execution_time))
    return average_i, average_j

    
def decision_to_go(slope):
    if(-10<slope<-5):
        carstate = "go"
    #elif
    #elif

    return carstate


def image_processing(image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blur to the grayscale frame
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # Apply binary thresholding to the blurred frame
        _, thresh = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY) # value should be modified 

        # Find contours in the binary frame
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        mask = np.zeros_like(image)

        cv2.drawContours(mask, contours, -1, (255, 255, 255), thickness=cv2.FILLED)

        
        return mask


    


def main():
    i = 0
    j = 0
    k = 0
    l = 0
    m = 0


    # Open the video file
    cap = cv2.VideoCapture("C:/Users/dongjin/Desktop/experiment.mp4")

    # Initialize car state to "go"
    carstate = "go"


    while cap.isOpened():
        key = cv2.waitKey(10) # Connect frame rate

        
        if key == 27:  # Press 'Esc' key to exit
            break

        elif key == 83:
            print("stop")
            carstate = "stop"

        elif key == 69:
            print("to_right")
            carstate = "to_right"
        elif key == 81:
            print("to_left")
            carstate = "to_left"

        elif key == 87:  
            print("go forward")
            carstate = "forward"
            # Motor go forward
        elif key == 65:  
            print("go left")
            carstate = "left"
        # Motor go left
        elif key == 68: 
            print("go right")
        carstate = "right"
        # Motor go right
    
    

    # Read continuous frames from the video
        ret, src = cap.read()
        if not ret:
            break

        print(src.shape)

        # Crop the source frame to a specific region of interest
        cropped_src = src[100:700, :300]

        mask = image_processing(cropped_src)
        
    
        upper_height = 0
        lower_height = 300
        upper_center_x, upper_center_y = get_average_position(mask, upper_height)
        lower_center_x, lower_center_y = get_average_position(mask,lower_height)

        #get_average(mask,upper_height)
        #get_average(mask,lower_height)
    
        #cv2.line(mask, (upper_center_x, upper_center_y),(lower_center_x, lower_center_y+lower_height), (0, 0, 255), 5)
        #print("slope: ", -(upper_center_y-(lower_center_y+lower_height))//(upper_center_x-lower_center_x))


        # Display the original and masked frames
        cv2.imshow("Original", src)
        cv2.imshow("Masked", mask)

    # Release the video and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()