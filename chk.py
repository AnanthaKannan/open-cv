import numpy as np
import cv2
import sys
import pytesseract
# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

faceCascade = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('data/haarcascades/haarcascade_lefteye_2splits.xml')
cap = cv2.VideoCapture(0)
# cap.set(3,640) # set Width
# cap.set(4,480) # set Height

while True:
    ret, img = cap.read()
    # img = cv2.flip(img, -1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(20, 20)
    )
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        roi_gray = cv2.medianBlur(roi_gray,1)
        converted_no = pytesseract.image_to_string(roi_gray, config='--psm 6')
        label = "LP" + converted_no
        cv2.putText(img, label, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,0,0), 2)

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

        cv2.imshow('plate', roi_gray)
        
    cv2.imshow('video',img)

    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break

cap.release()
cv2.destroyAllWindows()