import cv2

img = cv2.imread('D:/GB/bootcamp/ExploringOpenCV/test.jpg')

#img = cv2.resize(img, (500, 500))

cv2.imshow('Result', img)

cv2.waitKey(0)