'''

File - main.py
Project - Human Detection
OS Support - Ubuntu 16.04 LTS
Owner - Neuromancers, 2018

'''

# import packages
import funcs
import cv2

cap = funcs.startCam()

while(True):
	_, frame = cap.read()
	
	if funcs.isDark(frame):
		frame = funcs.enhance(frame, 4, 40)
	
	cv2.imshow("Feed", frame) 
	if cv2.waitKey(1) == 27: 
		break

funcs.stopCam(cap)
#just made some changes, try to ignore them
#XYZZZ
