import numpy as np
import cv2 as cv

jendela = np.zeros((500, 500, 3), dtype='uint8')

persegi = cv.rectangle(jendela, (125, 125), (375, 375), (255, 255, 255), 5)

M = cv.getRotationMatrix2D((250, 250), 30, 1.0)
rotasi = cv.warpAffine(persegi, M, (persegi.shape[1], persegi.shape[0]))

cv.imshow('Persegi', jendela)
cv.imshow('translasi', rotasi)
cv.waitKey(0)