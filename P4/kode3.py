import cv2
import numpy as np

height, width = 400, 600
output = cv2.VideoWriter('car_animation.avi',
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         20,
                         (width, height))

for x in range(0, width, 10):
    canvas = np.zeros((height, width, 3), dtype='uint8')
    canvas[:] = 255, 255, 255

    # Gambar badan mobil
    body_top_left = (x, 300)
    body_bottom_right = (x + 100, 350)
    cv2.rectangle(canvas, body_top_left, body_bottom_right, (255, 0, 0), -1)

    wheel1_center = (x + 25, 350)
    wheel2_center = (x + 75, 350)
    cv2.circle(canvas, wheel1_center, 10, (0, 0, 255), -1)
    cv2.circle(canvas, wheel2_center, 10, (0, 0, 255), -1)

    cv2.imshow('Car Animation', canvas)
    output.write(canvas)

    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
output.release()