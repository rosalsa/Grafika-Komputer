import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Membuat figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = [0, 100, 100, 0, 0, 100, 100, 0]
y = [0, 0, 50, 50, 0, 0, 50, 50]
z = [0, 0, 0, 0, 10, 10, 10, 10]

# Menghubungkan titik-titik menjadi sisi
vertices = [
    [0,1,2,3],  # bawah
    [4,5,6,7],  # atas
    [0,1,5,4],  # depan
    [2,3,7,6],  # belakang
    [1,2,6,5],  # kanan
    [0,3,7,4]   # kiri
]

# Import untuk membuat polygon 3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Membuat face dari rectangle
faces = [[(x[i], y[i], z[i]) for i in vert] for vert in vertices]

# Menambahkan ke plot
ax.add_collection3d(Poly3DCollection(faces, alpha=0.5))

# Setting label
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Rectangle 3D (Balok Tipis)')

# Menentukan batas sumbu
ax.set_xlim(0, 120)
ax.set_ylim(0, 60)
ax.set_zlim(0, 20)

plt.show()