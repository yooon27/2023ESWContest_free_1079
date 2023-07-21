
import pyrebase

#composition infomation
firebaseConfig = {
    'apiKey': "AIzaxxxxxxx",
    'authDomain': "image-54axxxxxx",
    'databaseURL': "https://image-54a1e-dxxxxxx",
    'projectId': "image-xxx",
    'storageBucket': "",
    'messagingSenderId': "xxxxxxx",
    'appId': "1:12176xxxxx:web:994f0ad48371bxxxxx",
    'measurementId': "xxxxxxxx"
    }

# Firebase app initialize
firebase = pyrebase.initialize_app(firebaseConfig)

# Get a reference to Firebase Storage
storage = firebase.storage()

# Upload an image file
storage.child('image_path').put('image_path')

def uploadModule(latitude,longitude,image_path):
    import pyrebase

    firebaseConfig = {
        'apiKey': "AIzxxxxxxxxxxxxxxxxxxxx",
        'authDomain': "imxxxxxxxxxxx",
        'databaseURL': "httpsxxxxxxxxxxxxxxx",
        'projectId': "ixxxxxxxxxx",
        'storageBucket': "ixxxxxxxxxxm",
        'messagingSenderId': "1217xxxxxx",
        'appId': "1:1217696xxx",
        'measurementId': "GxxxxxxxxxxH"
        }
    #Connect Firebase
    firebase = pyrebase.initialize_app(firebaseConfig)
    db = firebase.database()
    st = firebase.storage()
    
    #Retrieve Data
    number = db.child("numberMarker").get()
    
    snum = str(number.val())
    
    #Upload GPS and Image File
    st.child("image").child("image_name"+snum).put(image_path)
    db.child("gps").child(snum+ "lati" ).set(latitude)
    db.child("gps").child(snum+ "long").set(longitude)
    
    #Upload plusNumber
    plusNumber = number.val()+1
    db.child("numberMarker").set(plusNumber)

    print("complete upload module")

