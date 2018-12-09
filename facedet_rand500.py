import cv2 as cv
import numpy as np
import sys
import os

def recognize(img_path):

    img = cv.imread('rand500/' + img_path, 1)

    default_faces = default.detectMultiScale(img, 1.3, 5)
    cascade_10_faces = cascade_10.detectMultiScale(img, 1.3, 5)
    cascade_17_faces = cascade_17.detectMultiScale(img, 1.3, 5)

    for (x,y,w,h) in default_faces:
        cv.rectangle(img, (x,y), (x+w, y+h), (0,0,255),2)

    for (x,y,w,h) in cascade_10_faces:
        cv.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)

    for (x,y,w,h) in cascade_17_faces:
        cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0),2)

    line = img_path + ';' + str(len(default_faces)) + ';' + str(len(cascade_10_faces)) + ';' + str(len(cascade_17_faces)) + '\n'
    with open('rand500results.csv', 'a') as f:
        f.write(line)

    cv.imwrite("rand500result/" + img_path, img)

default = cv.CascadeClassifier('/home/skach/dev/facedet/haarcascade_frontalface_default.xml')
cascade_10 = cv.CascadeClassifier('/home/skach/dev/facedet/cascade.xml')
cascade_17 = cv.CascadeClassifier('/home/skach/dev/facedet/cascade_17.xml')


for img in os.listdir('rand500'):
    print(img)
    recognize(img)

sys.exit(0)



