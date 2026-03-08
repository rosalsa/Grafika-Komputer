import numpy as np
import cv2 as cv

biru = 255, 0, 0
jendela = np.zeros((500, 500, 3), dtype='uint8')
jendela[:] = (biru)

cv.rectangle(jendela, (125, 125), (375, 375), (255, 255, 255), 5)

cv.imshow("persegi", jendela)
cv.waitKey(0)