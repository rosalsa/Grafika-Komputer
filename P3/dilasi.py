import numpy as np
import cv2 as cv

jendela = np.zeros((500, 500, 3), dtype='uint8')

persegi = cv.rectangle(jendela, (125, 125), (375, 375), (255, 255, 255), 5)

M = np.float32([[2, 0, 0], [0, 2, 0]])
dilasi = cv.warpAffine(persegi, M, (persegi.shape[1], persegi.shape[0]))

cv.imshow('Persegi', jendela)
cv.imshow('translasi', dilasi)
cv.waitKey(0)