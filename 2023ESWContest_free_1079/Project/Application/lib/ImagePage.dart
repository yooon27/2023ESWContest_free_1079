import 'package:flutter/material.dart';
import 'package:photo_view/photo_view.dart';

class ImagePage extends StatelessWidget {
   ImagePage({Key? key,this.url}) : super(key: key);

  var url;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Image Detail"),
        backgroundColor: Color(0xff9AC5F4),
      ),
      body: Center(
        child: PhotoView(imageProvider: NetworkImage(url)),
      ),
    );
  }
}
