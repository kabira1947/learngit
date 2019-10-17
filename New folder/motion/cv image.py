import cv2
import numpy as np

img= cv2.imread('2.png',0)

print(img)

cv2.imshow("image",img)

cv2.waitKey(5000)
cv2.destroyWindow("image")
cv2.resizeWindow('img',(50,50))