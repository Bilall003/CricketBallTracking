import cv2
import numpy as np
from tkinter import filedialog

def film_detection(imageFrame):

	hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV).copy()


	lower = np.array([35, 0, 0], np.uint8) 
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

def main(file):
	cap = cv2.VideoCapture(file)

	_, frame1 = cap.read()
	_, frame2 = cap.read()


	while cap.isOpened():

		diff = cv2.absdiff(frame1, frame2)
		gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
		blur = cv2.GaussianBlur(gray, (5,5), 0)
		_, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
		contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


		for cont in contours:
			x, y, w, h = cv2.boundingRect(cont)

			if cv2.contourArea(cont)<120:
				
				if (x+w)-(y+h)<100:
					cut_img = frame2[y:y+h+20,x:x+h+20]
					# cv2.imwrite('ball/'+str(cnt)+'.jpg',cut_img)

					res = film_detection(cut_img)

					if res:
						frame1 = cv2.rectangle(frame1, (x, y), 
												(x + w, y + h), 
												(255 , 0, 0), 2)

		cv2.imshow("feed", frame1)
		frame1 = frame2
		ret, frame2 = cap.read()
		if cv2.waitKey(30) == 27:
			break

	cv2.destroyAllWindows()
	cap.release()


video = filedialog.askopenfilename()
if video == '':
	video = 0



main(video)