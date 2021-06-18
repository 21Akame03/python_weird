import time
import cv2
import subprocess as sp
import hand_tracker as htm


# ############
Wcam, Hcam = 640, 480
# ############

#  Hand tracking software for volume control


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

        # get the hand size 

        
        # get the length and midpoint of 2 landmarks
        length, midpoint = detector.distanceBetween2Lm(frame, lmlist, 4, 8, False)


        # max about 200 and min about 15
        currvol = ((int(length) -50) / 140) * 100
        print(int(length))
        print(f"{int(currvol)}%")

        # display bar level
        if length <= 50:
            cv2.circle(frame, (midpoint[0], midpoint[1]), 15, (0, 0, 255), cv2.FILLED)
        elif length >= 190:
            cv2.circle(frame, (midpoint[0], midpoint[1]), 15, (0, 255, 0), cv2.FILLED)
        # display bar error quick fix thingy 
        if currvol >= 0 and currvol <= 100 :
            height = 400 - (currvol/100 * 250)
            print(f"height: {height} \n")
            cv2.rectangle(frame, (50, 400), (85, int(height)), (0, 255, 100), cv2.FILLED)            
            prevvol = currvol
        else:
            height = 400 - (prevvol/100 * 250)
            print(f"invalid height: {height} \n")
            cv2.rectangle(frame, (50, 400), (85, int(height)), (0, 0, 255), cv2.FILLED)
        
        # current volume 
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
