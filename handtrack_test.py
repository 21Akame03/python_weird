import time
import mediapipe as mp
import cv2
import hand_tracker as htm

cap = cv2.VideoCapture(0)

detector = htm.handDetector()

# fps
PreviousTime = 0
currentTime = 0

while  True:
    success, frame = cap.read()

    frame = detector.findHands(frame)
    lmlist = detector.findposition(frame)
    # if len(lmlist) != 0:
    #     print(lmlist[4])

    # calculting the fps and displaying it
    currentTime = time.time()
    fps = 1/ (currentTime - PreviousTime)
    PreviousTime = currentTime

    cv2.putText(frame, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)

    cv2.imshow("Image", frame)
    cv2.waitKey(1)