import numpy as np
import cv2

cap = cv2.VideoCapture(0)       # 카메라 모듈 사용.

while(1):
    ret, src = cap.read()     #   카메라 모듈 연속프레임 읽기
    hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)    # BGR을 HSV로 변환해줌


    dst = src.copy()  # Duplication of image
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)   # Transform into grayscale


    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)    # Apply adaptive thresholding to create a binary image


    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Find contours to Draw the original line


    mask = np.zeros_like(src) # Create a mask image filled with zeros


    cv2.drawContours(mask, contours, -1, (255, 255, 255), thickness=cv2.FILLED) # Draw the contours of the white lines on the mask


# Apply bitwise AND operation to mask the original image

# Display the result
    cv2.imshow("mask", mask)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()