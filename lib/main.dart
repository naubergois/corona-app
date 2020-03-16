import 'package:flutter/material.dart';
import 'package:geolocator/geolocator.dart';
import 'dart:async';
import 'package:http/http.dart' as http;

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Corona Monitor App',
      theme: ThemeData(
     
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(title: 'Corona App Monitor'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.title}) : super(key: key);


  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;


  @protected
  @mustCallSuper
  void initState()  {

    //const oneSec = const Duration(minutes:1);
    const oneSec = const Duration(seconds:1);
    new Timer.periodic(oneSec, (Timer t) => get_position());

    
  }

  void get_position() async {

    Position position = await Geolocator().getCurrentPosition(desiredAccuracy: LocationAccuracy.high);
    print(position);
    print('/position/'+
        position.latitude.toString()+'/'+position.longitude.toString());
    
        try {
          await http.get(new Uri.http("192.168.1.72:5003", '/position/'+
                position.latitude.toString()+'/'+position.longitude.toString()+'/id'));


        } on Exception catch (_) {
          print('never reached');
        }
  }

  void _incrementCounter() {
    setState(() {
  
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
 
    return Scaffold(
      appBar: AppBar(
      
        title: Text(widget.title),
      ),
      body: Center(
       
        child: Column(
          
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            
          ],
        ),
      ),
       // This trailing comma makes auto-formatting nicer for build methods.
    );
  }
}
