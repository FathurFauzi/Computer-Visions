After we know how to display a media, we will learn how to draw something in the media..
- First we will add new library (numpy) and we will call it later as np.
- Then we will make a blank page (or you can draw on your images, and the code was still the same) the "blank" code is 
``` 
blank = np.zeros((500,500,3), dtype='uint8')
````
- np.zeros means to make an empty array/matrix (their value is zero/black)
- 500,500,3 means we will create 500 x 500 window with 3 color channel blue-green-red (bgr)
- uint8 means unsigned 8 bit integer. unsigned means there is no negative numbers, so 8 bit unsigned integers.. this was used for scaling bgr scale (0-255)

### to draw a line, we will use:

$$
cv.line(blank,\overset{\text{Starting Point}}{\overbrace{(0,0)}},\overset{\text{End Point}}{\overbrace{(250,67)}},(\overset{\text{color (bgr)}}{\overbrace{255,0,0}}),\overset{\text{thickness}}{\overbrace{5}})
$$
### to draw a rectangle, we will use:

$$
cv.rectangle(blank,\overset{\text{Starting Point}}{\overbrace{(21,67)}},\overset{\text{End Point}}{\overbrace{(300,300)}},(\overset{\text{color (bgr)}}{\overbrace{0,255,0}}),\overset{\text{thickness}}{\overbrace{3}})
$$

### To Draw Circle:

$$
cv.circle(blank,\overset{\text{Center Point}}{\overbrace{(250,250)}}, \overset{\text{radius}}{\overbrace{63}},(\overset{\text{color (bgr)}}{\overbrace{0,0,255}}), \overset{\text{thickness}}{\overbrace{-1}})
$$

- thickness -1 means it filled (solid)

### to draw an elipse, we will use:

$$
cv.ellipse(blank,\overset{\text{Center Point}}{\overbrace{(360,250)}}, \overset{\text{radius}}{\overbrace{(50,100)}},\overset{\text{Slope}}{\overbrace{67}},\overset{\text{starting angle}}{\overbrace{45}},\overset{\text{end angle}}{\overbrace{315}},(\overset{\text{color (bgr)}}{\overbrace{0,255,255}}), \overset{\text{thickness}}{\overbrace{-1}}))
$$


### to draw an Polygon, we will use:
$$
