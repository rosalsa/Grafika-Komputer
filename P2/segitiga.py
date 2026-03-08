import numpy as np
import cv2 as cv

biru = 255, 0, 0
merah = 0, 0, 255
hijau = 255, 0, 0
putih = 255, 255, 255
jendela = np.zeros((500, 500, 3), dtype='uint8')

koordinat1 = (250, 125)
koordinat2 = (125, 375)
koordinat3 = (375, 375)

cv.circle(jendela, koordinat1, 10, merah, -1)
cv.circle(jendela, koordinat2, 10, hijau, -1)
cv.circle(jendela, koordinat3, 10, biru, -1)

titik_segitiga = np.array([koordinat1, koordinat2, koordinat3])

cv.drawContours(jendela, [titik_segitiga], 0, putih, -1)

cv.imshow("persegi", jendela)
cv.waitKey(0)