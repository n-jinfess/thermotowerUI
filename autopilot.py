import os
from cv2 import VideoCapture
import numpy as np
import cv2

threshold = 200
area_of_box = 700        # 3000 for img input
min_temp = 102           # in fahrenheit
font_scale_caution = 1   # 2 for img input
font_scale_temp = 0.7    # 1 for img input


def framecap(vid):
    ret, frame=vid.read()
    return frame
    
def prepareframe(frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

        return gray

def detect(img):

    haar_cascade=cv2.CascadeClassifier('D:/Projects/420/haareyes.xml') 

    #detect a face and return the rectangualar coordinates 
    eyes=haar_cascade.detectMultiScale(img, scaleFactor=1.1,minNeighbors=15)
  
    return eyes

def drawrect(frame,eyes):
    for (x,y,w,h) in eyes:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=3)
    return frame

def gettemp(gray,eyes):
    temperature=0
    for (x,y,w,h) in eyes:
        mean=np.average(gray[x:(x+w),y:(y+h)])
        temperature=round(mean/2.25)
    
    return temperature   

def puttext(frame,eyes,temperature):
    for (x,y,w,h) in eyes:
        color = (0, 255, 0) if temperature < min_temp else (0, 0, 255)
        cv2.putText(frame, "{} F".format(temperature), (x, y),cv2.FONT_HERSHEY_SIMPLEX, font_scale_temp, color, 2, cv2.LINE_AA)

    return frame


def main(vid):
    while (True):
        frame=framecap(vid)
        gray=prepareframe(frame)

        eyes=detect(gray)

        frame=drawrect(frame,eyes)

        temperature=gettemp(gray,eyes)

        frame=puttext(frame,eyes,temperature)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    vid.release()
    cv2.destroyAllWindows()

cv2.destroyAllWindows()


