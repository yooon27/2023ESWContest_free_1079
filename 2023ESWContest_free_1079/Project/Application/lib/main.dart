import 'dart:typed_data';
import 'package:flutter/services.dart';
import 'firebase_options.dart';
import 'package:flutter/services.dart' show rootBundle;
import 'dart:async';
import 'package:flutter/material.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';
import 'package:permission_handler/permission_handler.dart';
import 'package:firebase_database/firebase_database.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_storage/firebase_storage.dart';
import 'package:contest/infoPage.dart';
import 'package:percent_indicator/percent_indicator.dart';
import 'dart:ui' as ui;
import 'ImagePage.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp(
    options: DefaultFirebaseOptions.currentPlatform,
  );

  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: const MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key}) : super(key: key);

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {

  //permission message
  Future<void> requestLocationPermission() async {
    final status = await Permission.location.request();
    if (status.isGranted) {
      print('Location permission granted.');
    } else {
      print('Location permission denied.');
    }
  }

  //firebase reference
  DatabaseReference ref = FirebaseDatabase.instance.ref();
  //server marker list
  List<Map<String, double>> gpsData =[];
  List<Map<String, double>> robotData =[];
  //marker list
  Set<Marker> markers = Set();
  Set<Marker> robotMarker = Set();
  //mapping controller
  GoogleMapController? _controller;
  BitmapDescriptor? robotMarkerIcon;
  //change the marker image
  void loadRobotMarkerIcon() async {
    final ByteData bytes = await rootBundle.load('assets/robot.png');
    robotMarkerIcon = BitmapDescriptor.fromBytes(bytes.buffer.asUint8List());
  }


  //showModalBottomSheet, show marker infomation
  void _showMarkerDetails(BuildContext context, MarkerId markerId) async {
    Reference _ref = FirebaseStorage.instance.ref().child('/image/${markerId.value}');
    String _url = await _ref.getDownloadURL();
    bool? isChecked = false;
    showModalBottomSheet(
      context: context,
      builder: (BuildContext context) {
        return Container(
          height: 500,
          margin: EdgeInsets.only(left: 10,right: 10,top: 10),
          child: Column(
            children: [
              Container(
                decoration: BoxDecoration(borderRadius: BorderRadius.circular(50),
                color: Colors.grey),
                height: 5,
                width: 40,
                margin: EdgeInsets.only(bottom: 20),
              ),
              GestureDetector(
                child:Image.network(_url),
              ),
              Padding(padding: EdgeInsets.symmetric(vertical: 10)),
              Container(
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.end,
                  children: [
                    Row(
                      children: [
                        Text("확대 :"),
                        IconButton(onPressed: (){
                          Navigator.push(context, MaterialPageRoute(builder: (context)=>ImagePage(url:_url)));
                          },
                            icon: Icon(Icons.zoom_in)),
                      ],
                    ),
                    Row(
                      children: [
                        Text("청소 상태 :"),
                        Checkbox(
                            value: isChecked,
                            onChanged: (value){setState(() {
                              isChecked = value;
                              print("object");
                            });}),
                      ],
                    ),
                  ],
                ),
              ),
              Padding(padding: EdgeInsets.symmetric(vertical: 5)),
              LinearPercentIndicator(
                barRadius: Radius.circular(5.0),
                padding: EdgeInsets.zero,
                percent: 0.5,
                lineHeight: 15,
                backgroundColor: Colors.grey,
                progressColor: Color(0xff9AC5F4),
              ),

            ],
          ),
        );
      },
    );
  }

  //clear marker list
  void clearFunc() {
    markers.clear();
    robotMarker.clear();
  }
  //read server list and make a local list
  Future readData() async {
    //connect realtime database
    final numberMarker = await ref.child("numberMarker").get();
    final gps = await ref.child("gps").get();
    final robotLocation = await ref.child("robot").get();
    final Robot = await ref.child("numberRobot").get();


    var number = numberMarker.value;
    var numberRobot = Robot.value;
    var _gps= gps.value as List<dynamic>?;
    var robot = robotLocation.value as List<dynamic>?;

    if (_gps != null && robot != null) {
      gpsData.clear();
      robotData.clear();
      //making a loacl list
    for(var data in _gps){
      double lati = data['lati'] as double;
      double long = data['long'] as double;
      gpsData.add({'lati': lati, 'long': long});
    }
    for(var data2 in robot){
      double lati = data2['lati'] as double;
      double long = data2['long'] as double;
      robotData.add({'lati': lati, 'long': long});
      }
    }

    setState(() {
      clearFunc();
      for (int i = 0; i < int.parse(number.toString()); i++) {
        //drain marker
        markers.add(
          Marker(
            position: LatLng(gpsData[i]["lati"]!.toDouble(), gpsData[i]["long"]!.toDouble()),
            markerId: MarkerId(i.toString()),
            icon:  BitmapDescriptor.defaultMarkerWithHue(BitmapDescriptor.hueCyan),
            //onTap marker
            onTap: () {
              _showMarkerDetails(context, MarkerId(i.toString()));
            },
          ),
        );
      }
      for (int i = 0; i < int.parse(numberRobot.toString()); i++) {
        //drain marker
        markers.add(
          Marker(
            position: LatLng(robotData[i]["lati"]!.toDouble(), robotData[i]["long"]!.toDouble()),
            markerId: MarkerId(i.toString()),
            icon: robotMarkerIcon ?? BitmapDescriptor.defaultMarkerWithHue(BitmapDescriptor.hueGreen),
            //onTap marker
            onTap: () {
              Navigator.push(context, MaterialPageRoute(builder: (context) => infoPage(),));
            },
          ),
        );
      }
    });

  }
  // get current location func + moving camera

  //initial camera position
  final CameraPosition _initialPosition = CameraPosition(
      target: LatLng(37.297567, 126.83670783333334),
      zoom: 20,

  );

  //initState
  @override
  void initState() {
    readData();
    super.initState();
    requestLocationPermission();
    //ref listen
    ref.onValue.listen((event) {
      readData();
      loadRobotMarkerIcon();
    });
  }


  //application start
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home:Scaffold(
        appBar: AppBar(
          backgroundColor: Color(0xff9AC5F4),
          title: const Text('Embedded Contest 2023'),
          actions: [
            IconButton(
              onPressed: (){
                setState(() {
                  Navigator.push(context, MaterialPageRoute(builder: (context) => infoPage(),));

                });
              },
              icon:const Icon(Icons.info_outline)),]
        ),



        body: StreamBuilder<Object>(
          stream: ref.onValue,
          builder: (context, snapshot) {
            return GoogleMap(
              onMapCreated: (GoogleMapController controller) {
                _controller = controller;
              },
              initialCameraPosition: _initialPosition,
              mapType: MapType.normal,
              myLocationButtonEnabled: true,
              myLocationEnabled: true,
              markers: markers,
            );
          }
        ),
      ),
    );
  }
}


