# 2023ESWContest_free_1079 : DEFAULT

<div align="left">
<a href="https://www.youtube.com/watch?v=rZodmwJkPVo"><img src="https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white"/></a>
</div>


<div align="center"><img src="https://github.com/yooon27/2023ESWContest_free_1079/assets/124117305/67385786-246f-4564-96f0-2f58e80b038e" width="500px;" alt="development project" /></div>


## 작품명 : 뭉mung

- 도로 환경 개선에 도움이 되도록 개발한 뭉mung은 자율주행로봇으로, 자체적으로 도로 차선 외의 쓰레기를 청소를 하며, 하수구 내의 쓰레기를 판단하여 하수구 막힘을 방지 및 주변 환경미화원에게 알리는 기능을 제공한다.

<br>

## HW 구성 

<div align = "center"><img src = "https://github.com/yooon27/2023ESWContest_free_1079/assets/124117305/bbea5959-a1e0-4483-9ac0-15addf8ce607" width = "700px;" alt="HW" /></div>

<br>

## 작품 종합 기능

- <a href="https://github.com/yooon27/2023ESWContest_free_1079/tree/main/2023ESWContest_free_1079/Project/Application">어플리케이션</a>
- <a href="https://github.com/yooon27/2023ESWContest_free_1079/tree/main/2023ESWContest_free_1079/Project/RaspberryPi_autonomous">차량 가장자리 자율주행 + 하수구 탐색 및 사진 촬영</a>
- <a href="https://github.com/yooon27/2023ESWContest_free_1079/tree/main/2023ESWContest_free_1079/Project/RaspberryPi_detect">담배꽁초 청소 기능</a>


<br>

## 개발결과물의 우수성
대부분의 도로에는 환경미화원분들께서 청소를 하신다. 차도의 경우에는 청소차량이 지나가면서 청소하지만 최하위차선 바깥 부분은 청소가 되지 않고, 교통체증을 일으킬 수 있다. 또한 비나 눈이 오는 기상 상황에서 모여진 쓰레기들은 하수구를 막아 사고를 발생시킨다. 이런 상황을 고려해 소형으로 바깥 차선을 인식하여 갓길 주행으로 교통방해를 하지않고, 자율주행을 통해 청소를 하며 하수구의 실시간 막힘도까지 파악하여 알릴 수 있는 로봇을 만들었다. 

차선의 바깥 부분에서 쓰레기를 인식하여 청소 하고, 하수구를 지날 시 내부 환경을 파악하여 청소가 필요하다고 판단이 될 시 사진을 찍어서 사용자가 확인할 수 있다. 현재 로봇의 상태와 주운 쓰레기를 확인할 수 있는 어플리케이션까지 제공을 한다. 어플리케이션으로 환경미화원이 이용하여 관리가 필요한 하수구를 우선적으로 청소할 수 있다. 

기존 도로 가장자리 청소가 미흡하여 나타나는 문제점을, 현 작품의 기능을 통해 (침수의 1차 원인을)해결하며 (침수)사고를 예방할 수 있도록 도움을 준다. 모터를 항시 가동하는 것이 아닌 담배를 발견하였때만 선택적으로 가동하여 에너지적으로 효율적이다. 이러한 부분에서 개발 결과물에 우수성이 있다고 본다.

<br>

### 개발 작품의 확장성
협동로봇으로 환경미화원과 함께 차도를 효율적으로 청소한다. 중,대형차가 들어가기 어려운 가로수길, 번화가 등 침수 위험역을 타켓팅하여 하수구를 관리한다. 
이때 차도 뿐만 아니라 인도에서도 담배꽁초(혹은 다른 쓰레기)를 수거하여 깨끗한 도로 환경을 만든다. 마지막으로 앱의 기능을 일반인도 일부 사용하게 하여, 청소함이 차면 직접 비우면서 시민들도 참여하도록 만들 수 있다.


<br>

## 전체 흐름도
<div align="center"><img src="https://github.com/yooon27/2023ESWContest_free_1079/assets/124117305/b2c86025-4c71-4e59-9992-b82815366ec4" width="600px;" alt="FlowChat" /></div>



<br>

## 파일 관리
<br/><br/>

📦2023ESWContest_free_1079 <br/>
📂Project <br/>
 ┣ 📂Arduino_sensor <br/>
 ┃ ┣ 📜 drain_detect.ino <br/>
 ┣ 📂Application <br/>
 ┃ ┣ 📂 android  <br/>
 ┃ ┃ ┣ 📂 app  <br/>
 ┃ ┃ ┣ 📂 gradle  <br/>
 ┃ ┃ ┃ ┣ 📂 wrapper  <br/>
 ┃ ┣ 📂 assets  <br/>
 ┃ ┣ 📂 ios  <br/>
 ┃ ┣ 📂 lib  <br/>
 ┃ ┃ ┣ 📜 firebase_options.dart  <br/>
 ┃ ┃ ┣ 📜 ImagePage.dart  <br/>
 ┃ ┃ ┣ 📜 infoPage.dart  <br/>
 ┃ ┃ ┣ 📜 main.dart  <br/>
 ┃ ┣ 📂 linux  <br/>
 ┃ ┣ 📂 macos  <br/>
 ┃ ┣ 📂 test  <br/>
 ┃ ┣ 📂 web  <br/>
 ┃ ┃ ┣ 📂 icons  <br/>
 ┃ ┃ ┣ 📂 splash  <br/>
 ┃ ┣ 📂 windows  <br/>
 ┃ ┣ 📜 README.md  <br/>
 ┣ 📂RaspberryPi_Autonomous <br/>
 ┃ ┣ 📂 Autonomous <br/>
 ┃ ┃ ┣ 📜 carControl.py  <br/>
 ┃ ┃ ┣ 📜 drain.py  <br/>
 ┃ ┃ ┣ 📜 line.py  <br/>
 ┃ ┃ ┣ 📜 start_autonomous.py  <br/>
 ┃ ┃ ┣ 📜 tracking.py  <br/>
 ┃ ┣ 📂 App <br/>
 ┃ ┃ ┣ 📜 carControl.py  <br/>
 ┃ ┃ ┣ 📜 robotState.py  <br/>
 ┃ ┃ ┣ 📜 upload.py  <br/>
 ┃ ┃ ┣ 📜 start_app_autonomous.py  <br/>
 ┃ ┃ ┣ 📜 tracking.py  <br/>
 ┃ ┣ 📜 README.autonomous.md <br/>
 ┣ 📂RaspberryPi_detect <br/>
 ┃ ┣ 📂 Detect_clean_test <br/>
 ┃ ┣ 📂 object_detect_clean <br/>
 ┃ ┃ ┣ 📂 detect_yolov5 <br/>
 ┃ ┃ ┃ ┣ 📂 __pycache__ <br/>
 ┃ ┃ ┃ ┣ 📂 classify <br/>
 ┃ ┃ ┃ ┣ 📂 data <br/>
 ┃ ┃ ┃ ┣ 📂 models <br/>
 ┃ ┃ ┃ ┣ 📂 runs <br/>
 ┃ ┃ ┃ ┣ 📂 segment <br/>
 ┃ ┃ ┃ ┣ 📂 utils <br/>
 ┃ ┃ ┃ ┣ 📜 start_detect.py <br/>
 ┃ ┃ ┃ ┣ 📜 requirements.txt <br/>
 ┃ ┣ 📂 App <br/>
 ┃ ┃ ┣ 📜 brushServo.py  <br/>
 ┃ ┃ ┣ 📜 robotState.py  <br/>
 ┃ ┃ ┣ 📜 start_app_detect.py  <br/>
 ┃ ┣ 📜 README.detect.md <br/>
 ┣ 📂server <br/>
 ┃ ┣ 📂detect_yolo <br/>
 ┃ ┃ ┗ 📂dataset <br/>
 ┃ ┃ ┃ ┣ 📂appstore_app <br/>
 ┃ ┃ ┃ ┗ 📂appstore_service <br/>
 ┃ ┃ ┗ 📂result_video <br/>
 ┃ ┃ ┗ 📜best_ESC.pt <br/>
 ┃ ┃ ┗ 📜trained_yolov5_custom_data.ipynb <br/>
 ┣ 📂Picture <br/>
 ┗ 📜README.md

<br><br>

## 팀 명단 및 역할
| Profile | Role | Part | Tech Stack |
| ------- | ---- | ---- | ---------- |
| <div align="center"><a href="https://github.com/yooon27"><img src="https://github.com/yooon27/2023ESWContest_free_1079/assets/124117305/cf97c9f2-2891-4a58-b276-4117dc236332" width="70px;" alt=""/><br/><sub><b>신윤성</b><sub></a></div> | 팀장 | PM, SW, CV| RaspberryPi, Arduino, C, Python, YOLOv5|
| <div align="center"><a href=""><img src="https://github.com/yooon27/2023ESWContest_free_1079/assets/124117305/f366ff79-8cf1-4a01-91fa-e8d6f1c840bb" width="70px;" alt=""/><br/><sub><b>이종민</b><sub></a></div> | 팀원 | HW manager | RaspberryPi, designed & made |
| <div align="center"><a href=""><img src="https://github.com/yooon27/2023ESWContest_free_1079/assets/124117305/681ef831-baab-4465-a0e0-9947e5e34e86" width="70px;" alt=""/><br/><sub><b>안서현</b></sub></a></div> | 팀원 | HW manager | RaspberryPi, 3D modeling(123D Design), designed & made |
| <div align="center"><a href=""><img src="https://github.com/yooon27/2023ESWContest_free_1079/assets/124117305/9574e9ba-70b3-4658-a3cc-b98d443f67fd" width="70px;" alt=""/><br/><sub><b>김동진</b></sub></a></div> | 팀원 | SW, CV | RasberryPi, OpenCV, Python, C++ |
| <div align="center"><a href="https://github.com/gubam"><img src="https://github.com/yooon27/2023ESWContest_free_1079/assets/124117305/84618138-ad6c-4476-a1cf-be24be954dcf" width="70px;" alt=""/><br/><sub><b>조규범</b></sub></a></div> | 팀원 | UI, HW | Python, Firebase, Flutter, Android, Fusion360 |
