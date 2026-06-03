from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# Ground / lantai
ground = Entity(
    model='plane',
    collider='box',
    scale=64,
    texture='grass',
    texture_scale=(4, 4)
)

# Boundary collider (dinding tak terlihat)
wall_thickness = 1
wall_height = 5
ground_size = 64

# Depan
Entity(
    model='cube',
    position=(0, wall_height/2, ground_size/2),
    scale=(ground_size, wall_height, wall_thickness),
    collider='box',
    visible=False
)

# Belakang
Entity(
    model='cube',
    position=(0, wall_height/2, -ground_size/2),
    scale=(ground_size, wall_height, wall_thickness),
    collider='box',
    visible=False
)

# Kanan
Entity(
    model='cube',
    position=(ground_size/2, wall_height/2, 0),
    scale=(wall_thickness, wall_height, ground_size),
    collider='box',
    visible=False
)

# Kiri
Entity(
    model='cube',
    position=(-ground_size/2, wall_height/2, 0),
    scale=(wall_thickness, wall_height, ground_size),
    collider='box',
    visible=False
)

# Objek contoh
Entity(
    model='cube',
    origin_y=-.5,
    scale=2,
    texture='brick',
    texture_scale=(1, 2),
    collider='box'
)

# Kamera editor
editor_camera = EditorCamera(enabled=False, ignore_paused=True)

# Player
player = FirstPersonController(
    model='cube',
    z=-10,
    color=color.orange,
    origin_y=-.5,
    speed=8,
    collider='box'
)

player.collider = BoxCollider(player, Vec3(0, 1, 0), Vec3(1, 2, 1))

# Cahaya
sun = DirectionalLight()
sun.look_at(Vec3(1, -1, -1))

# Langit
Sky()

app.run()