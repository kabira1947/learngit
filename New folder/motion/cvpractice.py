import cv2

import numpy as np
#green color
lowerbound=np.array([33,80,40])
higherbound=np.array([102,255,255])

#Okay before doing that lets initialize our camera object
cap=cv2.VideoCapture(0)

#font for the  text we will be printing in the screen

#front= cv2.InitFont(cv2.CV_FONT_HERSHEY_SIMPLEX,2,0.5,0,3,1)

# reading the main frame of the camera
ret,img=cap.read()

# resize it to make it a small fixed size for faster processing
img=cv2.resize(img,(320,480))

#convert this image to hsv format

imghsv= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

#after this we will be creating the filter which will create the mask for green color
mask=cv2.inRange(imghsv,lowerbound,higherbound)

cv2.imshow('cap',img)
cv2.imshow('mask',mask)

cv2.waitKey(1000)

