from ursina import *

# Membuat aplikasi game
app = Ursina()

# Membuat sebuah entitas
cube = Entity(
    model="cube",
    color=color.rgba(200/255, 40/255, 100/255, 1),
    scale=(1, 1, 1),
    rotation=(45, 45, 45),
)

# Menjalankan aplikasi
app.run()