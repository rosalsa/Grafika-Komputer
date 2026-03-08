import numpy as np
import cv2 as cv

jendela = np.zeros((500, 500, 3), dtype='uint8')
jendela[:] = (255, 0, 0)

cv.imshow("canvas", jendela)
cv.waitKey(0)