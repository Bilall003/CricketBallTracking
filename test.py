import cv2
import numpy as np

def film_detection(imageFrame):
	x = 0
	y = 0
	w = 0
	h = 0

	hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV).copy()


	lower = np.array([26, 0, 20], np.uint8) 
	upper = np.array([179,255,255], np.uint8) 
	mask = cv2.inRange(hsvFrame, lower, upper) 

	kernal = np.ones((5, 5), "uint8") 
	
	mask = cv2.dilate(mask, kernal) 

	contours, _ = cv2.findContours(mask, 
										cv2.RETR_TREE, 
										cv2.CHAIN_APPROX_SIMPLE) 
	
	for _, contour in enumerate(contours):  
		if cv2.contourArea(contour)<100:
			return True

	return False

img = 'custom/3.jpg'
img = cv2.imread(img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray = cv2.GaussianBlur(gray,(25,25),0)
_ , mask = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

# img = film_detection(img)


cv2.imshow('op',mask)


cv2.waitKey(0)
# cap = cv2.VideoCapture('Batting1.mp4')

# while cap.isOpened():
# 	_,frame = cap.read()
# 	frame = film_detection(frame)
# 	cv2.imshow('Test',frame)
# 	cv2.waitKey(30)

# cv2.destroyAllWindows()