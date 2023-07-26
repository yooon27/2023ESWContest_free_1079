#include <DFRobot_TFmini.h>

 // for TFmini plus LiDar 
SoftwareSerial mySerial(8, 7); // RX, TX (LiDar)

DFRobot_TFmini  TFmini;
uint16_t distance_center,strength;


int trig_1 = 2 , echo_1 =3; //ultrasonic_1 pin 
int trig_2 = 5, echo_2 = 6; //ultrasonic_2 pin 

long distance_1, duration_1; 
long distance_2, duration_2;
int count, distance_tot, distance_avg = 0; //ultrasonic mean value


void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);  //baudrate
  TFmini.begin(mySerial);
  pinMode(trig_1, OUTPUT);
  pinMode(echo_1, INPUT);
  pinMode(trig_2, OUTPUT);
  pinMode(echo_2, INPUT);
}

void loop() {
  if(TFmini.measure()){
    distance_center = TFmini.getDistance();       //Get distance data
  }
  

  delay(1);
  // put your main code here, to run repeatedly:
  digitalWrite(trig_1, HIGH); //digital HIGH, LOW output setting
  delay(1);
  digitalWrite(trig_1, LOW);
  duration_1 = pulseIn(echo_1, HIGH);
  distance_1=(duration_1*340/10000)/2;
  
  digitalWrite(trig_2, HIGH);
  delay(1);
  digitalWrite(trig_2, LOW);
  duration_2 = pulseIn(echo_2, HIGH);
  distance_2=(duration_2*340/10000)/2;
     
    //a
    if(count != 50){
      count += 1;
      distance_tot += (distance_center * 0.5);
      distance_tot += (distance_1 * 0.25);
      distance_tot += (distance_2 * 0.25);
    }

  else{
    distance_avg = distance_tot/50;
      if(distance_avg > 15 & distance_avg <30){
        Serial.println("Motor stop and take a picture"); //모터 멈추고 카메라로 사진 찍기
        Serial.print("Motor go"); //하수구 탈출 명령
        Serial.print("     ");
        Serial.print(distance_avg);
        delay(5000); //하수구 탈출 시간
    }
      distance_tot = 0;
      count = 0;
    }
Serial.print(count);
Serial.print("      ");
Serial.print("Distance_center = ");
Serial.print(distance_center);
Serial.print("cm        distance_1= ");
Serial.print(distance_1);
Serial.print("cm       distance_2= ");
Serial.print(distance_2);
Serial.print("cm       average= ");
Serial.println(distance_tot/count);


delay(50);  
}
