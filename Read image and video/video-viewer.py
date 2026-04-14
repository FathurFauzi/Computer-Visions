import os
import cv2

#this is for finding where our base code went
base_dir = os.path.dirname(os.path.abspath(__file__))

#this is used to be a path to access picture
file_path = os.path.join(base_dir, 'figures', '4-dof simulation.gif')

capture = cv2.VideoCapture(file_path)

#this is a functions 
def rescale(frame, scale = 0.3):
    width = int(frame.shape[1]*scale) #shape[1] will acces the width of the media
    height = int(frame.shape[0]*scale) #spale[0] means height of the media
    #int() is use to turn uneven number (decimal) to integers
    heightWidth = (width, height)

    return cv2.resize(frame, heightWidth, interpolation=cv2.INTER_AREA)

while True:
    isTrue, frame = capture.read()

    if not isTrue:
        capture.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue 
     
    rescaledFrame = rescale(frame)
    cv2.imshow('gif',frame)
    cv2.imshow('gif resized',rescaledFrame)

    #this branch will executed when user press 'd' button
    if cv2.waitKey(20) & 0xFF==ord('d'):
        break

#command to close all windows
capture.release()
cv2.destroyAllWindows()
