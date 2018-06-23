'''
File - funcs.py
Project - Human Detection
OS Support - Ubuntu 16.04 LTS
Owner - Neuromancers, 2018
'''

import cv2

width = 1280
height = 720
darknessThreshold = 30 * (width * height)

# initiate video capture
def startCam():
	global  width, height
	# create Video Capture object
	# set FPS
	# set dimensions
	cap = cv2.VideoCapture(0)
	cap.set(cv2.CAP_PROP_FPS, 30)
	cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
	cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
	
	return cap

	
# stop camera safely on 'Esc' key
def stopCam(cap):
	# release camera object
	# destroy all running window frames
	cap.release()
	cv2.destroyAllWindows()


# include dependencies to haar cascades
def haarCascades():
	haarCascadeMap = {}
	#source: https://github.com/opencv/opencv/tree/master/data/haarcascades
	haarCascadeMap['upperBody'] = cv2.CascadeClassifier('haarCascades\haarcascade_upperbody.xml')
	haarCascadeMap['lowerBody'] = cv2.CascadeClassifier('haarCascades\haarcascade_lowerbody.xml')
	haarCascadeMap['faceProfile'] = cv2.CascadeClassifier('haarCascades\haarcascade_profileface.xml')
	haarCascadeMap['fullBody'] = cv2.CascadeClassifier('haarCascades\haarcascade_fullbody.xml')
	return haarCascadeMap
	

# enhance image using contrast and brightness
def enhance(frame, contrast, brightness):
	# g(i,j) = c * f(i,j) + b for contrast and brightness
	frame[:] = contrast * frame[:] + brightness
	return frame
	

# checks if video capture occurs in dark
def isDark(frame):
	global  darknessThreshold, width, height
	# calculate average of pixels of frame
	# return true for darkness if the avergae is below threshold
	frameAvg= cv2.sumElems(frame)
	if (frameAvg[0] < darknessThreshold and frameAvg[1] < darknessThreshold and frameAvg[2] < darknessThreshold):
		return True 
	else:
		return False
	
