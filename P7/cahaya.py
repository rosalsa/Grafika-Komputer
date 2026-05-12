from vpython import *

scene = canvas(
    width = 800,
    height = 600,
    background = color.black,
    autoscale = False
)

sphere()

distant_light(
    direction = vec(0, -1, 0),
    color = color.green
)
local_light(
    pos = vec(0, 1, -2),
    color = color.yellow
)

local_light(
    pos = vec(4, 2, 0),
    color = color.red
)

while True :
    rate(30)