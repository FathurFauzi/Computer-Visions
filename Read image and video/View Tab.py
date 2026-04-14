import os
import cv2

#this is for finding where our base code went
base_dir = os.path.dirname(os.path.abspath(__file__))

#this is used to be a path to access picture
file_path = os.path.join(base_dir, 'figures', 'triple t.jpg')

# Just some cool stuff
print("Mencoba membaca dari:", file_path)

def rescale(frame, scale = 0.3):
    width = int(frame.shape[1]*scale) #shape[1] will acces the width of the media
    height = int(frame.shape[0]*scale) #spale[0] means height of the media
    #int() is use to turn uneven number (decimal) to integers
    heightWidth = (width, height)

    return cv2.resize(frame, heightWidth, interpolation=cv2.INTER_AREA)

#this makes program acces the image that we trace before
img = cv2.imread(file_path)
rescaledImg = rescale(img)

if img is None:
    print("Gagal: Gambar tidak dapat dimuat.")
else:
    print("Berhasil: Gambar dimuat!")
    cv2.imshow("Gambar",img)#this is to show the image to a tab
    cv2.imshow("Gambar mini",rescaledImg)
    print("Tekan tombol apa saja pada keyboard di jendela gambar untuk menutup.")
    cv2.waitKey(0)#to do nothing before we clicked something
    # this used to close the windows
    cv2.destroyAllWindows()