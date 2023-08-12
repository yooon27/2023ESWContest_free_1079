import numpy as np
import cv2
import os

# Dataset storage paths
dataset_path = "C:/Users/dongjin/Desktop/Trainingset"

dataset_path_right = "C:/Users/dongjin/Desktop/Trainingset/right"

dataset_path_left = "C:/Users/dongjin/Desktop/Trainingset/left"

dataset_path_forward = "C:/Users/dongjin/Desktop/Trainingset/forward"

dataset_path_to_left = "C:/Users/dongjin/Desktop/Trainingset/to_left"

dataset_path_to_right = "C:/Users/dongjin/Desktop/Trainingset/to_right"

i = 0
j = 0
k = 0
l = 0
m = 0


# Open the video file
cap = cv2.VideoCapture("C:/Users/dongjin/Desktop/Lane detect test data.mp4")

# Initialize car state to "go"
carstate = "go"


while cap.isOpened():
    key = cv2.waitKey(10) # Connect frame rate

    print(key)
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

    # Crop the source frame to a specific region of interest
    cropped_src = src[200:600, :]

    # Convert the cropped frame to grayscale
    gray = cv2.cvtColor(cropped_src, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to the grayscale frame
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply binary thresholding to the blurred frame
    _, thresh = cv2.threshold(blurred, 180, 255, cv2.THRESH_BINARY) # value should be modified 

    # Find contours in the binary frame
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create a mask with the same size as the cropped frame
    mask = np.zeros_like(cropped_src)

    # Draw filled contours on the mask
    cv2.drawContours(mask, contours, -1, (255, 255, 255), thickness=cv2.FILLED)
    
    

    # Save the frames with appropriate labels based on the car state
    if carstate == "right":
    
        cv2.imwrite(os.path.join(dataset_path_right, "right_%05d.jpg" % i), mask)
        i += 1

    elif carstate == "left":
      
        cv2.imwrite(os.path.join(dataset_path_left, "left_%05d.jpg" % j), mask)
        j += 1

    elif carstate == "go":
       
        cv2.imwrite(os.path.join(dataset_path_forward, "forward_%05d.jpg" % k), mask)
        k += 1

    elif carstate == "to_right":
      
        cv2.imwrite(os.path.join(dataset_path_to_right, "to_right_%05d.jpg" % l), mask)
        l += 1
    elif carstate == "to_left":
        
        cv2.imwrite(os.path.join(dataset_path_to_left, "to_left_%05d.jpg" % m), mask)
        m += 1
    
    # Display the original and masked frames
    cv2.imshow("Original", src)
    cv2.imshow("Masked", mask)

# Release the video and close all windows
cap.release()
cv2.destroyAllWindows()
