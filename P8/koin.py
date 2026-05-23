from vpython import *

# Membuat koin
coin = cylinder(
    pos=vector(0, 1, 0),
    axis=vector(0, 0.1, 0),
    radius=1,
    color=color.yellow
)

# Kecepatan rotasi koin (dalam radian per detik)
angular_speed = 1

# Loop animasi
while True:
    rate(50)  # Mengatur kecepatan frame rate

    # Gerakan rotasi koin
    coin.rotate(angle=angular_speed, axis=vector(0, 1, 1))