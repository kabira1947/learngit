import numpy as np
import cv2

# Create a black image
img2 = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
img = cv2.line(img2,(0,0),(511,511),(255,0,0),5)

img1 = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img3 = cv2.polylines(img2,[pts],True,(0,255,255))