import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import  storage

cred = credentials.Certificate("yashkey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattaindancerealtime-default-rtdb.firebaseio.com/",
    'storageBucket': "faceattaindancerealtime.appspot.com"
})


dir_path = "C://Users//yashp//Documents//sem4//miniproject//face//FaceRec//FFace-Copy//Images"

# Loop through all files in the directory
for filename in os.listdir(dir_path):
    if filename.endswith(".jpg"):
        # Set the path to the JPG image
        img_path = os.path.join(dir_path, filename)

        # Read the JPG image
        img = cv2.imread(img_path)

        # Convert the image to PNG
        img_png = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_png = cv2.imencode('.png', img_png)[1].tobytes()

        # Set the path to the new PNG image
        new_img_path = os.path.splitext(img_path)[0] + ".png"

        # Write the new PNG image
        with open(new_img_path, "wb") as f:
            f.write(img_png)

        # Remove the original JPG image
        os.remove(img_path)

# Importing student images
folderPath = 'Images'
pathList = os.listdir(folderPath)
print(pathList)
imgList = []
studentIds = []
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    studentIds.append(os.path.splitext(path)[0])

    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)


    # print(path)
    # print(os.path.splitext(path)[0])
print(studentIds)


def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList


print("Encoding Started ...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print("Encoding Complete")

file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File Saved")
