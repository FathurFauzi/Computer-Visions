# Ai-controlled Civil Equipment
### Feature-based (Distance) and Gesture-based (Gesture)
### .

<div align="center">
  <img src="/Distance%20and%20gesture%20Detector/Media/blind%20spot.jpg" alt="blindspot" height="300" width="auto">
</div>

In Construction site, accident because of blind-spot is inevitable. Its because the design of heavy equipment that have many blind spot. Beside that, the driver can sometime makes a mistakes too. Because of that, i was just thinking "What if we make the heavy equipment can have eyes" Thats where the idea from

But we have another problem, when we use regular computer vision, that usually track hand, it will have a high latency, because the program must detect the hands too in the camera, and then they calculate it. To solve it, we will make the hand to stand out and can be seen early by the computer.. Thats Why we using checkboard gloves

![Checkboard Gloves](/Distance%20and%20gesture%20Detector/Media/checkboard%20gloves.jpg)

using checkboard gloves is like when we using a vest in the construction. It will improve the hand's visibility so the heavy equipment can recognized it much faster, and the gesture can be calulate more faster. 

Beside checkboard gloves, i will also propose using ArUco as another identity mark. ArUco is simply a qr code that already recognized by OpenCv (our "library" to make computer vision), so when program see the marker, they will recognized it much Faster.

![ArUco ilustration](/Distance%20and%20gesture%20Detector/Media/Screenshot%20(224)%20-%20Copy.png)

As you can see in the figure, using aruco, we can project the coordinate, distance, slope, and more. by using it, we can also make the heavy equipment stop when they see the ArUco in some distance. 


![ArUco visualization](/Distance%20and%20gesture%20Detector/Media/ARUCO.jpg)

Unlike checkboard gloves, ArUco also contain unique identity. We can exploit that by using it as a "filter" to differentiate normal workers and Authorized worker. this "filter" will make only authorized worker can control the Heavy equipment.


![Uniform Concept](/Distance%20and%20gesture%20Detector/Media/1000076478.jpg)

to use it in construction site. i propose to put different aruco in front and back of workers's Vest. it will make program know wether the workers is facing the heavy equipment or not. And to make things better, i also propose it must use reflective materials, so program can detect it even in low light intensity. 