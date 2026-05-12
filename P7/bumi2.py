from vpython import *
import time

# membuat scene dengan pengaturan kamera
scene = canvas(title='Sistem Bumi', 
              width=800, height=600,
              range=2,  # jarak pandang awal
              background=color.black)

# membuat objek bumi
earth = sphere(pos=vector(0, 0, 0),
              texture=textures.earth,
              radius=1,
              shininess=0.1)

# cahaya pada bumi agar lebih realistis
sun = distant_light(direction=vector(1, 0, 0), color=color.white)

# fungsi untuk mengatur ulang pandangan kamera
def reset_view():
    scene.center = vector(0, 0, 0)
    scene.forward = vector(0, 0, -1)
    scene.up = vector(0, 1, 0)

# tombol untuk reset kamera
reset_button = button(bind=reset_view, text='Reset Kamera')

# label petunjuk
scene.append_to_caption("\n\nKontrol:\n- Drag mouse untuk memutar kamera\n- Scroll untuk zoom\n- Klik tombol untuk reset kamera")

# animasi
while True:
    rate(100)
    
    earth.rotate(angle=0.01, axis=vector(0, 1, 0)) # rotasi bumi
