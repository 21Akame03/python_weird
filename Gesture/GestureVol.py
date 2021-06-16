import time
import cv2
import numpy as np
import math
import subprocess as sp
import hand_tracker as htm


# ############
Wcam, Hcam = 640, 480
# ############



cap = cv2.VideoCapture(0)
cap.set(3, Wcam)
cap.set(4, Hcam)
detector = htm.handDetector(detector_confidence = 0.7)

# fps
PreviousTime = 0
currentTime = 0

prevvol = 0
while  True:
    success, frame = cap.read()

    # get the frame and detect the hand 
    frame = detector.findHands(frame)
    lmlist = detector.findposition(frame, draw=False)
    if len(lmlist) != 0:

        x1, y1 = lmlist[4][1], lmlist[4][2]
        x2, y2 = lmlist[8][1], lmlist[8][2]

        #   midpoint
        ## NOTE: // is beacause we need an integer value and not a decimal value which we get from /
        midpoint = [((x1 + x2)//2), ((y1 + y2)//2)]

        cv2.circle(frame, (x1, y1), 15, (255, 255, 255), cv2.FILLED)
        cv2.circle(frame, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
        cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 255), 3)
        cv2.circle(frame, (midpoint[0], midpoint[1]), 15, (150, 150, 150), cv2.FILLED)

        #length of the liine between thumb and index
        # A^2 = B^2 + C^2  ## pythagoras theorem
        length = math.sqrt(((x2 - x1)**2 + (y2 - y1)**2))

        # max about 200 and min about 15
        currvol = ((int(length) -50) / 140) * 100
        print(int(length))
        print(f"{int(currvol)}%")

        # display bar level
        if length <= 50:
            cv2.circle(frame, (midpoint[0], midpoint[1]), 15, (0, 0, 255), cv2.FILLED)
        elif length >= 190:
            cv2.circle(frame, (midpoint[0], midpoint[1]), 15, (0, 255, 0), cv2.FILLED)
        
        if currvol >= 0 and currvol <= 100 :
            height = 400 - (currvol/100 * 250)
            print(f"height: {height} \n")
            cv2.rectangle(frame, (50, 400), (85, int(height)), (0, 255, 100), cv2.FILLED)
            
            prevvol = currvol
        else:
            height = 400 - (prevvol/100 * 250)
            print(f"invalid height: {height} \n")
            cv2.rectangle(frame, (50, 400), (85, int(height)), (0, 0, 255), cv2.FILLED)

        # Popen(['amixer', 'sset', 'Master', amount], stdout = PIPE)
        cv2.putText(frame, f"Vol: {int(prevvol)}%", (frame.shape[1] - 200, 50), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 3)


    # calculting the fps and displaying it
    currentTime = time.time()
    fps = 1/ (currentTime - PreviousTime)
    PreviousTime = currentTime

    cv2.putText(frame, f"FPS: {str(int(fps))}", (10, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 3)

    # show the window
    cv2.imshow("Image", frame)
    cv2.waitKey(1)