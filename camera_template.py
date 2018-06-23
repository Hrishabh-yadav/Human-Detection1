'''
File - main.py
Project - Human Detection
OS Support - Ubuntu 16.04 LTS
Owner - Neuromancers, 2018
'''

# import packages
import funcs
import cv2

cam = funcs.startCam()

while(True):
	# read frame from feed
	_, frame = cam.read()
	
	# enchance feed if dark
	if funcs.isDark(frame):
		frame = funcs.enhance(frame, 4, 40)
	
	# display modified feed
	cv2.imshow("Feed", frame) 
	if cv2.waitKey(1) == 27: 
		break

funcs.stopCam(cap)
