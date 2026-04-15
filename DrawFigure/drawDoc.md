After we know how to display a media, we will learn how to draw something in the media..
- First we will add new library (numpy) and we will call it later as np.
- Then we will make a blank page (or you can draw on your images, and the code was still the same) the "blank" code is 
``` 
blank = np.zeros((500,500,3), dtype='uint8')
````
- np.zeros means to make an empty array/matrix (their value is zero/black)
- 500,500,3 means we will create 500 x 500 window with 3 color channel blue-green-red (bgr)
- uint8 means unsigned 8 bit integer. unsigned means there is no negative numbers, so 8 bit unsigned integers.. this was used for scaling bgr scale (0-255)

## To draw a line, we will use:

$$
cv.line(blank,\overset{\text{Starting Point}}{\overbrace{(0,0)}},\overset{\text{End Point}}{\overbrace{(250,67)}},(\overset{\text{color (bgr)}}{\overbrace{255,0,0}}),\overset{\text{thickness}}{\overbrace{5}})
$$
## A rectangle :

$$
cv.rectangle(blank,\overset{\text{Starting Point}}{\overbrace{(21,67)}},\overset{\text{End Point}}{\overbrace{(300,300)}},(\overset{\text{color (bgr)}}{\overbrace{0,255,0}}),\overset{\text{thickness}}{\overbrace{3}})
$$

## Circle:

$$
cv.circle(blank,\overset{\text{Center Point}}{\overbrace{(250,250)}}, \overset{\text{radius}}{\overbrace{63}},(\overset{\text{color (bgr)}}{\overbrace{0,0,255}}), \overset{\text{thickness}}{\overbrace{-1}})
$$

- thickness -1 means it filled (solid)

## Elipse :

$$
cv.ellipse(blank,\overset{\text{Center Point}}{\overbrace{(360,250)}}, \overset{\text{radius}}{\overbrace{(50,100)}},\overset{\text{Slope}}{\overbrace{67}},\overset{\text{starting angle}}{\overbrace{45}},\overset{\text{end angle}}{\overbrace{315}},(\overset{\text{color (bgr)}}{\overbrace{0,255,255}}), \overset{\text{thickness}}{\overbrace{-1}}))
$$


## Polygon:

$$
 pts = np.array(\overset{\text{Coordinate Points}}{\overbrace{[[40,470],[67,350],[100,270],[300,70]], }}\overset{\text{Turn data type to integer 32 bit}}{\overbrace{np.int32}})
$$

- np.array was used to sort and turn all coordinate into array that can be operated like matrix
- coordinate points is like a list which have list/object of x and y coordinate
- np.int32 used to turn any decimal coordinate into a 32 bit integer, if the value is decimal, it will round it into an integer
###
Then reshape it into cv2's desirable datatype 

$$
pts = pts.reshape((-1,1,2))
$$ 
- (-1) is to make the program count the point by themselves 
- (1) is to make all of coordinate is one being because polylines want it.
- (2) means in the lowest layer, it must be 2 number (in this case is x and y)
###
Finally, now we can draw it using :

$$
cv.polylines(blank,\overset{\text{Points}}{\overbrace{[pts]}},\overset{\text{connect/not}}{\overbrace{False}},(\overset{\text{color (bgr)}}{\overbrace{255,255,255}}),\overset{\text{thickness}}{\overbrace{4}})
$$

- If true, the last point will connect to the first one. If not, it wont.
###
then to draw a polygon, it'll be:

```
pts = np.array([[40,470],[67,350],[100,270],[300,70]], np.int32)
pts = pts.reshape((-1,1,2))
cv.polylines(blank,[pts],False,(255,255,255),4)
```
to make a filled one, we will use 

$$
cv.fillPoly(blank,\overset{\text{Points}}{\overbrace{[pts]}},(\overset{\text{color (bgr)}}{\overbrace{255,0,255}}),\overset{\text{edge type}}{\overbrace{cv.LINE\_AA}},\overset{\text{binary shifting}}{\overbrace{0}},\overset{\text{coordinate offset}}{\overbrace{(100,0)}})
$$


- edge type can be smooth (line_AA), or sharp (line_8)
- shift is to move all the binary value to left (basically divided by $2^n$, but faster) if shift 0, it means divided by $2^0\rightarrow$ (1), shift 3 means divided by $2^3\rightarrow$ (8), etc
- offset means add the existing value by those number. if offset (30,3) we will add the existing value (ex: 10,7) with the offset, so the new coordinate will be (40,10).

## Draw a Text

$$
cv.putText(blank,\overset{\text{Texts}}{\overbrace{'Hello World'}},\overset{\text{Coordinate refference}}{\overbrace{(67,400)}},\overset{\text{fonts}}{\overbrace{ cv.FONT\_HERSHEY\_SIMPLEX}},\overset{\text{Coordinate refference}}{\overbrace{(67,400)}},\overset{\text{Text scale}}{\overbrace{2}},(\overset{\text{color (bgr)}}{\overbrace{255,255,255}}),\overset{\text{Thickness}}{\overbrace{5}},\overset{\text{edge type}}{\overbrace{cv.LINE\_4}},\overset{\text{flipped or not}}{\overbrace{False}})
$$

- text scale means is it n times bigger than the normal one
- if false, the coordinate is in the bottom left edge  of the text. But if true , the coordinate is in the top left of the text, and the text will be flipped.

### Watch and try it by yourself in [Draw.py](Draw.py)