import cv2
import hand_tracker as htm


#  Presenter is about helping the presenter to manipulate the screen without having to 
#  insteract with a device and can do so by using his hands and hand gestures
#  
#  scroll up : index and middle finger up with the thumb closed
#  scroll down : index and middle finger down with thumb closed


cap = cv2.VideoCapture(0)
cap.set(3, 768)
cap.set(4, 480)

# detector module
detector = htm.handDetector(detector_confidence=0.7, track_confidence=0.7)


while True:
    success, frame = cap.read()
    
    # detect hands
    frame = detector.findHands(frame, draw=True)
    # find hand coordinates
    hands = detector.findposition(frame, draw=True)


    cv2.imshow("Presenter", cv2.flip(frame, 1))
    cv2.waitKey(1)
