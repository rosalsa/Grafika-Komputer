from ursina import *

def update():
    global speed
    if held_keys['w']:
        cube.y += time.dt * speed
    elif held_keys['s']:
        cube.y -= time.dt * speed
    elif held_keys['a']:
        cube.x -= time.dt * speed
    elif held_keys['d']:
        cube.x += time.dt * speed
    elif held_keys['escape']:
        application.quit()

app = Ursina()

speed = 5

cube = Entity(
    model='cube',
    texture='test_tileset',
    position=(0, 0, 0)
)

EditorCamera()

app.run()