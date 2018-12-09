import cv2 as cv
import numpy as np
import os

def recognize(ret, frame):
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    colored_gray=cv.cvtColor(gray, cv.COLOR_GRAY2BGR)

    default_faces = default.detectMultiScale(gray, 1.3, 5)
    cascade_7_faces = cascade_7.detectMultiScale(gray, 1.3, 5)
    cascade_17_faces = cascade_17.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in default_faces:
        cv.rectangle(colored_gray, (x,y), (x+w, y+h), (0,0,255),2)

    for (x,y,w,h) in cascade_7_faces:
        cv.rectangle(colored_gray, (x,y), (x+w, y+h), (255,0,0),2)

    for (x,y,w,h) in cascade_17_faces:
        cv.rectangle(colored_gray, (x,y), (x+w, y+h), (0,255,0),2)


    resized = cv.resize(colored_gray, (800,600))
    cv.imshow('cap', resized)
    if cv.waitKey(1) & 0xFF == ord('p'):
        image_name= str(len(os.listdir('screenshots')))
        print('screenshot name:' + image_name)
        cv.imwrite('screenshots/' + image_name + '.jpg', resized)

default = cv.CascadeClassifier('/home/skach/dev/facedet/haarcascade_frontalface_default.xml')
cascade_7 = cv.CascadeClassifier('/home/skach/dev/facedet/cascade.xml')
cascade_17 = cv.CascadeClassifier('/home/skach/dev/facedet/cascade_17.xml')

cap = cv.VideoCapture(0)

while True:

    ret, frame = cap.read()
    recognize(ret, frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()


