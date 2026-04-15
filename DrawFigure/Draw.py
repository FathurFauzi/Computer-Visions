import os
import cv2 as cv
import numpy as np

base_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(base_dir,"..",'Read image and video', 'figures', 'triple t.jpg')

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('kosong',blank)

# Draw a  blue line from (0,0) to (250,67) with thickness of 5 px
cv.line(blank,(0,0),(250,67),(255,0,0),5)

#draw a green rectangle from (21,67) to (300,300) with thickness of 3 px 
cv.rectangle(blank,(21,67),(300,300),(0,255,0),3)

#draw a filled red circle Which the center is (250,250) with its radius is 63 px 
cv.circle(blank,(250,250), 63, (0,0,255), -1)

#draw a filled yelow elipse  Which the center is (360,250), with its radius is (50,100)px rotated 67 degree, start from 45 degree to 315 degree
cv.ellipse(blank,(360,250),(50,100),67,45,315,(0,255,255),-1)

#draw a white open polygon that connect [40,470],[67,350],[100,270],[300,70] with the thickness is 4px
pts = np.array([[40,470],[67,350],[100,270],[300,70]], np.int32)
pts = pts.reshape((-1,1,2))#this is just to rewrite it to type that desired by cv..
cv.polylines(blank,[pts],False,(255,255,255),4)#True will make last point connected to the first one

#draw a smooth pink filled polygon that connect [40,470],[67,350],[100,270],[300,70]
cv.fillPoly(blank,[pts],(255,0,255),cv.LINE_AA,0,(100,0))

#draw a white hello world text with hershey simplex font that start from (67,500) (its in bottom left in the text), scale 2  and 5px thickness
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(blank,'Hello World',(67,400), font, 2,(255,255,255),5,cv.LINE_4,False)#False means Normal text

#draw a white Its me, Riko text with HERSHEY COMPLEX SMALL font that start from (67,500) , scale 2  and 5px thickness
cv.putText(blank,'Its me, Riko',(67,400), cv.FONT_HERSHEY_COMPLEX_SMALL, 2,(255,255,255),5,cv.LINE_AA,True) #true means mirrorred horizontally text

cv.imshow('Penuh',blank)

img = cv.imread(file_path)

#you can also add draw in pictures
cv.fillPoly(img,[pts],(255,0,255),cv.LINE_AA,0,(100,0))
cv.ellipse(img,(130,50),(75,50),90,0,360,(0,0,255),2)
cv.putText(img,'Tung tung tung Sahur',(0,100), font, 0.5,(0,255,255),1,cv.LINE_4,False)#true means flipped text

#now show it
cv.imshow('Bergambar',img)

cv.waitKey(0)