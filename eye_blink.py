# import the necessary packages
from scipy.spatial import distance as dist
from imutils.video import VideoStream
from imutils import face_utils
import numpy as np
import imutils
import time
import dlib
import cv2
import os

def eye_aspect_ratio(eye):
    # compute the euclidean distances between the two sets of
    # vertical eye landmarks (x, y)-coordinates
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])

    # compute the euclidean distance between the horizontal
    # eye landmark (x, y)-coordinates
    C = dist.euclidean(eye[0], eye[3])

    # compute the eye aspect ratio
    ear = (A + B) / (2.0 * C)

    # return the eye aspect ratio
    return ear

# Constants for EAR threshold to indicate a blink
LEFT_EYE_AR_THRESH = 0.25
RIGHT_EYE_AR_THRESH = 0.225

# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
print("[INFO] loading facial landmark predictor...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# grab the indexes of the facial landmarks for the left and
# right eye, respectively
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

# start the video stream
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(1.0)




# loop over frames from the video stream
while True:
    # grab the frame from the threaded video stream, resize
    # it, and convert it to grayscale
    frame = vs.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect faces in the grayscale frame
    rects = detector(gray, 0)

    # variables to track if each eye was blinked
    left_eye_blinked = False
    right_eye_blinked = False

    # loop over the face detections
    for rect in rects:
        # determine the facial landmarks for the face region, then
        # convert the facial landmark (x, y)-coordinates to a NumPy
        # array
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        # extract the left and right eye coordinates and compute the eye aspect ratio for each eye
        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]

        # Compute the eye aspect ratio for each eye
        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)

        # compute the convex hull for each eye and visualize it
        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)
        cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

        # Check if each eye's aspect ratio is below the blink threshold
        if leftEAR < LEFT_EYE_AR_THRESH:
            left_eye_blinked = True

        if rightEAR < RIGHT_EYE_AR_THRESH:
            right_eye_blinked = True

    # Display the message "Right Eye Blinked" if only the right eye was blinked
    if right_eye_blinked and not left_eye_blinked:
        cv2.putText(frame, "Right Eye Blinked", (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        with open("eye_signal.txt", "w") as f:
                f.write("Right Eye Blinked")


    

    # show the frame
    cv2.imshow("Eye Blink Detection", frame)
    key = cv2.waitKey(1) & 0xFF

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
