from ursina import *


def input(key):
    global current_texture
    if key == "space":
        cube.color = color.random_color()

    elif key == "up arrow":
        cube.texture = random.choice(texture_list)

    elif key == "down arrow":
        cube.rotation_z += 40

    elif key == 'left arrow':
        cube.rotation_x += 10

    elif key == 'right arrow':
        cube.rotation_y -= 10

    elif key == 'left mouse down':
        cube.scale *= 1.1

    elif key == 'right mouse down':
        cube.scale *= 0.9

app = Ursina()

speed = 5

cube = Entity(
    model='cube',
    texture='test_tileset',
    position=(0, 0, 0)
)

EditorCamera()

app.run()