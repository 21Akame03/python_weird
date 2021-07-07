import cv2
import time
import FaceDetector as fd

cap = cv2.VideoCapture(0)

while True:
    status, frame = cap.read()
    
    detector = fd.faceDetector()
    frame = detector.findFaces(frame)

    

    cv2.imshow("Face test", frame)
    cv2.waitKey(1)

