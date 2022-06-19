import numpy as np
from matplotlib import pyplot as plt

import cv2 as cv


imgL = cv.imread('im0.png',0)
imgR = cv.imread('im1.png',0)
kernel = np.ones((3,3),np.uint8)

stereo = cv.StereoBM_create(numDisparities=128, blockSize=15)
disparity = stereo.compute(imgL,imgR)
closing = cv.morphologyEx(disparity, cv.MORPH_CLOSE, kernel)
plt.imshow(closing,'gray')
plt.show()