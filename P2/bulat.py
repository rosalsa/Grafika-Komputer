import numpy as np
import cv2 as cv

biru = 255, 0, 0
putih = 255, 255, 255
jendela = np.zeros((500, 500, 3), dtype='uint8')
jendela[:] = (biru)

cv.circle(jendela, (250, 250), 100, putih, 5)

cv.imshow("lingkaran", jendela)
cv.waitKey(0)