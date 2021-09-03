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

detector = htm.handDetector()
    
while True:
    success, frame = cap.read()
    
    frame = detector.findHands(frame)
    lmlist = detector.findposition(frame)
   
    if len(lmlist) != 0:
        print(detector.find_fingers_up())

    cv2.imshow("Finger counter", frame)
    cv2.waitKey(1)

