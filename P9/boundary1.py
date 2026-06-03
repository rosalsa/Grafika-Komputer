from ursina import *

app = Ursina()

# Membuat objek sederhana
cube = Entity(model='cube', color=color.orange, scale=(1, 1, 1), position=(0, 0, 0))

# Menambahkan ground (tanah) untuk referensi
ground = Entity(model='plane', scale=(10, 1, 10), texture='white_cube', texture_scale=(10, 10))

# Menambahkan batasan visual
boundary1 = Entity(model='cube', scale=(0.2, 2, 10), position=(-4.5, 1, 0), color=color.red)
boundary2 = Entity(model='cube', scale=(0.2, 2, 10), position=(4.5, 1, 0), color=color.red)
boundary3 = Entity(model='cube', scale=(10, 2, 0.2), position=(0, 1, 4.5), color=color.red)
boundary4 = Entity(model='cube', scale=(10, 2, 0.2), position=(0, 1, -4.5), color=color.red)

# Mengatur kamera
camera.position = (0, 10, -20)
camera.rotation_x = 30
EditorCamera()
camera.look_at(cube)

app.run()