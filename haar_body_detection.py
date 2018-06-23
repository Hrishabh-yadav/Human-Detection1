'''
File - Upperbody_detect.py
Project - Human Detection
Owner - Neuromancers, 2018
'''

# import packages
import funcs
import cv2

# global properties
cam = funcs.startCam()

cascadeMap = funcs.haarCascades()
upperBody = cascadeMap['upperBody']
lowerBody = cascadeMap['lowerBody']
fullBody = cascadeMap['fullBody']

while(True):
	# read frame from feed
	_, frame = cam.read()
	
	# enchance feed if dark
	if funcs.isDark(frame):
		frame = funcs.enhance(frame, 4, 40)
	
	# convert to grayscale	
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	# detect features in feed using haar-cascades
	upperBodies = upperBody.detectMultiScale(gray, 1.1, 2)
	lowerBodies = lowerBody.detectMultiScale(gray, 1.1, 2)
	fullBodies = fullBody.detectMultiScale(gray, 1.1, 2)
	
	mod_frame = frame
	for (x,y,w,h) in upperBodies:
		mod_frame = cv2.rectangle(mod_frame, (x,y), (x+w, y+h), (255,0,0), 2)
	for (x,y,w,h) in upperBodies:
		mod_frame = cv2.rectangle(mod_frame, (x,y), (x+w, y+h), (0,255,0), 2)
	for (x,y,w,h) in upperBodies:
		mod_frame = cv2.rectangle(mod_frame, (x,y), (x+w, y+h), (0,0,255), 2)
	
	# display modified feed
	cv2.imshow("Feed", mod_frame) 
	if cv2.waitKey(1) == 27: 
		break

funcs.stopCam(cap)
