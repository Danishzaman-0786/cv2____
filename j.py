import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os
s=os.listdir(r'/home/danish/cv2____/photo_')
for name in s:
    p='/home/danish/cv2____/photo_'
    img=p+ '/' + name
    v=cv.imread(img)
    k=cv.resize(v,(250,250))
    cv.imshow('danish',k)
    cv.waitKey(0)
cv.destroyAllWindows()    