import cv2

face1 = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread("rhino.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face1.detectMultiScale(gray, 1.1,2)

for (x, y, w, h) in faces:
    cv2.rectangle(img,(x, y),(x+w,y+h),(255,10,10), 2)

cv2.imshow("image", img)

cv2.waitKey(0)