import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("yashkey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattaindancerealtime-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "2122117":
        {
            "name": " Yash Phuke",
            "major": "computer engineering",
            "starting_year": 2021,
            "total_attendance": 6,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2023-1-1 00:54:34"
        },
    "2122105":
        {
            "name": "Kiran Mishra",
            "major": "computer engineering",
            "starting_year": 2021,
            "total_attendance": 6,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2023-1-1 00:54:34"
        },
    "2122118":
        {
            "name": "Yuvraj Pawar",
            "major": "computer engineering",
            "starting_year": 2021,
            "total_attendance": 6,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2023-1-1 00:54:34"
        },
}
for key, value in data.items():
    ref.child(key).set(value)
