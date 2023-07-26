import 'dart:async';
import 'package:contest/infoPage.dart';
import 'package:flutter/material.dart';
import 'package:geolocator/geolocator.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';
import 'package:permission_handler/permission_handler.dart';
import 'package:firebase_database/firebase_database.dart';
import 'firebase_options.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_storage/firebase_storage.dart';



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

  //marker list
  Set<Marker> markers = Set();

  //mapping controller
  GoogleMapController? _controller;


  //showModalBottomSheet, show marker infomation
  void _showMarkerDetails(BuildContext context, MarkerId markerId) async {
    Reference _ref = FirebaseStorage.instance.ref().child('/image/${markerId.value}');
    String _url = await _ref.getDownloadURL();
    showModalBottomSheet(
      context: context,
      builder: (BuildContext context) {
        return Container(
          height: 500,
          child: ListView(
            children: [
              //bar
              Center(
                child: Container(
                  height: 10,
                  margin: EdgeInsets.symmetric(horizontal: 30 ,vertical: 10),
                  decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(20),
                      border: Border.all(color: Colors.black12, width: 3),
                    color:Colors.cyan ,
                  ),

                ),
              ),
              Center(child: Text('Marker ID: ${markerId.value}')),
              GestureDetector(
                child:Image.network(_url),
                onTap: () {
                },
              )

            ],
          ),
        );
      },
    );
  }

  //clear marker list
  void clearFunc() {
    markers.clear();
  }
  //read server list and make a local list
  Future readData() async {
    //connect realtime database
    final marker = await ref.child("numberMarker").get();
    final gps = await ref.child("gps").get();

    var number = marker.value;
    var _gps= gps.value as List<dynamic>?;

    if (_gps != null) {
      gpsData.clear();
      //making a loacl list
    for(var data in _gps){
      double lati = data['lati'] as double;
      double long = data['long'] as double;
      gpsData.add({'lati': lati, 'long': long});
    }}
    setState(() {
      clearFunc();
      for (int i = 0; i < int.parse(number.toString()); i++) {
        markers.add(
          Marker(
            position: LatLng(gpsData[i]["lati"]!.toDouble(), gpsData[i]["long"]!.toDouble()),
            markerId: MarkerId(i.toString()),
            //onTap marker
            onTap: () {
              _showMarkerDetails(context, MarkerId(i.toString()));
              print(i);
            },
          ),
        );
      }
    });

  }
  // get current location func + moving camera
   getCurrentLocation() async{
    Position position = await Geolocator.getCurrentPosition(
      desiredAccuracy: LocationAccuracy.high,
    );
    LatLng currentLatLng = LatLng(position.latitude,position.longitude);
    setState(() {
              _controller?.animateCamera(CameraUpdate.newLatLngZoom(currentLatLng,20));
    });
  }

  //initial camera position
  final CameraPosition _initialPosition = CameraPosition(
      target: LatLng(36.2967660, 126.8352470),
      zoom: 20,

  );

  //initState
  @override
  void initState() {
    super.initState();
    requestLocationPermission();
    getCurrentLocation();
    //ref listen
    ref.onValue.listen((event) {
      readData();
    });
  }


  //application start
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home:Scaffold(
        appBar: AppBar(
          title: const Text('mapping'),
          leading: IconButton(
              onPressed: (){
                setState(() {
                  getCurrentLocation();
                });
              },
              icon:const Icon(Icons.autorenew)),
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