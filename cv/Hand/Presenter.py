import cv2
import hand_tracker as htm
import pyautogui
import time

#  Presenter is about helping the presenter to manipulate the screen without having to 
#  insteract with a device and can do so by using his hands and hand gestures


cap = cv2.VideoCapture(0)
cap.set(3, 1024)
cap.set(4, 768)

# detector module
detector = htm.handDetector(detector_confidence=0.3, track_confidence=0.3, max_hands=1)

print(pyautogui.size())
bbox_x, bbox_y = 100, 100

# fps
PreviousTime = 0
currentTime = 0

while True:
    success, frame = cap.read()

    # detect hands
    frame = detector.findHands(frame, draw=True)
    # frame is flipped by default so unflip it
    frame = cv2.flip(frame, 1)

    # find hand coordinates
    lmlist = detector.findposition(frame, draw=False)
    
    #draw a bounding box for mouse control
    cv2.rectangle(frame, (bbox_x, bbox_y), (500, 400), (0, 0, 255), 2)

    # detect fingers
    if len(lmlist) != 0:
        #mouse 
        #click: check distance between index and middle finger
        #bounding box for mouse control
        
        

        fingers = detector.find_fingers_up()

        #scroll up 
        #check index and pinky finger
        #scroll down
        #check thumb, index and pinky
        if fingers[0] and fingers[1] and not fingers[2] and not fingers[3] and fingers[4]:
             pyautogui.scroll(5)
             print("Scroll up")
        elif not fingers[0] and fingers[1] and not fingers[2] and not fingers[3] and fingers[4]:
             pyautogui.scroll(-5)
             print("Scroll down")


    # calculting the fps and displaying it
    currentTime = time.time()
    fps = 1/ (currentTime - PreviousTime)
    PreviousTime = currentTime
    cv2.putText(frame, f"FPS: {str(int(fps))}", (10, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 3)


    cv2.imshow("Presenter", frame)
    cv2.waitKey(1)
