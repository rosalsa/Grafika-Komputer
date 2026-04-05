import cv2
import numpy as np

jendela = np.zeros((500, 500, 3), dtype="uint8")
cv2.circle(jendela, (250, 250), 50, (0, 255, 0), -1)
x, y = 250, 250

for i in range(100):
    new_jendela = jendela.copy()
    x += 5
    y += 5
    
    # Menggambar lingkaran pada posisi baru
    cv2.circle(new_jendela, (x % 500, y % 500), 50, (255, 0, 0), -1)
    cv2.imshow("Moving Circle", new_jendela)
    cv2.waitKey(30)

cv2.destroyAllWindows()