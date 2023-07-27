import cv2
import dlib
import time
import os

def faceLandmarks(im):
    # Path for the detection model, you can download it from here: https://github.com/italojs/facial-landmarks-recognition/blob/master/shape_predictor_68_face_landmarks.dat
    PREDICTOR_PATH = r"/Users/rohitpoddar/Documents/Artificial Intelligence Projetcs/Bumble-face/shape_predictor_68_face_landmarks.dat"

    # Create object to detect the face
    faceDetector = dlib.get_frontal_face_detector()

    # Create object to detect the facial landmarks
    landmarkDetector = dlib.shape_predictor(PREDICTOR_PATH)

    # Detect faces
    faceRects = faceDetector(im, 0)

    # Initialize landmarksAll array
    landmarksAll = []

    # For each face detected in the image, this chunk of code creates a ROI around the face and pass it as an argument to the 
    # facial landmark detector and append the result to the array landmarks 
    for i in range(0, len(faceRects)):
        newRect = dlib.rectangle(int(faceRects[i].left()),
                            int(faceRects[i].top()),
                            int(faceRects[i].right()),
                            int(faceRects[i].bottom()))
        landmarks = landmarkDetector(im, newRect)
        landmarksAll.append(landmarks)

    return landmarksAll, faceRects

def renderFacialLandmarks(im, landmarks):
    # Convert landmarks into iteratable array
    points = []
    [points.append((p.x, p.y)) for p in landmarks.parts()]

    # Loop through array and draw a circle for each landmark
    for p in points:
        cv2.circle(im, (int(p[0]),int(p[1])), 2, (255,0,0),-1)

    # Return image with facial landmarks 
    return im

def detect_face_landmarks_webcam():
    # Load the detector and predictor models for facial landmarks
    PREDICTOR_PATH = r"/Users/rohitpoddar/Documents/Artificial Intelligence Projetcs/Bumble-face/shape_predictor_68_face_landmarks.dat"
    faceDetector = dlib.get_frontal_face_detector()
    landmarkDetector = dlib.shape_predictor(PREDICTOR_PATH)

    # Open the webcam
    cap = cv2.VideoCapture(0)
    



    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()

        if not ret:
            break

        # Detect faces in the frame
        faceRects = faceDetector(frame, 0)

        for i in range(len(faceRects)):
            newRect = dlib.rectangle(int(faceRects[i].left()),
                                     int(faceRects[i].top()),
                                     int(faceRects[i].right()),
                                     int(faceRects[i].bottom()))

            # Detect facial landmarks for each face
            landmarks = landmarkDetector(frame, newRect)

            # Calculate lips width
            lips_width = abs(landmarks.parts()[49].x - landmarks.parts()[55].x)

            # Calculate jaw width
            jaw_width = abs(landmarks.parts()[3].x - landmarks.parts()[15].x)

            # Calculate the ratio of lips and jaw widths
            ratio = lips_width / jaw_width

            # Evaluate ratio
            if ratio > 0.32:
                result = "Smiling"
                with open("smile_signal.txt", "w") as f:
                    f.write("Smiling")
            else:
                result = "Not Smiling"



            # Draw the result text on the frame
            cv2.putText(frame, result, (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

            # Draw facial landmarks on the frame (optional)
            points = []
            [points.append((p.x, p.y)) for p in landmarks.parts()]
            for p in points:
                cv2.circle(frame, (int(p[0]), int(p[1])), 2, (255, 0, 0), -1)

        # Show the frame with the result
        cv2.imshow("Smile Detection", frame)



        # Exit the loop when 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close the display window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_face_landmarks_webcam()
