import cv2
import random
Height=int(input("Enter the height: "))
Width=int(input("Enter the width: "))

color=int(input("Choose a number, where 0=Black white \n1=Color: "))

img=cv2.imread("2092.jpg",color)
colors=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


a= img.shape[0]/Height
b= img.shape[1]/Width

rs=cv2.resize(img,(int(img.shape[0]/a),int(img.shape[1]/b)))
cv2.imwrite("resize1.jpg",rs)
