
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

print("complete")