# 제 21회 임베디드 소프트웨어 경진대회 자유공모부문
<div align="left">
<a href="https://www.youtube.com/watch?v=rZodmwJkPVo"><img src="https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white"/></a>
</div>


<!-- ## 개발 요약 -->
<div align="center"><img src="https://github.com/yooon27/2023ESWContest_free_1079/assets/124117305/67385786-246f-4564-96f0-2f58e80b038e" width="500px;" alt="development project" /></div>


### 작품명 : ERICOS(Environmental Responsive Intelligent Cleaning and Observation System Bot)

- 도로 환경 개선에 도움이 되도록 개발한 ERICOS는 자율주행로봇으로, 자체적으로 도로 차선 외의 쓰레기를 청소를 하며, 하수구 내의 쓰레기를 판단하여 하수구 막힘을 방지 및 주변 환경미화원에게 알리는 기능을 제공한다.

<br>



## 작품 종합 기능

- <a href="https://github.com/yooon27/2023ESWContest_free_1079/tree/main/2023ESWContest_free_1079/Project/Application">어플리케이션</a>
- <a href="">차량 가장자리 자율주행 + 하수구 탐색 및 사진 촬영</a>
- <a href="">담배꽁초 청소 기능</a>


<br>

## 개발결과물의 차별성
### 도로 가장자리 청소 및 정보 제공
대부분의 사람이 지나가는 도로에는 환경미화원분들꼐서 청소를 하신다. 차량도로의 경우에는 청소차량이 지나가면서 도로를 청소하지만 최하위차선 바깥 부분은 청소가 되지 않는다. 또한 비나 눈이 오는 기상 상황에서 모여진 쓰레기들은 하수구를 막아 사고를 발생시킨다. 우리는 이런 상황을 고려해 바깥 차선을 인식하여 자율주행을 통해 청소를 하며 하수구의 실시간 막힘도까지 파악하여 알릴 수 있는 로봇을 만들었다. 차선의 바깥 부분에서 쓰레기를 인식하여 청소 하고, 하수구를 지날 시 내부 환경을 파악하여 청소가 필요하다고 판단이 될 시 사진을 찍어서 사용자가 확인할 수 있으며, 현재 로봇의 상태와 주운 쓰레기를 확인할 수 있는 어플리케이션까지 제공을 한다. 기존에 도로의 가장자리 청소가 미흡하여 나타나는 문제점을, 현 작품의 기능을 통해서 해결하고 더 나아가 사고를 예방할 수 있도록 정보 제공하는 부분에서 개발 결과물에 차별성이 있다고 본다.
### 확장성
기존 도로 청소로봇은 매우 큰 상태로 도로 교통에 혼잡을 야기할 수 있었다. 그러나 우리가 개발한 작품은 어플리케이션을 통해서 현재 환경미화에 도움을 줄 수 있는 기능을 갖고 있다. 또한 하수구 막힘 사고를 예방하는 상태 제공함으로써 단순한 청소로봇 개념에서 벗어나 상황에 맞게 대응할 수 있는 로봇으로 활용방안 및 사용 가능성이 높다.


<br>

## 개발결과물의 시장성 및 활용성
### 


<br>

## 파일 관리
<br/>
'''
📦2023ESWContest_free_1079 <br/>
📂Project <br/>
 ┣ 📂Arduino <br/>
 ┃ ┣ 📜 drain_detect.ino <br/>
 ┣ 📂Application <br/>
 ┃ ┣ 📂 android  <br/>
 ┃ ┃ ┣ 📂 app  <br/>
 ┃ ┃ ┃ ┣ 📂 src  <br/>
 ┃ ┃ ┃ ┣ 📜 google-services.json  <br/>
 ┃ ┃ ┣ 📂 gradle  <br/>
 ┃ ┃ ┃ ┣ 📂 wrapper  <br/>
 ┃ ┣ 📂 assets  <br/>
 ┃ ┣ 📂 ios  <br/>
 ┃ ┃ ┣ 📂 Flutter  <br/>
 ┃ ┃ ┣ 📂 Runner  <br/>
 ┃ ┃ ┣ 📂 Runner.xcodeproj  <br/>
 ┃ ┃ ┣ 📂 Runner.xcworkspace  <br/>
 ┃ ┃ ┣ 📜 firebase_app_id_file.json  <br/>
 ┃ ┣ 📂 lib  <br/>
 ┃ ┃ ┣ 📜 firebase_options.dart  <br/>
 ┃ ┃ ┣ 📜 ImagePage.dart  <br/>
 ┃ ┃ ┣ 📜 infoPage.dart  <br/>
 ┃ ┃ ┣ 📜 main.dart  <br/>
 ┃ ┣ 📂 linux  <br/>
 ┃ ┃ ┣ 📂 flutter  <br/>
 ┃ ┃ ┣ 📜 main.cc  <br/>
 ┃ ┃ ┣ 📜 my_application.cc  <br/>
 ┃ ┃ ┣ 📜 CMakeList.txt  <br/>
 ┃ ┣ 📂 macos  <br/>
 ┃ ┣ 📂 test  <br/>
 ┃ ┣ 📂 web  <br/>
 ┃ ┃ ┣ 📂 icons  <br/>
 ┃ ┃ ┣ 📂 splash  <br/>
 ┃ ┃ ┣  index.html  <br/>
 ┃ ┣ 📂 windows  <br/>
 ┃ ┣ 📜 analysis_options.yaml  <br/>
 ┃ ┣ 📜 pubspec.yaml  <br/>
 ┃ ┣ 📜 README.md  <br/>
 ┣ 📂RaspberryPi_detect <br/>
 ┃ ┣ 📜 dc_motor_test.py <br/>
 ┃ ┣ 📜 servo_motor_test.py <br/>
 ┣ 📂RaspberryPi_ <br/>
 ┣ 📂server <br/>
 ┃ ┣ 📂wallpad <br/>
 ┃ ┃ ┗ 📂appstore <br/>
 ┃ ┃ ┃ ┣ 📂appstore_app <br/>
 ┃ ┃ ┃ ┗ 📂appstore_service <br/>
 ┃ ┣ 📂detect_yolo <br/>
 ┃ ┃ ┗ 📂dataset <br/>
 ┃ ┃ ┃ ┣ 📂appstore_app <br/>
 ┃ ┃ ┃ ┗ 📂appstore_service <br/>
 ┃ ┃ ┗ 📂result_video <br/>
 ┃ ┃ ┗ 📜best_ESC.pt <br/>
 ┃ ┃ ┗ 📜trained_yolov5_custom_data.ipynb <br/>
 ┗ 📜README.md
 '''
<br><br>

## 팀 명단
| Profile | Role | Part | Tech Stack |
| ------- | ---- | ---- | ---------- |
| <div align="center"><a href="https://github.com/yooon27"><img src="https://github.com/yooon27/2023ESWContest_free_1079/assets/124117305/cf97c9f2-2891-4a58-b276-4117dc236332" width="70px;" alt=""/><br/><sub><b>신윤성</b><sub></a></div> | 팀장 | PM, SW, CV| RaspberryPi, Arduino, C, Python, YOLOv5|
| <div align="center"><a href=""><img src="https://github.com/yooon27/2023ESWContest_free_1079/assets/124117305/197cb90c-4935-48a3-8db4-c8510ee70faa" width="70px;" alt=""/><br/><sub><b>이종민</b><sub></a></div> | 팀원 | HW manager | RaspberryPi, designed & made |
| <div align="center"><a href=""><img src="https://github.com/yooon27/2023ESWContest_free_1079/assets/124117305/681ef831-baab-4465-a0e0-9947e5e34e86" width="70px;" alt=""/><br/><sub><b>안서현</b></sub></a></div> | 팀원 | HW manager | RaspberryPi, 3D modeling(123D Design), designed & made |
| <div align="center"><a href=""><img src="https://github.com/yooon27/2023ESWContest_free_1079/assets/124117305/9574e9ba-70b3-4658-a3cc-b98d443f67fd" width="70px;" alt=""/><br/><sub><b>김동진</b></sub></a></div> | 팀원 | SW, CV | RasberryPi, OpenCV, Python, C++ |
| <div align="center"><a href="https://github.com/gubam"><img src="https://github.com/yooon27/2023ESWContest_free_1079/assets/124117305/84618138-ad6c-4476-a1cf-be24be954dcf" width="70px;" alt=""/><br/><sub><b>조규범</b></sub></a></div> | 팀원 | UI, HW | Python, Firebase, Flutter, Android, Fusion360 |
