import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Membuat titik acak dalam ruang 3D
num_points = 100
x = np.random.rand(num_points) * 100
y = np.random.rand(num_points) * 100
z = np.random.rand(num_points) * 100

# Menampilkan titik dalam ruang 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c='r', marker='o')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.set_title("Visualisasi sumbu X, Y dan Z")

plt.show()
