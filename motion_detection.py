import cv2
import time


def detect_motion():
    global frame1, frame2


    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) > 100:
            return True            
    
    
    return False



cap = cv2.VideoCapture(0)
fps= int(cap.get(cv2.CAP_PROP_FPS))

_, frame1 = cap.read()
_, frame2 = cap.read()

while True:
    _, frame1 = cap.read()
    _, frame2 = cap.read()

    time.sleep(1/fps)
    
    res = detect_motion()
    print(res)
    cv2.imshow('live',frame1)
    cv2.waitKey(1)