'''

File - funcs.py
Project - Human Detection
OS Support - Ubuntu 16.04 LTS
Owner - Neuromancers, 2018

'''

import cv2

# initiate video capture
def startCam():
	# create Video Capture object
	# set FPS
	# set dimensions
	cap = cv2.VideoCapture(0)
	cap.set(cv2.CAP_PROP_FPS, 30)
	cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
	cap.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
	
	return cap

	
# stop camera safely on 'Esc' key
def stopCam(cap):
	cap.release()
	cv2.destroyAllWindows()


# include dependencies to haar cascades
def haarCascades():
	return 0
