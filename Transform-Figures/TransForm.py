import os
import cv2 as cv
import numpy as np

base_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(base_dir,"..",'Read image and video', 'figures', 'triple t.jpg')

#translations (shifting image)
img = cv.imread(file_path)
cv.imshow("Origin",img)

def Transl (var, x, y):
    Matrix = np.float32([[1,0,x],[0,1,y]])
    dimension = (var.shape[1],var.shape[0])
    return cv.warpAffine(var, Matrix,dimension)

translated = Transl(img,-67,50)
cv.imshow("Tertranslasi",translated)

#rotating 
def Rotate(vr, ang,rotPoint=None):
    (height,width)= img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    rotMatrix = cv.getRotationMatrix2D(rotPoint,ang,1.0)
    dimension = (width,height)

    return cv.warpAffine(vr,rotMatrix,dimension)

#rotating is often counterclockwise.
terRotate = Rotate(img, 67)
cv.imshow("rotate", terRotate)

#we could also rotate the rotated image
rotTwice = Rotate(terRotate,-90)
cv.imshow("rotet kuadrat",rotTwice)
#with this, the rotated rotated iage will show black in their edge because it was "cut" in the first rotate
#to solve it, just use original image and acumulate the rotation with the recent one
#67+(-90)= 67-90 = 23

#flipping 
flipped = cv.flip(img,-1)#0 flipped horizontally, 1 vertically, and -1 both
cv.imshow("terbalek",flipped)
 
cv.waitKey(0)