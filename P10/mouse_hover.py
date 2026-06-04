from ursina import *

app = Ursina()

def update():
    if mouse.hovered_entity == cube:
        random_offset = 0.5
        cube.position = (
            cube.x + random.uniform(-random_offset, random_offset),
            cube.y + random.uniform(-random_offset, random_offset),
            cube.z + random.uniform(-random_offset, random_offset),
        )

cube = Entity(
    model="cube",
    texture="test_tileset",
    position=(0, 0, 0),
    collider="box",
)

app.run()