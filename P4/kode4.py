import cv2
import numpy as np

# Posisi awal dan akhir
start_pos = (50, 50)
end_pos = (500, 400)

num_frames = 120
width, height = 640, 480

for i in range(num_frames):
    # Buat frame buffer kosong
    frame = np.zeros((height, width, 3), dtype=np.uint8)

    # Hitung posisi saat ini dengan interpolasi linier
    t = i / (num_frames - 1)
    x = int(start_pos[0] * (1 - t) + end_pos[0] * t)
    y = int(start_pos[1] * (1 - t) + end_pos[1] * t)

    cv2.circle(frame, (x, y), 10, (0, 0, 255), -1)
    cv2.imshow('Tweening', frame)

    # Jeda untuk mengontrol kecepatan animasi
    cv2.waitKey(int(1000 / 30))

cv2.destroyAllWindows()