import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.imshow('hsv',hsv)
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,252,252])
    mask = cv2.inRange(frame,lower_blue,upper_blue)
    cv2.imshow('mask',mask)
    res = cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('result',res)
    if cv2.waitKey(1) == ord('d'):
        break
cap.release()
cv2.destroyAllWindows()












