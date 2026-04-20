import os
import cv2 as cv


capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()

    if not isTrue:
        print("Gagal membaca kamera.")
        break 
 

    # 4. Ubah ke Grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)


    blur = cv.GaussianBlur(gray, (3,3) ,cv.BORDER_DEFAULT)
    cv.imshow("blurred", blur)

    #use blur instead of img
    blrcanny = cv.Canny(blur,125,175)
    cv.imshow("blrred canny edge",blrcanny)


    #this branch will executed when user press 'd' button
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

#command to close all windows
capture.release()
cv.destroyAllWindows()
