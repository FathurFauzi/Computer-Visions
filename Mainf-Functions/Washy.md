I learned one of the most essential to learn computer vision. it is "cleaning" the image.. it actually a process to simplify the image so it will only show essential things so computer can recognized it. It's like when we butchering meat. we will only take the meat, and the other one, we will throw it . 
###
there wil be steps to cleaning the image.
the first one is to turn it into grayscale:

$$
gryscl = cv.\overset{\text{turn color space type}}{\overbrace{cvtColor}}(\overset{\text{variable}}{\overbrace{img}},\overset{\text{turn into grayscale}}{\overbrace{cv.COLOR\_BGR2GRAY}})
$$
- cvtColor used to turn one color space to another. example bgr to grayscale, hsv,etc
###
then we need to blur it. It is to make less noise and program can sort/ filter easily
$$
blur = cv.GaussianBlur(gryscl, \overset{\text{intensity}}{\overbrace{(5,5)}} ,\overset{\text{to blur border pixel}}{\overbrace{cv.BORDER\_DEFAULT}})
$$
- picture will be more blurry if the intensity getting higher
- itensity must be an even number. because blurr is actually calculate average color on certain range (if 3x3, it means it will detect color in 3x3 pixels) and use it as our new color pixel.
- if we use uneven intensity, the blurr will be wether blurred horizontally, or vertically (usualy to make moving effect)
- cv.BORDER_DEFAULT is the way to mirror the color of pixel if we calculate pixel in the border, this is just a basic so pixel in the border can blur too
### Now for the most valuable one: Canny
###
cany is an algorithm to find does any pixel has a big contrast to another or not. if yes, it will considered as edge and the output will be true (white pixel). this was used to filter noise more brutal than blur, because the output will be true or false:

$$
blrcanny = cv.Canny(blur,\overset{\text{least}}{\overbrace{125}},\overset{\text{highest}}{\overbrace{175}})
$$
- least and highest is a treshold to find color deviation between pixel.. if its low (below 125), it will be false (black), if its high (over 175) it will be true. 
- boolean between the treshold will depend on the high one. if it near the high one, it will also be true, so does the opposite
###
the next one is dilate

$$
dilate = cv.dilate(blrcanny,\overset{\text{check pixel around}}{\overbrace{(3,3)}}, \overset{\text{repeat 5 times}}{\overbrace{iterations=5}}
$$

- if there any true/white pixels around 3x3, it will also be white 
-repeat means this process will repeat 5 times
###
erode is the oppposite of dilate, the pixel will turn to black if it see a black pixel around it

$$
erode = cv.erode(dilate,\overset{\text{check pixel around}}{\overbrace{(3,3)}}, \overset{\text{repeat 4 times}}{\overbrace{iterations=4}})
$$

both dilate and erode use to connect a line in a pattern. it will make it one being so computer can recognized it easily. if we dint using it, for example in face... compter will think all the line in our face is another pattern and our face detector will be failed
###
now to transform an image:

$$
resize = cv.resize(img,\overset{\text{new resolutions}}{\overbrace{(500,500)}}, \overset{\text{make upscaling more smooth}}{\overbrace{interpolation=cv.INTER\_LINEAR}})
$$

then to crop it, we use:

$$
crop = resize[\overset{\text{height}}{\overbrace{50:200}},\overset{\text{width}}{\overbrace{200:400}}]
$$

- height means window will render only from x 20 to x 200, and from y 200 to y 400

you can try your own [here](WashImage.py)

now you know essensial command to filter image, now we will see how to [transform](../Transform-Figures/Transform.md) an image so computer can calculate it more easily