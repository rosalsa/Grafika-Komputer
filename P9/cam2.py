from ursina import *

app = Ursina()

Sky()

DirectionalLight()
AmbientLight(color=color.rgba(100, 100, 100, 0.5))

ground = Entity(
    model='plane',
    scale=30,
    texture='white_cube',
    texture_scale=(30, 30),
    color=color.light_gray,
    collider='box'
)

player = Entity(
    model='sphere',
    color=color.orange,
    scale=2,
    position=(0, 1, 0),
    collider='sphere'
)

def update():
    speed = 5 * time.dt

    if held_keys['w']:
        player.z += speed
    if held_keys['s']:
        player.z -= speed
    if held_keys['a']:
        player.x -= speed
    if held_keys['d']:
        player.x += speed

    # kamera third person
    camera.position = player.position + Vec3(0, 5, -12)
    camera.look_at(player)

app.run()