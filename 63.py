import cv2 as cv
img1=cv.imread("img1.jpg")
size1=(400,400)
img2=cv.resize(img1,size1)
cv.imshow("temp",img2)

