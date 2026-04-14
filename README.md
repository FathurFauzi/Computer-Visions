# Computer-Visions
My Goal is to make a program that can calculate distance an object from camera.

we will gonna use cv2 and os more often here...

at First, i learned how computer read , then create a windows to show what they read 
```
img = cv2.imread('File Path')

cv2.imshow("Gambar",img)
```
(.imread) is used to read that file, while (.imshow) is used to show the image to a tab
. You can see my results in [Here]("")
###
then i tried to view the video/gif using python.. and the code is:
``` 
capture = cv2.VideoCapture("File Path")

while True:
    isTrue, frame = capture.read()

    if not isTrue:
        
        capture.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue 
    

    cv2.imshow('window_name',frame)

    if cv2.waitKey(20) & 0xFF==ord('d'):
        break

    
capture.release()
cv2.destroyAllWindows()
```
- Capture Variable: Used as a connection object or pointer to the video file or camera, not just a path string.

- Looping: Necessary because a video is a sequence of frames that must be processed one by one in real-time.

- isTrue: A boolean to verify if a frame was successfully captured. It acts as a safety gate before processing the frame data.

- capture.read(): This command retrieves the current frame and automatically increments the internal pointer to the next frame in the stack.

- if not isTrue: Means the video has reached the end or failed. We use capture.set(..., 0) to reset the pointer to the first frame for looping.

- cv2.imshow('window_name', frame): Displays the image. The first parameter is the Title of the Window, while frame is the actual pixel data.

- cv2.waitKey(20): Acts as the frame rate controller (delay) and listens for keyboard events.

- & 0xFF: A bitwise mask to isolate the last 8 bits of the input, ensuring compatibility with ASCII standards across different operating systems.

- ord('d'): Converts the character 'd' into its Decimal ASCII value (100) so the computer can compare it with the keyboard input.

- capture.release(): Closes the video file or deactivates the webcam to free system resources.

- cv2.destroyAllWindows(): Closes all active GUI windows to clear the screen and memory.
    
And now, to resize it, we will use this command:

```
def rescale(frame, scale = 0.3):
    width = int(frame.shape[1]*scale) #shape[1] will acces the width of the media
    height = int(frame.shape[0]*scale) #spale[0] means height of the media
    #int() is use to turn uneven number (decimal) to integers
    heightWidth = (width, height)

    return cv2.resize(frame, heightWidth, interpolation=cv2.INTER_AREA)

    
rescaledFrame = rescale(frame)

```
- def is a command to make a function
- int() is to turn the answere from float to integer
- frame.shape[1] value is the width of frame
- frame.shape[0] value is the height of frame
- * scale means we wil multiply it with our scale
- heightWidth is a variable that contain unchangable value
- .resize is a command to resize the media
- .INTER_AREA is to downsampling media properly

Therefore, the whole program is...:
```
import os
import cv2

#finding where our base code went
base_dir = os.path.dirname(os.path.abspath(__file__))

#path to access media
file_path = os.path.join(base_dir, 'figures', '4-dof simulation.gif')

capture = cv2.VideoCapture(file_path)

#this is a functions 
def rescale(frame, scale = 0.3):
    width = int(frame.shape[1]*scale) 
    height = int(frame.shape[0]*scale) 
    heightWidth = (width, height)

    return cv2.resize(frame, heightWidth, interpolation=cv2.INTER_AREA)

while True:
    isTrue, frame = capture.read()

    if not isTrue:
        capture.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue 
     
    rescaledFrame = rescale(frame)
    cv2.imshow('gif resized',rescaledFrame)

    if cv2.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv2.destroyAllWindows()

```
Now we know how to display media, now its time to [draw something](DrawFigure/drawDoc.md) to the Window