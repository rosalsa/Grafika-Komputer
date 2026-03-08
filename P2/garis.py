import numpy as np
import cv2 as cv

hijau = 0, 255, 0
jendela = np.zeros((500, 500, 3), dtype='uint8')
jendela[:] = (255, 0, 0)

cv.line(jendela, (0, 0), (250, 250), hijau, 5)

cv.imshow("garis", jendela)
cv.waitKey(0)