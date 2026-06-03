from ursina import *

app = Ursina()

player = Entity(model='cube', color=color.red, position=(0, 0, 0))
left_boundary = -5
right_boundary = 5
movement_direction = 1

def update():
    global movement_direction

    player.x += time.dt * movement_direction

    if player.x < left_boundary or player.x > right_boundary:
        movement_direction *= -1

app.run()