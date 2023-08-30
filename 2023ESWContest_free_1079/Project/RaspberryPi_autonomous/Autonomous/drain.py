import imp
import serial
import time
import RPi.GPIO as GPIO
import cv2
import upload
import line

def capture():
    count = 100
    distance_avg = 0
    distance_tot = 0
    i = 0
    ser = serial.Serial('/dev/ttyUSB0',115200,timeout=None)
    ser.flush()
    while True:
        i+=1
        if i ==1000:
            upload.robotLoc()
            i=0
        

        if ser.in_waiting>0:
            line = ser.readline().decode('utf=8').rstrip()
            arr = line.split()
            
            distance_center = int(arr[1])
            distance_1 = int(arr[2])
            distance_2 = int(arr[3])
            distance_tot = int(arr[4])
            
                
            if distance_tot > 15 and count > 100:
                count = 0
                print("Motor stop\n")
                line.drainStop()
                time.sleep(2)
                print("take picture\n")
                    
                # Create a VideoCapture object for the Pi Camera 
                picam = cv2.VideoCapture(2)

                # Capture a frame from the Pi Camera
                ret_pi, frame_pi = picam.read()

                # Release the Pi Camera capture object
                picam.release()
                    
                markerNumber = upload.markerNum()

                # Save the captured frame to the Raspberry Pi home directory
                image_path = "/home/raspberrypi/captureImage"  # Change the path as needed
                cv2.imwrite(f"{image_path}/{markerNumber}.jpg", frame_pi)
                
                    
                print("Motor go\n")
                line.drainStop()
                print(distance_tot)
                time.sleep(5) #escape drain
            
                    
                print("picture transmit\n")
                    
                upload.drainLoc()
                
            #Break the loop if 'q' key is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            count += 1
            print(distance_center, distance_1, distance_2, distance_tot)
    # Release the VideoCapture object and close the window
