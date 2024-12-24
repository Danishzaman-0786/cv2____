import cv2 as cv
import numpy as np
import os as s
#v=cv.imread("/home/danish/cv2____/images (6).jpeg")
#o=s.listdir("/home/danish/cv2____/input_img")
##print(o)
#c="/home/danish/cv2____/input_img"
a=cv.VideoCapture(0)
s=cv.VideoWriter_fourcc(*"AVID")
x=cv.VideoWriter("new_mp4",s,40.0,(600,480),0)
while a.isOpened():
    ret,f=a.read()
    if ret==True:
        f=cv.cvtColor(f,cv.COLOR_BGR2GRAY)
        f=cv.flip(f,1)
        x.write(f)
        cv.imshow("danish",f)
        if cv.waitKey(25) & 0Xff==ord('x'):

          break
    else:
          break  
a.release()
x.release()              
cv.destroyAllWindows()                