Now we came to transforming image.. It was not that much, we will do a translation, rotation, and flipped. resizing and crop already talked on [Washy.md](../Mainf-Functions/Washy.md), So we wont talk about it here.

To translate/shift an image by some, we need to make a function first:
```
def Transl (var, x, y):
    Matrix = np.float32([[1,0,x],[0,1,y]])
    dimension = (var.shape[1],var.shape[0])
    return cv.warpAffine(var, Matrix,dimension)
```
- np Float makes al datatypes there into a 32 bit float/decimals..
- reason we using 1,0,x and 0,1,x is because computer change coordinate like 

$$
x_{new}=1⋅x_{before}+0⋅y_{before}
+\text{variable offsets}
$$

 While variable offsets is x that we use as a parameters, not the original one.
 ###
 y axis is almost similar:

$$
x_{new}=0⋅x_{before}+1⋅y_{before}
+\text{variable offsets}
$$

end the variable offsets were y that we use as an offsets.

we can also use this equations to find the 

​