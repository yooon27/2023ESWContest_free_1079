import cv2
import time

# Create a VideoCapture object for the webcam (use 0 for the default webcam)
webcam = cv2.VideoCapture(0)

# Set the streaming interval (in seconds)
stream_interval = 5
i = 0

# Get the current time in seconds
start_time = time.time()

while True:
    # Capture frame-by-frame from the webcam
    ret_webcam, frame_webcam = webcam.read()

    # Perform any image processing or manipulation here, if needed
    # For example, you can resize the frames to fit the same window:
    frame_webcam_resized = cv2.resize(frame_webcam, (640, 480))

    # Display the frame
    cv2.imshow("Webcam Streaming", frame_webcam_resized)

    # Check if the specified interval has passed
    current_time = time.time()
    if current_time - start_time >= stream_interval:
        start_time = current_time  # Reset the start time

        # Create a VideoCapture object for the Pi Camera 
        picam = cv2.VideoCapture(2)

        # Capture a frame from the Pi Camera
        ret_pi, frame_pi = picam.read()

        # Release the Pi Camera capture object
        picam.release()

        # Save the captured frame to the Raspberry Pi home directory
        image_path = "/home/raspberrypi"  # Change the path as needed
        cv2.imwrite(f"{image_path}.{i}.jpg", frame_pi)
        i = i + 1

        print("Image captured and saved:", image_path)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close the window
webcam.release()
cv2.destroyAllWindows()
