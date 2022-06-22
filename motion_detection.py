import cv2
import time


def detect_motion():
    global frame1, frame2, main_frame
    res = False
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)

        if cv2.contourArea(contour) <10:
            res = True
            print(x,y,w,h)
            # cv2.rectangle(main_frame,(x,y),(w,h),(255,0,0),2)
            
    
    frame1 = frame2
    _, frame2 = cap.read()

    return res, frame1



cap = cv2.VideoCapture('Batting1.mp4')
fps= int(cap.get(cv2.CAP_PROP_FPS))

_, frame1 = cap.read()
_, frame2 = cap.read()
_, main_frame = cap.read()

while True:
    _, frame1 = cap.read()
    _, frame2 = cap.read()
    _, main_frame = cap.read()

    time.sleep(1/fps)
    
    _,framee = detect_motion()

    cv2.imshow('live',main_frame)
    cv2.waitKey(1)