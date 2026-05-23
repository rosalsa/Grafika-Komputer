from vpython import *

# Membuat bola
ball = sphere(pos=vector(0, 10, 0), radius=1, color=color.red)

# Kecepatan awal
velocity = vector(0, -9.8, 0)  # Kecepatan awal dengan gravitasi

# Loop animasi
while True:
    rate(50)  # Mengatur kecepatan frame rate

    # Update posisi bola
    ball.pos += velocity * 0.01  # 0.01 adalah langkah waktu

    # Update kecepatan (gravitasi)
    velocity.y += -9.8 * 0.01  # Percepatan gravitasi