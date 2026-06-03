from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

ground = Entity(
    model='plane',
    scale=30,
    texture='white_cube',
    texture_scale=(30, 30),
    color=color.light_gray,
    collider='box'
)

player = FirstPersonController()
player.position = (0, 2, 0)

app.run()