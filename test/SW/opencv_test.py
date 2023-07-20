
print("test")
import numpy as np
import cv2
import os

# 데이터셋 저장 경로
dataset_path = "C:/Users/ehdwl/Desktop/Trainingset"
os.makedirs(dataset_path, exist_ok=True)

dataset_path_right = "C:/Users/ehdwl/Desktop/Trainingset/right"
os.makedirs(dataset_path_right, exist_ok=True)

dataset_path_left = "C:/Users/ehdwl/Desktop/Trainingset/left"
os.makedirs(dataset_path_left, exist_ok=True)

dataset_path_forward = "C:/Users/ehdwl/Desktop/Trainingset/forward"
os.makedirs(dataset_path_forward, exist_ok=True)

i = 0
j = 0
k = 0

cap = cv2.VideoCapture("C:/Users/ehdwl/Desktop/road_video2.mp4")  # 비디오 파일 경로

carstate = "stop"

while cap.isOpened():
    k = cv2.waitKey(10) & 0xFF  # 프레임 속도와 연결
    if k == 27:
        break
    elif k == 82:
        print("go forward")
        carstate = "go"
        # motor go
    elif k == 81:
        print("go left")
        carstate = "left"
        # motor go left
    elif k == 83:
        print("go right")
        carstate = "right"
        # motor go right
    elif k == 84:
        print("stop")
        carstate = "stop"
        # motor stop

    ret, src = cap.read()  # 비디오에서 연속 프레임 읽기
    if not ret:
        break

    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 그레이스케일로 변환

    blurred = cv2.GaussianBlur(gray, (5, 5), 0)  # 가우시안 블러링 적용

    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)  # 이진화 적용

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # 윤곽선 검출

    mask = np.zeros_like(src)  # 결과 영상 생성

    cv2.drawContours(mask, contours, -1, (255, 255, 255), thickness=cv2.FILLED)  # 윤곽선을 마스크에 그리기

    # 레이블 정보 저장
    cv2.imshow("original", src)
    cv2.imshow("Result", mask)

    if carstate == "right":
        cv2.imwrite(os.path.join(dataset_path_right, "right_%05d.jpg" % i), mask)
        i += 1
    elif carstate == "left":
        cv2.imwrite(os.path.join(dataset_path_left, "left_%05d.jpg" % j), mask)
        j += 1
    elif carstate == "go":
        cv2.imwrite(os.path.join(dataset_path_forward, "forward_%05d.jpg" % k), mask)
        k += 1

cap.release()
cv2.destroyAllWindows()
