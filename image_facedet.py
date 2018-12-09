import cv2 as cv
import numpy as np
import sys

def recognize(img, out_path):

    default_faces = default.detectMultiScale(img, 1.3, 5)
    cascade_7_faces = cascade_7.detectMultiScale(img, 1.3, 5)
    cascade_17_faces = cascade_17.detectMultiScale(img, 1.3, 5)

    for (x,y,w,h) in default_faces:
        cv.rectangle(img, (x,y), (x+w, y+h), (0,0,255),2)

    for (x,y,w,h) in cascade_7_faces:
        cv.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)

    for (x,y,w,h) in cascade_17_faces:
        cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0),2)

    cv.imwrite("results/" + out_path, img)

default = cv.CascadeClassifier('/home/skach/dev/facedet/haarcascade_frontalface_default.xml')
cascade_7 = cv.CascadeClassifier('/home/skach/dev/facedet/cascade.xml')
cascade_17 = cv.CascadeClassifier('/home/skach/dev/facedet/cascade_17.xml')

if (len(sys.argv) < 3):
    print("Usage: image_faceRec.py <image> <outfile>")
    sys.exit(2)
else:
    img_path = sys.argv[1]
    out_path = sys.argv[2]
    img = cv.imread(img_path, 1)
    recognize(img, out_path)
    sys.exit(0)



