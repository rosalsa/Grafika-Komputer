import numpy as np
import cv2 as cv

merah = 0, 0, 255
jendela = np.zeros((500, 500, 3), dtype='uint8')

cv.line(jendela, (250, 250), (250, 250), merah, 10)

cv.imshow("titik", jendela)
cv.waitKey(0)