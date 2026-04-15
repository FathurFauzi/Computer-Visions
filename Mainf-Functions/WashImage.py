import os
import cv2 as cv

base_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(base_dir,"..",'Read image and video', 'figures', 'cat.jpg')

img = cv.imread(file_path)
cv.imshow('Original',img)

#into a grayscale
gryscl = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gryscl)

#blur
blur = cv.GaussianBlur(gryscl, (3,3) ,cv.BORDER_DEFAULT)
cv.imshow("blurred", blur)

#use blur instead of img
blrcanny = cv.Canny(blur,125,175)
cv.imshow("blrred canny edge",blrcanny)

#dilate
dilate = cv.dilate(blrcanny,(3,3), iterations=5)
cv.imshow("dilated",dilate)

#erode
erode = cv.erode(dilate,(3,3),iterations=4)
cv.imshow("erode",erode)

#resize
resize = cv.resize(img,(500,500),interpolation=cv.INTER_LINEAR)
cv.imshow("resized",resize)

#crop
crop = resize[50:200,200:400]
cv.imshow("cropped",crop)

cv.waitKey(0)
