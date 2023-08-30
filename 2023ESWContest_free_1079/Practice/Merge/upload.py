import pynmea2
import pyrebase
import serial

firebaseConfig = {
    'apiKey': "AIzaSyCd5azxskAsJPxzUhYrJKbFe0nO99Kj4_E",
    'authDomain': "image-54a1e.firebaseapp.com",
    'databaseURL': "https://image-54a1e-default-rtdb.firebaseio.com",
    'projectId': "image-54a1e",
    'storageBucket': "image-54a1e.appspot.com",
    'messagingSenderId': "121769632696",
    'appId': "1:121769632696:web:994f0ad48371b86107254d",
    'measurementId': "G-DXRCVJGZ9H"
    }

#get a firebase database and storage reference
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
st = firebase.storage()

def location():
    while True:
        port="/dev/serial0"
        ser =serial.Serial(port,baudrate=9600,timeout=0.5)
        dataout = pynmea2.NMEAStreamReader()
        newdata =ser.readline()
        data =newdata.decode('latin-1')
        if data[0:6] == "$GPRMC":
            newloc=pynmea2.parse(data)
            lat=newloc.latitude
            lng=newloc.longitude
            break
    return lat,lng

def drainLoc():
    latitude,longitude =location()
    number = db.child("numberMarker").get()
    snum = str(number.val())
    st.child("image").child(snum).put(f"/home/raspberrypi/captureImage/{snum}.jpg")
    db.child("gps").child(snum).child("lati" ).set(latitude)
    db.child("gps").child(snum).child("long").set(longitude)
    plusNumber = number.val()+1
    db.child("numberMarker").set(plusNumber)
    print("upload complete")

def robotLoc():
    latitude,longitude = location()
    db.child("robot").child(0).child("lati" ).set(latitude)
    db.child("robot").child(0).child("long").set(longitude)

def markerNum():
    number = db.child("numberMarker").get()
    snum = str(number.val())
    return snum