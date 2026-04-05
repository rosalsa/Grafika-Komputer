import cv2
import numpy as np, time

canvas1 = np.zeros((500, 500, 3), dtype="uint8")

for i in range(10):
    cv2.imshow("Animation", canvas1)
    cv2.waitKey(500)

    canvas1[:] = 255, 255, 255
    cv2.imshow("Animation", canvas1)
    cv2.waitKey(500)

    canvas1[:] = 0, 0, 0

cv2.destroyAllWindows()