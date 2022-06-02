#Import Libraries

import cv2
import numpy as np


video = cv2.VideoCapture('test_vid.mp4')


def detect(gray, frame):
    edges = cv2.Canny(gray, 50, 200)
    lines = cv2.HoughLinesP(edges, cv2.HOUGH_PROBABILISTIC, np.pi/180, 30, minLineLength=30, maxLineGap=5)

    for x in range(0, len(lines)):
        for x1,y1,x2,y2 in lines[x]:
            #cv2.line(inputImage,(x1,y1),(x2,y2),(0,128,0),2, cv2.LINE_AA)
            pts = np.array([[x1, y1 ], [x2 , y2]], np.int32)
            cv2.polylines(frame, [pts], True, (0,255,0))
            
    return frame

while True:
    _, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = detect(gray, frame)
    cv2.imshow('Video', canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()