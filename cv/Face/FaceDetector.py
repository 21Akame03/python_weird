import cv2
import mediapipe as mp



class FaceDetector() :
    def __init__(self, mode=False, max_face=2, detection_confidence=0.7, tracking_confidence=0.7):
        # mediapipe setup
        self.mpFace_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mpFace_mesh.FaceMesh(mode, max_face, detection_confidence, tracking_confidence)
        self.mpDraw = mp.solutions.drawing_utils
        self.drawSpec = self.mpDraw.DrawingSpec(thickness=1, circle_radius=1)


    def find_face_mesh(self, frame, draw=False) :
        # process image into RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # apply the model using the api
        result = self.face_mesh.process(image)
        
        if draw :
            # draw the points on the screen
            if result.multi_face_landmarks:
                for lm in result.multi_face_landmarks:
                    self.mpDraw.draw_landmarks(frame, lm, self.mpFace_mesh.FACE_CONNECTIONS, self.drawSpec, self.drawSpec)
        
        return frame

    
       

# test code
def main() :
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)
    
    # mediapipe detector
    detector = FaceDetector()
    
    run = True

    while run == True:
        success, frame = cap.read()
    
        # reassign the frame with the modified image
        frame = detector.find_face_mesh(frame)


        cv2.imshow("Face_mesh",cv2.flip(frame, 1))
        cv2.waitKey(1)


if __name__ == '__main__':
    main()
