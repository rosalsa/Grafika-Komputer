import numpy as np
import cv2 as cv

jendela = np.zeros((500, 500, 3), dtype='uint8')

persegi = cv.rectangle(jendela, (125, 125), (375, 375), (255, 255, 255), 5)

M = np.float32([[1, 0, 100], [0, 1, 50]])
translasi = cv.warpAffine(persegi, M, (persegi.shape[1], persegi.shape[0]))

cv.imshow('Persegi', jendela)
cv.imshow('translasi', translasi)
cv.waitKey(0)