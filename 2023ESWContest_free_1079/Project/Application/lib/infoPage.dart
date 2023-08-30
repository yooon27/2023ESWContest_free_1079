import 'package:flutter/material.dart';
import 'package:firebase_database/firebase_database.dart';

class infoPage extends StatefulWidget {
  const infoPage({Key? key}) : super(key: key);

  @override
  State<infoPage> createState() => _infoPageState();
}

DatabaseReference ref = FirebaseDatabase.instance.ref();

var states;
var butts;
bool openChecked = false;
bool brushChecked = false;

Future openBox(checked) async{
  await ref.child("open").set (checked);
}

Future rollBrush(checked) async{
  await ref.child("brush").set (checked);
}

Future robotState(state) async{
  await ref.child("robotState").set(state);
}

Future getNumberButts() async{
  final numberButts = await ref.child("numberButts").get();
  butts  = numberButts.value;
}


class _infoPageState extends State<infoPage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
          backgroundColor: Color(0xff9AC5F4),
          title: Text("Robot Information"),
        actions: [
          IconButton(onPressed: (){
            setState(() {
              getNumberButts();
            });
          }, icon: Icon(Icons.autorenew)),
        ],
      
      ),
        body:ListView(
          padding: EdgeInsets.symmetric(horizontal: 30,vertical: 50),
          children: [
            Text("담은 꽁초 갯수 : ${butts}",style: TextStyle(fontSize: 20),),
            Padding(padding: EdgeInsets.symmetric(vertical: 20)),
            Row(
              mainAxisAlignment: MainAxisAlignment.start,
              children: [
                Text("상자 열기 : ",style: TextStyle(fontSize: 20),),
                Switch(
                    value: openChecked,
                    onChanged: (value){
                      setState(() {
                        openChecked = value;
                        openBox(openChecked);
                      });
                    },
                ),
                Text("브러쉬 : ",style: TextStyle(fontSize: 20),),
                Switch(
                  value: brushChecked,
                  onChanged: (value){
                    setState(() {
                      brushChecked = value;
                      rollBrush(brushChecked);
                      print(value);
                    });
                  },
                ),
              ],
            ),
            Padding(padding: EdgeInsets.symmetric(vertical: 50)),
            Container(
              decoration: BoxDecoration(
                  border: Border.all(color: Color(0xff9AC5F4))),
              child: Column(children: [
                Center(child: Text("로봇 컨트롤",style: TextStyle(fontSize: 20),)),
                Padding(padding: EdgeInsets.symmetric(vertical: 20)),
                Container(
                  decoration: BoxDecoration(borderRadius:BorderRadius.circular(3.0),
                    color: Colors.black
                  ),
                  child: TextButton(
                      onPressed: (){
                        setState(() {
                          states = "stop";
                          robotState("stop");
                        });
                        },
                      child: Text("STOP",style: TextStyle(fontSize: 20,color: Colors.white),)),
                ),
                Padding(padding: EdgeInsets.symmetric(vertical: 20)),
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                  children: [
                  Container(
                    decoration: BoxDecoration(borderRadius:BorderRadius.circular(3.0),
                        color: Colors.black
                    ),
                    child: TextButton(
                        onPressed: (){
                          setState(() {
                            states = "left";
                            robotState("left");
                          });
                        },
                        child: Text("LEFT",style: TextStyle(fontSize: 20,color: Colors.white),)),
                  ),
                  Container(
                    decoration: BoxDecoration(borderRadius:BorderRadius.circular(3.0),
                        color: Colors.black
                    ),
                    child: TextButton(
                        onPressed: (){
                          setState(() {
                            states = "go";
                            robotState("go");
                          });
                        },
                        child: Text("GO",style: TextStyle(fontSize: 20,color: Colors.white),)),
                  ),
                  Container(
                    decoration: BoxDecoration(borderRadius:BorderRadius.circular(3.0),
                        color: Colors.black
                    ),
                    child: TextButton(
                        onPressed: (){
                          setState(() {
                            states = "right";
                            robotState("right");
                          });
                        },
                        child: Text("RIGHT",style: TextStyle(fontSize: 20,color: Colors.white),)),
                  ),

                ],),
                Padding(padding: EdgeInsets.symmetric(vertical: 20)),

                Container(
                  margin: EdgeInsetsDirectional.only(bottom: 20),
                  decoration: BoxDecoration(borderRadius:BorderRadius.circular(3.0),
                      color: Colors.black
                  ),
                  child: TextButton(
                      onPressed: (){
                        setState(() {
                          states = "tracking";
                          robotState("tracking");
                        });
                        },
                      child: Text("Line Tracking",style: TextStyle(fontSize: 20,color: Colors.white),)),
                ),
                Padding(padding: EdgeInsets.symmetric(vertical: 10)),

                Text("현재 상태 :  ${states}",style: TextStyle(fontSize: 20)),
                Padding(padding: EdgeInsets.symmetric(vertical: 10)),


              ],),
            ),

          ],
        ),

    );
  }
}
