import numpy as np
import cv2
import os

# Dataset storage paths
dataset_path = "C:/Users/ehdwl/Desktop/Trainingset"
dataset_path_right = "C:/Users/ehdwl/Desktop/Trainingset/right"
dataset_path_left = "C:/Users/ehdwl/Desktop/Trainingset/left"
dataset_path_forward = "C:/Users/ehdwl/Desktop/Trainingset/forward"

i = 0
j = 0
k = 0

# Open the video file
cap = cv2.VideoCapture("C:/Users/ehdwl/Desktop/road_video2.mp4")

# Initialize car state to "go"
carstate = "go"

while cap.isOpened():
    k = cv2.waitKey(10) & 0xFF  # Connect frame rate
    if k == 27:  # Press 'Esc' key to exit
        break
    elif k == 82:  # Press 'R' key to go forward
        print("go forward")
        carstate = "go"
        # Motor go forward
    elif k == 81:  # Press 'Q' key to go left
        print("go left")
        carstate = "left"
        # Motor go left
    elif k == 83:  # Press 'S' key to go right
        print("go right")
        carstate = "right"
        # Motor go right
    elif k == 84:  # Press 'T' key to stop
        print("stop")
        carstate = "stop"
        # Motor stop

    # Read continuous frames from the video
    ret, src = cap.read()
    if not ret:
        break

    print(src.shape)
    # Crop the source frame to a specific region of interest
    cropped_src = src[100:500, :]

    # Convert the cropped frame to grayscale
    gray = cv2.cvtColor(cropped_src, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to the grayscale frame
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply binary thresholding to the blurred frame
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

    # Find contours in the binary frame
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create a mask with the same size as the cropped frame
    mask = np.zeros_like(cropped_src)

    # Draw filled contours on the mask
    cv2.drawContours(mask, contours, -1, (255, 255, 255), thickness=cv2.FILLED)

    # Display the original and masked frames
    cv2.imshow("Original", src)
    cv2.imshow("Result", mask)

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

# Release the video and close all windows
cap.release()
cv2.destroyAllWindows()
