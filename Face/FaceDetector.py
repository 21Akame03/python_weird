import cv2
import mediapipe as mp


class faceDetector() :
    def __init__(self, mode= False, max_num_face=2, detection_confidence=0.5, tracking_confidence=0.5) :
        self.mpDraw = mp.solutions.drawing_utils
        self.mpface = mp.solutions.face_mesh
        self.faces = self.mpface.FaceMesh(mode, max_num_face, detection_confidence, tracking_confidence)
        # drawing specifications of the face mesh 
        self.spec_drawing = self.mpDraw.DrawingSpec(thickness=1, circle_radius=0)



    def findFaces(self, frame, Draw=False) :
 
        # image converted to RGB since mediapipe can only process RGB images and not BGR images
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.faces.process(image)

        #draw the landmarks on the frame 
        if results.multi_face_landmarks :
            for face_landmarks in results.multi_face_landmarks :
                self.mpDraw.draw_landmarks(frame, face_landmarks, self.mpface.FACE_CONNECTIONS, self.spec_drawing, self.spec_drawing)

        return frame
    
       
def main() :
    cap = cv2.VideoCapture(0)

    while True:
        status, frame = cap.read()
        
        detector = faceDetector()
        frame = detector.findFaces(frame)
        

        cv2.imshow("Face mesh", frame) 
        cv2.waitKey(1)

if __name__ == '__main__':
    main()
