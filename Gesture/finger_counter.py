import cv2
import hand_tracker as htm
import os
import time

###########################
WCam, HCam = 640, 480
##########################
## finger counting 

cap = cv2.VideoCapture(0)
cap.set(3, WCam)
cap.set(4, HCam)

while True:
    success, frame = cap.read()




    cv2.imshow("Finger counter", frame)
    cv2.waitKey(1)

