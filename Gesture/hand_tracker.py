import cv2
import mediapipe as mp
import time


class handDetector() :

    def __init__(self, mode = False, max_hands = 2, detector_confidence = 0.5, track_confidence = 0.5):
        self.mode = mode
        self.max_hands = max_hands
        self.detector_confidence = detector_confidence
        self.track_confidence = track_confidence

        # object of hand detector 
        self.mpHands = mp.solutions.hands
        self. hands = self.mpHands.Hands(self.mode, self.max_hands, self.detector_confidence, self.track_confidence)

        # drawing of points
        self.mpDraw = mp.solutions.drawing_utils

    
    def findHands(self, frame, draw=True) :
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # use mediapipe classifier
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handlm in self.results.multi_hand_landmarks:
                if draw:
                    # pass in image to be displayed
                    self.mpDraw.draw_landmarks(frame, handlm, self.mpHands.HAND_CONNECTIONS)
        
        return frame


    def findposition(self, frame, handno=0, draw=True) :
        lmlist = []

        if  self.results.multi_hand_landmarks:
            myhand =  self.results.multi_hand_landmarks[handno]
            for id, lm in enumerate(myhand.landmark):

                # find integer position of the points
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm = [id, cx, cy]

                lmlist.append(lm)

                if id == 0:
                    cv2.circle(frame, (cx, cy), 15, (255, 255, 0), cv2.FILLED)
                else:
                    cv2.circle(frame, (cx, cy), 5, (245, 25, 15), cv2.FILLED) 

                
        return lmlist


def main():
    cap = cv2.VideoCapture(0)

    detector = handDetector()

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


if __name__ == '__main__':
    main()