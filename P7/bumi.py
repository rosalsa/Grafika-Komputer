from vpython import * 

mycanvas = canvas (
    width = 1080,
    height = 600,
    background = color.black,
    title = '3D Scene',
    autoscale = False
)

cube = sphere (
    pos = vector(0, 0, 0),
    radius = 1,
    size = vec(1, 1, 1),
    texture = textures.earth
)

mycanvas.camera.pos = vector(3, 2, 3)
mycanvas.camera.axis = vector(-3, -2, -3)
mycanvas.range = 2

while True :
    rate(30)