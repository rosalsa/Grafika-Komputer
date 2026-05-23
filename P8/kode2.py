from ursina import *

# Membuat aplikasi game
app = Ursina()

# Membuat sebuah entitas
cube = Entity(
    model="cube",
    texture="brick",
    scale=(1, 1, 1),
    position=(0, 0, 0),
)

# Fungsi Rotasi
def update():
    cube.rotation_y += time.dt * 100
    cube.rotation_x += time.dt * 50

# Menjalankan aplikasi
app.run()