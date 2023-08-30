#robotState
# 서버에서 값을 받아오는 모듈
import pyrebase

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

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

def robotState():
    fb = db.child("robotState").get()
    state = str(fb.val())
    return state


def boxState():
    box = db.child("open").get()
    state = bool(box.val())
    return state
    
def brushState():
    brush_ = db.child("brush").get()
    state = bool(brush_.val())
    return state    
