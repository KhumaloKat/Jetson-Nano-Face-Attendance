import cv2
import os 
from datetime import datetime
import FaceRecognitionModule as frm 
# import FirebaseModule as fbm 
import LedModule as lm 
from time import sleep

frameWidth = 640
frameHeight= 480

cap = cv2.VideoCapture(0)

encodeList, classNames = frm.findEncodings("ImagesAttendance")

# Led = lm.ledRBG(17,27,22)
# Led.color('off')


def markAttendance(name):
    # Led.color('green')

    with open('Attendance.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])


        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'{name},{dtString}\n')
            # fbm.postData(name,dtString)

while True:

    _, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    
    imgFaces, names = frm.recognizeFaces(img, encodeList, classNames, 0.2)

    for name in names:
        if name == "unknown":
            # Led.color('red')
            sleep(0.2)
        else:
            markAttendance(name)

    # Led.color('off')

    cv2.imshow("Image",imgFaces)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break