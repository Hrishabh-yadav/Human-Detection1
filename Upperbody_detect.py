'''
File - Upperbody_detect.py
Project - Human Detection
Owner - Neuromancers, 2018
'''
import cv2
import funcs
c= funcs.startCam()
b= funcs.haarCascades()
while(True):
    _, frame = c.read() #read frame from feed
    if (funcs.isDark(frame)) :  #checking if it is dARK
        funcs.enhance(frame,4,40)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # convert to grayscale
    bodys = b.detectMultiScale(gray, 1.1, 2)   #DETECTING PRESENCE OF UPPER BODY
    for(x,y,w,h) in bodys:   
            img = cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
    cv2.imshow('img',frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break
funcs.stopCam(c)
