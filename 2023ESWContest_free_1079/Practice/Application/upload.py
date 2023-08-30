import pyrebase
import realtimeLocation
import time

firebaseConfig = {
    'apiKey': "AIzaSyCd5azxskAXXXXX",
    'authDomain': "image-5XXX",
    'databaseURL': "https://ixxxxxxxxxxxx",
    'projectId': "imxxxxx",
    'storageBucket': "imagxxxxxxxxxxx",
    'messagingSenderId': "12176xxxxx",
    'appId': "1:12176963xxxxxxxxxxx",
    'measurementId': "xxxxxxxxx"
    }
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
st = firebase.storage()

def drainLoc(image_path):
    latitude,longitude =realtimeLocation.location()
    number = db.child("numberMarker").get()
    snum = str(number.val())
    st.child("image").child(snum).put(image_path)
    db.child("gps").child(snum).child("lati" ).set(latitude)
    db.child("gps").child(snum).child("long").set(longitude)
    plusNumber = number.val()+1
    db.child("numberMarker").set(plusNumber)
    print("complete upload module")

def robotLoc():
    latitude,longitude =realtimeLocation.location()
    db.child("gps").child(0).child("lati" ).set(latitude)
    db.child("gps").child(0).child("long").set(longitude)
